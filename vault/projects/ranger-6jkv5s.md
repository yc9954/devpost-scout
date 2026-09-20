---
slug: "ranger-6jkv5s"
url: "https://devpost.com/software/ranger-6jkv5s"
title: "Ranger"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1509
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/transcript_audio"
---

# Ranger

> Audio is a luxury we take for granted, that deaf folks don't get. Ranger is a wearable AR solution aiming to fix that, visualizing audio around them, and bringing them into the world of *sound*.

[Devpost](https://devpost.com/software/ranger-6jkv5s) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[accessibility]] [[education]] [[finance_payments]] [[transportation]]
  <sub>weak: developer_tools</sub>
**user** [[frontline_worker]]
**substrate** [[transcript_audio]]

**stack** adb, edge, jetson-nano, linux, machine-learning, python, unity

## How they structured the write-up

- 💭 inspiration
- 🖥 what it does
- 🛠 how we built it
- 🛑 challenges we ran into
- 🏆 accomplishments that we're proud of
- 🧠 what we learned
- ✏️ what's next for ranger

## Body

Our wild (west) setup - Jetson Orin Nano on the left, power bank on the right, and a mic array in the middle, all hooked up to a Meta Quest. ODAS audio spatial visualization - one of the tools we used for analysis and debugging during development. 💭 Inspiration Sometimes helpful ideas come from the silliest places. One day, as our team was playing Fortnite instead of doing our homework, we realized how helpful it was to have a "sound ring" in game. Noises like enemy footsteps or gunshots are displayed with a visual indicator to show what direction they came from. Luckily, we aren't trapped in Moisty Mire shotgunning ChugJugs, but we did realize people hard of hearing could benefit from this in real life. Both innocuous situations (dropping your wallet in the street and a parent calling you down to dinner) and intense situations (scary noises that would make anyone want to pick up the pace a bit walking home at night, an ambulance screaming by) are much more difficult to navigate for those who can't process auditory input. Visualizing sound helps you enter and understand conversations easily, avoid dangerous situations, and generally be aware of important goings-on in your surroundings. We wanted to build portable, wearable technology that would bring our vision from our colorful video game screen to the real world. We see our product as a proof-of-concept for something that could truly - cheaply, portably, fashionably - transform the lives of deaf people. 🖥 What it does Ranger is an edge-based AR solution for audio visualization that uses a Meta Quest frontend to indicate to the wearer where sounds are coming from. The user wears a hat, which has a microphone array to capture omnidirectional audio and send it to our processing unit, a Jetson Nano. Ranger classifies all different sorts of real-world sounds using a classifier model and displays them as icons on a circular grid, placing markers according to distance and direction. For speech, we live-transcribe conversations using Whisper which allows those hard of hearing to immediately parse what's happening, even if speech comes from behind them. The sound visualization does not interfere with your real-world view, only enhancing the information already available. It's a real-life HUD, enriching the wearer's experience and using edge computing to bring them into the wonderful world of sound. 🛠 How we built it Hardware : 1 Meta Quest 3 1 Jetson Orin Nano Mics (ReSpeaker 4-Mic Circular Microphone Array, Boya Bluetooth TX/RX) (Most importantly) A giant cowboy hat Software : Python Unity ML Models (Yamnet, Whisper) Ranger runs completely on the edge! All heavy computation is done on a Jetson Orin Nano; all communication is done with direct wired USB-C connections. For a TL;DR: using the Jetson Orin Nano, we developed an audio processing software that takes in a 4-channel microphone input, triangulates the direction, amplitude, and type of the loudest sound occurring at any time step, transcribes any detected speech, and sends all this information to the Meta Quest 3 using network-over-USB. For those interested in a more in-depth overview: Real-time Voice Transcription We use Whisper Mini running on the Jetson Nano for real-time voice transcription. To accomplish real-time voice transcription, we capture the last 10 seconds of a user’s audio and process it immediately. Although the Jetson Nano has the ability to run larger Whisper versions (up to the recently released turbo one with 800M parameters), our priority was reducing latency. Sound triangulation To determine where sound comes from relative to the user, we use a ReSpeaker microphone array. We set it up to triangulate the audio channels to pinpoint where audio comes from (an example of this technique below). This approach gave us a vector with angle and volume, which allows us to position our classified sounds as relatively positioned icons in our 3D scene. Sound classification Sound classification is done using a convolutional neural network (CNN). The model runs on the Jetson and classifies audio in a probability distribution of up to 500 candidate labels. Using this class along with the latest source of noise from the sound triangulation, we’re able to accurately pinpoint what a noise is and where it comes from relative to the user! 🛑 Challenges we ran into This was our first time doing a hardware-based project, and our inexperience showed up immediately . We found ourselves sifting through mountains of cables, walking back and forth to the hardware booth every 20 minutes, and flipping between "ITSSOOVER" and "WERESOBACK" faster than the GPU fan on our Jetson Nano. We all loved Operating Systems, Concurrency, and Computer Architecture in school, but building a project completely from scratch, with very little electric or audio engineering knowledge, through largely un-trekked territory was an uphill battle. We had several significant challenges: 1) Parsing raw input data intelligently We planned this out without a pretty cursory understanding of auditory science, so we had to spend a lot of time understanding hardware synchronization concerns, channel mixing, and in-built audio driver configurations. Spending a lot of time thinking and diagramming though, rather than just spurting out poorly written code, was incredibly helpful later during integration. 2) Interfacing between backend and frontend We originally wanted to use bluetooth to communicate between the Jetson Nano and Meta Quest but ran into a ton of issues with trying to get low fidelity bluetooth communication schemes working. After a lot of tinkering, we decided to connect them together with a USB-C cable and used Android Debug Bridge to treat the wire as a network connection through a server socket. 3) Developing a fully on-the-edge system The Jetson Nano relies on a DC power supply, which we tried to get around with a USB-A adapter and a power bank. Our lack of electric engineering know-how showed here, though, as we didn’t realize the USB-A adapter was inherently capping our voltage. We want to give a huge thank you to Mr. Chitoku Yato at Nvidia for saving us on this with a custom USB-C to DC cord. 🏆 Accomplishments that we're proud of The thing we’re all the most proud of is that we actually built what we set out to build! For our first hardware hack, with three different, distinct devices, across different frameworks, operating systems, and modalities of energy, this was an incredible feat. In the trenches of every challenge - Unity running slower than molasses on our rundown Intel Macs, bugs with multithreaded audio device access, bizarre audio sampling configurations provoking questions that not a soul on StackOverflow seemed to ask - we pushed past it and got things working. Each of us had a different moment we started jumping for joy: “I started going crazy when we first saw the visualization of the DOA (direction of audio)“ - Tyler “When I got to see a radar - like white dots on the circle - and the dots started to move when I did, I almost teared up“ - Samuel “After I spent 4 hours straight on our second Jetson Mini getting the Whisper model working with Cuda“ - Charan “I will never again feel happiness like I did when I saw the Android Debug logs on the Meta Quest print the first packet we sent“ - Sarvesh 🧠 What we learned Hardware is called hardware because it’s hard and you can wear it. Getting through our first hardware hack gave us a lot of confidence both for building on this idea and pursuing new ones. Hardware : Nuances of DC power conversion and portability Mechanics of audio input processing Remote usage and sharing of graphic/audio drivers Software : Supporting machine learning for edge devices Cabled network communication Unity scripting and scene visualization ✏️ What's next for Ranger The Meta Quest is the best affordable AR wearable right now, but eventually, we'd want the lightest-weight solution so people would be happy to use Ranger for long periods. We fiddled around with some AR glasses, but many smaller companies focus on treating the glasses as an external monitor, and the Meta RayBans do not have a display. This year, though, the new Meta RayBans will have a visual display, so we could easily swap our (lovably) bulky Quest for a sleek, non-invasive pair of shades. Our team has been chewing on this idea for a long time, and we want to develop this beyond our 36-hour sprint here at TreeHacks. During our development, we thought of a million insanely cool stretch goals to upgrade our current version, and each could be a project on its own. Special audio software that can perform Single Source Separation would let us transcribe multiple voices at once. A more advanced beam-forming location and tracking algorithm would let us intelligently classify objects over time. Porting over multilingual Voice Language Models to our brave little Jetson could expand this project globally, unlocking a new world of interaction for deaf people. This idea has a remarkable depth that we only scratched the surface of, and our intention in the future is to dive deep . <div