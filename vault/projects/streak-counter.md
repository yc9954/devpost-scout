---
slug: "streak-counter"
url: "https://devpost.com/software/streak-counter"
title: "Streak Counter"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 740
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "substrate/video_visual"
---

# Streak Counter

> Streaks, reimagined. 30+ unlockable badges, stats tracking, and friendly competition. See who responds faster, who breaks more, and earn achievements for milestones, holidays, and hidden secrets.

[Devpost](https://devpost.com/software/streak-counter) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**domain** [[developer_tools]] [[immigration_refugee]]
**substrate** [[video_visual]]

**stack** adobe-illustrator, blender, javascript, shader-graph

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what i learned
- whats next

## Body

Inspiration When the Turn-Based component was announced at Lens Fest 2025, it was pretty clear they wanted people to make games with it. All the demos were chess, word games, quiz battles, that kind of thing. But while watching the presentation I kept thinking about one thing: turn count. That simple number incrementing with each exchange between two users. Snapchat already has something like that, streaks. Its been part of the platform forever but there hasn't been a way to track or enhance it within a Lens. So that's what I decided to build. Not exactly groundbreaking I know, but I wanted to see how far I could push it beyond just a number. What It Does The lens tracks streak days between two users using the Turn-Based component with a 24 hour rolling window plus grace period to match how native streaks work. The main visual is a 3D number attached to the users forehead showing the current streak count with a little fire icon. Theres also a border around the screen edges made with a shader that changes colors as the streak goes up. Beyond that I wanted it to be more than just a counter so it also has: A slide out stats menu showing longest streak, total snaps, average response time and fastest response time for both users Over 30 unlockable badges for things like hitting milestones, snapping on holidays, or sending at 11:11 A memo system that shows different messages based on time of day, how fast you responded, streak context and other stuff Bitmoji is used throughout the UI, with each users avatar shown next to their stats in the menu and the other players Bitmoji appearing next to memo messages in a chat bubble. How I Built It The project has a few main systems: Streak Controller handles all the Turn-Based events, manages the variables, calculates timing and exposes an API for other components to use. Getting the timing right was tricky since streaks should only increment once per day and response times need to measure from send to send not send to open. Badge System is a carousel of 30+ badges each with different unlock conditions. Some are simple like reaching day 7 and others are more fun like snapping at exactly 11:11. This system also uses persistent storage so badges persist per user across streaks with any amount of friends. Memo Controller has around 100 contextual messages sorted by priority. Stuff like holiday greetings, late night quips, milestone celebrations, and filler messages when nothing special is happening. For the visual design I worked with Amber Wright who did creative comps and helped concept the whole thing with me. Challenges Debugging async functions in Lens Studio is rough. The editor doesnt show errors from Promises so I spent way too long tracking down bugs that ended up being simple async/await issues. The Turn-Based component was built with games in mind so it expects a fullscreen auto-capture flow. Getting it to work like a normal snap lens where users just tap to take a photo took a few weeks of back and forth with Lens Studio support. We had to work through issues like the engine freezing on capture, incomplete turn data errors, and variables not persisting when set during the capture event. Eventually got it working with some workarounds they suggested but it was a process. Matching the one per day rule for streaks took some trial and error. I needed to track dates carefully so rapid back and forth snapping wouldnt inflate the count but also had to make it testable without waiting a full day between each test. I also ran into limitations with user data access. Since Turn-Based uses some external server, some APIs are be restricted in order to protect the user’s privacy. I couldn't get access to access to certain user info like birthdays so I had to cut a few features I had planned around that. What I Learned The Turn-Based component can do more than just games. Its really just about tracking exchanges between two people over time which is exactly what streaks are. Whats Next While making the submission video I ended up taking a lot of test videos of my cats. So one thing I want to add is the ability for the streak count to attach to pet faces as well as human foreheads. Seemed like an obvious addition after that. <div