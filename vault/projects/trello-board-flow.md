---
slug: "trello-board-flow"
url: "https://devpost.com/software/trello-board-flow"
title: "Card mirror (by Placker)"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 569
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "user/frontline_worker"
---

# Card mirror (by Placker)

> Automatically Link & Sync cards across Trello boards

[Devpost](https://devpost.com/software/trello-board-flow) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[transportation]]
**user** [[frontline_worker]]

**stack** javascript, placker, trello

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for board mirror (by placker)
- try it out

## Body

Create mirrors directly from your cards in Trello Quickly navigate between your mirrors inside of Trello Set rules to create mirrors automatically Use mirrors to distribute cards effectively across teams Create a personal master board to manage all cards that are assigned to you Simplify team meetings by raising relevant cards automatically Break down your work effectively by linking checklist items to cards. Inspiration At placker.com we help our users to bring focus in their work by making complex work simple. A key driver in complexity in work is that work needs to be split into smaller pieces then distributed amongst teams or grouped into bigger chunks. To manage distributed work effectively, you need to link and sync cards. This is where card mirrors come into play. What it does This power-up links and syncs cards across boards in Trello, either by making mirrors manually or making mirrors automatically, for example to mirror a card to my personal board when I'm assigned to the card, or to raise an impacted card to the stakeholders board by assigning the 'stakeholder' label to the card. Mirrors cannot only be created between cards, it is also possible to create mirrors from a checklist item on one board to a card on another board. Or to share cards across multiple boards. This way it is possible to create cascading work breakdown structures that helps teams to manage a portfolio in programs in projects, or a product backlog that consists of epics and user stories into tasks to sync the work between the product team and the development team. How I built it The power-up is based on the placker platform, for this power-up we added two features; 1. the ability to create mirrors by using mirror rules in Placker and 2. the ability to mirror multiple cards in one mirror group. Challenges I ran into Allowing multiple cards in a mirror group turned out to be tricky as it could happen that the update on one card triggered and update on another and a loop was introduced. Accomplishments that I'm proud of We have been testing these features already with a selected user group and the responses have been very great, this power-up contains a lot of the lessons we have learned over the years with regards to why and how people mirror cards, with more features to come very soon. What I learned We have learned a lot on the technical side related to managing async updates in groups and ensuring rules get executed correctly. On the functional side on why and how our users are using mirroring and what features are What's next for Board mirror (by Placker) We will release more triggers and actions for the rules, specifically the ability to automatically create item to card mirrors when a user is assigned to a checklist item. We will be moving the mirror overview and mirror actions to the card-back-are so they are more clear in Trello and some other UI/UX improvements based on feedback that we'll get from our user group. Try it out The power-up is not yet officially released, when you are already a placker user, please reach out to us in the chat https://placker.com so we can add you to our Mirror user group and help you get set. Until then, be sure to test our Projects by Placker Power-up in the power-up directory on Trello.com <div