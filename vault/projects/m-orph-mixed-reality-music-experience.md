---
slug: "m-orph-mixed-reality-music-experience"
url: "https://devpost.com/software/m-orph-mixed-reality-music-experience"
title: "(m)ORPH Mixed Reality Music Experience"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 547
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# (m)ORPH Mixed Reality Music Experience

> (m)ORPH Mixed Reality is an innovative music-listening experience where players can mix, manipulate, and interact with songs in a completely immersive manner... hear your room come alive with sound!

[Devpost](https://devpost.com/software/m-orph-mixed-reality-music-experience) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

  <sub>weak: realtime_stream</sub>
**domain** [[developer_tools]]
**user** [[developer]]

**stack** meta, netcode, unity

## Body

Changing the RoomMesh background to something cool and audio-reactive Clapping to push all Orph sound objects away Grabbing and throwing Orph sound objects Local multiplayer sharing of Orph sound objects Local multiplayer shared musical experience Morph MR Developer Walkthrough Video (m)ORPH Mixed Reality Music Experience is an innovative music-listening experience where players can mix, remix, and interact with songs right in their own room. Having worked on AAA music games like Amplitude, Guitar Hero, and RockBand, I’m constantly looking for new ways that music lovers can engage with music and feel transformed. I have found that XR is ideally suited for these types of immersive music explorations. In (m)ORPH, interactive sound objects are floating all around your room, so you feel surrounded by music in all directions. As you move through your space, the mix evolves, some elements gets louder or quieter, and the song changes in unique ways; or you can freeze and place elements of the song all around your favorite chair for an enveloping sonic experience. I am submitting a proof-of-concept Quest 3/3s demo that supports single-player and colocated multiplayer modes, controller-free hand and microgestures, and Meta spatial audio rendering. In 2021, I premiered the free (m)ORPH VR app on AppLab: Morph VR app link For this Horizon Start Developer competition, I took the opportunity to completely reinvent my app as a mixed reality experience, with these significant updates: Ported from Unity 2019 & older OVR SDK to Unity6 and Meta v81 SDKs and latest Meta spatial audio renderer Reinvented object motion and controls to support hand-grabbing, rigidbody throwing, freezing, recentering, and orbiting, to take advantage of mixed reality real-world rooms rather than virtual rooms. Added brand new colocated local multiplayer mode so people can join in the same room to interact with music together. Players can hear the same music from different perspectives, share audio objects, and alter each other’s mixes in real time. Removed controllers and replaced with hand controls and microgestures. Thumb taps to freeze and re-center objects, thumb swipes to change room visual effects, "smack" sound objects to trigger audio events, and "clap" to disperse objects. Added audio FX objects that add reverb, delay, or filtering to sound objects they get near to. Added audio-reactive visuals to drum objects to make them feel more alive. Due to time constraints, I faced challenges that I will fix in the future: Colocated multiplayer — something about the implementation of the shared spatial anchor I could not get right. In my build, the client player needs to join with the same orientation that the host used when starting the level, otherwise the grabbed network objects move in an inverted manner. This is broken as the client player should be able to join in any starting orientation and align to the shared anchor so that networked object placement is aligned. I wanted to share all sound objects as network grabbable but it killed FPS. I had to reduce the number of shared objects in multiplayer. In conclusion, I’m excited to continue development of the (m)ORPH Mixed Reality Music Experience , fix issues, and add new features and many more songs from other artists. My goal is for players to engage music in complete immersion and feel like their room is alive with sound! <div