---
slug: "cross-device-controls"
url: "https://devpost.com/software/cross-device-controls"
title: "Cross-device Controls"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 988
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Cross-device Controls

> Creating plugins that allow Logitech devices to interact within Logitech's hardware and software ecosystem, reducing dependency on accessing hardware controls outside of the workflow.

[Devpost](https://devpost.com/software/cross-device-controls) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** c#, css, html, javascript, logiactionssdk, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for cross-device controls

## Body

Inspiration Wanting to use the MX Creative Console as a control center for other Logitech devices such as the Litra series of lights and the Z407 speaker system What it does The first proof of concept are a plugin for powering on and off and adjusting the lighting of the Litra Glow, Litra Beam, and Litra Beam LX, including RGB controls for the LX. The second is a plugin that replaces the wireless controller for the Z407 speaker system. How I built it Litra Layers The plugin layers device discovery/control services, single-thread command queues, state/mapping persistence, and a lightweight local settings web server around Litra actions. For device I/O, it uses HidSharp as the cross-platform HID layer (USB/Bluetooth), which maps to native OS HID stacks per platform. The settings interface lets users assign friendly names to their Litra devices, which helps them distinguish between multiple lights in the action list, which makes it easier for them to distinguish when they have several of the same model. Users can also create groups to control multiple devices with a single action. The plugin maintains stable identifiers behind the scenes, these custom names and group configurations persist even when devices reconnect on different USB ports or Bluetooth pairing cycles. When the plugin can't automatically match a reconnected device to its previous configuration, users see a reassignment prompt and interface where they can manually link the physical device back to their saved settings, preserving all their customizations and group memberships without having to reconfigure everything from scratch. Z407 Layers Since I wanted this plugin to be cross-platform, the biggest hurdle was handling BLE consistently on both Windows and macOS. I ended up building two distinct backends that plug into a shared device manager: Windows: I went the native route, using an in-proc service. This talks directly to the WinRT Bluetooth APIs, keeping everything fast and bundled within the main process. macOS: macOS Bluetooth is difficult with C#, so I built an out-of-proc Python bridge. I used the bleak library to handle the CoreBluetooth communication, and linked it back to my main app using JSON-RPC over stdio. It essentially treats the Python script as a background helper that "pipes" data back and forth. The result? Both versions expose the same IBleService contract. This means the higher-level logic (e.g., driving the specific Z407 characteristics) doesn't even know which OS it's running on. "It just works." The plugin also includes a built-in web UI where users can scan for Z407 devices to connect to and name them. It uses a similar mapping layer as the Litra plugin for consistent parameters to remap devices in the event that their IDs change. Challenges we ran into Litra How to give individual devices of the same type unique IDs on Windows. Using the device path works, but it changes if the user plugs it into a different port. Currently, I've implemented a mapping ID structure to give "new" serial numbers or device paths a unique ID. This ID is used for parameters. If the device changes ports and is recognized as new, the old mapping is marked as missing since it can't resolve the older ID. At this point, the user is prompted with an option to remap the old, including its custom name, to the new device, maintaining the parameters for actions already assigned to the Creative Console or Actions Ring. Trying to create more graphical representations of individual device parameter actions to make it easy to identify which light the action corresponds to. There are inconsistencies and limitations in how images and text are rendered for different types of actions. Z407 BLE controls can be a bit of a challenge with respect to device discovery and obtaining control, especially if another device is already controlling it. The device name is identical for all Z407 units, so if there are more than one, it can be hard to identify which is which. I added a feature to send a command to trigger one of the sounds on the speaker to identify it before setting it as the default. This isn't ideal if your partner is listening to something on theirs or if a neighbor happens to also have one. Accomplishments that we're proud of Litra A fully functioning Litra plugin with full support for RGB controls on the Beam LX. Additionally, the plugin features a web UI for creating custom groupings for synchronous controls. Z407 A complete collection of commands that are normally issued by the Z407's wireless controller, including input switching, pairing mode, and a new "release control" command. In the event that there might be multiple devices nearby, it includes a web UI for selecting the default device to connect to. What I learned A lot! HID and BLE commands are great, but there are limitations with what's possible. There are a lot of considerations with respect to designing the UX for these plugins in the context of the Actions Ring and the MX Creative Console. On the Actions Ring, there aren't any dynamic folders, so standalone actions are required to support it. On the Creative Console, having a lot of standalone actions for each device would take up a lot of real estate, which is why the plugin provides a dynamic devices folder and a dynamic groups folder. Both folders include an action to quickly access the settings UI. Honestly, I find myself obsessed with optimizing the UX of these plugins to make the user feel like everything just makes sense and there's no wrong path to get to what they need. What's next for Cross-device Controls Optimizing the UX and exploring other possible interactions between other devices. If there's a way to develop a plugin that can access and present actions for more device controls available through Options+, that would be a game changer for Logitech, the MX Creative Console, the Actions Ring, and for users who are invested in Logitech's ecosystem. <div