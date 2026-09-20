---
slug: "spellcraft-mx"
url: "https://devpost.com/software/spellcraft-mx"
title: "Spellcraft MX"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 717
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
---

# Spellcraft MX

> Building a magic-themed, cross-reality wand interaction system with Logitech MX Ink, blending gestures, buttons, and voice to explore intuitive spellcasting and spatial interaction in AR and VR.

[Devpost](https://devpost.com/software/spellcraft-mx) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[voice_speech]]

**stack** meta, openxr, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spellcraft mx

## Body

MX Ink with wand overlapped + controllers AR Spellcasting with 3D-printed wand and virtual wand model turned off (WIP Prototype) 3D-printed Wand Attachment Assembled Wand on MX Ink In-Hand Ergonomics Inspiration Spellcraft MX was inspired by two very different worlds colliding. On one side, while working on medical XR simulations, I experienced how pen-shaped input devices such as Logitech MX Ink enable far more natural pointing, drawing, and spatial interaction than traditional VR controllers. On the other, I grew up fascinated by fantasy stories where simple hand movements and a wand could trigger powerful effects. This contrast sparked a question: what if spatial input in XR could feel expressive and intentional, rather than button-driven and abstract? Spellcraft MX explores this idea by reimagining MX Ink as a wand-like input device, combining precise spatial tracking with expressive gestures and voice input to create interactions that feel closer to how people intuitively imagine a "spell casting" action in AR and VR. What it does Spellcraft MX is a cross-reality interaction system that uses Logitech MX Ink as a wand-like spatial input device. Users can perform gesture-based and button-based interactions, combined with voice input, to trigger different actions and in-game spells. The same interaction model works across both AR and VR modes, allowing users to switch contexts while retaining consistent interaction mechanics. In AR mode, depth-based occlusion or a 3d printed wand covering the MX Ink is used to visually integrate the device with the user’s real hands and environment. How we built it Spellcraft MX is built in Unity using OpenXR on Meta Quest. Logitech MX Ink is used as the primary input device, with controller fallback for accessibility and testing. Gesture classification is used to differentiate between multiple actions based on motion patterns, and an optional voice input is integrated to complement gestures and reduce ambiguity. In AR mode, depth-based occlusion is used to improve realism when interacting with the wand in the real world. We are also working on a 3D printed cover for the MX Ink, which, when used in AR mode, greatly increases the experience. The project focuses on building a reusable interaction layer that works consistently across both AR and VR. Challenges we ran into Designing gestures that feel expressive yet are easy to recognize reliably was a key challenge. Reducing false positives in gesture detection while maintaining responsiveness required careful tuning and iteration. Integrating multimodal input introduced latency. Achieving stable depth-based occlusion in varying real-world lighting conditions was also challenging. Additionally, designing interactions that feel consistent across both AR and VR required careful UX decisions. Accomplishments that we're proud of Building a unified interaction system that works across both AR and VR Integrating Logitech MX Ink as a primary spatial input device Implementing gesture-based interaction for spell casting and an optional voice input-based spell casting Achieving convincing depth-based occlusion in AR for hand-object interaction Creating a 3D printable model for the MX Ink, which can be used to give a real feel of a wand in hand Designing an interaction model that goes beyond traditional controller metaphors What we learned This project reinforced the importance of designing interactions around physical affordances rather than forcing traditional controller paradigms into new contexts. Combining multiple input modalities can significantly improve usability and reduce ambiguity, but requires careful UX design to avoid overwhelming the user. We also learned that small details such as visual feedback and input gating can dramatically affect how reliable an interaction system feels in XR. What's next for Spellcraft MX Spellcraft MX is currently in an early exploration phase, with the focus on interaction design rather than content. Next steps include expanding the gesture vocabulary, improving the robustness of gesture recognition, refining the AR occlusion pipeline, creating a world in VR, and iterating on multimodal input using gestures, buttons, and voice. Once the core interaction system is stable, we plan to prototype a small set of magic-themed interactions, such as basic attack and levitation spells, along with simple enemies and interactive environment objects to better showcase MX Ink’s capabilities in our system. Voice commands will be further refined to support intent disambiguation during spellcasting. Longer term, Spellcraft MX could evolve into novel interaction experiences beyond just demos. We would also love to explore multiplayer for either a PVE or a PVP system. <div