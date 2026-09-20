---
slug: "kendo-habits-sylh2u"
url: "https://devpost.com/software/kendo-habits-sylh2u"
title: "Kendo Habits"
hackathon: "The Worthy Web App Challenge"
organization: "Progress"
winner: true
words: 969
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/clinician"
  - "user/educator_student"
  - "user/government_staff"
---

# Kendo Habits

> A gamified habit builder. Get closer to your ideal self while having fun!

[Devpost](https://devpost.com/software/kendo-habits-sylh2u) · hackathon [[The Worthy Web App Challenge]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**user** [[clinician]] [[educator_student]] [[government_staff]]
  <sub>weak: document_pdf</sub>

**stack** firebase, kendoreact, react

## How they structured the write-up

- inspiration
- what it does
- how is kendo-habits contributing to a good cause?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kendo habits

## Body

Welcome to Kendo Habits - A Gamified Habit Builder! A fun and calm sign-in page, that also reminds you to love yourself! Add, Label, Describe, Modify and Complete your daily habits in the, well umm, "Your daily habits" page! And see your "Kendo XP" grow (right) A closer look at all the details you can use to describe a habit. Combined with a sleek slidebar to check off habits, no one can stop you! A visually appealing virtual garden - a direct reflection of how far you've come in your habit building journey! Your habit streaks (each row is a habit) from the most recent week, which can also be filtered by label type using the side panel. An example of filtering habits: here all "workout" habits are highlighted in black. Hover over a square to see the habit and date (right) Monitor (and export as pdf) your habit patterns, longest streaks & current streaks of each habit, in visually aesthetic KendoReact Charts! And finally, an aesthetically pleasing register page! Inspiration "You do not rise to the level of your goals, you fall to the level of your systems" "Every action you take is a vote for the type of person you wish to become". These quotes from my recent read, "Atomic Habits" by James Clear, really struck a chord with me. It gave me the vision to build a system that helps people Progress (no pun intended, well maybe) towards their ideal self. The vision to build an enjoyable system that celebrates even the smallest wins (a significant win, nonetheless). Kendo Habits was born. What it does "Kendo Habits" makes habit-building enjoyable, automated, and easy! It gives you both visual and auditory feedback for every habit you complete. Not only do you earn "Kendo XP" 💰 and level up, with all the progress you make, but you also get rewarded with pretty trees to customize your virtual garden with beautiful plants and trees. The beauty of your garden is a direct reflection of all the work you've put into yourself in real life. The more habits you complete, the better your garden starts to look, and before you know it, these new habits have become your new identity! Congratulations! What's more, you get to keep track of your habit streaks, and your true habit patterns with the beautiful UI components and charts from Kendo-React. All you have to do is focus on checking off that habit and we'll automate the rest! Gone are the days of misplacing books, or loose sheets of paper where you meticulously kept track of your habits. Kendo Habits to the rescue! How is Kendo-Habits contributing to a good cause? Change starts with the individual. The individual wants to succeed. The individual wants to make their mark on the world! And it all starts with a habit - perhaps even a trivial one. The thing about habits is that it has this snowball effect - you improve other areas of your life - you start becoming the person you want to be. Now that person could be an amazing teacher, doctor, or perhaps even the Chief Officer of an NGO, touching the lives of thousands of people positively. Kendo-Habits helps people achieve their true potential, and produce more of such people. The secret to success is not an infinite well of willpower - it is small consistent habits done for so long, that it becomes your identity. How we built it The entire app was built with React, powered by Kendo React components on the front-end, and Firebase in the backend for real-time updates of your habits. Challenges we ran into Incorporating real-time updates to work with firebase and react, when the user updates their habit description, habit labels, or habit completion was quite challenging for someone like me who didn't know anything about react until late April of this year. And getting habit completion data to reflect in the "habit streaks" page and the "habit charts" page was a handful, to say the least. The virtual garden in particular was very challenging. Giving the user a way to customize their garden in an intuitive, but fault-tolerant way seemed to be an insurmountable task. However, the intuitive nature of KendoReact's components allowed me to focus on the features of my project. I never felt like I was juggling two things at a time - for instance, I could focus on making the virtual garden work because of the out-of-the-box Navigation Panel that KendoReact provides. Accomplishments that we're proud of Real-time updates with firebase for almost everything you do in Kendo Habits, is something I'm really happy about. Working out math with dates in order to update the Kendo React charts was also a great learning opportunity. This process of handling math with dates was definitely alleviated by the "Date Math" functions that come with KendoReact. Getting the virtual garden to work was a truly rewarding experience. I definitely had to get my creative juices flowing to come up with the idea of using a mini-version of the garden to control any tree in the bigger, more visually appealing garden. And finally, I'm really happy with the end result of actually drawing the different trees and garden tiles (or assets) by myself in Inkscape. What we learned I learned that creating web apps can be much more enjoyable than usual when you have libraries like KendoReact that provide building blocks common to several apps - navigation, side-panels, app-bars, charts, and the like, to name a few. What's next for Kendo Habits Look forward to growing Kendo Habits into something much bigger, according to how people respond. I personally would love to add more types of "garden items" to the virtual garden, because I enjoy the process of creating visual assets in software like Inkscape. <div