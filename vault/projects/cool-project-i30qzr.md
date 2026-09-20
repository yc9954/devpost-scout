---
slug: "cool-project-i30qzr"
url: "https://devpost.com/software/cool-project-i30qzr"
title: "SocialSense AR"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 669
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
---

# SocialSense AR

> Allowing the neurodivergent community to augment their reality into where they can thrive, powered by Computer Vision and AR (Meta Quest).

[Devpost](https://devpost.com/software/cool-project-i30qzr) · hackathon [[NexHacks]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: retrieval_grounding, revocation_withdrawal, sensor_fusion</sub>
**domain** [[accessibility]]
  <sub>weak: mental_health</sub>
  <sub>weak: video_visual</sub>

**stack** anthropic, augmented-reality, computer-vision, filternet, gemini, nextjs, oculus-gear-vr, openai, opencv, overshoot, python, sam, tcp, tensorflow

## Body

Inspiration Growing up alongside individuals on the autism spectrum and working with children with learning disabilities, our team saw how overwhelming everyday environments can be. Bright lights, visual clutter, constant motion, and overlapping conversations can trigger anxiety, shutdowns, or social withdrawal. Research shows, over 90% of autistic individuals experience sensory sensitivities, and nearly 70% of neurodivergent people have shown atypical sensory processing. In social settings, these challenges often lead to exclusion, as over 60% of people with ADHD report experiencing social rejection. Rather than asking neurodivergent individuals to adapt to overstimulating environments, we asked, What if the environment adapted to them? This question led to the creation of SocialSense. What it does SocialSense AR is a real-time mixed-reality system running on Meta Quest 3, powered by a multimodal agent named Vibe. Vibe interprets what the user sees and hears, then dynamically augments their environment to reduce sensory overload to support both focus and social interaction. Users can: Remove or remap triggering colors Dim or black out high-stimulus objects like screens and lights Blur background motion and suppress ambient noise with Focus Mode Activate Conversation Mode, which isolates the speaker, suppresses background conversations, tracks conversational context history, and highlights social cues such as tone shift or sarcasm. All features grounded in research literature. All features are controlled via natural language voice commands, allowing for low-friction interaction. How we built it SocialSense AR is built on a real-time, multimodal perception stack. We combine YOLO-based object detection with Meta’s Segment Anything Model (SAM) to identify and segment relevant visual assets in a 3D environment. Overshoot paired with Gemini Vision provides a reasoning feedback loop that evaluates assets in any novel environment. Audio and language understanding are powered by OpenAI Whisper, which enabled neurodivergent focused features such as speaker tracking, conversation summarization, and working-memory support. Whisper provides low-latency connectivity between audio commands and vision augmentation pipelines. A augmentation algorithm applies selective dimming, color remapping, motion blur, all in real time. Behind the scenes, complex perception and reasoning systems run continuously. For the user, the experience is much more simple. They are able to create a calm and clear world designed to help them thrive. Challenges we ran into One of our biggest challenges was developing on the Meta Quest 3, which has limited native support for running heavy AI and computer vision models directly on-device—especially within Unity. Real-time segmentation, object detection, and multimodal reasoning exceed what can be reliably hosted on the headset alone. To overcome this, we engineered a hybrid pipeline that effectively “unlocked” camera passthrough access and streamed visual data to an external compute system for processing. The results were then sent back to the headset, where we layered interactive AR augmentations in real time. This approach allowed us to maintain low latency while running state-of-the-art vision models that would otherwise be impossible on-device. Accomplishments that we're proud of We’re most proud of building a fully interactive, native augmented reality experience—not just a passive visual filter. SocialSense doesn’t simply alter how neurodivergent users see the world; it gives them direct agency to reshape it. By tightly integrating computer vision with AR interactions, we enabled users to dynamically control their sensory environment in real time, creating a system that is both adaptive and empowering rather than prescriptive. What we learned We learned how to deeply integrate computer vision pipelines into live augmented reality environments, moving beyond static overlays to perception-level transformation. More importantly, we learned how to design systems that allow users to define their own sensory boundaries—using AI not as a novelty, but as an accessibility layer that meaningfully changes how people experience the world around them. What’s next for this project As AR hardware continues to evolve, we see SocialSense transitioning from bulky headsets to lightweight, socially unobtrusive AR glasses. Miniaturizing the form factor is critical for adoption—especially for neurodivergent users who may feel uncomfortable drawing attention in public spaces. As AR glasses mature, SocialSense can become an everyday assistive layer: wearable, discreet, and seamlessly integrated into daily life. <div