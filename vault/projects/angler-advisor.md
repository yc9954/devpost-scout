---
slug: "angler-advisor"
url: "https://devpost.com/software/angler-advisor"
title: "Angler Advisor"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 703
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Angler Advisor

> Angler Advisor is the PartyRock AI Assistant that prepares you for your next fishing trip. Whether a beginner or expert, Angler Advisor recommends the optimal reel, rod, bait and tackle to catch fish.

[Devpost](https://devpost.com/software/angler-advisor) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** amazon-web-services, claude, partyrock, stablediffusion

## How they structured the write-up

- inspiration
- what angler advisor does
- how i built angler advisor
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for angler advisor

## Body

Angler Advisor produces a plan for catching rockfish on the Chesapeake Bay. Inspiration My inspiration was how easily AWS PartyRock enabled me to mix together no-code recommendations for movies, wine-pairings and more. I saw nothing to represent the wider amateur fishing community, and thinking of my good friend in Maryland who loved to fish for rockfish, I envisioned a generative AI application powered by the Claude LLM foundation model that could produce ready-made "cheat" sheets suitable for fishing enthusiasts of all levels of experience. What Angler Advisor does There are many variables that go into planning a successful fishing outing. You tell Angler Advisor: Where you want to go fishing, What kind of fish you want to catch, and Your level of experience. Angler Advisor fine-tunes its advice to your personal level of fishing knowledge. It provides informative recommendations: Best bait for your target fish. Best gear to pack for a successful outing. Tips for recognizing your target fish when you catch it. It further offers a free-form chat window with the Claude LLM foundation model where you can ask questions if you need further information to make your fishing trip a success. There is also a Stable Diffusion XL-powered photorealistic rendering of what your target fish looks like to help you recognize it when you reel it in. How I built Angler Advisor It was pretty easy, the initial prompt of what type of fishing assistant application I wanted took me halfway there. Then I resized the windows and laid them out a little differently, since the text widgets for user input only need short (one-line) inputs. I added/altered the widgets for fish recognition tips and a photo (which should be as photorealistic as possible) to benefit beginners. I also added an input for experience level so that Claude could adjust its level of advice to the user's level of knowledge. Challenges I ran into There were a few challenges I had when working with AWS PartyRock: While easy for the No-Code developer to build something quick and easy, there was no good way to bring-in custom data and maps to enhance and supplement Angler Advisor. Claude did not always follow the prompt instructions, for example to not include a preamble summarization of the prompt text itself in situations where I would like only the output to be displayed. Prompt advice recommended by Anthropic in their documentation didn't always work. Stable Diffusion XL does not always generate realistic photos of fish, and also ignores instructions to not include a sometimes cartoonish background in its generated images. Flickr API calls or an image search engine would likely perform better. The layout UI for editing the application was sometimes difficult to use and would hide the editing sidebar on the right-hand side of my browser window. In particular, the Save button in the lower-right corner would frequently be cut-off, and I had to zoom out the window to 50% to be able to click it. To reduce hallucinations from Claude when users submit irregular input, like when users ask to fish for "Martian Scallops" on the "Moon" and their experience level is "Jelly Donut," I include instructions in the prompt to let Claude know it is okay to say that it doesn't know. Accomplishments that I'm proud of The "cheat" sheets Angler Advisor produces are perfect for printing to take with you on a boat or to keep close-by in your vehicle when you next go to the creek, river, lake or bay. It should help the beginning fishing hobbyist in particular, because navigating the diversity of bait and gear suitable for any particular fish or location can be overwhelming to newcomers. What I learned AWS PartyRock is good for throwing together a no-code generative AI application that can generate content for arbitrary prompts that don't require fine-tuning or augmentation with external data sources. What's next for Angler Advisor With greater integration of external APIs it should be straightforward to hook it up with relevant advertising, product recommendations that users can quickly purchase right from links within the AI-generated advice, and greater personalization to the needs of the particular user so that Angler Advisor becomes an indispensable part of their regular fishing ritual. <div