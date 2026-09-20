---
slug: "scrubbzly"
url: "https://devpost.com/software/scrubbzly"
title: "Scrubzzly"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 485
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
---

# Scrubzzly

> A fun puzzle game to order issues on your scrum board. Create a path using rotatable blocks to the issue with the higher priority.

[Devpost](https://devpost.com/software/scrubbzly) · hackathon [[Devs Unleashed]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** atlassian, flutter, forge, jira

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scrubbzly

## Body

Finished puzzle Start of the game Puzzle Game End of the game Issues to sort overview Inspiration The problem: You have your scrum board with a bunch of issues on it. You chose what to do for the next sprint but not in which order. Sorting them can be a tedious task. So what, if there was a more fun way to do it? What it does Scrubzzly is a simple puzzle game to sort all the issues on your scrum board. The goal is to create a path from the S block to either block A or B. A corresponds to one issue and B to another issue. Which issues these are can be seen at the top. Which end block you choose determines which issue is more important and should be put higher up in the order. You create the path outline by rotating individual blocks. Rotating is done with a left button click. The actual path is drawn by right clicking on the blocks. This creates a red line. Now you need to get that red line to either A or B. Every time a puzzle board is created two random paths are created that go from S to A and B. That guarantees that there is always a valid path to either block. Then these path blocks are created randomly and with a random orientation on top of that path. Blocks that are not a path can also contain path blocks or a solid block that doesn't allow a path. All this randomness contributes to the difficulty of the game because it is not always immediately obvious how to build the path. The puzzle is finished when you’ve drawn a red line all the way to block B and do a final right click on it. The game is finished once all issues have been sorted. Then you can see your total score plus the current high score. You can earn extra points by being fast. There a timer that ticks down. For every 10 seconds counted down you lose 10 extra points. If the timer ticks down to 0 you still get 10 points for completing the puzzle but no extra points. How we built it It's build using Atlassian Forge with a custom Flutter UI. Challenges we ran into Embedding Flutter as custom UI was not straight forward and required a lot of tweaking to get it working. Accomplishments that we're proud of All the paths in the game are randomly generated and are not too easy. What we learned A lot about Atlassian Forge and Flutter game development. What's next for Scrubbzly A multiplayer mode where the team can play together. Installation link The link to install the game inside your Jira site: https://developer.atlassian.com/console/install/dfe44326-1572-4733-87d4-ce2764d53769?signature=c7b3e2f5a9fe571e58532193fd5593388215b8a7414d1136eb4b4aad658ba4c2&product=jira Try out a demo You can try out a demo of just the game without needing to have a scrum board here: https://achim-rohn.de/scrubzzly <div