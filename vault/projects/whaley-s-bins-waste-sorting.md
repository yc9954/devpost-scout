---
slug: "whaley-s-bins-waste-sorting"
url: "https://devpost.com/software/whaley-s-bins-waste-sorting"
title: "Whaley's Bins Waste Sorting"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 977
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/immigration_refugee"
  - "substrate/video_visual"
---

# Whaley's Bins Waste Sorting

> Whaley's Bins game turns players into eco-heroes, educating them on recycling through fun gameplay. It inspires real-world action, showing sorting isn't daunting but a key step towards sustainability.

[Devpost](https://devpost.com/software/whaley-s-bins-waste-sorting) · hackathon [[Global Gamers Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[accessibility]] [[agriculture_food]] [[immigration_refugee]]
**substrate** [[video_visual]]

**stack** dart, firebase, flutter

## How they structured the write-up

- 🌱 sustainability issues
- 🌎 real-world impact
- 🎮 game concept
- 🖥️ multiplatform
- 💡 google wallet
- 🔋 greener development
- 💙 accessibility
- 🚀 roadmap

## Body

Supported on Windows, iOS, Android, Web & macOS Microsoft Store Mobile game Achievements macOS game - main screen macOS game - gameplay How do you properly recycle old paint? And a coffee cup—should it go into the "paper" or "packaging" bin, or perhaps neither? Starting with waste recycling might seem daunting, but it doesn’t have to be. Whaley, the friendly whale, is here to guide you as you learn to navigate the complexities of recycling while helping to keep the ocean clean. Learn from a game - apply it in real life! 🌱 Sustainability Issues Why is waste management topic important for a sustainable world? In some EU countries, over 60% of household waste still ends up in a landfill and only 20% of global waste is recycled each year. The ocean is burdened with approximately 12 million tons of plastic waste annually. Within the UN Sustainable Development Goals , three goals directly relate to waste: Goal 11: Make cities and human settlements inclusive, safe, resilient and sustainable Goal 12: Ensure sustainable consumption and production patterns Goal 14: Conserve and sustainably use the oceans, seas and marine resources for sustainable development What does this mean? Learning about waste sorting and initiating waste management activities in your community can address various sustainability challenges, such as: Improving air quality and better waste management in cities Reducing global food waste Protecting air, water, and soil Cutting down on waste generation Preventing and reducing marine pollution 🌎 Real-World Impact By engaging players in sorting waste through a fun, interactive setting, the game raises awareness about the various types of waste and their proper disposal methods. This knowledge can seamlessly translate into real-world actions, making players more mindful of how they dispose of waste. The game simplifies the concept of waste sorting, showing that it is an achievable task. This approach can demystify the process for those who might find the idea of waste sorting daunting or complex, encouraging them to initiate small-scale sorting efforts at home or within local community spaces. 🎮 Game Concept Swap items in each "row" by dragging one item onto another to place each item into the correct waste bin. Learn about waste sustainability as you play—if you didn't pass the level, Whaley will share a fun fact and ask a question about it for a chance to unlock the next level! This method of learning feels motivating and lightweight without any pressure, demonstrating how sustainability education can work for all ages. Bonuses and achievements add layers of excitement, rewarding accomplishments such as completing rows of correctly sorted items or playing in battery saver mode, aligning with the game's eco-conscious theme. For an added challenge, sometimes a "highspeed lane" activates, causing items above one bin to move at a different speed until the end of the level. All players can unlock special achievement card collectibles, compete with friends, and see who scores higher on the online leaderboard. 🖥️ Multiplatform The game features a responsive UI, designed and released on the following platforms: iOS (phones and iPads) - live Android (phones and tablets) - live Web - live macOS - live Windows - live 💡 Google Wallet There are five achievement cards that can be collected in the game based on finished levels and overall score. Those playing on Android can add the achievement as a collectible card to Google Wallet. The vision for this integration is that in the future, we could collaborate with local waste-sorting authorities in different countries, offering perks for those who show a card in the wallet, e.g., show your achievement card and get a discount for household waste collection services or similar sustainability-related promotions in real life. Cards have a similar aesthetic and use aquatic themes, with each having a slight color accent correlating with one of the bin colors used in the game. 🔋 Greener Development Inspired by the "Mind your app footprint!" talk at Flutter Heroes 2024, I included special bonus points for users who turn on "battery saver" mode (on supported platforms). This encourages players to enable battery saver to score more points. Additionally, I opted for a level-generation logic instead of storing level configuration files within the package, reducing the app's size. I also minimized network requests to decrease the payload - less data transfer means less energy needed to power servers, network equipment, and devices during transmission. 💙 Accessibility Usage of Semantics for Accessibility Tools I used Flutter semantics widgets like Semantics, MergeSemantics, and ExcludeSemantics to enhance the user experience by providing clearer navigation. High Contrast Mode on Demand I added an "increase contrast" button for users with visual impairments who are more comfortable using higher contrast between background and text. Color-Blind Friendly Palette and Assets I employed a color-blind-friendly UI to ensure the game is enjoyable for people with various types of color blindness. Game assets are designed with black borders, making them distinguishable from the background. Below, the simulator showcases demos for deutan, protan, tritan, and black-white color weakness. Support User-Defined Font Sizes I avoided force-scaling text or font size to allow users to define larger fonts from the device settings. I preferred Wrap over Row to accommodate large elements for those who might need them. Tactile Feedback for Buttons I used haptic feedback (light impact) on buttons to provide a non-visual cue that an action has been performed. 🚀 Roadmap Here are some future improvements planned for our roadmap: Improving test coverage New trivia questions New trash item types Asset Licensing Information All assets used in this application, including images and sounds, are either created by the author or are licensed under CC0, aligning with the permissions granted by authors such as 'Scribe' (Daniel Stephens), 'nene', and Lukas Klingsbo. Press Start 2P font is licensed under the SIL Open Font License, Version 1.1. Acknowledgments Special thanks to Dmitrijs for helping with the testing! <div