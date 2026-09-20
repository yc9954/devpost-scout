---
slug: "cloudcam"
url: "https://devpost.com/software/cloudcam"
title: "Cloudcam"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1086
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Cloudcam

> Using Cloudinary’s efficient processing and delivery, Cloudcam makes video messaging creative, instant, and personal.

[Devpost](https://devpost.com/software/cloudcam) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** claude, cloudinary, java, mediarecorder, three.js, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cloudcam

## Body

Inspiration We use social media to stay close with the people we care about. But the more we started to reflect, the more we started to notice how our online interactions were lifeless, especially when it came to expression and creativity. Most platforms give you filters. You pick one, hit record, and that's it. You can't play. You can't draw a little note for your friend mid-video, then flip on a glitch effect and laugh at how weird it looks, all in the same take. The moment a creative idea hits you, you're locked out. The tools we had didn't keep up with that, so we built Cloudcam. What it does Cloudcam is a browser-based video messaging tool built around a live, dynamic canvas that responds to you (your touch, your voice, your environment) as you record. Draw directly on your video while it's recording. Leave notes, doodles, arrows to your liking! Toggle effects mid-take . Switch from glitch to mirror to ASCII art without stopping the recording. Audio-reactive visuals that pulse and shift with your voice in real time. Instant cloud publishing via Cloudinary. The moment you stop recording, your video is processed, optimized, and ready to share without the need to wait or export. A personal gallery where all your clips live, streamable at any quality, anywhere. The whole thing runs in the browser. No app to download, and no account wall to get through! How we built it The core of Cloudcam is a single composited <canvas> element that owns every frame of the output stream. Everything from webcam feed, drawings, to effects gets rendered into that one canvas in real time. We built it in vanilla JavaScript with ES modules , and took advantage of just the raw web platform. The stack: Three.js for WebGL-powered 3D effects Canvas 2D API for drawing and compositing Web Audio API to read mic and drive audio-reactive effects MediaRecorder API to capture the canvas stream directly as video Cloudinary REST API for instant upload and delivery Cloudinary Video Player SDK for gallery playback Each effect (glitch, mirror, blob, ASCII, emoji filter, freehand drawing) plugs into a shared interface with init , render , and destroy hooks . A compositor loop calls them in sequence every frame, so stack and toggle effects can be in any order without breaking the stream. When the recording is finished, the video blob is uploaded directly to Cloudinary using an unsigned preset. Challenges we ran into Getting effects to feel instantaneous . The whole promise of Cloudcam is that switching filters mid-take feels natural. Getting the compositor loop fast enough that toggling effects at 30fps felt seamless took a lot of profiling and rethinking how we allocated frame budget across heavier effects like ASCII rendering. Making drawing feel good on a live video . Drawing on a static image is easy, but drawing on a canvas that's actively compositing a webcam feed, running effects, and streaming audio data is a different problem. We had to be careful about event handling and layer ordering so each stroke didn't flicker or lag behind a user's input. Cross-browser video recording . video/webm doesn't work in Safari. video/mp4 doesn't work in Firefox. We had to negotiate the codec at runtime and let Cloudinary smooth over the format differences on delivery. The Cloudinary widget timing problem . In a no-bundler environment, the Cloudinary Upload Widget script loads asynchronously. A straightforward call to window.cloudinary.createUploadWidget() on page load fails silently. We had to poll until the function was actually attached, not just until window.cloudinary existed. Accomplishments that we're proud of We shipped something that actually feels good to use. Cloudcam isn't a demo that works once if you click in the right order. The drawing, the effect toggling, and the instant upload all holds together as a real experience. We built a real-time video compositor from scratch. The entire rendering pipeline of webcam capture, effect stacking, audio reactivity, and canvas compositing runs in vanilla JavaScript with zero build tooling. Getting six different effects to run simultaneously at 30fps in a browser, all composited into a single shareable stream, is something we're proud of. We made mid-take effect switching work. This was the core creative bet of the product, and it could have easily felt janky or broken. Instead it feels like a natural extension of recording. You can glitch, mirror, or draw on yourself mid-sentence without the video hiccuping or the audio dropping. Zero-wait publishing. Cloudinary's pipeline is fast enough that by the time a user has hit stop and looked back at their screen, the clip is already in their gallery and shareable. We rethought what a video message could be. Most messaging apps treat video as a passive capture: you point, you record, you send. Cloudcam treats it as a creative act. We're proud to have built something that makes people want to send more videos. What we learned The biggest thing: the **browser is more powerful than people give it credit for . captureStream , MediaRecorder , and AnalyserNode together form a complete real-time video studio. We didn't need a native app. We didn't need a backend for the core recording loop. The platform was enough. We also learned that product feel is a technical problem . The difference between an effect toggle that feels snappy and one that feels laggy is a few milliseconds of frame budget. Getting Cloudcam to feel effortless required the same care as getting it to work. And Cloudinary changed how we thought about the upload problem entirely. We stopped thinking of it as a step the user has to wait through and started thinking of it as something that just happens. That shift from "export and share" to "record and it's already there" is what made the product feel right. What's next for Cloudcam The immediate vision is integration with existing messaging platforms . Imagine sending a Cloudcam clip directly from a DM thread, the same way you'd send a voice memo, but with glitch effects and your handwriting all over it. Beyond messaging, we see a natural home for Cloudcam with content creators who want a faster, more playful way to make short-form video. The real-time effects and instant delivery cut the production loop down to almost nothing. On the technical side, we want to expose more of Cloudinary's transformation layer to users and let them apply post-processing on top of their clips before sharing. Color grading, overlays, format conversion, for example, all without leaving the browser. <div