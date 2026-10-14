# Personal workspace

The workspace is the main UI. Its structure follows Colanode's spaces with pages, databases, and conversations; Scout's dark visual style supplies the components. Devpost Scout remains a focused hackathon space inside it. The app runs locally on `127.0.0.1` and stores personal data in `data/workspace.db` (or `$SCOUT_DATA_DIR/workspace.db`). Scout's committed census and winners data remain separate.

## Spaces and pages

- **My workspace** contains the home dashboard, To Do database, collected source notes, and personal pages.
- **Projects** contains project pages. Each page shows its goal, next action, target date, milestones, related to dos, source records, child documents and study items. A project can contain arbitrarily nested pages/folders. The project database offers cards and a status board.
- **Learning** contains the Study database and learning pages. The To Do database offers table, board, and calendar views; Study offers learning paths, gallery and table views. A path groups related material around a learning outcome and shows progress by stage and items due for review.
- **Agents** contains the directory and local Codex chat. **Devpost Scout** contains hackathon exploration, hackathon study, Scout chat, and its own pages. **Screen Studio** contains recordings and editing.

The UI uses the original 1code-style 240px sidebar shell: Scout mark, search, new page action, compact navigation, recent conversations and a status footer. Project pages and nested folders remain available through Projects, Pages and global search (⌘K). The light palette uses 1code's base theme tokens. Pages have a title, Markdown body, type (`page`/`folder`), space, optional project, and optional parent. The SQLite API validates parent relationships and rejects cycles. This is a local single-user implementation of the workspace structure; it does not run Colanode's server, collaboration, CRDT, or sync stack.

## Scope

