---
slug: "stylesnatch"
url: "https://devpost.com/software/stylesnatch"
title: "StyleSnatch"
hackathon: "Adobe Express Add-ons Hackathon"
organization: "Adobe"
winner: true
words: 805
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# StyleSnatch

> Any design on a canvas

[Devpost](https://devpost.com/software/stylesnatch) · hackathon [[Adobe Express Add-ons Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[small_business]]
**substrate** [[geospatial]] [[video_visual]]

**stack** python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stylesnatch

## Body

What the sidebar could look like Upload your design (even with handwritten modifications!) Get the design directly in Adobe Express and modify as you like Here is what it's doing in the background: identify shapes, their colours and font (ugly but works!) Inspiration My family has a consignment store. It's a small business, I wouldn't even say we have a "brand". So when it comes to design, we need something quick and simple . Working with heavy software like Illustrator is a bit of an overkill, while templates in beginner friendly design tools are hard to choose. AI has been of great help, but modifying small details via prompts is basically impossible. I wanted to create the best of both worlds : quickly generate a design from a photo like ChatGPT, all while being able to modify element by element like a handmade design. What it does StyleSnatch is an add-on for Adobe Express that lets users: Upload a photo of a design they like (poster, flyer, sketch, etc.) Automatically extract the layout , including text boxes and shapes Detect the original font using Adobe font recognition API Recreate the design in an editable Express canvas, with modifiable elements and structure It gives users a real-world shortcut : go from inspiration to customisation without needing to describe the design in prompts or start from scratch. Stylesnatch is not designed to reproduce or resell copyrighted works, but rather to provide users with editable structure and inspiration based on their own input. It’s a tool, not a one-click copier: users upload what they want and control the output. These reproductions aren’t going to be pixel perfect copies but starting points for beginner designers. The goal is to enable transformative use: remixing, learning, and adapting designs into something new and personal like moodboards or templates. How we built it To quickly validate the concept for the hackathon, I built a lightweight prototype using: OpenCV (for shape and text block detection) WhatFontIs API (for quick font identification) (These tools were chosen for speed and simplicity. They worked well for a quick test, but I’m not tied to them. Future versions could use custom models or Adobe's internal APIs for tighter integration and better compatibility.) The mockup generates JS code you can copy-paste into Adobe Express Playground to generate the design, as well as a JSON file and an image for debugging. The final version of the mockup will have the following workflow: User uploads an image into the add-on sidebar The image gets sent to a server where object, font and layout detection take place The output is a code that is interpreted by Adobe Express to place the design elements on the canvas The user then modifies the design as they wish Challenges we ran into "Translating" identified coordinates into coordinates on the canvas. The mockup doesn't quite get it right. I used geometry and font experimental APIs detailed in Adobe Express documentation, but it wasn't always super obvious how to use them. If we work together on this project, we would definitely overcome these challenges! 💪 Accomplishments that we're proud of This was a super cool domain to explore! My daily job is mostly data visualisation, so this isn't really my area of expertise. But I'm glad I took on this challenge and I can't wait to see what's next! What we learned Oof, lots of things! I tried out a bunch of different libraries while making the mockup and saw how tricky identifying shapes can be. There's still a long way to go, but the task is definitely doable with a bit more guidance from senior devs. 🙏 What's next for StyleSnatch Connect the identification tool I made with the actual add-on, instead of copy-pasting like I did for the mockup Integrate not just basic shape identification , but other things too In my demo video I mentioned the use case for legacy designs . For the longest time our store's logo was just this old print out on a piece of paper. We went to a graphic designer to scan it properly and then get a vectorised version. My dream would be to be able to scan and vectorise on the go . And this is definitely doable! Shipping plan: I can create the first version in about a week, film my progress every day and post it on TikTok and YouTube. This will encourage others to build their own add-ons and use Adobe Express. At the same time, I will be testing it out irl at my store and other small business owners in my network. I really want to work on this and I can test this out irl, this hackathon inspired me a lot! I have lots of ideas of where to take this further, so honestly, just say when 😁 <div