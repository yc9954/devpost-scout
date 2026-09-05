# Killing ideas cheaply

This is the part that mattered most and is easiest to skip. Before writing any
code we ran candidate ideas through five tests. **Fail one and the idea is
dead** — not weakened, dead. Six ideas were executed; one survived.

Do this after you have the corpus (`METHOD.md` stages 1–2), because three of the
five tests need it.

## The five tests

| # | Test | The question |
| --- | --- | --- |
| 1 | **Prompt** | Would a person who writes a better prompt get the same result? |
| 2 | **Server** | Move the feature to a server API or a server-side MCP. Does it die? |
| 3 | **Occupancy** | How many of the N entries already do it, and how well are they placed? |
| 4 | **60-second** | Does a judge, alone, with no login, go "huh" inside a minute? |
| 5 | **24-hour** | Can you build it reliably in the time you actually have? |

**Test 2 is the one that decides.** If the thing survives being moved to a
server, the platform you are building on is a front door and the judges will see
that. Ask it literally: rewrite the feature as a server endpoint plus a chat box
in your head, and see whether anything is lost.

## Find the platform's real territory first

Before generating ideas, enumerate what the platform can do that **nothing else
can**, and count how crowded each of those is. Ours, over 470 entries at the
time:

| Only the in-page runtime can do this | entries | best rank |
| --- | ---: | ---: |
| use the user's own logged-in session, no API key | 43 | 11th |
| what is *actually rendered* — contrast, overlap, font fallback | ~0 | 263rd |
| device-local data | 33 | 1st |
| device **sensors** — camera, mic, serial | **3** | 199th |
| **changing the tool surface itself at runtime** | 23 static / **0 runtime** | — |
| the fact that a person is looking at this frame right now | 20 | 8th |

Two columns, not one. A lane with zero occupants and a best rank of 263rd is
telling you something. A lane with three occupants whose best is 199th is
telling you something different — that one was our strongest axis and we still
killed it, on test 5.

## The executions, and what each taught

**✗ Editable plans instead of approvals — died on test 1.** Saying "payment
records are kept five years" is just a follow-up prompt. The one surviving
property (rules held in an engine outside the model, enforced deterministically)
was already done sharper by two better-placed entries.
→ *Zero occupancy is not evidence of a good idea. Nobody may have done it
because it isn't attractive.*

**✗ Sealed negotiation — died on test 2.** Keeping each side's reserve price
secret needs a trusted third party. In-page tools run in the page's JavaScript;
anything in your browser's memory is readable in devtools. So the seal has to be
server-side, and the moment it is, the platform is decoration.

**✗ Accessibility adaptation from measured rendering — died on test 3.** An
entry at 13th already did declare → negotiate → apply → verify. The measurement
axis was alive; the destination was taken.

**✗ Local files that never leave the device — died on test 3.** 33 entries,
including the 1st-placed one, and the purest form of it already built.

**⚠ Camera-based verification that never shows the model the image — held on
test 5.** Best axis available (3 entries, server literally cannot do it). But
webcam permission plus lighting plus local OCR accuracy inside 24 hours was not
safe, and **a demo that fails once takes Execution down with it.** With more time
this was first choice.

**✅ Survivor — a tool minted at runtime from a demonstration, where the same
screen also decides what the tool may never return.**

Why the two halves are one idea: minting defines the agent's **capability**;
withholding defines its **field of view**. The natural moment to decide both is
the same moment — when the tool is born. Decide earlier and the site doesn't
know the user's situation; decide later and it is already too late.

## Then try to kill the survivor, in public

Our first field-position claim said the survivor's core was **0 of 470**. It was
wrong, and a reader found it. The regex had wanted "record a macro" and "learn
from demonstration"; the entry that defeated us wrote *"turns that demonstration
into a tool"*. Widening the pattern took the count from 0 → 1 → 3, and against
the full field (2,392) it is at least 8.

Two things follow, and both are load-bearing:

1. **The differentiator was never the scarce half.** It was the conjunction —
   declaration-derived validation, executed edge cases, deregistration on drift,
   the tool shareable as a contract. Single pillars are always more crowded than
   you think; combinations are what survive.
2. **Publish the widest count and name the entries that beat you.** Every judge
   in our run marked the self-refutation as a reason to trust the rest. The
   entry that defeated the claim was the one entry our own filter could not
   see — which is exactly the failure mode the project was about.

Run `agents/field-position.md` to do this against your own corpus, and let it be
unflattering.
