---
slug: "project-n4altjz2bihc"
url: "https://devpost.com/software/project-n4altjz2bihc"
title: "BWI (Brain Wheelchair Interface)"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 718
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "substrate/video_visual"
---

# BWI (Brain Wheelchair Interface)

> Control ANY wheelchair with your mind.

[Devpost](https://devpost.com/software/project-n4altjz2bihc) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[health_clinical]] [[mental_health]] [[scientific_research]]
**substrate** [[video_visual]]

**stack** 3d, 3dprinting, arduino, cad, cyton, daisy, openbci, python, wheelchair

## How they structured the write-up

- control any wheelchair with your mind
- inspiration
- 🔧 how we built it
- challenges we faced
- what we learned
- what's next
- impact

## Body

BWI (Brain Wheelchair Interface) Control ANY wheelchair with your mind Inspiration Millions of people need a wheelchair for mobility, but many have weak motor control made traditional wheelchairs, whether manual or joystick-controlled, nearly impossible to use independently. Realizing this struggle that people face with something as fundamental as moving from room to room sparked a question: What if thought alone could be enough? There are approximately 5.4 million people in the United States living with some form of paralysis . For many in this community, existing mobility solutions fall short. Traditional wheelchairs require hand dexterity. Sip-and-puff systems demand consistent breath control. Voice-activated systems struggle in noisy environments. But the mind? The mind remains sharp, capable, and ready even when the body cannot follow. Brain-computer interfaces (BCIs) have shown remarkable promise in research labs, but remain inaccessible and prohibitively expensive. We wanted to change that by creating a universal, affordable brain-controlled wheelchair system that could retrofit any existing wheelchair. This is for everyone who has the will to move but not the means. 🔧 How We Built It Hardware Architecture 1. EEG Signal Acquisition 16-electrode EEG headset for capturing brain signals Cyton and Daisy boards for dual-channel signal processing E-clips attached to the ears for proper grounding 2. Universal Wheelchair Adapter Custom motor controllers with overlap-fit design No permanent modifications required Compatible with standard manual and powered wheelchairs 3. Safety & Navigation System Real-time object detection with Overshoot AI Central dashboard for system control and monitoring Automatic emergency braking when hazards detected Overshoot AI Integration Overshoot AI powers our safety system by providing real-time object detection and collision avoidance. The system processes live camera feeds to identify obstacles, people, and hazards. When danger is detected, it automatically overrides user commands to prevent accidents. Visual warnings appear on the central dashboard , giving users real-time feedback on their environment and system status. Signal Processing Pipeline The brain signals undergo processing stages: $$\text{Raw EEG} \xrightarrow{\text{Filter}} \text{Cleaned Signal} \xrightarrow{\text{Feature Extraction}} \text{Control Commands}$$ We detect motor imagery patterns —electrical signals generated when users imagine movement: Forward : Imagining pushing forward Turn Left/Right : Imagining turning the head Stop : Relaxed baseline state The system maintains low latency to ensure responsive control: $$\text{Total Latency} = t_{\text{acquisition}} + t_{\text{processing}} + t_{\text{motor}} < 750\text{ ms}$$ Software Stack EEG Headset → Signal Processor → Classifier → Motor Controller ↓ Dashboard & Safety Monitor ← Overshoot AI Python for signal processing and classifier Overshoot AI API for obstacle detection Arduino for motor control Dashboard for centralized control and monitoring Challenges We Faced Signal Variability & Noise EEG signals are incredibly noisy with amplitudes in the microvolt range \(\approx 10-100 \mu V\). We solved this by adding e-clips to the ears as grounding points , which eliminated electrical interference and gave us clean, reliable signals. Sampling Rate Delays Our initial sampling rate caused latency between thought and action, a critical safety issue. We optimized the Cyton and Daisy boards and implemented a ring buffer architecture to reduce total system latency to under 100ms for responsive control. What We Learned Technical: BCI signal processing, real-time embedded systems, the critical importance of proper grounding, and integrating AI safety systems like Overshoot AI. Personal Growth: Building for someone you love changes everything. The 5.4 million people with paralysis each represents a unique story and dreams of independence. What's Next Improved classifier models with transfer learning to reduce calibration time Hybrid control : Combine BCI with minimal physical input for increased reliability Enhanced Overshoot AI integration for more sophisticated navigation Clinical trials with occupational therapists and users with mobility impairments Open-source the design so others can build and improve upon our work Impact BWI is a promise to the 5.4 million people living with paralysis that independence is within reach. In the U.S. alone, over 6 million people rely on wheelchairs for daily mobility, including 302,000 individuals living with spinal cord injuries, the highest-need and highest-cost population. For many, care costs reach $500K–$1M in the first year after injury and $113K–$184K every year thereafter, turning mobility into a lifelong financial and emotional burden. By making brain-controlled wheelchairs affordable, intuitive, and universally compatible, BWI aims to break that cycle, restoring not just movement, but dignity, autonomy, and joy to millions who deserve more than survival. Built for everyone fighting to move freely. https://github.com/larcxx/MindControlledWheelchair <div