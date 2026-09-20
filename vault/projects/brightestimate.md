---
slug: "brightestimate"
url: "https://devpost.com/software/brightestimate"
title: "BrightEstimate"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 745
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/climate_energy"
  - "user/small_business"
  - "substrate/video_visual"
---

# BrightEstimate

> Elevate everyday proposals to professional grade with our universal tool, empowering contractors and small businesses to thrive globally using cutting-edge AI.

[Devpost](https://devpost.com/software/brightestimate) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[climate_energy]]
**user** [[small_business]]
**substrate** [[video_visual]]

**stack** amazon-web-services, bedrock, llms

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for brightestimate

## Body

Example of one quotation created Inspiration From what we've seen in our own work, it's tough for independent contractors and small business owners to whip up proposals or quotes. Getting a pro to do it costs a pretty penny, and setting up a CRM system isn't exactly a walk in the park (you need a whole IT squad and management backup). And this issue isn't just for the folks in developed countries; it's even tougher for small-scale contractors in the developing world who just don't have the means to put together solid proposals, and quotes, or even explain their process clearly. That's why we wanted to make life a bit easier by using Large Language Models to help out with creating proposals, emails, and other important business docs. We started with solar energy contractors because this way, we're not just making things easier; we're also pushing for cleaner energy and more jobs in a sector that's only going to get bigger. We picked PartyRock for this because it's quick for making prototypes, gives us the latest LLMs to play with, and works on mobile browsers too. Being able to access this tool on the go was a big deal for us. What it does This tool lets any contractor, small business owner, sales guy, or whoever, create a proposal for new business, an email template to send it off to the customer, and an image that sketches out the solution. For solar installers, this means taking the info from a technical survey, the details about the install site, and what tech gear they'll need, and turning it into a proposal, an email, and a visual sneak peek of the setup. You can check it out at BrightEstimate . How we built it We went with PartyRock because it's great for quick prototypes and lets us use the latest in generative AI. Claude was our go-to for responses because it beat out Llama and was quicker than the Jurassic models. For making images, Stable Diffusion XL gave us the best results in a good amount of time. We also spent a lot of time making the UI as easy to use as possible, with clear spots for users to put in details about their site visits, what equipment they'll use, and info about their company. Challenges we ran into The biggest headache was PartyRock's UI, which didn't let us add buttons, dropdowns, or other stuff to control when the LLMs would kick in. So, every little change meant a new response and another call to the APIs, which wasn't exactly efficient. Plus, we couldn't pull in outside data to make the results better or export what we got out of it. Our main struggle was making the labels and text boxes user-friendly. Accomplishments that we're proud of One of the things we're most proud of is how we managed to create something that's genuinely useful for a group of people who are often overlooked when it comes to tech solutions. By focusing on solar energy contractors, we're not just helping them streamline their proposal process; we're also contributing to a bigger cause, clean energy. Seeing our tool being used in the field and getting positive feedback from users who've never had access to something like this before has been incredibly rewarding. What we learned Using PartyRock showed us that you can really do a lot with the latest Large Language Models for prototyping and trying out new ideas. It's also clear that we can scale up what we're doing with AWS tools like Sagemaker and Amazon Bedrock. There's a huge potential for using Generative AI to tackle all sorts of problems, and it's more accessible now than ever, opening up tons of new opportunities. Moreover, we learned the importance of user-friendly design and the need for tech solutions to be accessible and practical for their intended users, not just advanced in terms of technology. What's next for BrightEstimate Here's what we're thinking of doing next: Make it usable for different kinds of contractors across other sectors. Bring in Retrieval Augmented Generation (RAG) to get even more accurate results and pull in private company info. Try out other foundational models so we can offer this in more languages. Pair it up with no-code tools and frameworks to create native mobile apps. Furthermore, we're exploring partnerships with educational institutions and industry associations to ensure that our solution meets the evolving needs of contractors and small business owners. <div