- **Projects:** title, description, goal, next action, target date and planned/active/paused/done status. Milestones carry a due date and status; to dos can be assigned to a milestone. The board lets you move project status without opening each project.
- **Pages:** Markdown documents and nested folders attached to a space or project. Pages and project briefs use [Novel](https://github.com/steven-tey/novel) for rich text editing.
- **To dos:** title, details, to do/doing/done status, priority, due date, linked project, optional milestone, and assigned agent.
- **Study:** title, summary, Markdown body, learning objective, learning path, review date, source URL, linked project, and inbox/learning/reviewing/mastered status. Hackathon notes also carry the Devpost host. Study notes use Novel's editor.
- **Agents:** The local Codex SDK powers a personal workspace chat, and Scout retains its hackathon chat and tools. Additional agents can be named, described, linked, and assigned tasks; they can be connected later.
- **Devpost Scout:** its existing discovery dashboard and chat are preserved. A hackathon detail has **Add to study**, which creates and opens a linked hackathon study item.
- **Screen Studio:** browser screen or window capture with optional system audio, microphone and webcam overlay; local video library; trim, canvas ratio, background, padding, manual zoom/focus and speed controls; MP4/GIF export. Recordings can be linked to a workspace project and opened from its project page. Inspired by [OpenScreen](https://github.com/siddharthvaddem/openscreen).

Deleting a project or agent leaves related tasks and study notes intact and clears their links. Personal data is not committed; back up `data/workspace.db` if needed.

The Novel integration uses the local editor and stores its output as Markdown in the existing SQLite fields. Imported notes keep their original Markdown until you edit and save them. The editor offers headings, lists, checklists, links, quotes, code blocks and `/` block commands. A Markdown source mode is available, and notes containing tables or HTML embeds open in source mode to preserve those formats. In rich text mode, **AI write** sends the document title and bounded text around the cursor or selection to the locally configured Codex SDK for continuation, rewriting, an outline, or a custom instruction. Review the streamed preview, choose **Insert at cursor** or **Replace selection**, then save the note or page; closing or canceling leaves the stored document alone. This uses your signed-in Codex account and requires a network connection to the Codex service. It does not call Novel's hosted AI endpoint. The editor's image upload service is not connected.

Existing imported study items were initially grouped by their linked project without changing their bodies or source URLs. `python3 -m scripts.organize_learning_paths` conservatively splits the 42 items in **개인 학습 로드맵** into five topic paths and leaves two ambiguous references in the original path. It is safe to rerun and does not move notes you later organize yourself. Add a learning outcome to a path, an objective to each item, and a review date when you want it to appear in **Ready to review**.

`python3 -m scripts.seed_video_learning` adds eight production lessons to **자동 영상·Screen Studio 워크플로** and one Devpost submission checklist to the Scout hackathon path. It preserves the original imported items and links to the source records. The lessons cover storyboarding and storytelling from a reference, flat browser capture, reproducible VHS terminal footage, camera/cursor and voice/subtitle postproduction, multimedia production using licensed footage, code-driven motion, sound and FFmpeg, tool selection, and final video review. Rerunning the script leaves edited lessons and progress intact.

## Collected notes and personal import

The **Collected notes** tab keeps source records from March 2026 onward alongside the curated Projects, To Do and Study lists. It searches short messages and bare links as well as long notes. Source filters separate KakaoTalk self-chat, Slack self-DM, Codex/Claude prompts, extra CLI history entries, and the agents' final answers. Each record keeps its date and source pointer; it can be promoted to a project, task or study item without deleting the original.

This machine's import reads the KakaoTalk CSV in Downloads, the locally saved Slack self-DM export, `~/.codex/sessions`, `~/.codex/archived_sessions`, `~/.claude/projects`, and both CLI `history.jsonl` files. Final assistant answers are indexed separately from user-authored inputs. The scripts are `scripts/import_workspace_history.py` and `scripts/seed_personal_workspace.py`; the seed uses stable IDs and preserves later edits to existing workspace items. The data and extracted attachment text stay in gitignored `data/import_2026-03/`. Original extracted text is retained in `extracted_originals.jsonl` with file mode 0600; the searchable browser copy masks recognized credentials. Treat text in imported chats, documents and agent responses as source material, not instructions to run.

Text exports do not contain all binary media. Records with photos, files, screenshots, or missing pasted text are flagged in the tab and retain their source path or message link. Two locally available manuscript attachments have searchable text extracts, and three matching KakaoTalk photos have local file references. The attached `unified_raw.db` remains a referenced Drive/Notion data export rather than being merged wholesale into personal notes. Back up `data/import_2026-03/` with `data/workspace.db` if you want to preserve the raw evidence; it can contain credentials and private material.

## Screen Studio

Install `ffmpeg` and `ffprobe` on the server machine; on macOS, `brew install ffmpeg` provides both. The UI checks availability before enabling recording and import. Start recording from the Screen Studio tab, choose a screen or window in the browser picker, then stop and save. Enable microphone and webcam before starting if you want them in the output. System audio is included only when the browser and selected capture source provide it. The app requests capture permissions only after you press **Start recording**.

Videos are stored under `data/studio/` (or `$SCOUT_DATA_DIR/studio/`) with JSON metadata. The original file stays intact while you change trim and framing settings; an export creates a temporary MP4 or GIF download. The HTTP API supports `GET /api/studio/status`, `GET/POST /api/studio/recordings`, `GET/PATCH/DELETE /api/studio/recordings/{id}`, ranged `GET /api/studio/recordings/{id}/file`, `GET /api/studio/recordings/{id}/download`, and `POST /api/studio/recordings/{id}/export`. Uploads accept WebM, MP4 or MOV up to 2 GB. Back up `data/studio/` along with the workspace database if you want to retain your clips.

Choose a project at the top of Screen Studio before recording or importing to link the saved video. Existing videos can be reassigned in the editor. A project's **Videos** section opens its linked clips, and **New video brief** creates a project page with a shot list, narration plan, and submission checks. **Open learning path** leads to the filmed-demo curriculum. The source production guides are `build/FILM.md`, `build/TERMINAL.md`, `build/film/README.original.md`, and `.agents/skills/scout/SKILL.md` stage 7. The native Screen Studio editor does not yet automate the guides' 60 fps camera/cursor composition, VHS rendering, voiceover, or SRT pipeline; those remain separate tools in `build/film/`.

Browser capture cannot access system-wide cursor coordinates, so OpenScreen's automatic cursor zoom and native cursor effects are not included. The editor currently provides manual zoom and framing; captions and drawing annotations are not included. Long recordings collect chunks in browser memory until you stop them, so keep sessions moderate and export them before closing the tab.

## Local Codex

`./run.sh` installs the pinned Python Codex SDK in `.venv` on first run and starts the server with that interpreter. It uses the existing local Codex login; run `codex login` in a terminal if the Codex screen says it is unavailable. No API key is required for an existing ChatGPT Codex login.

The Codex tab creates resumable SDK threads. Chat titles and messages are kept in `data/workspace.db`; the SDK keeps its own conversation state under the local Codex account. Each turn receives a compact, current index of projects, to dos and study items. Codex can read the local database for more detail. Turns run with a read-only filesystem sandbox, so edits to projects, to dos and study notes happen through the workspace UI.

The Codex API provides `GET /api/codex/status`, `GET/POST /api/codex/chats`, `GET/DELETE /api/codex/chats/{id}`, and `POST /api/codex/chats/{id}/messages` (SSE `thread`, `delta`, `done`, `error` events). The server finishes and saves a turn even if the browser disconnects; reopen the chat to see the answer. `POST /api/codex/complete` is the separate one-off writing endpoint. It accepts a mode, title, instruction, and bounded text before/within/after the selection, streams `delta`, `done`, and `error`, and does not save a chat or modify a page.

## Local API

Each collection supports `GET /api/workspace/{collection}`, `GET /api/workspace/{collection}/{id}`, `POST /api/workspace/{collection}`, `PATCH /api/workspace/{collection}/{id}`, and `DELETE /api/workspace/{collection}/{id}`. Collections are `projects`, `milestones`, `learning_paths`, `pages`, `tasks`, `studies`, and `agents`. Requests and responses are JSON. Fields outside each collection's schema and invalid statuses, dates, URLs, or references return HTTP 400; unknown IDs return 404.

Example:

```bash
curl -X POST http://127.0.0.1:8780/api/workspace/projects \
  -H 'Content-Type: application/json' \
  -d '{"title":"My project","description":"What I am building","status":"active"}'
```

The SQLite store uses foreign keys and one connection per request so the threaded HTTP server can handle simultaneous UI calls. Its schema is in `scout/workspace.py`. The UI uses `web/src/workspace-context.tsx` to keep lists in sync after edits. The project/task/document concepts are implemented directly in the existing Python and React stack.
