---
slug: "qalammr"
url: "https://devpost.com/software/qalammr"
title: "QalamMR"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 567
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# QalamMR

> QalamMR is the world's first Spatial Calligraphy Workshop. It uses Logitech MX Ink haptics to simulate the invisible forces of art—friction, flow, and gravity—teaching you to feel the masterpiece.

[Devpost](https://devpost.com/software/qalammr) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** blender, logitech-mx-ink-sdk, meta-mixed-reality-utility-kit, meta-xr-interaction-sdk, opencv, python, shader-graph, unity

## How they structured the write-up

- 1. elevator pitch
- 2. the evolution: why qalamai wasn't enough?
- 3. key innovations
- 4. technical feasibility
- 5. why logitech mx ink is essential?

## Body

1. Elevator Pitch Building upon my success with QalamAI (the world's first AI calligraphy teacher on iOS), QalamMR breaks free from the constraints of 2D screens to create the world's first Spatial Calligraphy Workshop . Using Meta Quest's mixed reality and the Logitech MX Ink , I am transforming the user's physical desk into a master's studio. It’s not just about drawing; it’s about immersing the user in a full simulation where dynamic guides, holographic overlays, physical haptics, and spiritual storytelling converge to teach the ancient art of Thuluth. 2. The Evolution: Why QalamAI wasn't enough? With QalamAI, I successfully digitized the visual instruction of calligraphy. But a 1000-year-old art form cannot be fully contained on a flat iPad screen. The 2D Limit: On an iPad, the reference image, the drawing area, and the feedback are all fighting for space on a single flat plane. It's cognitively overwhelming. The Spatial Solution (QalamMR): I am "unfolding" the UI into the real world. The user holds a virtual reed pen (mapped to MX Ink), sees their drawing on their real desk, while instructional guides, master videos, and historic masterpieces float spatially around them. 3. Key Innovations A. The "Living Meshk" Station Innovation: I created a hybrid workbench. On the Desk: A holographic "Master Plate" (Pink Overlay) is projected directly onto the physical paper for precise shape comparison. In the Air: A "Spatial Video Screen" floats to the user's right, playing a high-resolution recording of a master calligrapher. Users watch the rhythm in real-time, then look down to replicate the physics. B. Haptic "Carved Path" & Dual-Tip Physics Innovation: The holographic master path is a "Haptic Channel." The MX Ink provides resistance if the user strays from the path. Simultaneously, my physics engine simulates the traditional "Wahshi & Unsi" (dual-tip) mechanics, requiring the user to physically angle the MX Ink correctly for thin vs. thick strokes. C. The Inkwell Ritual Innovation: To complete the simulation, infinite ink is replaced by a virtual inkwell placed on the physical desk. Users must physically dip the MX Ink, learning the rhythm of ink management. D. The Gallery of Wisdom-Spatial Storytelling Observation: Calligraphy is 50% technique, 50% patience ( Sabr ). Learners often lose motivation. Innovation: To the user's left, a "Spatial Gallery" displays high-fidelity 3D scans of historic masterpieces (e.g., from Akşehir İmaret Mosque ). When a user gazes at a piece, an immersive audio guide tells its story and Sufi philosophy (e.g., "This piece reads 'All on earth shall perish,' reminding the artist to focus on eternal beauty" ). This keeps the learner spiritually connected to the craft. 4. Technical Feasibility I am not starting from scratch. Existing Core: I have already built and validated the core physics and AI analysis engine for QalamAI (iOS/Python). The Port: My task is to port this logic to Unity and map my existing physics parameters to the Logitech MX Ink SDK . Validation: As a developer with deep domain expertise, I have already encoded the geometric rules of 10+ Thuluth letters into machine-readable metadata. 5. Why Logitech MX Ink is Essential? QalamMR is a spatial simulation that requires specific hardware inputs: Precision 6DOF Tracking: To align the virtual reed pen perfectly with the user's hand and the holographic overlays. Pressure & Tilt: To drive my complex dual-tip and hydrodynamic ink engines. Haptics: To give physical presence to the holographic guides and simulate paper texture. <div