---
slug: "zoneout-atz5pe"
url: "https://devpost.com/software/zoneout-atz5pe"
title: "ZoneOut"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 717
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ZoneOut

> Zoned out during a lecture? Your very own lecture buddy is here to save you! With real-time Q&A based on audio, text & visual context from the lectures, you'll be acing your classes again in no time!

[Devpost](https://devpost.com/software/zoneout-atz5pe) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** chromadb, colpali, openai, rtms, vlm, zoom-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Homescreen with Chat from Demo Inspiration We've all been in classes or meetings where we ZoneOut, even if for a few seconds, and came back to see that the cure to cancer has been invented! Inspired by attending online lectures this Friday (we're dedicated students), we found out that this isn't as uncommon as you'd think. As a matter of fact, the average retention rate of a student after just 45 mins of online learning is just 61% , which is HIGHER than the average person. Moreover, the average drop in engagement is 87% (scaling exponentially!) on average, in meetings with larger sets of participants. What it does ZoneOut utilizes textual, visual & audio contexts from meetings, enabling our AI assistant to teach, revise & explain any concept, In-Depth & in Real-Time , to users to maintain higher levels of retention, productivity & engagement. How we built it We built ZoneOut with a complex, yet execution directed architecture, developed completely on Windsurf . We used the Zoom API to connect the client to a Real-Time Media Server (RTMS) via a Handshake protocol, and consequently sampled data at microintervals as well as based on when a sentence/section of an idea being discussed finished. We collected textual data from the chat, audio data via live transcripts and visual screensharing/camera data with help from Zoom's API. We then used OpenAI for embedding the text & images with Chain-Of-Thought (CoT) Reasoning to keep context well-fitted and connected, independent of context window sizes and to keep images & text associated with one another. We also used parallel computation to allow us to index this data using Chroma concurrently, associating images with concepts in both audio & textual formats in different timestamps. Finally, we used a similarity search RAG system with ChromaDB for the audio/transcript & textual data, and a vision-based RAG system on ColPali (VLM) , which we accelerated using a caching system that we developed, allowing us to use it without reloading it into memory again & again. The outputs of both RAG systems are then passed through OpenAI's API to format it nicely. We also optimized sampling parameters to avoid hallucinations caused by excess external information or misunderstanding contextual information. We then send this data back to the client, who's now back in the loop of everything that's happening! Challenges we ran into Originally, the RTMS faced issues with streaming audio & video. After a lot of debugging & troubleshooting, we found & cured the error by handling edgecases through intensive vision programming back & forth, sending our sample code to the Zoom team so they can debug other teams. Then, our VLM workflow turned out to be too slow as the VLM was being loaded into memory repeatedly. So again, after coding a lot of reacharounds, we finally implemented our own caching system to supercharge our VLM, which now works with various forms of handwriting effectively. We also faced hallucinations wherein the model knew information it should not, and misinterpreted information it had. We cured this using indexing & CoT, to reach the product we have today! Accomplishments that we're proud of This hackathon has been a proud technical moment for all 3 of us. Our achievements stem from our challenges. We very quickly figured out the edge case of professors writing on whiteboards, both virtual & real, instead of explaining things like equations. So we developed a multi-language model workflow to work around. Another proud accomplishment was improving the Zoom RTMS repo, as we were the first people that figured it out, turning our curiosity into open source contributions in Zoom's repos. Next was integrating a complex parallel workflow to interpret & contextualize images, text & audio data altogether, particularly because of how LLMs & VLMs can be very funky sometimes. After that, was when we implemented our own caching system to boost our VLM system, after having faced a barrage of vision problems. Finally, was our creative use of prompt engineering, context windows & frontend-backend structuring for Windsurf to swap between entirely different frontend frameworks (HTML/CSS & React) & even simple backend worflows without breaking the frontend or the backend, letting us build very quickly, despite initial samples & software not being completely compatible, causing issues in the webSockets & handshake protocol, amongst other incompatibility issues. <div