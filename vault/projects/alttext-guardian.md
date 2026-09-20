---
slug: "alttext-guardian"
url: "https://devpost.com/software/alttext-guardian"
title: "AltText Guardian"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 1279
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AltText Guardian

> AltText Guardian detects image submissions lacking post description, generates auto-reply alt-text for the OP using a vision model.

[Devpost](https://devpost.com/software/alttext-guardian) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[video_visual]] [[web_dom]]

**stack** devvit, google-gemini, typescript

## How they structured the write-up

- try out alttext-guardian in your own community!
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for alttext guardian

## Body

Image shows AltText-Guardian, Generated Image description in AutoReply message Image shows AltText-Guardian, Generated Image description in AutoReply message Image shows AltText-Guardian, Generated Image description in AutoReply message Try out AltText-Guardian in your own community! Inspiration I lost my vision to a stroke a few years ago, and had to adjust from being an avid competitive gamer, Redditor, marathon runner, computer user… to coming back online to an inaccessible internet. Unfortunately, there's few options for the blind and visually impaired online. Especially in long-form forums or gallery-like communities like Reddit. There's Lemmy, which is a Reddit-alternative, but there's still tons of issues with it (see: Lemmy is not a good Reddit alternative yet ), and frankly… why should the blind need to move off main-Reddit? That's why I want to invest time and energy into this mod-tool. If I can make accessibility an easy ping for an average user, they might just be willing to click an extra button before posting. What it does Image-heavy subs (r/aww, r/Art, r/photography, r/OldSchoolCool) are effectively unusable for screen-reader users because almost no posts have descriptions. AltText Guardian detects image submissions lacking post description, generates auto-reply alt-text for the OP using a vision model. Mods get an automatically generated alt-text description in their auto-reply mod bot using a computer-vision text renderer. They never have to think about if they're doing accessibility "right"! How we built it With a lot of love, a little bit of stress, and a lotttttt of patience. TypeScript end-to-end, with open source preferred wherever it fit (MIT-licensed; full source on GitHub). Built on Devvit. AltText Guardian hooks into Reddit's PostSubmit and PostUpdate triggers, runs a scheduled job after a configurable grace period (default: 2 minutes), and posts a nudge comment if the OP hasn't added a description. Grace period, minimum description length, and optional "Needs Description" flair are all configurable per-subreddit. Image detection. A dedicated module identifies image and gallery posts across i.redd.it, imgur, Reddit native galleries, and arbitrary URLs with image extensions; including the ones with query strings that break checks, e.g.: .endsWith() . Idempotent state machine. The trickiest part was ensuring the scheduler and PostUpdate trigger don't fight each other when an OP edits the post mid-grace-period. The scheduler holds a TTL lock in Redis; PostUpdate uses NX-claims to atomically reserve work. Retries and concurrent edits can't produce double-nudges. Vision model on Reddit's allowlist: Google Gemini 2.5 Flash-Lite. Image bytes are fetched by the app, base64-encoded, and sent to Gemini via inline_data for direct multimodal analysis. The draft output is run through a sanitizer that strips Markdown links, image embeds, and mentions before being appended to the nudge comment; important because the comment posts under a bot account, and the description shouldn't become an injection vector. The app owner sets a free Google AI Studio API key once via devvit settings set geminiApiKey ; it's an app-scoped secret, so a single key works across all installations. Tested with Vitest + fast-check ; property-based tests cover the scheduler's decision logic and the comment sanitizer, which is exactly where edge cases hide. This means: No paid API required; but paid API helps with large user volume if/when necessary Challenges we ran into Reddit doesn't natively support alt text on images and there aren't any searchable mod tools that address problem. That's the root problem, a known accessibility gap in the community for years ( example thread ), and it's what makes a moderator-side workaround necessary in the first place. My hope is that it makes accessibility seamless/easy for mods who want to be inclusive but just aren't sure how. Finding a vision model I could actually use was a pain. I started with Qwen2.5-VL-7B-Instruct through Hugging Face Inference Providers, but it had been sunset and not on Reddit's allowlist and several of the older Gemini models I tried had been sunsetted by Google. I worked through implementing Llama 4 and a few other options before discovering Devvit's HTTP Fetch Policy (thanks to @fsv in the Reddit Dev Discord server) Reddit restricts outbound network calls to an allowlist of approved domains. Reddit only has a handful of computer-vision-capable models on the dev allowlist. So I switched to Google Gemini. Not my preferred tool because I <3 and prefer Open Source, but it's already on Reddit's dev allowlist and it works well! Gemini had its own problems. The newer, more capable Gemini models are gated behind paid API tiers, which made free-tier deployment harder. Older models I'd targeted got deprecated mid-development (Gemini 2.0 Flash was retired in w/in the past month or so). And the free tier itself was hit by quota cuts. Ran into limit: 0 /429 error, which sounds like a normal throttle but actually means the model/account combination has zero free-tier quota allocated, so... rip. Updated to Gemini 2.5 Flash-Lite, which has decent free-tier quotas. The broader picture is that accessibility on Reddit remains a problem ( another community thread ). AltText Guardian patches one piece of it from the mod-tool side, but still only enables accessibility if someone happens to be a mod, and happens to care about accessibility. So, ideally I'd love to talk with some Reddit devs to integrate a more platform-specific version of this tool somehow. Helps users like me, and helps Reddit be a superhero. Accomplishments that we're proud of Helping to create a solution to questions and posts like these: Is there a way to add alt text to an image added to a post? — r/accessibility How do I put in a request for alt text in images? — r/reddithelp How to write effective alt text for my posts — r/accessibility How to add alt text to Reddit post — r/Blind And also, getting responses like this from the Reddit Dev Discord Ticket section really reassure me that I'm on the right track to building an actually hopefully, helpful tool: "I'm speechless , I wish more people would have tried solving actual problem people face rather than generating a solution for a problem which doesn't exist. What a great app :blobcatlove:"; "Amazing!" What we learned The world of technology and a more image-based world has grown denser and more prolific in recent years. Yet, people with disabilities/vision conditions like me, can't move at the same pace, we don't "see" the world the same way. So, I learned just how many people on Reddit could benefit from this, found so many people's posts asking when will it be a tool, why it isn't already, and struggling with screen readers not able to relay the post images they're coming across (or, having subpar computer vision tools that generate garbled trash, and just annoy the users). Getting the tools to work and integrate seemingly “seamlessly” is certainly not an easy process, especially being legally blind myself, but my motto is “build it and they will come”. There’s tons of active communities for blind/low vision users (e.g. Games for Blind Gamers, a Dev server ), but they just need a richer platform and UX. We've lost a world of context, so we need to make Reddit more equitable and accessible experience. Happy to be part of that, no matter the hurdles and troubleshooting! What's next for AltText Guardian Increase quality and threshold requests with a paid API tier for computer vision analysis. Ideally, it would be wonderful to use open-sourced models, instead of relying on Google Gemini. Other than that, I'd like to increase the API usage limits if the tool becomes popular, and I'd like to user richer models for better descriptions, and figure out ways to enhance the user experience for disabled users so that the Reddit/Lemmy disparity isn't such a big deal. <div