---
slug: "knights-acsending-undead-incursion"
url: "https://devpost.com/software/knights-acsending-undead-incursion"
title: "Knight's Ascend - Undead Incursion Update"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 832
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Knight's Ascend - Undead Incursion Update

> Face the Undead and Rise! Knight’s Ascend returns with a chilling new update! Defend the realm against a necromancer. Train, upgrade, and battle together through waves of the undead.

[Devpost](https://devpost.com/software/knights-acsending-undead-incursion) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** audacity, blender, meta-horizon-desktop-editor, meta-horizon-gen-ai, typescript, visual-studio

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for knight's ascend

## Body

In the previous version the sky was peaceful. But now the necromancer and his army have arrived. The old gate told the players that something was about to come. Now the gate has openend, we are ready for battle. The UI has been overhauled. The new icons help with visual immersion. Progression: Level up and unlock new abilities Progression: Show everybody how far you have come with your titles. Progression: Collect new weapons and equip them at the blacksmith. The Necromancer looms over the sky - can you defeat his army? When you are ready, join the fight! The Undead Incursion Update awaits you! Inspiration The sky has darkened - the undead incursion is upon us! Every fantasy world needs a compelling antagonist, and the threat of an undead necromancer felt like a natural fit. In terms of world-building, I drew inspiration from iconic sources such as World of Warcraft , The Lord of the Rings , and Warhammer . 🔄 What's New in This Update UI Overhaul : The interface has been redesigned for immersion and visual consistency. Icons have been added throughout. Undead Incursion : Players can now fight against the necromancer army in special PvE encounters. By doing so they unlock new items and abilities. Ability Customization : Players can now tailor their skill loadouts before battle - mix and match unlocked abilities to suit your needs. There are three types ability slots: Passive Abilities - Modify how your character reacts in battle. Attack Abilities - Modify your attacks and generate mana. Active Abilities - Use Mana for powerful spells. Unlockable Titles & Items : New progression features let players earn unique titles and collect powerful weapons as they rise through the ranks. Bugfixes : In the previous version there certainly were a few bugs that have been fixed. Like Combat ending after 100 rounds, floating text not disappearing or the UI not being able to handle certain numbers. How we built it Development continued in the Meta Horizon Desktop Editor, with careful iteration and the feedback of engaged players guiding improvements. The updated UI was built with usability and aesthetic consistency in mind. In the previous version, abilities and items were hardcoded as enums as a proof of concept. Now, a new Ability System has been introduced with a modular architecture to easily allow for future expansion. Challenges we ran into UI design : Crafting a polished, user-friendly interface is difficult when designing for 3 platforms, so certain trade-offs had to be made e.g. Semi-Transparent surfaces look better on Mobile and PC than in VR - I plan to make these visual options customizable for players. System flexibility : Adding the new ability and item system meant rewriting parts of the old codebase. Future additions should now be easier to integrate. Time Constraints : I had a limited window to work on this update, so I had to prioritize the most impactful features, like the new ability system, UI overhaul and visual changed of the world. I relied again on an asset pack by Kay Lousberg , when adding the undead characters, which helped maintain visual cohesion throughout the world. For the icons i used an asset pack i bought by the artist Steven Colling . Accomplishments that we're proud of The overhauled UI makes the game more approachable and engaging, the icons add to visual clarity. Players now feel more empowered with the ability to build custom strategies through ability loadouts, its also more fun to just experiment and try new combinations. Titles, abilities and items make progression more rewarding and visible. The undead incursion was introduced gradually across several updates before this submission, teasing the new content and building anticipation. What we learned This update pushed me to go beyond the foundational mechanics and think more about user experience and long-term progression and engagement. I got more familiar with the Horizon API , and discovered new possibilities. The creation of future worlds will definitely be faster and smoother. What's next for Knight's Ascend Compared to the last version the abilities and items are no longer just a proof of concept, they allow for engaging experimantation. It now easier to add new abilities and weapons which i want to keep doing, especially in the time right after submission. There are certainly more UI and visual improvements to be made, in this update i focused more on creating a solid codebase to enable future additions more easily. Creating animations, visual effects and wearables for the players are still open tasks. The new "Persistent World Variables" allow to create more engaging community gameplay, where the players work together over weeks towards a common goal. This opens the door to future updates or linked worlds, where the players enter another realm and together free it from evil. The world could evolve as players reach milestones, such as the number of defeated enemies or resources donated. First tests of how this mechanic might work are already included in this update. <div