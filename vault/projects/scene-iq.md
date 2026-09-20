---
slug: "scene-iq"
url: "https://devpost.com/software/scene-iq"
title: "Scene iQ"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 454
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/vision_ocr"
  - "substrate/transcript_audio"
---

# Scene iQ

> SceneIQ transforms raw video into structured, searchable scene intelligence using temporal reasoning, motion modeling, and interaction graphs for instant, timestamp-accurate retrieval.

[Devpost](https://devpost.com/software/scene-iq) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[graph_reasoning]] [[vision_ocr]]
**substrate** [[transcript_audio]]

**stack** custom-temporal-scene-segmentation, engine, ffmpeg, flask, numpy, opencv, persistent-multi-object-tracking, python, pytorch, retrieval, scene-graph-modeling, scipy, semantic, ultralytics-yolov8

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scene iq

## Body

Query-driven retrieval showing motion-aware scene matching with importance scoring and exact timestamp output. Demonstrates object detection and highlights limitations of traditional models in capturing missing relational context. Examples of generated scene graphs showing entity relationships such as riding, wearing, holding, and spatial positioning. SceneIQ analyzes a YouTube video, segments scenes, and enables semantic timestamp-based retrieval. SceneIQ retrieves the trophy lift moment using persistent character IDs and motion-aware ranking for instant timestamp navigation. Inspiration Video today is treated as a sequence of independent frames. But narrative video — sports, interviews, films, lectures — is not frame-based. It is event-based. While watching long-form content, we realized something simple: People don’t search for frames. They search for moments : “Goal celebration.” “Trophy lift.” “Two people arguing.” “Man driving car scene.” Existing systems detect objects per frame but fail to model: Temporal continuity Persistent identity Interaction dynamics Scene importance SceneIQ was built to shift video understanding from static detection to structured temporal intelligence. What it does SceneIQ transforms raw video into structured, searchable scene-level intelligence. It : Segments video into narrative-consistent scenes Detects and tracks entities persistently across time Models motion intensity and velocity Infers interactions between people and objects Builds scene-level semantic representations Ranks scenes by importance Enables timestamp-accurate natural language retrieval Instead of returning labels, SceneIQ returns: Structured moments. Example: Query: “Football World Cup trophy celebration” SceneIQ returns: Trophy detected Multi-person interaction cluster High motion spike Timestamp: 01:42:18 – 01:44:03 Importance score: 0.93 How we built it Video Input: → Structural Scene Segmentation (groups frames into narrative-consistent scenes) → Multi-Object Detection (identifies key entities in each frame) → Persistent Multi-Object Tracking (maintains identity across time) → Motion Intelligence Layer (analyzes movement patterns and intensity) → Interaction Graph Modeling (infers relationships between entities) → Scene Importance Scoring (ranks scenes by narrative significance) → Semantic Retrieval Engine (returns exact timestamps based on user query) Challenges we ran into Accomplishments that we're proud of -Fully local execution -Deterministic explainable pipeline -Structured scene-level abstraction -Temporal entity persistence modeling -Motion-aware importance ranking -Interaction graph reasoning Timestamp-accurate semantic retrieval -Modular architecture suitable for research extension Most importantly : SceneIQ understands evolving events - not isolated frames. What we learned Temporal continuity is more powerful than frame-level detection Motion dynamics reveal narrative significance Interaction density signals meaningful moments Structured representations outperform raw label outputs Efficiency and interpretability can coexist We also learned that narrative reasoning does not require massive transformer architectures. Carefully engineered temporal modeling can achieve strong semantic understanding. What's next for Scene iQ Graph Neural Network refinement for interaction graphs Transcript-aware multimodal fusion Cross-video narrative linking Zero-shot semantic query generalization Large-scale evaluation benchmarks Long term vision: Make video searchable by meaning. From: Video as media → Video as structured knowledge. <div