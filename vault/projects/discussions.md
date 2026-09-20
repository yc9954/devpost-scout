---
slug: "discussions"
url: "https://devpost.com/software/discussions"
title: "Discussions"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 637
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Discussions

> Discussions is a board view & a dashboard widget where members of the board/dashboard can chat, discuss and ideate freely among themselves about anything.

[Devpost](https://devpost.com/software/discussions) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[realtime_stream]]

**stack** express.js, heroku, netlify, tailwindcss, twilio, vuejs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for discussions

## Body

New empty Discussions View Add Discussions app from board's Views Center Tag or mention any member while typing your message Add any emoji you want in your message You can react to any message using emojis You can reply to any message in its separate thread When you mention a member in your message, they are notified If any of your teammate is typing in the same board, know it in real-time Add Discussions Widget in a dashboard and see messages sent in small view See full discussions in the full screen view of the Discussions widget Inspiration I have always loved solving problems, especially problems related to productivity. Before starting on this hackathon, I looked at the "Inspiration" board on Devpost and other external review sites like G2, Capterra, etc. to see the major problems that the users of Monday are facing. And I noticed that the chat feature in the board view is something a lot of people wanted. I realized this feature could have a significant positive impact on the productivity of 100% of the organizations on day 1. Hence, I went ahead with this problem. What it does Discussions app is a board view and a dashboard widget where members of the board/dashboard can chat, discuss & ideate about anything. Members of the board/dashboard can do the following: Send messages on the board/dashboard. Tag or mention any user in their message. Add any emojis while typing their message. React to the messages using emojis. Reply to the messages in a separate thread. React to thread messages using emojis. Notifications go out to the users who have got tagged in the messages. See “3 members are tying…” message in real-time if any of the members are typing in the same board view or dashboard widget at the same time. How I built it Vue.js is used to build the frontend. Express is used to build the backend, and Twilio Chat is used to create the flow of the discussion. Tailwind.css is used for the app's design, and I have extended and added a few relevant classes to match Monday's design system. Netlify is hosting the frontend and Heroku is hosting the backend. Challenges I ran into The significant challenge I ran into was while setting up the base with Twilio Chat. It took a lot of time to make sure all the APIs and data stored in done securely so that the app becomes scalable to multiple organizations. Another minor challenge that I ran into was that there were a few components for which the design system had no reference. I added the closest possible design based on the design system and the current Monday's product design. Accomplishments that I'm proud of I'm pleased that the design of the app looks very close to Monday.com, which will make it easier for users to adapt. And I'm proud of the impact that this app will have on Monday's users in the coming weeks/months, once the Discussions app is live on the marketplace. What I learned I learned about the OAuth flows, in general. Another great thing I got to know via this hackathon is the Monday product and the immense possibilities that it could have on its users by converting it into a platform. I’m really excited about that and looking forward to being a part of the marketplace ecosystem. What's next for Discussions The next steps are to make the app feature complete, stress test the app for scale, and apply for marketplace release. Pending features - Allow users to tag board items while typing a message. Add unread message flow, so that users can see whatever they have missed out. Allow users to go back and read ancient messages. Then, stress test the app at scale. Apply to release on the marketplace. <div