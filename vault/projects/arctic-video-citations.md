---
slug: "arctic-video-citations"
url: "https://devpost.com/software/arctic-video-citations"
title: "Arctic - Video Citations"
hackathon: "THE FUTURE OF AI IS OPEN"
organization: "Snowflake"
winner: true
words: 206
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
---

# Arctic - Video Citations

> Grounded content is vital for GenAI Business use cases. The same applies for video...

[Devpost](https://devpost.com/software/arctic-video-citations) · hackathon [[THE FUTURE OF AI IS OPEN]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[document_pdf]]

**stack** arctic, llamaindex, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for arctic - video citations

## Body

Your assistant with playback citations + Snowflake Arctic Click play and watch from where the citation was mentioned Inspiration We love RAG applications (using GenAI to search documents) but what we think is cooler is doing RAG on videos. Watching a video, summarizing it, and then grounding answer to exact moments on the video is the goal of this project. What it does You load a video, it will summarize it and enable you to ask questions using Snowflake Arctic model. With the answer a citation will come with the exact moment the answer was mentioned. Automatic playback!. How we built it Using Snowflake Arctic model, Replicate and Streamlit. Challenges we ran into Chunking video data is complex, specially taking care of the timestamps for playback capabilities. Accomplishments that we're proud of The video chunking function, and the playback citations are the best accomplishments of this project. What we learned Arctic model is a great start, but the context window is too small! What's next for Arctic - Video Citations Adding more analysis on the videos, like topic chunking, fact sub-chunking. And topic/fact classification and video comparisons. For example: Grab 2 videos ,ask a question and compare what each video says about the same thing. <div