---
slug: "story-stitch"
url: "https://devpost.com/software/story-stitch"
title: "Story Stitch"
hackathon: "Reddit Games and Puzzles Hackathon"
organization: "reddit"
winner: true
words: 703
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Story Stitch

> Story Stitch: Weaving Collaborative Crazy and Goofy Tales, One Sentence at a Time

[Devpost](https://devpost.com/software/story-stitch) · hackathon [[Reddit Games and Puzzles Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** devvit, devvit-realtime, reddis, redditapi, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for story stitch

## Body

Adding your goofy idea. Welcom Page After submission. can post the idea as comment as well. Project Story: Story Stitch Inspiration The inspiration behind Story Stitch came from my love of collaborative storytelling and Reddit’s strong community culture. I wanted to create a game that sparks creativity, fosters engagement, and brings people together to co-create shared narratives in a fun and interactive way. The freedom to go crazy with your stories and share those with people adds to the fun. I decided to use a block template instead of webview in order to explore and demonstrate the power of block-components provided by reddit What it does Story Stitch is a collaborative storytelling game where players build a story together, one sentence at a time. The game starts with a story prompt , and players can add a sentence (1–10 words) to continue the narrative. Each round provides three optional words as prompts. Players earn points by creatively incorporating these words into their sentences. Real-time updates ensure all participants see the evolving story instantly. The game tracks user contributions and allows players to share their additions as Reddit comments for further engagement. How I built it I used Reddit's Devvit Platform and the following features to build Story Stitch: Reddit API : To fetch subreddit data, handle user comments, and integrate the game seamlessly into Reddit posts. Redis : For persistent storage of the ongoing story and tracking user contributions. Realtime API : To broadcast story updates instantly to all participants, ensuring a dynamic and live experience. Block Templates : I designed a clean and accessible UI using components like <VStack> , <HStack> , and <image> to make the game visually appealing. Reddit AI : Assisted me in efficiently implementing and refining Devvit tools, saving time and effort during development. It helped a lot in searching for elements and also debugging the code. Challenges I ran into I had to go through the documents, and learn each and every feature, which was helpful but a bit cumbersome. Implementing real-time updates while maintaining smooth and consistent state management across all participants using Realtime was a bit difficult as I didn't find the documents as descriptive. Handling comment delays when posting using Reddit’s API and ensuring feedback is timely. Limited flexibility in block template UI customization required creative workarounds to deliver a clean and polished interface. Debugging Redis issues when persisting and reliably fetching story data for each post. It wasn't easy to make a proper pop-up modal with text formatting. Accomplishments that I'm proud of Successfully built a dynamic, real-time storytelling game that seamlessly integrates with Reddit's platform. I have used all the powerful features of Reddit's devvit, like, Realtime, Reddis, Doouble-Step forms, Reddit API, Block elements, and more. Implemented a unique scoring mechanism that rewards creativity and encourages players to incorporate prompt words. (though the scores are not stored yet, they are calculated for each user, this will be implemented in future scope.) Designed an accessible and visually appealing interface using Devvit’s Block UI components. Created a game that fosters collaboration and brings Reddit communities together in a fun and engaging way. What I learned Throughout this project, I learned how to fully leverage Reddit’s Devvit platform , especially its APIs, Redis storage, and real-time capabilities. I gained valuable experience with state management, asynchronous programming, and delivering a seamless user experience with block components. I was able to dive deep into Devvit, and I think I have learned most of the features offered by it. This gives me immense confidence to build more apps on devvit. What's next for Story Stitch Leaderboards : I plan to implement scoring leaderboards to highlight top contributors in the community. Custom Flair : Award users with special “Storyteller” flair based on their participation and creativity. Story Sharing : Add options to export completed stories, allowing communities to save and share their collaborative creations. Themed Prompts : Introduce themed rounds (e.g., fantasy, sci-fi, humor) to add variety and excitement to the game. Story Stitch is just the beginning of a collaborative journey. I’m excited to see how Reddit communities embrace it, and I look forward to building more features that make storytelling even more creative and engaging! 🚀✨ <div