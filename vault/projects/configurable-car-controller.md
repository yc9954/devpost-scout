---
slug: "configurable-car-controller"
url: "https://devpost.com/software/configurable-car-controller"
title: "Physics Car"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 582
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/transportation"
---

# Physics Car

> Customize this configurable drag-and-drop car controller to use in any world! Its "almost real" physics system features 43 tweakable parameters to emulate the real life physics of your favorite cars.

[Devpost](https://devpost.com/software/configurable-car-controller) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[civic_government]] [[transportation]]

**stack** blender, desmos, horizon, substance3d, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for configurable car controller

## Body

"Yamada" Car Render Asset Import Buyable "Physics Cars" in ModCity Drifters Driving on Mobile Driving Instructions Inspiration Our Remixable World submission, ModCity Drifters , needed a vehicle system for players to drive around on our roads with. We love the Warthog driving physics in the original Halo games and wanted to capture that same feeling. What we ended up creating is a fully configurable car controller system that includes 43 different tweakable parameters! These parameters are based on real-world physics, meaning creators using this system could find the torque curves of their favorite actual cars and recreate them accurately in Horizon Worlds. In ModCity Drifters , we specifically wanted this so we could create cars that were popular in 90s Japan for players to buy and race. What it does Physics Car is a drag-and-drop car controller system with configurable parameters. World creators can easily drag our base car, the "Yamada" (based on the original 1977 Honda Civic) into any world for an immediate way to let players drive around. Car fans looking to create virtual versions of their favorite real-life cars can locate the correct graphs online and easily adjust our controller parameters to emulate that specific one. Creators can use this physics system for more than just cars, too. Any mesh works if there's a seat to drive it! There's infinite possibilities just by using Physics Car as a base. How we built it The end system is a mash-up of multiple systems. Inspiration for the engine RPM mechanics was taken from Wassimulator's Better Software Conference talk , then on top of that we built a standard-ish raycast-based suspension system. After getting driving to work, we added friction forces to the wheels to properly apply force to the ground. The final and longest portion of development was polish. We took our time making sure the control scheme was usable on different platforms, sound effects and particles to add flavor, and solid models to really solidify how "real" the cars feel to drive. Challenges we ran into This asset required a lot of math and advanced reasoning to create the physics parameters. It took a lot of trial and error to make the controller feel "almost real" while still being intuitive and fun to drive, especially since not all of the required Rigidbody properties are exposed by Horizon. However, through a lot of tweaking, guesstimating, and failed solutions we have something that works well. Accomplishments that we're proud of The Physics Car provides something new that doesn't currently exist in Horizon Worlds. We genuinely enjoy driving it! Everything from RPM, suspension, sound effects, to even tire smoke is completely adjustable. The variety of unique vehicles you can make with this feels awesome. It ended up working perfectly for the different purchasable cars we included for ModCity Drifters! What we learned This project really solidified our knowledge of both Horizon's physics APIs and how to simulate very interconnected systems manually, especially relating to angular velocities and friction forces. What's next for Configurable Car Controller We only included one basic car preset to use in this specific asset to keep it as manageable as possible, but we 3D modeled and emulated 3 other real-life cars to use in ModCity already. If creators love using our Physics Car, we'd love to make the other presets available stand-alone to use for plug-and-play as well! From there we could also create planes, boats, and other variations of different physics-based vehicle controllers. There's tons of possibilities. <div