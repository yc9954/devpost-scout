---
slug: "fizzbruzz"
url: "https://devpost.com/software/fizzbruzz"
title: "FizzBruzz"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 682
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/web_dom"
---

# FizzBruzz

> Community-sourced tech content for brain-rotted minds.

[Devpost](https://devpost.com/software/fizzbruzz) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[web_dom]]

**stack** codemirror, huggingface, mongodb, next.js, nextauth, prismjs, stackblitz, tailwind

## How they structured the write-up

- tracks to be considered for
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fizzbruzz

## Body

Tracks to be considered for best overall yay :3 (because why not) most likely meme startup (fizzbruzz will outdo all the other huzz) would blow up on tiktok (i'd like to think the costco guys would give us five big booms) lowkey actually kind of good (more like highkey but i digress) Most iq points lost (in the sense that you gain so many it's like an overflow) Most centered div (we literally have a guide about centering divs bruh) i’m just a chill guy sponsored by Build City (no dip) skibidi ai swag (there was definitely ai used to some extent) ciara cade best professional dev (after using our app, you should be the best dev there is) codedex i wanna learn stuff prize (if you don't learn something, at least you saw fat brian) wakaba prize (i'm running out of bits here okay bye) Inspiration I've always wanted tuah code. What it does Imagine Coursera, but better. Learn web development courses on Next.js easily, and be graded based on what you wrote. Easy dubs. From a selection of courses, you can follow guides for your little monkey brain. Leveraging on AI to grade your work. It's fun, I guess. For every course you take, you'll be guided in-depth through your current task (be that declaring text elements, centering divs, etc.) and be provided relevant code snippets for inspiration. Once you feel ready, you can use our in-browser code editor and Next.js project previewer to get real-time feedback on what you've wrote. From there, we'll evaluate your work and determine if you're ready to move on to the next steps in your engineering career. How we built it We used a variety of tools to make the process easy, but to start off, we used MongoDB, NextJS, and AuthJS. Our inspiration was Coursera, so using an easy UI library such as Radix UI made styling super simple! As for the more complicated part, we used StackBlitz WebContainers API to render the mini projects based off each guide. Each guide is written in Markdown that is rendered by PrismJs. For grading, we used HuggingFace. Challenges we ran into The StackBlitz WebContainers API, which is what we use to display a preview of the user's project in-browser has a lot of special requirements to make things work: It requires special headers to be configured. Figuring out how to set these headers with Next.js proved to be quite the challenge. Only one instance of a WebContainer can be booted at a time. This is a difficult thing to track where there's a lot of application state updates and several GET/POST requests being handled asynchronously. To resolve this, we ended up using a context which tracks if a WebContainer has been booted or not and preserves that instance if it was. By never having to to teardown the first booted instance this way, the load time of preview was significantly decreased after the first initial preview. Regex parsing for converting Markdown into HTML with PrismJs and marked sucked. +1000 aura to whoever can find the bug that causes the syntax highlighting not to work with TypeScript in the utils files. Integrating our AI model for code reviewing was tricky. And if you think about it, we technically created two projects: FizzBruzz and the calculator. I'll leave it to you to decide which one is the the more technically impressive one. The scope of this project was a massive undertaking. Accomplishments that we're proud of This is definitely a difficult project to undertake. We're glad we were able to create an MVP while still spending time with our families for the holidays (dawwww). What we learned The power of open-source UI libraries. Radix UI and Tailwind were critical for us to create a pleasing UI. What's next for FizzBruzz We only hope that the FizzBruzz Community keeps this platform alive forever more. One things we'd like to implement is any user to create courses after getting mod approval. This is a plausible feature but it would require users to copy and paste externally most likely. <div