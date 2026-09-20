---
slug: "fire-cv"
url: "https://devpost.com/software/fire-cv"
title: "Fire CV"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 650
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Fire CV

> Fire safety real time training and education for people and their safely in simulated 3d fires and also provides safety guidance for real fires

[Devpost](https://devpost.com/software/fire-cv) · hackathon [[NexHacks]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
  <sub>weak: vision_ocr</sub>
**domain** [[disaster_emergency]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** cloudflare, gpstracking, html, node.js, overshoot, python, react, three.js, typescript

## How they structured the write-up

- inspiration:
- our 3d model:
- our computer vision model with fire cv:
- challenges we ran into
- accomplishments we're proud of

## Body

Fire Building Educator For Gates-Hillman System Team Inspiration: When one of our team members was in middle school, his school was attacked by an arsonist. Although everyone eventually made it out, students were hurt at the exit. The experience left a lasting impression: in emergencies, panic and uncertainty can be just as dangerous as the threat itself. Most buildings still rely on static exit signs and generic floor plans that don’t adapt to blocked paths, smoke, or real-time hazards. That gap inspired our project. We wanted to build an emergency evacuation system that doesn’t just tell people where exits are, but actively guides them to safety using real-time data, 3D maps, and intelligent path planning. We use multi-agent heuristics to ensure that every user is given a constantly-updating optimal path to safety. Moreover, to account for swarm mechanics, we use the Hungarian algorithm, ensuring users are dispersed across safe exits to prevent crowding. Through this project, we aim to empower people to make safer decisions when every second counts. Our 3d model: We created a high-fidelity digital 3d transparency model of the Gates Hillman Center, and we developed a custom extrusion pipeline using Three.js. By parsing 2D architectural floor plans, we programmatically projected wall heights and geometries to generate an accurate 3D structural model. This approach ensured that the final environment maintained precise spatial proportions and reflected the building's complex layout. Our Computer Vision Model with Fire CV: We developed an image retrieval system by indexing a large-scale dataset on AWS. To enable efficient spatial discovery, we leveraged a Vision Language Model (VLM), specifically a Qwen-based encoder, to transform raw images into high-dimensional embeddings. These vectors were stored in a FAISS index for high-performance Approximate Nearest Neighbor (ANN) search. By querying this index, we were able to cross-reference visual features with historical GPS tracking and gyroscope data to pinpoint the user's location in a 3d model at the highest precision, allowing us to estimate precise geographical coordinates for any given image. Crucially, our system must perform with minimal latency, which is why we use Overshoot's real-time API to tag images and query their location. Without their streaming framework, user feedback on hazards in their environment would not be able to be taken into account fast enough. This latency reduction at scale allows our system to handle many users simultaneously, allowing us to use otherwise time-intensive algorithms to plan optimal paths for all of them individually. This is critical - we're able to achieve load balancing on evacuation paths. Challenges we ran into Getting the 3d model was incredibly challenging. While they're generally decent at taking multimodal input, AI models aren't powerful enough to generate accurate 3D outputs. We started with trying to render the building models in Blender, but the process was too manual and would not be able to be accomplished accurately at scale. Another major challenge was real-time localization. Accurately determining a user’s position indoors, especially during an emergency with low visibility and sensor noise and imprecise GPS tracking is extremely difficult. We focused on indexing precise coordinates using image matching of the user's environment, and relying on fast, sublinear time location retrieval and obstruction detection to make real-time decisions. Accomplishments we're proud of Built a camera-only indoor localization system that works with with GPS and CV. Created a real-time evacuation guidance engine that dynamically reroutes users as fires and hazards evolve Designed accurate multi-floor 3D models of real CMU buildings for evacuation training Implemented AI-generated fire scenarios with realistic fire and smoke propagation Developed graph-based navigation with dynamic path blocking for emergency-safe routing Enabled live video analysis → guidance delivery with low-latency WebSocket updates Integrated crowd-aware exit assignment to reduce bottlenecks during evacuation Built a quantitative safety evaluation system for evacuation performance and decision quality Unified training simulation and real-world emergency response in one platform Made the system work on ordinary smartphones, no special hardware required <div