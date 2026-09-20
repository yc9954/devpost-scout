---
slug: "magical-girl-os"
url: "https://devpost.com/software/magical-girl-os"
title: "Lumi Lens"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 1194
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Lumi Lens

> Where neurodivergent support creates a fun, engaging experience! Lumi Lens gamifies socialization and reading emotions with playful overlays and AI dialogue. Social interaction is no longer daunting!

[Devpost](https://devpost.com/software/magical-girl-os) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[video_visual]]

**stack** deepface, google-gemini, python, raspberry-pi, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lumi lens

## Body

Working Display on Glasses Emotion Detector Widgets TLT Screen for Glasses (before it broke…) App Icon Inspiration Our inspiration for this project stemmed from a need within the neurodivergent community: the challenge of identifying faces and interpreting emotions in real time. Social situations can be overwhelming, especially in high stress contexts, and we wanted to create glasses that provide a supportive, assistive layer to help people navigate those moments and respond with confidence. To align with the hackathon’s whimsical theme, we reimagined the experience as if stepping into an isekai inspired world, where everyday interactions become part of a magical adventure. Many neurodivergent people are drawn to anime and the sense of wonder it creates. Lumi Lens embraces this by helping users discover their inner magical girl, adding playful overlays, hearts, and progress bars powered by automatically generated AI dialogue that adapts to emotion. By gamifying social interactions, Lumi Lens transforms stressful moments into opportunities to unlock hidden powers and approach connection with a sense of magic and joy. What it does Lumi Lens begins by recognizing or simulating an emotional state happy, neutral, or upset. Once an emotion is detected, the system uses AI dialogue generation to craft a short, whimsical response that feels like a magical sidekick whispering encouragement. That response, along with playful visual elements like hearts and progress bars, is then displayed. The output will appear on the camera overlay, on the prototype glasses display. The result is an experience where emotion is transformed into magical dialogue and visuals making social interaction feel much less overwhelming and more like stepping into a supportive, whimsical adventure. How we built it We combined hardware prototyping, iOS development, and AI integration into one magical experience. Our prototype glasses are powered by a small microcontroller and OLED display, which can show icons, hearts, and playful cues. On the software side, we created an iOS app that overlays supportive AI-generated dialogue and whimsical visuals on top of the camera feed. Instead of focusing on rigid pipelines, we focused on crafting the feeling of transformation. When an emotion is detected or selected, Lumi Lens responds with glowing progress bars, sparkling overlays, and dialogue that feels like a magical sidekick whispering you some guidance. The result is a system that turns everyday interactions into moments of wonder like unlocking hidden magical girl powers in the middle of real life. We split tasks between each other for efficiency. Eva integrated the Gemini API and was our main design lead. Susan engineered the hardware and glasses, as well the connection between devices. Sema designed and helped integrate the UI, and Jennifer programmed the iOS app along with the facial recognition software onto the Raspberry Pi. Challenges we ran into Our original plan for live face and emotion recognition ran into hardware and software roadblocks, which pushed us to design a simulation mode so the demo could still bring the vision to life. Communicating between the glasses and the phone app required more setup than we anticipated. We had to troubleshoot the WiFi connection between the Raspberry Pi and the iPhone. Time pressure forced us to adapt quickly. We had to cut key features, such as documenting dialogue context with a microphone, but in the future we plan to integrate them further! Due to a wide variety of features, mainly being the physical design and hardware, we had to go for material runs which took time. For instance, we needed to obtain batteries and adhesives, which wouldn’t have been a problem if we committed solely to software. Due to our inexperience, most of our time was spent learning how devices, like the Raspberry Pi, and tools, like XCode, operated before we could use them to create our project. We found ourselves short on time after we solidified our framework since we couldn’t develop until later. Accomplishments that we're proud of We were able exercise a multitude of skills, including hardware engineering, app development, and AI integration. We learned Swift and Python on the fly, having to distinguish which functions to attribute to the Pi or the iOS app. Additionally, we had to troubleshoot a bunch of ways to connect the devices. In the end, we were able to get our AI to send information to each other through a shared WiFi connection. Being able to creatively adapt to challenges and improvise accordingly, even if that meant shifting from our original vision. Creatively building a unique hardware glasses prototype and a software demo mode. Working together, making our idea a reality, with the power of friendship! What we learned We started as beginners, but this project challenged us and forced us to level up our abilities. We set up GitHub for the first time (using it for real outside of school homework) and learned basic collaboration, such as cloning, branching, pull requests, and resolving merge conflicts. We learned to navigate Visual Studio Code and Xcode, figuring out how to manage projects, signing, and iPhone deployment. We learned Swift (and one person learned Python) from zero and built a working overlay UI with live updates. We created our first transparent overlay on top of a camera view, made possible by experimenting with external display mirroring to glasses. We were able to integrate an API key securely in a mobile app, seeing how the program can call for Gemini API to generate short adaptive lines. We explored the basics of emotion/vision pipelines and why real-time CV is hard on limited hardware, then designed simulation paths to keep the experience testable. We practiced rapid prototyping under pressure: scoping features, adding fallbacks (.txt files, on-screen controls), and keeping the user experience magical even when the hardware fought back. Overall, we learned that with hard work, dedication, and teamwork, we can create anything we put our minds to! What's next for Lumi Lens We want to bring the original vision from our flowchart to life and ship a polished, magical version of Lumi Lens. The next chapter begins with reconnecting live emotion detection through a Raspberry Pi or on-device ML so emotions can stream directly into the app in real time. From there, we’ll strengthen the bond between the phone and the glasses, ensuring dialogue and icons appear instantly on both. This would be a way to step into a magical world and embrace your inner magic that all neurodivergent have. Lumi Lens would also grow beyond just happy, neutral, or upset, expanding into a richer emotional vocabulary with tailored AI responses that feel even more personal and enchanting. On the app side, we plan to polish Lumi Lens complete with customizable settings, themes, and whimsical “magical modes,” integrating artistic aspects like glowing hearts, and sparkles. Behind the scenes, we’ll boost performance and reliability by adding caching, enabling offline fallbacks, and reducing latency so the magic never stutters. For the hardware, we envision a more comfortable glasses enclosure with better battery life and brightness, making Lumi Lens practical for everyday wear. Ambitiously, we would want to run user studies with neurodivergent students and mentors, tuning the prompts, visuals, and accessibility features so the experience can create an empowering experience for those who wish for it. <div