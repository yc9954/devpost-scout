---
slug: "vr-ultrasound-training-simulator"
url: "https://devpost.com/software/vr-ultrasound-training-simulator"
title: "V2VR Ultrasound Training Simulator"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 1170
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# V2VR Ultrasound Training Simulator

> We transformed the MX Ink into a precision-tracked VR ultrasound probe, unlocking immersive, portable echocardiography training with the Meta Quest 3, anytime and anywhere.

[Devpost](https://devpost.com/software/vr-ultrasound-training-simulator) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[geospatial]] [[video_visual]]

**stack** meta, openxr, quest, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vr ultrasound training simulator

## Body

MX Ink Ultrasound Probe VR Ultrasound Sim in hardshell case Patient scanning in VR Demo with client Demo with client Inspiration We’ve seen firsthand how hard it is to truly learn ultrasound. Students crowd around a single machine. They wait for limited lab time. They depend on volunteer patients. And even after hours of observation, many still struggle with the most important part: spatial intuition and understanding how probe movement in 3D space translates into the 2D image on screen. We believe that XR can greatly enhance those traditional methods of learning, and become a powerful tool to remove many of those existing barriers. So we set out to build something we wish had existed when we were training: a portable, realistic, repeatable way to practice scanning anytime, anywhere. Our dynamic team of innovators have varied backgrounds in ultrasound imaging, VR/XR development, product design/3d printing, and entrepreneurship. These diverse skillsets enabled us to create an enterprise solution that combines the best of these existing technologies into a truly unique medical training experience. What it does We built a fully immersive, VR ultrasound training simulator powered by the Meta Quest 3, incorporating the Logitech MX Ink, Touch controllers, and custom 3D printed peripherals. This hardware set, combined with our VR application software, gives the user a robust training system that, as one user puts it, "feels remarkably real", allowing them to intuitively understand 3D spatial imaging. Using our custom 3D printed sleeve, we transformed the MX Ink into a realistic ultrasound probe capable of precision tracking. When you hold it, it feels like a probe. When you move it, the anatomy responds in real time. With our compact, 3D printed mannequin, users feel tactile and haptic probe feedback with the MX Ink, when scanning the mannequin's contoured surface. Inside VR, users can: Immerse themselves in a virtual clinic or hospital room. In mixed reality mode, they can scan within the comfort and familiarity of their own room; Dynamically scan the heart of a virtual patient using the MX Ink and our compact training mannequin; Shrink down to the size of an ant and freely explore the detailed interior anatomy of a beating heart. Move comfortably through chambers, valves, and arteries as if you were the size of a blood cell; Operate a fully interactive ultrasound machine with the touch controllers and learn about the main functions of the machine; Receive real-time feedback on probe angle and positioning using our proprietry guidance and self-testing system; Access additional learning resources to enhance their understanding of anatomy, pathologies, and imaging techniques in our Library and Sandbox rooms. Students can now access something powerful, beyond simply watching a tutorial. They're scanning, they're adjusting the probe in realtime, and learning through feel and fine motor movement. And everything fits into a compact case, making it portable enough for classrooms, clinics, or remote settings. How we built it Unlike other training simulators that require a PC/laptop to run, ours was built for the standalone Quest 3, running on the Snapdragon XR2 gen 2 chipset. This required us to optimize for performance, while minimizing any noticeable latency. Developed using Unity with the Meta Quest SDK, we integrated Logitech’s MX Ink API for precision probe tracking and spatial mapping. Our UIUX development includes an innovative calibration system so our physical mannequin stays properly aligned with the virtual patient. We also created a fully interactive ultrasound machine in VR which allows users to learn about and access various functions of a real machine, using the Quest 3's touch controllers for hand controls. Other user accessibility features include: options to select left or right hand scanning modes; the ability to use the touch controller as the probe; our heart and cut plane learning modes which allow the user to visually see the ultrasound beam as it scans a 2D slice of the patient's heart. This was one of those "a ha" moments that new users saw immediate benefit from when trying our sim for the first time. Challenges we ran into Working within the performance limits of standalone XR hardware forced us to be intentional about every design decision. We optimized anatomy models to preserve anatomical accuracy without sacrificing frame rate. We went through months of product design engineering to perfect the physical assets. For the probe sleeve, we tested weight, grip, balance, and stability so it would feel natural in hand and refined it until movement felt stable and trustworthy. We also built a compact, training mannequin with an adjustable mount so posture and positioning would feel realistic, allowing patients to be scanned in 2 postions, on their back or on their side, just like in a real world, point of care clinical setting. And perhaps one of the hardest challenges so far: designing a guidance system that teaches without overwhelming. In medical training, cognitive overload is real. We stripped back unnecessary UI and focused on clarity, simplicity, and feedback that supports learning rather than distracting from it. Each obstacle made the system better. Accomplishments that we're proud of We built: A commercially viable, immersive ultrasound simulator with anatomically responsive imaging; Custom peripherals that meaningfully extends the Logitech MX Ink into a precision medical training device and a compact training mannequin that eliminates the need for a real test patient; A real-time feedback and guidance system designed specifically for spatial skill acquisition; A portable kit that can realistically be deployed in classrooms or institutions and can be remotely managed through MDM systems like ArborXR. During external trials, trainees told us something that meant a lot: They finally understood how probe movement affects what they see. They felt more confident. They wanted to keep practicing. That really reinforced to us that what we are doing is extremely impactful. What we learned Building this in XR allowed us to take an abstract and difficult-to-visualize concept, then using VR's unique spatial perspective, turn it into something more intuitive and natural. We learned that: Muscle memory helps to retain and can enhance traditional learning methods; Feedback should guide without feeling overwhelming; We can design beyond the limits of existing hardware eco systems and integrate our own custom peripherals even if none existed before; Precision tools like the Logitech MX Ink can unlock entirely new categories of real-world applications. We learned just how powerful experiential learning can be when technology is used appropriately, and how to bridge medical expertise with software engineering, a skill we will carry forward. What's next for VR Ultrasound Training Simulator We’re looking ahead toward: Clinical validation studies comparing VR training to traditional methods; More partnerships with hospitals and teaching institutions and building on our commercial subscription SaaS business model; Expanded modules: pediatric, vascular, general, and POCUS (point of care ultrasound); Broader pathology libraries for advanced training; Web front end support for instructors to track, monitor, and test their students' progress throughout their learning process. Our goal is to improve education and make ultrasound training more accessible, more repeatable, and more equitable, starting here, and expanding into other procedural skills. <div