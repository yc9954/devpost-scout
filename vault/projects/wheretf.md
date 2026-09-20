---
slug: "wheretf"
url: "https://devpost.com/software/wheretf"
title: "WhereTF"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 1259
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/structured_db"
---

# WhereTF

> The first AI-powered home inventory app built for busy households. Stop asking “Where TF is it?”—start finding your stuff fast, without the “did you even look?” argument.

[Devpost](https://devpost.com/software/wheretf) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**user** [[developer]] [[legal_professional]]
**substrate** [[structured_db]]

**stack** bolt.new, elevenlabs, entri, ionos, openai, stripe, supabase

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what we learned
- what's next for wheretf
- challenges i’m entering
- bonus prizes i'm targeting

## Body

WhereTF's landing page has an interactive component - move the letters (get searching!) to find the sign up button Easily sign up for WhereTF via email. Use WhereTF to search for items. Exact matches immediately appear with location as a dropdown. Hit search to see all matching items! WhereTF congratulates users when they find an item. If there are no matching items, users can see AI powered suggestions based on the locations of similar items, rules, etc. Easily add items in bulk by containers - you can even describe the contents of a container via voice mode. Inputs are cleaned and logged. Panic mode is a fun way to help people search. A voice will provide obvious tips alongside an alarm for a 30 second countdown. Activate premium through a Stripe integration to access the AI searches. Use code FRIENDSFREE to try! Manage your household to add members and generate a view-only link to your inventory that guests can search. Inspiration I wanted to build something widely relatable, and nothing felt more universally shared (and frustrating) than the daily hunt for household items. My inspiration came from home: my husband has what I lovingly call "man eyes"... he’s constantly asking me where things are without actually looking. I, like many women, seem to have a mental inventory of everything in the house. It’s a dynamic that plays out in homes everywhere, and it gets even worse with more people in the house. What started as a goofy idea turned into a genuinely useful tool: WhereTF helps you inventory your whole house in minutes. You can even share read-only links with guests like Airbnb visitors or house sitters. What it does WhereTF helps you log and locate your household items quickly, collaboratively, and with a bit of humour. Check out the project media in my submission, or my video, for a peek at what WhereTF looks like in action. Add items by voice or text - AI processes voice input to store items individually in a searchable database, tagged to containers and rooms AI-powered location suggestions - e.g., "Your hiking stuff is usually in the basement, try looking in the green duffel bag." Add everyone in your household so you're never the only one searching Panic Mode for those high-stakes moments (yes, it yells tips at you) I wanted to ensure that WhereTF is lightweight and fast to add items - otherwise no one will use it! How I built it WhereTF was built over the course of a month, as a team of one, entirely in my spare time while working full-time (and I got married in June!). Bolt made it possible to launch a real product - without writing a single line of code. While I work in tech, I don't know how to code, so this was a great challenge for me! I used: Bolt.new as the core platform to build and connect everything together Supabase for backend and authentication (Bolt handled the integration) ElevenLabs for voice AI, making the app conversational Netlify for deployment Stripe for payment integration (this one took the longest!) Entri + IONOS for securing my custom domain: www.where-tf.com Challenges I ran into The biggest challenge? Integrating Stripe. What seemed like a simple task turned into days of troubleshooting, debugging, and forums - I was close to quitting. Integrating the Stripe sandbox went so swimmingly, I posted a video about how easy it was! When it came time to upgrade to live Stripe, I nearly cried, it went so terribly wrong. I used so many tokens setting up the subscription functionality, I really didn't want to remove it. Over many frustrated days, I figured it out (and started to feel like a real software engineer). Also, in a twist of irony, my demo of Panic Mode (the funniest feature in the app) didn’t work due to screen share issues when I was invited onto the Bolt Builder Feature Livestream. But hey, it’s all part of the fun! Accomplishments that I'm proud of I built this entire product as a team of one with zero development experience . I had never set up a database before, couldn’t code, and honestly thought Supabase was a rap. I was able to ship this entire product without phoning a software engineer friend for help (I'm so proud of this!!) I was invited to be featured on Bolt’s live project stream Integrated Stripe, Supabase, voice AI, and full deployment workflows Secured a custom domain and shipped on time Generated over 60,000 views across platforms sharing the build-in-public journey Got reposted and encouraged by Bolt leadership and judges Received real-world feedback from users who immediately wanted to use it or share it with their families What we learned Building in public is powerful. Sharing your journey brings encouragement, accountability, and incredible feedback. No-code tools are more powerful than ever- but integrating systems like Stripe is honestly still really tough What's next for WhereTF Packaging this into a mobile app and launching on iOS and Android app stores Improving AI-powered search and optimizing AI components to reduce infrastructure costs Enhancing onboarding, reminders, and collaborative controls to serve larger households Challenges I’m entering Custom Domain Challenge - www.where-tf.com was secured via Entri & IONOS. The name itself is the solution: when someone shouts, “Where TF is it?”, now there’s an app for that. It works equally well as “Where To Find” or “Where The F***,” depending on whether you're showing your grandma ;). Voice AI Challenge - I used ElevenLabs to solve the single biggest problem with inventory apps: no one wants to add thousands of items one by one. With voice mode, users just describe what’s in a cabinet, and ElevenLabs + AI handles the rest... breaking it into individual items, tagged to containers and rooms. I also used ElevenLabs' API for Panic Mode , where a sarcastic voice yells unhelpful tips like, “Have you even TRIED opening your eyes?”, a crowd favourite on socials. Deploy Challenge - Deployed the full-stack Bolt app on Netlify with ease. Startup Challenge - Integrated Supabase for backend and Stripe for monetization - proving that no-code can power serious apps. Bonus Prizes I'm Targeting Uniquely Useful Tool - WhereTF solves a real-world, everyday problem that everyone can relate to. It’s simple, fast, and actually fun other inventory apps aren’t. Sharpest Problem Fit WhereTF is designed specifically to help households stop losing stuff and asking each other questions about where things are. It's a problem that I think affects every single household around the world. Most Viral Project - From my videos, I was able to accumulate over 60,000+ views across TikTok, Instagram, X, and YouTube. I was lucky to receive tons of shares, encouragement from the Bolt team, and a snowball of support from friends, family, followers, and so many internet strangers that started following my journey. Top Build-in-Public Journey - I documented every step, from thinking about quitting, to debugging Stripe, to finally launching. I was even invited to speak on Bolt’s featured project stream. The response online was incredible. 60,000+ views! We Didn’t Know We Needed This - The most common comment I got: “My partner and I NEED this, we’ve been talking about how someone needs to build this forever. I’m sharing it with them immediately.” What started as a joke became a product people now say they can’t live without. Thanks for your time reading my submission! If you’ve ever lost something at home and thought, "There has to be a better way…" now there is. It’s called WhereTF. <div