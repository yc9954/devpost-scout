---
slug: "date-a-voice"
url: "https://devpost.com/software/date-a-voice"
title: "date.a.voice"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 1021
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# date.a.voice

> date.a.voice presents the first ever "voice assistant" dating simulator, now accessible on Amazon Alexa. Lockdown is the perfect time to practice your dating skills and try wooing a virtual partner!

[Devpost](https://devpost.com/software/date-a-voice) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**mechanism** [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]]

**stack** alexa, amazon-polly, conversations-api, node.js, ssml

## How they structured the write-up

- what's new!!
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for date.a.voice

## Body

date.a.voice splash date.a.voice logo What's New!! Over the past few weeks our team has been working hard on making Date.A.Voice even more interactive and engaging through adding new visuals, immersive background audio, and male dating options . On top of that, we've improved the flow of the dialogue to make the dates more smooth and conversational. To learn about the updates in more detail check out the recaps below. A quick video showcasing the new features: Visuals Date.A.Voice now has a unique avatar for each of your favourite dating companions, each with their own personality and design! Whether you're someone who enjoys rocking your favourite pair of jeans or a fancy top, we've got you covered with someone who matches your style. We've also included dynamic visual responses in addition to our custom audio responses. You'll be able to see your date's questions and responses in speech bubbles as well as a unique visual background depending on the setting of the date. Your date will also react to each of your responses so you'll be able to tell if your date is going well or if the love ship has sailed 🚢. Male Voices Date.A.Voice also now allows user to pick between male and female dating options with custom Amazon Polly voices for each character. We hope that this addition will allow for all users to find enjoyment from our skill. Immersive Audio Date.A.Voice now supports immersive background audio for each date! Whether that's the sound of waves crashing along the sandy beach 🏖or the clinking of utensils in a restaurant 🍷 we've added sounds to make the conversation feel even more real. Inspiration Amazon Alexa has always struggled with making real, meaningful conversations. However, the new Alexa Conversations API promises to deliver exactly that: smart, real conversations. Meanwhile, dating simulators have always been heavily text-based and are visual experiences. Naturally, my curiosity led me to consider the possibility: is it possible to design a voice-based virtual date experience with Alexa? This is the challenge we decided to take on. What it does Date.A.Voice allows you to go on a date with multiple possible voice assistants. The personality of each partner determines how they will react to your actions and words. Try to make your partner happy, and you will maybe find success! Love is just one invocation away! How we built it Overall, a lot of effort went into research and planning the architecture of the entire app so that when it's all put together in the Alexa Developer Console, it runs smoothly. We used Alexa's new Conversations API to build the main model of the skill to design real, fluid conversation. We used Amazon Polly and Speech Synthesis Markup Language (SSML) to simulate different voices. We also experimented with different tones for each voice in order to reflect the mood of your date partner during the conversation. If your answers to the questions fit the personality of your date you'll notice that their tone will reflect that. You'll also find that during the date you're able to change your answers to date questions. This was an important feature we wanted to include because a conversation should feel seamless and flexible. Alexa Conversations API was able to make that even easier with built in functionality to repeat previous questions. Challenges we ran into Because Conversations API is very new, there is a lack of developer experiences with the technology. This required us to really get creative and learn from existing Alexa skills, great documentation and tutorials, as well as other sources of inspiration to create this ground-breaking app. Even so, the Conversations API beta is incredible in the scope of its features and we were impressed by what it could do and what we could make out of it. We encountered some source control issues, but we were able to resolve it by communicating well and backing up our code on Github. Accomplishments that we're proud of We are incredibly proud of the fact that we were able to leverage the strengths of Alexa Conversations while still putting in all the features that make for a creative and interesting dating simulator game. We were able to utilize our unique and diverse strengths as a team by giving ownership of specific flows to each team member so they would feel committed to their role and could make for seamless experiences. For example, we would have a script lead to focus on making the lines for each character sound consistent and fluid, a database lead to handle the storage and retrieval of data, a technical lead to own the functions and handlers etc. The most crucial step was the synthesis of our ideas, which we did by having weekly meetings to bridge the different parts of the skill we were working on. We are proud that we were able to successfully combine our skills to create an incredible skill experience. What we learned We learned a lot about Amazon's APIs and developer tools for Alexa skills. Before, we had never thought of creating our own Alexa skill, let alone one as complex as this one, with 5 unique characters to interact with. We also learned about important elements of game design and script writing, as equal effort was spent architecting the solution as well as actually building the interaction model and writing the Node.js codebase. What's next for Date.A.Voice Next steps for Date.A.Voice include incorporating male voices to create for a more expressive and inclusive experience. This may involve tweaking some lines for the characters, but in general, we have written the characters to be gender-neutral. As well, due to our success, we feel capable of taking on more complex interactions that leverage further Alexa Conversations tools such as context carryover to make a more realistic conversation experience. We also want to incorporate rich audio soundscaping using the APL for audio beta feature to manage and mix audio files. By including the sound of waves crashing on the beach, or ambient sound at a restaurant we hope to create a more immersive experience that we can customize to each date’s experience. <div