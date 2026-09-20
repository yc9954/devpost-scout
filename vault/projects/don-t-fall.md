---
slug: "don-t-fall"
url: "https://devpost.com/software/don-t-fall"
title: "Don't Fall!"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 558
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "user/patient_family"
---

# Don't Fall!

> Don’t Let Them Down: Jump, Rescue, Repeat. Friends are Waiting. Watch every Step.

[Devpost](https://devpost.com/software/don-t-fall) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**user** [[patient_family]]

**stack** javascript, lensstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for don't fall!

## Body

GIF Gameplay Inspiration We wanted to take the classic "endless runner" genre and make it personal. Usually, in platformers, you are running for coins or high scores, which can feel repetitive. We asked ourselves: "What if the stakes were higher? What if you were running to save your real-life friends?" The inspiration came from wanting to utilize the social graph within Snapchat to create an emotional connection, making the player feel like a hero for their specific circle of friends. What it does Don't Fall! is a precision-based AR platformer where the environment is procedurally populated by the player's actual Snapchat friends. Dynamic Gameplay: As the player navigates the 3D obstacle course, the game fetches random profiles from their friend list and places them on "safe" tiles. The Rescue Mechanic: When the player successfully lands on a tile occupied by a friend, that friend is marked as "Saved." High-Stakes End Screen: If the player falls, the game ends. A dynamic "Survivor Status" board appears, listing exactly who was saved (with a celebratory Bitmoji) and who was left behind, encouraging the user to try again to get a "perfect run." How we built it User Context System: We utilized the User Context API to fetch the player's friend list asynchronously. Asset Management: We wrote a custom script to handle the instantiation of 3D Bitmoji avatars on the tiles in real-time. To ensure performance wasn't impacted, we implemented a pooling system that recycles tiles and avatars. Game Logic: The core loop uses a state machine to track "Saved" vs. "Unsaved" friends. We used arrays to store the friends encountered in the current session so that the end screen (UI) matches the gameplay exactly. UI/UX: We used the 2D UI system to create the "Survivors" HUD and the scrollable results list at the end, dynamically injecting the 2D Bitmoji stickers corresponding to the specific friends encountered. Challenges we ran into Asynchronous Data Loading: Fetching friend data (names and avatars) takes time. We had to ensure the game didn't lag or show "empty" tiles while waiting for the Bitmoji 3D assets to load from the remote service. Randomization Logic: Ensuring that the same friend didn't appear twice in a short sequence required writing a specific shuffling algorithm for the friend array. Accomplishments that we're proud of Seamless Personalization: The game feels native to every single user because it adapts to their social circle immediately. Complex State Tracking: Successfully passing data from the 3D world (collision with a friend's tile) to the 2D UI (the end screen report) without data loss or mismatch. Visual Polish: The transition between the 3D gameplay and the 2D UI overlay feels smooth and professional. What we learned Building this deepened our understanding of Lens Studio's Bitmoji Module and the intricacies of handling 3D Bitmoji assets. We learned how to balance heavy asset loading (3D avatars) with smooth frame rates. We also learned the importance of "emotional UI"—players react much more strongly to seeing their friend's face on a scoreboard than just a text name. What's next for Don't Fall! Power-Ups: Adding shields or "double jumps" to help save more friends. Social Roasting: Adding a feature to automatically tag the friends you didn't save in a Snap, with a caption like "Sorry I dropped you!" Global Leaderboards: Tracking who has saved the most friends cumulatively over time. <div