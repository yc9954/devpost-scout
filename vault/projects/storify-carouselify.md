---
slug: "storify-carouselify"
url: "https://devpost.com/software/storify-carouselify"
title: "Storify & Carouselify"
hackathon: "Coda's AI at Work Challenge"
organization: "Coda"
winner: true
words: 637
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Storify & Carouselify

> Quickly turn your blog articles into IG Stories and Carousels with the help of Coda AI

[Devpost](https://devpost.com/software/storify-carouselify) · hackathon [[Coda-s AI at Work Challenge]]

## Facets

**substrate** [[video_visual]]

**stack** coda, coda-ai, edit-images-pack, gpt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for storify & carouselify

## Body

A fun and useful twist on the usual "Summarize the story for me" use of LLM AIs. Inspiration I have an Instagram profile @codatricks . And I don’t fill it. In fact, many agencies and professionals have social accounts and never post regularly. Not everyone can afford a social media marketing person to do this for them. And as for the makers themselves, often they just don’t have the time. One of the relatively easy ways to make some content for the socials is to take existing long-form articles (blog posts, press releases etc) and turn them into bite-sized carousel slides and stories: Not only these are fairly easy to make (because they can be templatized) — these sound exactly like a job for Coda AI to compose. And then to turn those key ideas into images, we can use my previous year's hackathon contender , the Edit Images Pack! (so meta!) 💡 Another possible use case for this is for personal studies and research. With S&C, you can turn news and long-reads into digestible story cards for your own reading — to consume content quickly and in a visual way. This is similar to how some news sites such as Google News sometimes format popular articles as Stories. What it does The doc generates bite-sized slides out of the stories you feed to it. It takes your long-form story (or you can generate one with Coda AI right in the doc) It extracts key ideas and summarizes them. You can adjust the desired number of slides and desired length of the pieces, and retouch them yourself. And finally, it turns them into downloadable images. You get to select the background, the fonts, the colors, and the layout. You can prepare yourself some assets and reuse the templates across projects for your brand look. How we built it The project is built with Coda, Coda AI, and the Edit Images Pack , my previous year's entry to the Packathon organized by Coda. As with all my projects, this one was built with my Coda Best Practices in mind, so it has the characteristic doc structure that I encourage everyone to use. The main interface is a single page workflow that takes you through all the steps, from adding a new story to reaching your Download button. Challenges we ran into The Coda AI doesn't always want to obey. It took a lot of tweaking to make it stop including the overall story title in each slide's titles (e.g. it would often do the "The Something Something: Remarkable Somethings" instead of just "Remarkable Somethings"). I'm not sure I fixed it entirely, so good thing there's a Refresh button 🙂 Another part where it disobeys is when I try to constraint it into just one slide or too few characters for an exported idea. The other challenge was that the Formula Editor didn't like working with my Edit Images pack for some reason. It would break formula formatting, cramp everything into a single line (a tangled and unmaintainable piece of code). I got my large formulas broken several times and had to rewrite them. (I reported this to Coda) Accomplishments that we're proud of I tried this doc on the Coda's own article about AI, and was able to carouselify it in about 30 seconds. Isn't that a feat? 🔥🔥🔥 What we learned Coda AI doesn't always listen. I could try polish the prompt to perfection, but since I was time-constrained (I'm submitting at least 4 totally different projects to this hackathon) I decided to just let it be and include the refresh button instead. It's still early days so I guess this is okay. What's next for Storify & Carouselify Subscribe to my Instagram 🙂 and you’ll see it used for most of my content very soon. <div