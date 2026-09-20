---
slug: "spark-stackable-physical-algorithms-for-robotics-kids"
url: "https://devpost.com/software/spark-stackable-physical-algorithms-for-robotics-kids"
title: "SPARK : Stackable Physical Algorithms for Robotics Kids"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 769
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/web_dom"
---

# SPARK : Stackable Physical Algorithms for Robotics Kids

> A hands-on robotics kit that teaches kids how to code using physical blocks, and real robot behavior. No screens, no syntax, just logic and creativity.

[Devpost](https://devpost.com/software/spark-stackable-physical-algorithms-for-robotics-kids) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** arduino, autodesk-fusion-360, c++, css, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- business model and market competition
- what we learned
- what's next for spark

## Body

3D printed Blocks website-challenges Website-homepage website-challengeCatalog Inspiration This project was inspired by our experience mentoring students from kindergarten through 8th grade during a STEM exploration field trip prior to the hackathon. Working directly with younger students showed us how excited they become when learning is hands-on, physical, and playful, but also how quickly that excitement fades when concepts become abstract or overly screen-based. We wanted to build a robotics learning platform that meets kids where they are, using physical interaction first, and digital tools only as support, so programming feels like a puzzle they can touch, build, and understand. What it does Our solution is a hands-on robotics learning kit that teaches programming using 3D-printed, puzzle-style blocks instead of screens or cards. Each physical block represents a programming instruction, such as start, movement, turns, or loops. Kids create programs by physically snapping these blocks together in sequence. The robot then reads the assembled instruction chain and executes the program in the real world. The robot itself is not modular yet, modular hardware is a planned future implementation, but the current design already allows kids to learn core programming ideas like sequencing, repetition, and cause-and-effect. To support learning, we built a companion website that offers guided challenges. These challenges visually explain what each block does, how the block code works, and what the robot should do before the child runs the program. This gives kids structure, feedback, and confidence while still encouraging experimentation. How we built it We built the system by integrating an Arduino robot, NFC-enabled instruction 3D printed blocks, and an Arduino-based scanning pen that translates physical blocks sequences into executable robot behavior. The robot’s control logic interprets the scanned instructions and performs movements accordingly. In parallel, we developed a web platform that supports the physical kit with guided challenges and free-play controls, bridging hands-on robotics with a digital learning experience. Challenges we ran into One of our biggest challenges was designing something that is simple enough for young kids, but still teaches real programming logic. Physical block design, instruction clarity, and robot behavior all had to align so kids could immediately understand what their program was doing. Another challenge was balancing cost with functionality while still thinking like a startup, not just a demo. In our first prototype, we ran into a practical issue: we didn’t have enough tinkering instruments and hardware available to build the complete NFC-based system right away. To keep progressing, we designed and tested the entire programming workflow using simple push buttons as input commands. This approach helped us validate the core logic sequencing, timing, command execution, and robot response before moving to the final interaction method. Once the logic was stable and reliable, we upgraded the system to use NFC-enabled 3D-printed blocks , making the experience more intuitive, engaging, and kid-friendly. Link: Tinkercad simulation Accomplishments that we're proud of We’re proud that we created a system that turns programming into a physical puzzle, not a screen-based activity. Kids can see, touch, and rearrange their logic, and immediately watch it come to life through the robot. We also successfully built a complete experience: physical hardware, a working robot, and a guided learning website that supports real education, not just a one-off demo. Business Model and market competition Our target audience is parents, schools, and after-school programs looking for engaging STEM tools for kids. While competitors like LEGO robotics kits exist, they often: Cost $400 or more, Require heavy screen use, are complex for younger kids. Our kit focuses on: Physical learning first, Lower cognitive overhead, a more accessible entry point into robotics and programming We spent approximately $100 building our prototype. With optimization, such as moving to ESP32 microcontrollers and custom PCB boards. Production costs can be significantly reduced at scale. We plan to sell the kit for around $300, making it more affordable than most robotics kits on the market while still delivering strong educational value. This pricing makes our product especially attractive for families and schools that want high impact without premium pricing. What we learned Through this project, we learned how to design for children as end users, which requires clarity, durability, and immediate feedback. We gained experience integrating hardware, embedded systems, and web platforms, while also thinking critically about cost, usability, and scalability as a real startup product. What's next for SPARK Next, we plan to Introduce modular robot components, expand the platform with additional instruction blocks, sensors, and more advanced challenges. We also aim to refine the curriculum-driven aspects of the website, explore classroom deployment, and continue developing the project into a scalable, market-ready robotics education startup. <div