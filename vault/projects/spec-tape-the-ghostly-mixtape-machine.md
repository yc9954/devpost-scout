---
slug: "spec-tape-the-ghostly-mixtape-machine"
url: "https://devpost.com/software/spec-tape-the-ghostly-mixtape-machine"
title: "Spec-Tape: The Ghostly Mixtape Machine"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 947
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Spec-Tape: The Ghostly Mixtape Machine

> Spec-Tape is a your web application that combines 1990s mixtape nostalgia with paranormal audio investigation themes and making spooky playlists!

[Devpost](https://devpost.com/software/spec-tape-the-ghostly-mixtape-machine) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** html, javascript, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spec-tape: the ghostly mixtape machine

## Body

Kiro learning from Steering docs Hardware blunder, first Spec-Tape project that was scraped Kiro planning and integrating testing from the start Spec-Tape track lists for A and B sides v1 Spec-Tape mixtape player interface v1 Spotify playlist suggestion based on Spec-Tape tracks v3 EVP analysis result v3 Track lists for A and B sides v3 Mixtape player interface v3 Inspiration The idea for Spec-Tape came from the perfect storm of 90s nostalgia and Halloween spookiness for the Kiroween hackathon. We (Kiro and I) wanted to capture that magical feeling of creating mixtapes in the 90s - the careful curation, the personal touch, the anticipation of sharing something special with friends. But we gave it a paranormal twist: what if your mixtape could analyze ghostly voices? The concept merged the tactile, analog experience of cassette culture with modern AI capabilities, creating something that feels both nostalgically familiar and mysteriously otherworldly. What it does Spec-Tape is a single-file web application that recreates the authentic 90s mixtape experience with a supernatural edge. Users can create personalized "Spec-Tapes" by naming their mixtape and adding up to 10 tracks per side (A and B). The centerpiece is a beautifully animated cassette player with functional controls, spinning tape spools, and that classic boombox aesthetic. But here's where it gets spooky: the "Spectral Interlude" feature lets users input suspected EVP (Electronic Voice Phenomena) transcripts, which our AI analyzes to generate formal paranormal investigation reports. These reports classify the spectral activity, analyze emotional valence, identify phonetic anomalies, and suggest meanings. Users can share their findings with a single click, and hidden Easter eggs (including the Konami code) unlock special Halloween effects. How we built it We built Spec-Tape as a completely self-contained HTML file using a modern tech stack. The visual interface uses Tailwind CSS for that authentic 90s aesthetic - dark charcoal backgrounds, neon accent colors, oversized 3D buttons, and monospace fonts that scream "retro digital." For audio, we integrated the Web Audio API with Tone.js to create actual sound generation and playback controls. The AI-powered EVP analysis connects to Google's Gemini API, using a carefully crafted system prompt that makes the AI act as a "paranormal linguistics expert." We implemented sophisticated state management in vanilla JavaScript, CSS keyframe animations for the spinning tape spools, and even a complete Easter egg system with sequence detection and special effects. Everything loads from CDNs, making it truly portable and shareable. We also focused on accessibility features and used Lighthouse to test for mobile and desktop web versions, we made some fixes and changes especially to heading ordering, labels and ARIA, and we're now at 94 Accessibility score, there are still a few items to remediate. Challenges we ran into The biggest challenge was architecting a complex, feature-rich application within the constraint of a single HTML file. We had to carefully manage dependencies, ensure proper loading order, and optimize for both functionality and file size. The audio system presented unique hurdles - creating convincing tape player behavior with Web Audio API while maintaining cross-browser compatibility. The EVP analysis feature required extensive prompt engineering to get the AI to consistently generate properly formatted paranormal reports that felt authentic yet entertaining. We also struggled with the Easter egg system, particularly preventing the Konami code from interfering with normal keyboard shortcuts. The 90s aesthetic was surprisingly challenging to nail - balancing authentic retro design with modern usability standards. Accomplishments that we're proud of We're incredibly proud of creating a fully functional, single-file web application that genuinely captures the magic of 90s mixtape culture. The animated cassette player with spinning spools and authentic controls feels remarkably real. The AI-powered EVP analysis system produces genuinely entertaining and shareable paranormal reports that perfectly match the Halloween theme. Our Easter egg implementation is sophisticated - the Konami code triggers a full-screen spectral effect, and hidden click areas unlock bass drops. The application works seamlessly across modern browsers without any installation or setup. Most importantly, we created something that's both nostalgic and innovative, familiar yet surprising - exactly what we hoped to achieve for Kiroween. What we learned This project taught us the power of constraint-driven design - building everything in a single file forced us to be creative and efficient. We gained deep experience with the Web Audio API and learned how to create convincing audio experiences in the browser. Working with AI APIs for creative applications showed us new possibilities for human-AI collaboration in entertainment. We discovered that authentic retro design requires careful attention to period-appropriate details - from color palettes to typography to interaction patterns. The project also reinforced the importance of Easter eggs and hidden features in creating memorable user experiences. Most surprisingly, we learned that sometimes the most innovative solutions come from combining seemingly unrelated concepts - in our case, mixtapes and paranormal investigation. What's next for Spec-Tape: The Ghostly Mixtape Machine The future of Spec-Tape is deliciously spooky! We're planning to add actual audio recording capabilities so users can capture real EVP sessions directly in the app. A "Spectral Library" feature would let users browse and share community-generated paranormal reports. We want to implement more sophisticated audio analysis - real spectral analysis of uploaded audio files, not just text transcripts. Social features could include "Haunted Playlists" where users share their supernatural mixtapes with embedded EVP reports. We're also considering mobile app versions with device sensor integration - imagine using your phone's microphone for real-time EVP detection, or having the app respond to environmental factors like low light or electromagnetic interference. The ultimate goal is to create a complete paranormal investigation toolkit disguised as a nostalgic mixtape player, bridging the gap between retro entertainment and modern ghost hunting technology. <div