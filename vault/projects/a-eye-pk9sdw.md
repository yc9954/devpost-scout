---
slug: "a-eye-pk9sdw"
url: "https://devpost.com/software/a-eye-pk9sdw"
title: "A-Eye"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1240
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# A-Eye

> We built a real-time tool that converts live camera input into audio instructions, helping the visually impaired navigate unfamiliar locations with more independence without compromising safety.

[Devpost](https://devpost.com/software/a-eye-pk9sdw) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[transportation]]
**user** [[developer]] [[general_public]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** asyncio, bytetrack, cloudflare, elevenlabs, fastapi, mongodb, opencv, python, typescript, ultralytics

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a-eye

## Body

Picture of the glasses themselves with the phone case and elastic band. Picture of how a user may wear the glasses on their head. Diagram of how our computer vision model detects various objects in the camera frame, like a chair, door handle, and a person. Inspiration Most of us take walking for granted. We glance at a street corner and instantly know if it's safe to cross. We spot a door handle without thinking. We read a sign, check our surroundings, and keep moving, all in a single second. For the 43 million people living with blindness worldwide, none of that is automatic. Our teammate's neighbor has been blind since birth. Watching him navigate a familiar route, cane sweeping, checking his surroundings at every curb, relying on muscle memory built over years of careful trial and error, made something clear to us: the tools he depends on haven't changed much in decades. White canes feel what's directly ahead. GPS tells you where to turn. But nothing tells him there's a step down, that he's drifted off the sidewalk, or that the door he's looking for is three feet to his left in rooms that he has never been in before. A-Eye was born from that observation. A promise to give the world's most fundamental freedom back to the people who need it most. Not a workaround nor a gadget. A friend built into a pair of glasses that sees the world and speaks it right back to you at any time. What It Does A-Eye is a pair of glasses that uses computer vision to guide the blind, providing instructions on where to go and how to navigate safely. The system guides users to their destination while helping them navigate around obstacles and hazards in their path. With real-time audio guidance, users can confidently navigate both indoors and outdoors without assistance. When the user puts it on, a series of subsystems is activated sequentially: VisionTool : Captures live camera frames and runs YOLOv8 with continuous object tracking, assigning unique IDs to all detected obstacles across frames to eliminate app hallucinations and flicker before any audio is uttered. DepthGauge : Applies a focal-length formula using real-world object dimensions (a person at ~0.45m wide, a car at ~1.8m wide) to convert bounding box sizes into calibrated distance estimates, allowing for precise instructions like "person ahead, 3 feet." SurfaceClassifier : Performs real-time semantic segmentation of the ground plane, distinguishing sidewalks from roads and curbs, making sure safety warnings happen the moment the user drifts toward incoming traffic. RouteCreation : Detects whether the user is indoors or outdoors and automatically switches navigation modes, activating Exit-Seeking mode indoors to locate and guide the user toward a door and handle before handing off to GPS-based outdoor routing. DoorAgent : When indoors, isolates door and handle detections from the vision stream and generates thorough verbal instructions for locating, approaching, and physically opening the exit, including handle type identification (lever, knob, push bar). SpeechController : Manages a priority-lane audio queue where critical warnings (e.g., "STOP" ) instantly interrupt all other speech, while a smart deduplication layer prevents audio spam, backed by ElevenLabs for synthesis with a local fallback to ensure guidance never goes silent. MapsInstructions : Pulls live turn-by-turn walking directions from Google Maps and translates compass bearings into spatial clock-face instructions (e.g., "turn left at 10 o'clock" ), combining GPS-level routing with immediate physical safety monitoring in one experience. How We Built It A-Eye is built as a thin-client / heavy-server system designed for real-world wearability: Vision : YOLOv8-small (Ultralytics) with ByteTrack multi-object tracking for persistent ID assignment; yolov8-seg for real-time ground surface segmentation Distance Estimation : Custom focal-length pipeline with class-specific real-world dimensions calibrated per object class Door Detection : YOLOv8 fine-tuned on the DoorDetect dataset for door and handle localization Speech : ElevenLabs API for natural voice synthesis with a priority queue controller Routing : Google Maps Directions API with a bearing-to-clock-face translation layer Streaming : Cloudflare Tunnels + WebRTC allowing an iPhone to stream video to a laptop for processing and receive audio instructions back in real time Telemetry : MongoDB Atlas for structured event logging of all detections, decisions, and safety warnings; raw video is never stored Core Stack : Python 3, FastAPI, OpenCV, asyncio Challenges We Ran Into Latency Budget : The full pipeline, including capture, network, inference, TTS, network back, and playback, had to stay under 500ms for safety-critical warnings to be useful. We resolved this by bypassing ElevenLabs entirely for CRITICAL-priority alerts and routing them directly to local TTS, cutting response time to under 50ms. Audio Overload : Early builds announced every detection the moment it appeared, making the system fully unusable within seconds. Designing the deduplication layer with per-class cooldown timers and the priority interrupt system required many rounds of iteration to feel calm rather than chaotic. Surface Classification Edge Cases : Driveways, painted crosswalks, and bike lanes consistently confused the sidewalk/road classifier. We introduced a confidence threshold; below 70%, the system stays silent rather than issue a potentially wrong warning. Indoor Positioning Without Infrastructure : GPS drops indoors and most buildings aren't mapped at the room level. We developed a vision-first fallback, using object class distribution (ceiling tiles, floor patterns, doors) as an indoor/outdoor signal rather than relying on GPS fixes alone. Accomplishments That We're Proud Of End-to-End Working System : A-Eye successfully demonstrates the full pipeline, from a live iPhone camera stream through real-time obstacle detection, surface classification, door guidance, and turn-by-turn navigation, all delivered through natural voice with no screen interaction required. Priority Speech Architecture : Building a speech controller that feels genuinely calm and useful is harder than it sounds. The priority queue, deduplication, and multi-engine fallback working together in real time is one of our most technically satisfying achievements. Indoor/Outdoor Integration : Automatically detecting environment transitions and switching navigation modes without any user input was a fundamental engineering challenge that no existing consumer product has solved cleanly yet. Privacy-First Telemetry : Logging rich enough data for developers to debug and improve the system, while making sure no raw video ever leaves the device, required careful architectural decisions we're proud to have made from day one. What We Learned Building A-Eye gave us relevant experience at the intersection of real-time computer vision, audio UX design, and accessibility engineering. We learned that the hardest problems weren't the AI models that govern these systems, which are largely solved, but the orchestration layer: when to speak, what to say, how to prioritize, and when to stay silent. We also gained a genuine appreciation for how high the bar is in assistive technology. A bug in a productivity app is annoying. A wrong warning in a navigation system for a blind person crossing a street is a safety issue of the most important degree. That weight and responsibility shaped every design decision made here. What's Next for A-Eye Facial Recognition & Social Context : Recognize friends and family as they approach, whispering their name, and describe social cues like expressions or a wave to make interactions more natural Precision Object Search : Let users ask "find my keys" or "where is the remote" ; the AI guides their hand directly to specific items using audio cues Real-Time OCR : A high-speed reading mode that scans menus, labels, and signs, not just reading text aloud, but summarizing documents quickly or surfacing specific information like expiration dates on command <div