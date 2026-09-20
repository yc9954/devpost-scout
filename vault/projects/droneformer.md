---
slug: "droneformer"
url: "https://devpost.com/software/droneformer"
title: "DroneFormer"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 794
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# DroneFormer

> Controlling UAVs with natural language!

[Devpost](https://devpost.com/software/droneformer) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[disaster_emergency]]
**user** [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** ml, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for droneformer

## Body

POCARI SWEAT!!!!!!!!!! It knows what it wants Inspiration Building domain-specific automated systems in the real world is painstaking, requiring massive codebases for exception handling and robust testing of behavior for all kinds of contingencies — automated packaging, drone delivery, home surveillance, and search and rescue are all enormously complex and result in highly specialized industries and products that take thousands of engineering hours to prototype. But it doesn’t have to be this way! Large language models have made groundbreaking strides towards helping out with the similarly tedious task of writing, giving novelists, marketing agents, and researchers alike a tool to iterate quickly and produce high-quality writing exhibiting both semantic precision and masterful high-level planning. Let’s bring this into the real world. What if asking “find the child in the blue shirt and lead them to the dinner table” was all it took to create that domain-specific application? Taking the first steps towards generally intelligent embodied AI, DroneFormer turns high-level natural language commands into long scripts of low-level drone control code leveraging advances in language and visual modeling. The interface is the simplest imaginable, yet the applications and end result can adapt to the most complex real-world tasks. What it does DroneFormer offers a no-code way to program a drone via generative AI. You can easily control your drone with simple written high-level instructions. Simply type up the command you want and the drone will execute it — flying in spirals, exploring caves to locate lost people with depth-first search, or even capturing stunning aerial footage to map out terrain. The drone receives a natural language instruction from the user (e.g. "find my keys") and explores the room until it finds the object. How we built it Our prototype compiles natural language instructions down into atomic actions for DJI Tello via in-context learning using the OpenAI GPT-3 API. These actions include primitive actions from the DJI SDK (e.g. forward, back, clockwise turn) as well as custom object detection and visual language model query actions we built leveraging zero-shot image and multimodels models such as YOLOv5 and image processing frameworks such as OpenCV. We include a demo for searching for and locating objects using the onboard Tello camera and object detection. Challenges we ran into One significant challenge was deciding on a ML model that best fit our needs of performant real-time object detection. We experimented with state-of-the-art models such as BLIP and GLIP which either were too slow at inference time, or were not performing as expected in terms of accuracy. Ultimately, we settled on YOLOv5 as having a good balance between latency and ability to collect knowledge about an image. We were also limited by the lack of powerful onboard compute, which meant the drone needs to connect to an external laptop (which needed to serve both the drone and internet networks, which we resolved using Ethernet and wireless at the same time) which in turn connects to the internet for OpenAI API inference. Accomplishments that we're proud of We were able to create an MVP! DroneFormer successfully generates complex 20+ line instructions to detect and navigate to arbitrary objects given a simple natural language instruction to do so (e.g. “explore, find the bottle, and land next to it”). What we learned Hardware is a game changer! Embodied ML is a completely different beast than even a simulated reinforcement learning environment, and working with noisy control systems adds many sources of error on top of long-term language planning. To deal with this, we iterated much more frequently and added functionality to deal with new corner cases and ambiguity as necessary over the course of the project, rewriting as necessary. Additionally, connectivity issues arose often due to the three-tiered nature of the system between the drone, laptop, and cloud backends. What's next for DroneFormer We were constrained by the physical confines of the TreeHacks drone room and obstacles available in the vicinity, as well as the short battery life of the Tello drone. Expanding to larger and more complex hardware, environments, and tasks, we expect the DroneFormer framework to handily adapt, given a bit of prompt engineering, to emergent sophisticated behaviors such as: Watching over a child wandering around the house and reporting any unexpected behavior according to a fine-tuned classifier Finding that red jacket that you could swear was on the hanger but which has suddenly disappeared Checking in “person” if the small coffee shop down the street is still open despite the out-of-date Google Maps schedule Sending you a picture of the grocery list you forgot at home DroneFormer will be a new type of personal assistant — one that always has your back and can bring the magic of complex language model planning to the embodied real world. We’re excited! https://medium.com/@sidhantbendre22/hacking-the-moonshot-stanford-treehacks-2023-9166865d4899 <div