---
slug: "hardware-context-protocol"
url: "https://devpost.com/software/hardware-context-protocol"
title: "Hardware Context Protocol (MCP for Hardware)"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 854
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# Hardware Context Protocol (MCP for Hardware)

> Giving AI a physical embodiment for the world. Control multiple hardware platforms cooperatively via LLM prompts. Deployed with a custom voice-activated autonomous chef robot.

[Devpost](https://devpost.com/software/hardware-context-protocol) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** asi:one, cv, flask, inverse-kinematics, json, python, tcp

## How they structured the write-up

- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- 3dof end-effector commanding
- camera and vision detection
- what's next for hardware context protocol

## Body

System Demonstration APRIL tag detection model (used for world-frame localization) GUI for interacting with the HCP Overview Model Context Protocol (MCP) revolutionized the capabilities of LLMs by offering a radically new way of creating software for our everyday lives. Missing from this was meaningful capability to interact with the real world beyond a screen, and inspired us to develop our Hardware Context Protocol (HCP). It enables LLMs to control hardware components via well-defined exposed interfaces, allowing AI to interact with the world through reading sensor data, commanding actuators, and bringing them all together with context. The problem that inspired us was household serving (or rather, the lack of an intelligent machine to do so) - think making salads, finding snacks. We proved that our HCP SDK is a fast and iterable way to bring intelligence into the homes of everyday individuals by integrating its functionality into a robot arm. Hardware Context Protocol What it does We created an SDK that allows the user to create a minimal JSON-based definition of a certain hardware node and what actions it exposes to the LLM. This then bootstraps a custom TCP networking layer deployable on the hardware node compliant with our novel HCP interaction layer. The LLM goes through an initial discovery period where any HCP-bootstrapped TCP nodes are able to subscribe to it and pass relevant context in the HCP-defined schema. Sensors, like a camera, can detect the locations of objects and items of interest within their sensing frame, exposing them to the model; these can then be used to inform control actions orchestrated by the HCP. Challenges we ran into Architecting HCP to be a scalable architecture that would cleanly integrate a fully in-software LLM to real-life hardware. Exposing generic hardware interfaces on actuator interfaces (such as the demo'd SOARM101) to be controllable by the LLM, developing inverse kinematics and smooth path planning for safe operation of the robot arm as well. Accomplishments that we're proud of Creating a fully-fledged SDK that we were able to use to bootstrap demo hardware nodes at near-zero ramp-up or integration cost. Creating a fully custom TCP networking stack under a publish/subscribe model that was HCP-compatible and allowed seamless multi-node orchestration. Creating a seamless agentic loop between pure-software LLMs and distributed hardware nodes, both for sensing and environment manipulation. What we learned Building HCP taught us that bridging the digital reasoning power of LLMs with the physical world requires both a solid networking backbone and a thoughtful interface abstraction. We learned how critical it is to design schemas that balance simplicity with extensibility. This enables both small embedded devices and complex robotic systems to integrate seamlessly. We also realized that context management is the heart of intelligent automation: giving LLMs structured, real-time situational awareness unlocks emergent problem-solving behaviours that feel almost human. SOARM-101 Integration The goal of the SOARM-101 integration is to provide an actuation platform that can be controlled by the HCP SDK. While the HCP SDK provides an authoritative interface for exposing a hardware node's capabilities, integrating a robotic arm required significant effort. The robotic arm provides control functionality to move to a desired position and grab and move objects. LLM interprets the user’s prompt about what they want to eat and moves the arm to pick up the desired ingredients to make a suitable dish. 3DOF End-Effector Commanding In robotic manipulation challenges, the goal is typically to track an end-effector position in the world. However, the SOARM-100 only exposed an API to command joint angles, requiring us to develop our own single-link-chain inverse kinematics model . The solver can solve for multiple manipulator configurations (elbow up/down). The advantage of this approach is that it generalizes the HCP's interaction with the arm (fully in world-frame space), thereby enhancing the control system's generalizability. The development of the model required implementing a custom simulator to validate that null-space solutions are rejected, as well as to provide a sanity check that the forward and inverse kinematics models yield sane results. A figure of the simulator is shown below and has proved to be helpful in debugging and iterating off-target. Camera and Vision Detection A camera was used to identify the locations of each object for the robot to interact with, using AprilTags and OpenCV. It exposes each object's type and position to the HCP layer so the LLM can guide the robot to interact with them. This approach of publishing generic data can be easily expanded to any type of sensor in the future, to help the model gain a better understanding of its environment. What's next for Hardware Context Protocol Our next step is to expand the HCP SDK into a fully modular ecosystem that supports standardized drivers, cloud-based orchestration, and real-time safety supervision layers. We hope to release open-source tools, including the ones developed at this very hackathon, for rapidly bootstrapping HCP-compatible nodes across a variety of microcontrollers. In the long term, we envision HCP serving as the foundation for a universal hardware abstraction layer for AI agents, enabling LLMs to intuitively control everything from IoT devices to full-scale industrial robotics, bringing physical intelligence to any environment. <div