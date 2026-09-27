"""Claude mode: streaming tool loop over the Anthropic SDK. The only module that
imports `anthropic`. Emits the same (event, data) sequence as local_agent.run."""
import json
import uuid

from scout import config, tools

SYSTEM = """You are Scout, the agent inside devpost-scout: a toolkit for entering a Devpost \
hackathon on measured evidence. You help the user pick a hackathon, read its rubric, see the \
field that already exists, and find ideas proven elsewhere and absent here.

Rules — each one was paid for once:
- Only measured numbers. Every count, prize, date or rank you state comes from a tool result in \
this conversation; never estimate or invent one. Quote Devpost verbatim for judging criteria.
- Always state the census date (from the tool result) when you cite counts or lists, and that \
status is derived from the submission dates against today.
- A search shortlist is NOT a ranking. When you use search_winners or vault_lookup, say so: FTS \
over titles and taglines measures the query's vocabulary, not the field. Zero matches is not \
evidence nobody built it.
- The tie-break criterion (first listed) decides bunched fields; say so when you show a rubric.
- An unpublished gallery is not an empty field. When `field` reports gallery_unpublished, say \
the field is unmeasured.
- Ideas from `ideate` are candidates, not ideas, until they survive the five kill tests \
(prompt, server, occupancy, 60-second, 24-hour). Say which claim is weaker when the \
hackathon's own field was unavailable.
- Prize figures use static FX and are approximate; say so once per answer when relevant.
- Slow network tools (hackathon_brief, field, scout) take seconds to minutes. If the user \
clearly named a hackathon, just run them; only ask first when the request is ambiguous \
(several census matches, or unclear which hackathon).
- Prefer the local census (list_hackathons, census_stats) for anything it can answer; it is \
instant and needs no network.
- Write in concise markdown. Link Devpost URLs from the results. Do not repeat card data the UI \
already renders — summarise and interpret it.
"""

TOOL_RESULT_CAP = 60_000


def _client():
    import anthropic
    return anthropic.Anthropic()


def _compact(res):
    """What the model sees: the full result, capped."""
    s = json.dumps(res, ensure_ascii=False)
    if len(s) <= TOOL_RESULT_CAP:
        return s
    data = dict(res.get('data') or {})
    for k in ('rows', 'notes', 'candidates'):
        if isinstance(data.get(k), list):
            data[k] = data[k][:25]
            data[f'{k}_truncated'] = True
    return json.dumps({**res, 'data': data}, ensure_ascii=False)[:TOOL_RESULT_CAP]


def _run_with_progress(name, args):
    """Run a tool in a worker thread so long jobs stream job_progress live.
    Yields ('progress', data)* then ('result', res)."""
    import queue
    import threading
    q = queue.Queue()

    def emit(step, pct, note, job_id=None):
        q.put(('progress', {'job_id': job_id, 'step': step, 'pct': pct, 'note': note}))

    def work():
        q.put(('result', tools.run(name, args, emit=emit)))

    threading.Thread(target=work, daemon=True).start()
    while True:
        kind, payload = q.get()
        yield kind, payload
        if kind == 'result':
            return


def _blocks_to_dicts(content):
    out = []
    for b in content:
        d = b.model_dump(mode='json', exclude_none=True)
        out.append(d)
    return out


def run(chat, text):
    """Generator of (event, data). Persists role/content blocks in chat['api_messages']."""
    import anthropic
    mid = uuid.uuid4().hex[:12]
    yield 'message_start', {'chat_id': chat['id'], 'message_id': mid, 'mode': 'claude'}
    chat['messages'].append({'role': 'user', 'text': text, 'tool_calls': []})
    entry = {'role': 'assistant', 'text': '', 'tool_calls': [], 'id': mid}
    chat['messages'].append(entry)
    messages = list(chat.get('api_messages') or [])
    messages.append({'role': 'user', 'content': text})
    usage = {'input_tokens': 0, 'output_tokens': 0}

    try:
        client = _client()
    except Exception as exc:                                         # noqa: BLE001
        yield 'error', {'message': f'could not create the Anthropic client: {exc}'}
        yield 'message_end', {}
        return

    try:
        for rnd in range(config.MAX_TOOL_ROUNDS + 1):
            with client.messages.stream(
                model=config.MODEL,
                max_tokens=16000,
                thinking={'type': 'adaptive'},
                system=SYSTEM,
                tools=tools.SCHEMAS,
                messages=messages,
            ) as stream:
                for event in stream:
                    et = event.type
                    if et == 'text':
                        entry['text'] += event.text
                        yield 'text_delta', {'text': event.text}
                    elif et == 'content_block_start' and event.content_block.type == 'thinking':
                        yield 'thinking', {'text': 'Thinking…'}
                    elif et == 'content_block_stop' and event.content_block.type == 'tool_use':
                        b = event.content_block
                        yield 'tool_call', {'id': b.id, 'name': b.name, 'input': b.input}
                final = stream.get_final_message()
            usage['input_tokens'] += final.usage.input_tokens
            usage['output_tokens'] += final.usage.output_tokens
            messages.append({'role': 'assistant', 'content': _blocks_to_dicts(final.content)})

            tool_uses = [b for b in final.content if b.type == 'tool_use']
            if final.stop_reason == 'pause_turn':
                continue
            if final.stop_reason in ('end_turn', 'refusal', 'stop_sequence') or not tool_uses:
                if final.stop_reason == 'refusal':
                    yield 'error', {'message': 'the model declined this request'}
                break
            if final.stop_reason == 'max_tokens':
                yield 'error', {'message': 'response truncated at max_tokens'}
                break
            if rnd >= config.MAX_TOOL_ROUNDS:
                yield 'error', {'message': f'stopped after {config.MAX_TOOL_ROUNDS} tool rounds'}
                break

            # every tool_use in this turn is answered in ONE user message
            results = []
            for b in tool_uses:
                args = b.input if isinstance(b.input, dict) else {}
                res = None
                for kind, payload in _run_with_progress(b.name, args):
                    if kind == 'progress':
                        yield 'job_progress', payload
                    else:
                        res = payload
                entry['tool_calls'].append({'id': b.id, 'name': b.name, 'input': args, 'result': res})
                yield 'tool_result', {'id': b.id, 'name': b.name, 'ok': res['ok'],
                                      'summary': res['summary'], 'data': res['data']}
                results.append({'type': 'tool_result', 'tool_use_id': b.id,
                                'content': _compact(res), 'is_error': not res['ok']})
            messages.append({'role': 'user', 'content': results})
    except anthropic.AuthenticationError:
        yield 'error', {'message': 'Anthropic rejected the API key (authentication error).'}
    except anthropic.RateLimitError:
        yield 'error', {'message': 'Rate limited by the Anthropic API; try again shortly.'}
    except anthropic.APIStatusError as exc:
        yield 'error', {'message': f'Anthropic API error {exc.status_code}: {exc.message}'}
    except anthropic.APIConnectionError as exc:
        yield 'error', {'message': f'Could not reach the Anthropic API: {exc}'}
    except Exception as exc:                                         # noqa: BLE001
        yield 'error', {'message': f'{type(exc).__name__}: {exc}'}

    # keep the history consistent: never persist a dangling tool_use without its result
    if messages and messages[-1]['role'] == 'assistant' and any(
            isinstance(b, dict) and b.get('type') == 'tool_use' for b in messages[-1]['content']):
        messages.pop()
    chat['api_messages'] = messages
    yield 'message_end', {'usage': usage}
