---
slug: "escape-from-heat-island"
url: "https://devpost.com/software/escape-from-heat-island"
title: "Escape From Heat Island"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 775
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "substrate/video_visual"
---

# Escape From Heat Island

> The city is turning into an urban heat island, and it's getting too hot! Plant trees to lower temperatures and stop the residents from fainting. Keep the neighbourhood alive!

[Devpost](https://devpost.com/software/escape-from-heat-island) · hackathon [[Global Gamers Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[climate_energy]] [[developer_tools]] [[transportation]]
**user** [[developer]] [[general_public]]
**substrate** [[video_visual]]

**stack** c++, dart, filament, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for escape from heat island

## Body

Escape From Heat Island! Start Menu This is a new neighbourhood in Animal City. New buildings are being added every day. It's getting hotter and hotter. The residents are in danger! At 35 degrees, they will start fainting. Plant trees to cool the neighbourhood. Reduce traffic to lower the temperature. Now keep going across the whole neighbourhood, before all the residents faint! Don't let them down! Game Over! Inspiration I wasn't truly aware of "urban heat islands" until I moved to Singapore and experienced it first-hand. I decided to build Escape From Heat Island to spread awareness of the phenomenon. "Urban heat islands" are inner-city areas that become dangerously hot due to a combination of: 1) more heat absorbed by roads, buildings, asphalt and concrete 2) more heat produced by air-conditioning, refrigeration and vehicles 3) lack of vegetation Heat islands aren't just uncomfortable; they can be fatal to humans and animals. If global temperatures continue to increase - particularly in humid areas - this will be a growing problem. We need to take proactive measures to allow urban centers to develop sustainably. With Escape From Heat Island, I hope to bring attention to some options for doing so. First, we need to increase the amount of natural vegetation like trees, shrubs and bushes. These shade the ground from direct sunlight, reducing the heat absorbed by artificial surfaces like roads and buildings. They also indirectly cool their surroundings by evaporating water from the air. Second is to reduce the heat introduced by vehicles. Heavy traffic contributes significantly to urban temperatures, even with electric vehicles. If we could reduce the number of vehicles (or even better, reduce the amount of roads), urban temperatures can be reduced considerably. Other options include installing solar panels, increasing the albedo (colour) of surfaces, using different construction materials, and many others. What it does You are in control of a new neighbourhood in Animal City. New buildings are popping up constantly - each one will raise the ambient temperature by 1 degree celsius. At 35 degrees, the residents will start fainting. Tap the footpath to plant a tree, or tap the road to install a barrier. Both of these will reduce the temperature by 1 degree. Try and keep the residents healthy as long as possible! How we built it Escape From Heat Island is somewhat unique - a 3D game written in Flutter! I had previously written a cross-platform Flutter package called flutter_filament for creating Flutter apps with 3D rendering & animation by wrapping the Filament . I decided this would be a good opportunity to showcase the package. I sourced the 3D models from https://kaylousberg.itch.io , added some keyframe animations with Blender, then started iterating on a few game concepts. I'm not a game developer, but hot reload/restart made this process a lot easier! I feel this is something that could help Flutter/Dart play a larger role in the game industry in future. Challenges we ran into Before starting Escape From Heat Island, flutter_filament only exposed basic rendering and animations. Specifically, there was no collision detection, no asset instancing and no viewport picking; these required some effort to implement. Much harder, though, were fundamental questions of game design. I hadn't really made a game before, and I discovered it's very difficult to go from nothing to something resembling a game. Camera positioning, game loop design, movement speeds, grid layout, etc - these are all quite difficult, and totally separate from the nuts and bolts of the actual software development. Additionally, building a cross-platform game means thinking about screen-sizes, control systems (mouse vs touch), orientation, resolution, etc. It's not trivial. Accomplishments that we're proud of I think Escape From Heat Island does a great job at showing the importance of managing heat in urban areas, and some of the options available to combat the issue. I think the animations, models, UI and sound are all really fun. The core concept is really interesting and I think it could be expanded on to make a fully-fledged game! What we learned Game design is hard! Rapid iteration and prototyping are very important, and deciding on the right scope from the outset is critical. There will inevitably be issues that don't crop up until the last stage before release, so it's important to drill down to the absolute minimal game loop as early as possible. What's next for Escape From Heat Island Expanding on this concept would be amazing - in particular, making a fully-fledged environmental management simulator. I also think there would be huge value in using Flutter and flutter_filament to create an actual 3D game editor (similar to Unity/Unreal). Fingers crossed! <div