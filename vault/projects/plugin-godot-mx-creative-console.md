---
slug: "plugin-godot-mx-creative-console"
url: "https://devpost.com/software/plugin-godot-mx-creative-console"
title: "Godot Plugin - MX Creative Console"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 1035
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Godot Plugin - MX Creative Console

> Transform your Godot workflow with the MX Creative Console. Master the timeline, manipulate 3D transformations, and sculpt levels with analog precision.

[Devpost](https://devpost.com/software/plugin-godot-mx-creative-console) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** gdscript, godot

## How they structured the write-up

- the inspiration behind the plugin
- use cases and dial/keypad functionalities

## Body

The Inspiration Behind the Plugin Developing video games and interactive experiences is a fascinating process, but inherently tied to a constant friction: the user interface. Modern and massively growing engines like Godot Engine offer incredibly powerful visual tools, but the developer is still forced to interact with three-dimensional spaces and complex timelines using the two-dimensional paradigm of the mouse and keyboard. Dragging tiny numerical sliders, trying to click a rotation gizmo in a cluttered scene, or making micro-adjustments in an animation curve generates enormous cognitive and physical fatigue. Integrating Logitech's advanced MX Creative Console directly into this development ecosystem would greatly improve Godot's interface and the usability of its tools. Historically, hardware with physical dials and tactile precision has been reserved almost exclusively for video editors or colorists. By introducing this level of analog control into game development, we present an unprecedented opportunity to evolve how creators interact with the engine. We want to break the "click" barrier to give back organic control to the artist, level designer, and programmer, allowing them to sculpt, animate, and design instinctively with their own hands. Use Cases and Dial/Keypad Functionalities Godot Engine offers a massive array of tools, and there are countless options to integrate the functionalities of the MX Creative Console into its ecosystem. Below, we highlight some of the most important and revolutionary use cases we have planned: 1. Spatial Transformations and Environment Sculpting Moving objects in a 3D environment with a mouse requires using on-screen gizmos that often overlap or are difficult to select, slowing down level design. Analog Rotation and Scale: Through the console's keypad, the user can quickly select the type of transformation to use (Move, Rotate, or Scale) and choose the exact axis to modify (X, Y, or Z). Upon doing so, the dial assumes total control: a smooth turn applies the transformation with extreme mathematical precision for fine adjustments, while a fast turn allows for drastic changes. Possible Auxiliary Buttons: Snap / Magnet: A dedicated button to instantly toggle the magnetic grid or angular snapping, allowing for perfect alignment of modular architecture. Quick Reset: Purge buttons to instantly return an object's position, rotation, or scale to zero (0,0,0) in case of an error during modification. Space Switch: Dynamically toggle between the object's Local Space and the Global Space with a single touch. 2. Animation Mastery (AnimationPlayer) Animation requires surgical precision. Using the mouse to move the playhead often results in frustrating millisecond errors or misalignments on the timeline. Time Dial: The main dial of the MX Creative Console is mapped directly to Godot's temporal control. Turning the dial allows advancing or rewinding the animation frame by frame with perfect mechanical fluidity. Action Keypad: The backlit buttons allow capturing the current state and instantly adding position, rotation, or scale Keyframes with a single touch, or jumping back and forth between timestamps without moving the cursor. 3. Particle Systems Tuning The creation of visual effects (VFX) such as explosions, fire, or magic requires many iterative trial-and-error adjustments. Emission Adjustment: Use the dial to smoothly increase or decrease the amount of emitted particles, modify their initial velocity, or alter their spatial scale, observing the visual impact immediately in the 3D viewport. Seed Control: A keypad button configured to instantly generate a new random physics seed, allowing for rapid evaluation of different chaotic behavior patterns. 4. Rapid 2D Environment Editing (TileMaps) Painting 2D levels with Godot's TileMap tool is a time-consuming process. Quick Rotation: While using the brush tool, the dial allows you to rotate the selected Tile in exact increments before placing it on the grid. Layer Navigation: Use the console buttons to instantly move up or down between different drawing layers (Foreground, Background, etc.) without taking your eyes off the canvas. Brush Adjustment: The dial can also be used to dynamically increase or decrease the size of the painting area or radius. 5. Real-Time Game Controls (Live Debugging) Hardware-integrated physical controls to manage game execution. When testing the project, developers will have instant control without leaving the console. Execution Controls: Physical quick-access buttons to Play, Pause, and Stop the current project. Camera Override: Buttons to instantly toggle between the player's camera and a Free Camera (Editor Camera) to inspect the world and look for hidden bugs. It will also allow switching between 2D and 3D rendering views. Time Manipulation: Using the dial to modify the engine's simulation speed (Engine.time_scale), slowing down the game in real-time to perform precise slow-motion debugging. 6. Other Integration Options Lighting Adjustments: Select a light in the scene (SpotLight, OmniLight) and use the dial to smoothly adjust the light energy, attenuation range, or shadow softness, operating the editor as if it were a real photography set. Shaders and Visual Materials: Link the aluminum dial to custom mathematical variables ( Uniforms ). The developer can maximize the 3D screen and simply turn the dial to see how the roughness, color, or emission of a PBR material changes, without the user interface getting in their field of view. Our Technical Vision (How it will be implemented) On a technical level, we have been researching the data flow and determined that to implement this synergy, we need to build a communication bridge. On one hand, we will develop a native mini-addon inside Godot that hosts a local server (for example, via WebSockets) to allow direct, asynchronous, and secure communication with the editor's core. In parallel and externally, we will create the official Logitech plugin interacting with the Logi Actions SDK. This plugin will be responsible for connecting to our Godot addon, interpreting the use of the MX Creative Console, and sending physical action commands (such as the dial's rotation degrees or pressed buttons) to the editor in real-time. The Added Value for the Ecosystem This plugin's integration directly tackles creator bottlenecks and fatigue. By using the console's "Contextual Dials", it will intelligently understand what the user is doing in Godot and adapt its functions on the fly: if you select the 3D environment, the dial rotates objects; if you select the timeline, it navigates the animation. This standardizes the workflow, drastically improves ergonomics during long sessions, and adds a layer of total, pleasant immersion to the art of creating video games. <div