---
slug: "listenly-text-to-speech-for-confluence"
url: "https://devpost.com/software/listenly-text-to-speech-for-confluence"
title: "Listenly | Text-to-speech for Confluence"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1287
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Listenly | Text-to-speech for Confluence

> Make your Confluence speak!

[Devpost](https://devpost.com/software/listenly-text-to-speech-for-confluence) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[mental_health]] [[transportation]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** amazon-polly, amazon-web-services, atlaskit, forge, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for listenly

## Body

Clicking on the Listen button in the page header will open a player window where you can play, pause and rewind the audio. Click the Flag button to choose a language that corresponds to the text. Adjust the speed by clicking the Playback speed button. Listenly is a text-to-speech app for Confluence built on the Forge platform that allows you to listen to your Confluence pages voiced by a computer-generated voice powered by Amazon Polly . Inspiration Is it me getting older or is the world changing too fast? Probably both, but I think it is hard to argue that life has changed greatly in the last few years, especially since the pandemic started. There's hardly anything in our lives that hasn't been affected, but one of the most noticeable changes is the way we work now. We had to adapt to the new schedule working from home and got used to wearing a white-collar top with pajamas bottoms (well, that’s not too bad 😊). There are no traffic jams, but it's got even easier to get late to work when it is three feet away from your pillow. We also consume information differently now. For example, there's been dozens of researches and surveys lately that show a vast increase in the audio consumption since the pandemic. It feels like listening has become a new way to read, which seems to fit perfectly into the sped-up, productivity-focused, multitasking world of now. And while the popular text-first media have successfully adapted (or were the ones who were setting the trend), the tools that we use for work (and spend most of our time at) have been lagging a bit. If we stick to this article above, it also points out that "only 10% of people listen to audio content related to their job". Of course, they talked about podcasts, but the idea had already clicked with our team at that moment: "Can't our work be more like a podcast?". We ourselves use Confluence in our day-to-day work and we wanted to build something that would allow people (and us, of course) to interact with the same ol' in a new way, so we decided to teach Confluence to speak. In our opinion, having text-to-speech functionality in such a powerful and versatile tool doesn't look like a gimmick, but rather a must-have in 2022, allowing you to choose the way of working with information that suits you best. What it does In a nutshell, Listenly is an app that converts the text on your Confluence pages to speech. After you’ve installed the app, clicking on the Listen button in the page header will open a player window where you can play, pause and rewind the audio generated from the text on the page. Click the Flag button to choose a language that corresponds to the text. You can also adjust the speed by clicking the Playback speed button. Though simple in the concept, it gives quite a lot: Make Confluence more accessible While Listenly can't fully replace a screen-reader, it can certainly make Confluence more accessible to visually impaired or dyslexic users. For me myself wearing glasses, it's such a relief when I get a chance to make my eyes rest without sacrificing my productivity. Get knowledge your own way About 30% of the general population are considered verbal learners, who have a better ability to learn through the words they hear. Having different ways of interaction with the knowledge base available, you can actually choose the way that is more efficient for you. Multitask Reading requires your full attention on the process, which is by no means a bad thing, but listening allows you to consume information while jogging or doing yoga, brushing your teeth ten minutes before an early Zoom call, or even during this very call (if it is one of those that could have been an email 😁). Proofread Listening to what you wrote is a great way of proofreading as it makes you look (with your ears) at your text from a different perspective, particularly when your eyes are blurred after working on it for a while. Moreover, you can do it faster yourself and make it less burdensome for your colleagues. Make it more engaging for your readers Listenly offers an additional way to keep your readers' attention. “ Trinity Audio’s research that focused on AI-narrated audio articles revealed that almost half of the total listeners listened through the entire content as the completion rate clocked at an impressive 48.87%.” And according to our personal research, it can also reduce the number of "TL;DR" in the comments 😂 Don't forget to have fun Striving for extreme productivity all the time can lead to a mental exhaustion and burnout. Please, don't be hard on yourself and don't forget that you can make even boring paperwork sound more fun. How we built it Custom UI and React are used to create Listenly's aesthetically pleasing, yet functional user interface. Combined with the Atlaskit , we were able to give it a truly native look and feel. Our solution for streaming audio is to use browsers' native functionality, which enables us to decrease the time "from click to sound" while also granting better security. We use the mighty Amazon Polly to integrate speech synthesis in our app. In short, we get the textual information from Confluence via the REST API and requestConfluence in particular to be then passed to and processed by Polly. Credentials for Amazon are securely stored in Forge's environment variables . As soon as it has recognized the text and an audio file has been generated, it sends the audio file to the frontend for playback. Data for the user interfaces are pulled from the backend using Forge's Resolver and invoke Bridge APIs combined to call backend functions from the frontend. The player state and the language used are saved using the Storage API . Challenges we ran into Unfortunately, we weren’t able to use the Forge UI as we couldn’t find the necessary components to build the player UI. Since AWS SDK does not work in Forge due to existing technical limitations , so we had to implement the functionality and sign the requests using the AWS4-HMAC-SHA256 algorithm manually. Let multiple people have ownership of a Forge app. This makes it easier for teams to build and manage their apps. At the moment, it’s not possible for a team to have ownership of a Forge app as the app ID is linked to the Atlassian account and is unique for each developer, which makes it difficult to work together with one codebase. Neither background playback nor any other background process on the Confluence page is possible as for now. There is no way to recognize that the iframe was closed in order to save the player state, so we had to save the state every 3 seconds. Accomplishments that we're proud of We are proud that we built the app, obviously 🥂 What we learned With more insight into the platform, we can say without a doubt that it has grown quite a bit. Our team held a hackathon a few months after Forge was released to challenge ourselves and learn more about it by actually working with it, and I have to say that it has really evolved since then. What's next for Listenly The following are a few items from our current backlog we'd like to work on: Highlighting the text that is currently being voiced Capability to select part of the text to be voiced Playing from any place in the text Add preliminary markup of the page to voice only selected parts of the page Improve tables reading <div