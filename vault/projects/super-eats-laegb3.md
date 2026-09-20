---
slug: "super-eats-laegb3"
url: "https://devpost.com/software/super-eats-laegb3"
title: "Super Eats"
hackathon: "Meta Quest Presence Platform Hackathon 2024"
organization: "Meta"
winner: true
words: 1001
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/video_visual"
---

# Super Eats

> Super Eats: Sync, Coordinate, and Cook— a cross-platform multiplayer MR game

[Devpost](https://devpost.com/software/super-eats-laegb3) · hackathon [[Meta Quest Presence Platform Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** c#, c4d, ios, maya, metapresenceplatform, photonfusion2, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for super eats

## Body

Mobile player checking and communicating the location of customers; Headset player opens window in that direction and sees a ramen order Mobile player prepares food accordingly Food appears in headset view Delivering food out to the customers Inspiration True multiplayer XR/MR begins when everyone in the room can play even when there’s only one headset. Our project introduces an innovative multiplayer game designed to overcome barriers to the widespread adoption of XR/MR technologies, specifically the limitations of multiplayer experiences. Unlike conventional console games that enable shared gaming experiences within a single room, headsets isolate each player to their own virtual spaces. In scenarios such as house parties or family game nights, especially when only one headset is available, XR/MR games are often not the preferred choice. This is part of our vision and belief that the broader adoption of these technologies will be driven by providing multi-modal access to its content, accommodating diverse contexts and users. Key to this expansion is the development of a robust ecosystem that supports seamless data sharing across platforms and devices. What it does Our game —centered around a collaborative food truck adventure—unites players by allowing headset and non-headset users to collaborate intimately within the same physical space. This dynamic setup enhances the appeal of mixed reality for group entertainment in domestic settings, making immersive and interactive gaming accessible regardless of the number of headsets available. By emphasizing the social context alongside the content, our project positions mixed reality games as viable options for same-room multiplayer experiences. Story World and Objectives Set in a dynamic universe, "Super Eats" tasks players with navigating a food truck across various imaginative worlds. The interior of their physical room transforms into the food truck, journeying through exotic locations and interacting with hungry customers through a small service window due to a toxic external environment. Players aim to satisfy these customers efficiently to earn stars and aspire to be recognized as the top food truck in the universe. Challenges and Mechanics Toxic World Challenge: Players must manage the hazardous external environment by strategically operating the food truck’s service window. Mixed Reality Interaction: With the service window closed, the headset-wearing player cannot see the customers. The mobile player, equipped with a device connected to a surveillance camera, guides the headset player, signaling when and where to interact with customers. Player Roles Mobile Player (Central Systems Operator): This player handles internal logistics, manages food orders, and communicates customer positions and optimal service times. Headset Player (Food Truck Operator): Focuses on direct interaction with customers, handling orders and delivering food through the service window. How we built it Multi-Player Mechanism: Utilizing Photon Fusion 2, we established a robust connection between the headset and mobile players in a classic Host-Clients setup, with the headset player as the Host. Headset User Experience: We integrated interaction and audio SDKs, along with the passthrough feature and scene understanding from the Presence platform, to enhance the headset player's functionality. Mobile User Experience: We implemented basic 2D interactions such as drag & drop, and custom scripts to detect physical shaking to make the preparation of food more fun. Modeling & UI Assets: Key visual assets, such as the kitchen table, projector, and alien customers, were developed using Maya and C4D. Automation of rigging and animation was achieved through Mixamo, while UI designs were crafted in Figma. Challenges we ran into Designing "Super Eats" posed several unique challenges: Cross-platform Interaction: Achieving smooth interactions between the headset and mobile player was crucial. We engaged in bodystorming to physically enact the game experience, which helped us refine the dynamics between the two types of gameplay. Task Division and Balance: We carefully considered how to distribute tasks and ensure both roles were equally engaging and significant. This balance was vital to prevent skewing the fun level or diminishing the role's importance, especially since the mixed reality aspect inherently offers an appealing experience. Game Design and Mechanics: As first-time game developers, we tackled the steep learning curve of understanding the intricate aspects and considerations necessary in game creation. Accomplishments that we're proud of We are immensely proud of several achievements in this project: Problem-First Approach: We tackled the project with a focus on a prevalent issue — scenarios where only one headset is available at a physical location. Our approach ensured that we addressed real-world constraints head-on, paving the way for more inclusive gaming environments. Innovative Vision: Our project pushes the boundaries of current technology by exploring the integration of seamless device connectivity and synchronization within mixed reality environments. Venturing into the relatively unexplored interface between mixed reality games and mobile devices, we are charting new territories in what we believe is a burgeoning field. Technical Aspects: We achieved seamless integration between Meta Quest and mobile devices, enabling robust data sharing capabilities. This includes precise location sharing and real-time game status updates between devices, enhancing the interactivity and coherence of the mixed reality experience. Creation of Custom Assets: We developed bespoke 3D assets for the game, including the unique creatures (customers), the kitchen table, and the portal opening machine. What we learned Room Model Data: This proved crucial for cross-platform data sharing, enabling a cohesive gameplay experience across different devices. Passthrough and Opening Portals: These features are key in bridging the virtual and real worlds within our game environment. Cross-Platform/Device Considerations: Venturing into this new field has highlighted the significant differences in perspective, scale, and gameplay experience between headset and mobile device users. Addressing these disparities is critical for balanced and engaging game design. What's next for Super Eats Refining Gameplay Journey: We aim to streamline both onboarding and offboarding processes to ensure a smoother user experience from start to finish. Expanding the Game Universe: Plans are in place to enrich "Super Eats" with additional worlds, challenges, and customer types, further enhancing the game’s depth and appeal. Optimizing Cross-Device Interactions: Continued development will focus on improving the synchronization and interaction between different devices, potentially exploring asynchronous gameplay possibilities or play options in separate rooms. <div