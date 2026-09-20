---
slug: "microbeat-accessible-tech-for-motor-cognitive-rehab-at2mx4"
url: "https://devpost.com/software/microbeat-accessible-tech-for-motor-cognitive-rehab-at2mx4"
title: "MicroBeat: Accessible Tech for Motor Cognitive Rehab."
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 870
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/video_visual"
---

# MicroBeat: Accessible Tech for Motor Cognitive Rehab.

> MicroBeat turns Portuguese-speaking anthems and giant buttons into a low-cost, open-source rhythm game that rehabilitates body and mind, engineering that treats health, human and accessible.

[Devpost](https://devpost.com/software/microbeat-accessible-tech-for-motor-cognitive-rehab-at2mx4) · hackathon [[DSH Hacks V1]]

## Facets

  <sub>weak: sensor_fusion, simulation_digital_twin</sub>
**domain** [[elder_child_care]] [[health_clinical]] [[mental_health]]
  <sub>weak: accessibility, education</sub>
**user** [[educator_student]]
  <sub>weak: patient_family</sub>
**substrate** [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** arduino, c++, esp32, gdscript, godot, iot, nano-banana, pixabay, seeed-studio-xiao, udp, unsplash, wifi

## Body

Inspiration Portugal is aging fast, and ageing brings a rise in chronic disease, dementia and conditions that strip away mobility and cognition. Traditional rehabilitation equipment is expensive, sterile and repetitive and its small controls exclude exactly the people who need it most: those with Parkinson's or recovering from a stroke, for whom fine motor control is an obstacle, not a starting point. We are Rafael and Gabriel , we are 14 years old , in 8th grade, from Guarda, Portugal. At the robotics club of Associação Desenvolver o Talento (ADoT) , mentored by Professor Mateus Vitorelli , we asked ourselves: what if therapy stopped being a painful duty and became a celebration? MicroBeat was born from that question, built on three pillars motor skills, cognition and emotion and on one conviction: Portuguese-speaking culture can be the therapeutic engine. What it does MicroBeat is a rhythm music game (inspired by Dance Dance Revolution ), purpose-built as a motor and cognitive rehabilitation tool: "a neuroplasticity cycle disguised as entertainment". On screen, colored arrows fall to the sound of a national anthem; the player responds by pressing giant physical buttons. The system awards points only when the color is right and the press lands exactly on the beat : $$\text{score} = \begin{cases} +1, & \text{if correct color and } \lvert t_{\text{press}} - t_{\text{beat}} \rvert \le \epsilon \ 0, & \text{otherwise} \end{cases}$$ The tolerance is the "Alignment Zone", calibrated by the therapist for each user. That strictness is therapeutic: it trains eye–hand coordination and induces a state of flow that pulls attention away from joint pain and onto the challenge. The neuroplasticity cycle has 4 phases : (1) auditory and visual stimulus → (2) cognitive processing (color, speed, reaction time in milliseconds) → (3) gross motor action (the intentional button press) → (4) immediate digital feedback (the score that reinforces dopaminergic pathways). How we built it (from physical to digital) Physical input. 100 mm "arcade" buttons, triggerable with the palm, fist or elbow no finger precision required. A 12 VDC LED, a microswitch rated for 10^7(10,000,000) cycles, mounted in a 24 mm hole. Edge processing. A Seeed Studio XIAO ESP32-S3 microcontroller, coin-sized, dual-core Xtensa LX7, with native Wi-Fi and Bluetooth. The pin is configured with pinMode(BUTTON, INPUT_PULLUP) . Signal stability. Mechanical "bouncing" produces false triggers; we solved it with a 5 ms debounce routine in C++ (Arduino IDE / Wiring library). Transmission. Wireless, over Wi-Fi, using UDP on port 4242 non-blocking and low-latency. We chose UDP over TCP, whose handshake adds delay. Removing cables is also safety: no fall risk, full freedom of movement. Game engine. Godot Engine (open-source, Nodes/Scenes architecture, GDScript ~ Python). _process(_delta) reads the UDP port every frame; _simular_tecla() creates an InputEventAction with pressed=true and immediately pressed=false via Input.parse_input_event without that "release", the key would stay stuck. Valid directions: left, down, up, right . Art and culture. We use anthems from 9 CPLP countries (Angola, Brazil, Cape Verde, Guinea-Bissau, Equatorial Guinea, Mozambique, Portugal, São Tomé and Príncipe, Timor-Leste). Backdrops start from real photos of Portuguese-speaking landscapes (Christ the Redeemer, the Serra da Estrela Tower, Luanda) from Unsplash/Pixabay, processed by the Nano Banana (Google) AI into a cartoon style cutting visual noise and cognitive load, keeping geographic fidelity, and removing the "clinical coldness". Challenges we ran into False triggers (bouncing): mechanical bounce gave several reads per press; fixed with the 5 ms debounce. "Stuck" button: without sending pressed=false after true , Godot held the key down: we had to simulate the release explicitly. Latency: TCP's handshake slowed the response; we moved to UDP/4242 to keep the beat faithful to the press. Visual cognitive load: real photographs overloaded the screen; AI cartoon processing lowered the noise without losing geographic identity. Hardware dependence: unlike a phone app, there is an upfront cost (board, buttons, enclosure) and assembly: a trade-off we accept for real physical accessibility. Accomplishments we're proud of We tested at ADoT with children (including those with motor limitations), family members, adults and the elderly. Children showed great enthusiasm; older users adopted the technology naturally, the familiarity of the anthems lowered their resistance. We saw potential in psychomotor and rhythmic training, eye–hand coordination, memory, attention and reaction time, with reduced anxiety. And perhaps the biggest accomplishment: two 14-year-olds proving that cheap hardware + open-source software + cultural identity can turn a painful therapy into a rhythmic celebration on an open, replicable, low-cost platform. What we learned Music connects to the limbic system and long-term memory: childhood anthems resist cognitive decline and boost engagement, especially in the elderly and in dementia. We learned that physical accessibility is decisive , big buttons remove the frustration of missing tiny keys, and that every engineering choice (UDP over TCP, debounce, the button "release") directly shapes the therapeutic experience. We also learned to be honest: the project still lacks formal clinical validation , and saying so is part of the method. What's next Clinical collaboration with therapists, special-education teachers and care homes, to refine the mechanics and gather medical metrics. Expansion: new games on the same button infrastructure, focused on active ageing. Virtual Reality (VR): a leap in sensory immersion. Per-profile calibration: different timing tolerances (e.g. Parkinson's vs. the Autism spectrum) require individually tuning the "Alignment Zone". <div