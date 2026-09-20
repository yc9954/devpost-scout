---
slug: "firstframe"
url: "https://devpost.com/software/firstframe"
title: "FirstFrame"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 1277
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# FirstFrame

> FirstFrame lets studios review AI-generated video in seconds, not after the full render. It streams each scene as it’s ready, cutting review waits while preserving provenance and secure storage.

[Devpost](https://devpost.com/software/firstframe) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** blackblazeb2, genblaze, gmicloud

## How they structured the write-up

- the problem
- what we built
- what that changes
- how it works, in one picture
- try it without an account
- why it holds up
- what's next

## Body

FirstFrame FirstFrame architecture diagram FirstFrame Watch the spot while it is still rendering. TL;DR Generative video makes you wait for the file before you are allowed to look at it. We killed that wait. A spot starts playing 9.3 seconds in, while it is still being generated. The full render of the same job takes 65.7 seconds. That is 7.1× faster to the moment a human can decide , measured by the app itself on job j_47cdc2 , and still live on the deployed instance so you can open it and check the number. Reject a bad take in the middle of the render , in plain English. The note goes into the next attempt and the refined take joins the same player, no reload, no second link. Approving seals the master for 30 days. Not by policy, by physics: storage itself refuses the delete. Every spot also carries its own provenance inside the video file, so it survives being downloaded and re-uploaded. No account, no key, no card. The deployed instance generates real imagery for anyone who opens it. We improved the SDK on the way , and sent four fixes back upstream. The gap widens with the length of the spot. Full render waits for every scene. First frame waits for one. Two clocks, one spot, both started together. The top one stops when a human can first judge the work. The bottom one stops when the render finishes. Everyone else only has the bottom clock. The problem A small studio ships about 40 AI-generated product spots a week. They reject roughly a third of them. Here is how that rejection actually happens. Someone writes a brief, presses generate, and then waits three to five minutes doing something else. The file arrives. They open it, watch four seconds, and say no. The shot was wrong from the first frame. So the person spent four minutes to learn something that was visible at second three, and then they do it again. Four minutes per attempt is the ceiling on how good the work can get, because that is how many attempts fit in an afternoon. Nothing about that is a generation problem. It is a delivery problem. Everyone waits for the file to close before anyone is allowed to look at it. What we built FirstFrame is a review room where the spot starts playing before it is finished. You paste a brief and press New spot. About nine seconds later there is video on screen and you can already tell whether it is right, while the rest of the scenes are still being generated behind it. No progress bar, no email when it is done, no downloading a file to find out. If it is wrong, you say why. Type "too dark, and lose the people in the background" on the scene you do not like. That note goes straight into the next attempt, the new take appears in the same player without a reload, and the take you rejected is kept as evidence of what changed and why. If it is right, you approve it. The master gets sealed the moment you do. For the next 30 days nobody can delete or overwrite it. Not you, not us, not a script with a bug in it, not someone with a stolen password. The client's deliverable is the client's deliverable. Every spot carries its own receipts. Which model made each scene, what the prompt was, which takes were rejected on the way, and a hash of every asset that went in. It travels inside the video file itself, so it survives being downloaded, moved and re-uploaded. Press Verify and the room re-checks it against the copy sitting in storage right now, not against what it remembers. What that changes before with FirstFrame Time to a first opinion 3 to 5 min 9.3 s Rejecting a bad take after paying for the whole render during it Attempts in an afternoon a handful as many as you have opinions That last row is the one that matters. Four minutes per attempt is the real ceiling on how good a spot can get, because it decides how many attempts fit in an afternoon. Take the wait out and the same reviewer, in the same afternoon, gets to be far pickier. How it works, in one picture Each scene is generated, cut into two-second pieces, and pushed to Backblaze B2 the instant it exists. The player is attached to a playlist that keeps growing under it. That is the whole trick, and it is why the first frame does not have to wait for the last one. Backblaze B2 is doing more than holding files here. It is what makes the master untouchable after approval, it is what lets a client's reviewer watch the approved cut through a key that physically cannot write, delete or even look at anything else, and it is what cleans up after a render that dies halfway through so nobody pays for the debris. Try it without an account The deployed instance generates real images with no API key, no card and no signup. Open the review room, paste a brief, and watch a spot get built. No setup, no credentials, nothing to install. Why it holds up The architecture is portable, not a trick. Incremental streaming works on any storage account, with nothing special switched on. There is no premium feature holding the product up and no configuration a customer has to beg for. The speed comes from publishing each scene the instant it exists instead of at the end, which is a design decision, not a purchase. Nothing here claims to work because a function returned success. The Object Lock proof issues a real delete against the sealed master and asserts the refusal. The permissions proof re-authenticates with the key it just created and confirms it gets denied a write and a listing. The manifest is pulled back out of the finished video and hash-compared before we are willing to call it verifiable. There are 358 executable assertions across the pipeline and the server, and one command runs all of them and exits non-zero the moment any of it stops being true. It stays up when storage does not. Every storage call is metered, the app backs off instead of hammering, playback keeps serving, and an approval that lands during an outage seals the master automatically once storage returns, with nobody re-approving anything. That is production behaviour, wired in from the start. We improved the SDK we built on. Four defects found while building, sent back as three pull requests and an issue , each with a reproduction, a root cause and tests that fail without the fix. One of them breaks the zero-key quickstart in the SDK's own README on a clean install. Another breaks the example the SDK ships, on its first line. What's next Per-scene approval, so a spot can ship while one shot is still being refined. Real video models through bring-your-own-key, so a studio sees its own pipeline instead of ours. And publishing the two generation providers we had to write, because "evaluate this thing end to end without credentials" turned out to be everybody's problem, not just ours. For the technical judges The engineering write-up lives in the repository, with every claim linked to the line of code that does it: the storage architecture and why the prefix layout is the data model, Object Lock including the subtlety that separates a screenshot from a real guarantee, the scene DAG with its fan-in, the vision judge, and the provider failover you can trigger on camera. github.com/migarci2/firstframe <div