---
slug: "last-bottle"
url: "https://devpost.com/software/last-bottle"
title: "Last Bottle"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 1266
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Last Bottle

> Make your last single use bottle, your last. Explore a plastic bottle's recycling journey, exposing the harsh realities of how ineffective the recycling solutions are to the global plastic problem.

[Devpost](https://devpost.com/software/last-bottle) · hackathon [[Global Gamers Challenge]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**substrate** [[video_visual]] [[web_dom]]

**stack** fastapi, flame, flutter, google-save-to-wallet, google-wallet, hive, nextjs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for last bottle

## Body

Last Bottle Cover Image Example screenshots of the Last Bottle game Example screenshots of the Last Bottle game Example screenshots in Japanese of the Last Bottle game Inspiration When thinking about how I could make a difference in terms of a sustainable game, I started by looking at the things I'm already doing. This lead me to recycling, it's not that I necessarily go out of my way to recycle but when the option is there I will chose it. My plan was to make a game that pushed people, like myself, to go out of their way and recycle more. I started by researching the recycling process where I discovered that recycling is actually very ineffective. It turns out that the majority of plastic can't or won't be recycled. More surprisingly, most of the plastic that people put in a recycling bin doesn't get recycled successfully and instead ends up in a landfill or incinerator. So what began as an idea to convince people to recycle more, lead me to learning more deeply about the problem and modifying the game idea to instead share the truths about the recycling process. The goal of the game is now to get people to realize that the world's plastic pollution problem isn't going to be solved by recycling, and that other solutions need to be created to prevent plastic production. What it does The game begins with a single use water bottle, which the player will "consume" very quickly. This is an intentional design decision to show how fast single use plastic goes from "useful" to "trash". After the bottle is consumed the player is on a journey to recycle it, which is designed as a very long and difficult process. As the player attempts to make it to the recycling bin, they have to avoid several obstacles which will get harder with each attempt. The obstacles include trash heaps, rivers, fires, and more. The obstacles are designed to mirror the very real outcomes that a typical plastic bottle may experience after it's use. When a player hits an obstacle the game ends and the player can attempt recycling again with a new bottle. Throughout the game, the player can unlock various trading cards. For example when hitting a trash obstacle for the first time, the player will learn about how common it is for single use plastic to end up in a landfill. Each trading card is a fact about the recycling process which the player can share with friends through Google Wallet. So how does one win the game? When a player does make it to the recycling bin, it's not an immediate win, in real life only a small portion of plastic that's put in recycling bins is actually reused or recycled successfully. To simulate this the player will spin a wheel and see if their bottle is in the lucky minority that's reused. This is intended to show the player that after doing their part of placing plastic in the recycling bin, it's out of their control and up to luck as to whether the bottle is successfully recycled. The game will show players how many attempts they've made at recycling and how many attempts were successful. The numbers might surprise some, and with the way the game is designed it's not possible to have a high rate of recycling - mirroring what we experience in reality. One goal of the game is to make people frustrated with how hard it is to "win", winning meaning you recycled your plastic bottle successfully. The idea is to get players to make the connection to how frustrating recycling is in the real world and show it is not itself a viable solution. How I built it The game is built with Flutter and uses the Flame game engine. The game is not entirely build in Flame, and is a mix of Flame and normal flutter. Flame is used for the main game play of avoiding obstacles and handling collisions. Then a material app is used for the menu, spin wheel, end screens, and everything else. Hive is used for simple on device data storage. There isn't a lot of data stored in hive, it's mostly the user's score and the trading cards they've unlocked. Riverpod is also utilized for state management, and is used to globally access the Hive instance. The Google Wallet integration includes a lightweight backend to generate the passes and return the pass url to the flutter app. This is built in Python using FastApi. The landing page was built from a modified version of an open source Next.js landing page project. For a detailed step-by-step explanation on how this game was built you can refer to this YouTube playlist where I'm going to show start to finish how to build this game. This will be an ongoing series and only the initial videos are currently live. Challenges I ran into The Google Wallet integration was somewhat challenging initially. At first, I was hoping to build this game with no backend at all. That ultimately didn't seem like a secure solution because of the nature of how the passes need to be signed. This was also my first experience using Flame so there was a learning curve there, however having already known Flutter, Flame was quite nice to work with. I ran into several issues with running this on the web and ultimately decided not to support web for this initial launch and instead focus only on Android and iOS. Accomplishments that I'm proud of I'm proud to have completed and deployed full featured apps for iOS and Android. What I'm most happy about is that the app is localized in Japanese, which is something I've never done before. What I learned The most surprising thing I learned was how the recycling process works. I suppose I never gave it much thought and always assumed that plastic placed in the recycling bin would actually be reused. Turns out it isn't that simple and to successfully reuse plastic the process is much more complex. Additionally, I learned many new programming related skills. Some of the things I've learned here I'll definitely take with me to other projects regardless if they are games or other apps. The main skills I gained from building this app are: Working With Flame To Build Games Using Flame Audio Localization Google Wallet Integration What's next for Last Bottle I think the game has a lot of potential, right now there are essentially 5 levels. Although to the user levels aren't selected, each time they recycle the games difficulty increases. One improvement would be adding additional obstacles and making it even more challenging. I'd also like to add the ability to collect more bottles along the way which will give the user more spins. Similar to this I think making the spinner update the odds based on other mini games could be a nice addition. For example if the user answers a trivia question correctly about recycling they get better odds on the spinner. One other major idea is to move through the process of reuse and play as different types of single use plastic. For example once the water bottle is reused then it becomes a plastic straw. Then the player plays as the plastic straw and encounters some specific challenges that plastic straws face. The process can continue with other types of single use plastic. With all of this additional trading cards would be collected, which would include other facts about the plastic waste and recycling problem. <div