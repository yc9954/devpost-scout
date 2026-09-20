---
slug: "duckstar"
url: "https://devpost.com/software/duckstar"
title: "DuckStar"
hackathon: "AWS Game Builder Challenge "
organization: "Amazon"
winner: true
words: 1191
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# DuckStar

> Dreaming of becoming a pop or rock star? Co-create incredible music with your AI PopStars & AI Music Producers, launch your own record label, release albums & compete in viral worthy lip-sync battles.

[Devpost](https://devpost.com/software/duckstar) · hackathon [[AWS Game Builder Challenge]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[disaster_emergency]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** amazon-web-services, amplify, bedrock, lambda, sagemaker

## How they structured the write-up

- inspiration
- what it does
- vicarious living through music
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what's next for duckstar
- potential

## Body

DuckStar Create your AI pop star to help you do challenges AI Music to help you produce good songs Music Maker Lip Sync Point system Lip sync against AI Avatar DuckStar Pitch Inspiration I come from a family of musicians: my dad was a lead guitarist who owned a music studio, my sister is a music teacher, and my brother has won numerous songwriting competitions. Yet, I am the "proverbial ugly duckling" when it comes to music, with the voice of a frog and the rhythm of an elephant. But times have changed, and with the power of AI , I can finally join my family’s flock and find my groove in the music world! What It Does DuckStar is a hybrid game/music creator/social network that helps everyone find their musical rhythm—no matter how duckling they start. It's your one-stop pond for creativity, fun, and building a community of fellow feathered stars. Here are its key features: 1. End-to-End Music Creation Lyric Ideation: Generate catchy lyrics with a little or a lot of input. Create a Beat: Create quacking good beats and tunes, with AI assistance for track and loop creations. Customize Your Style: Pick your genre, describe your vibe, and your AI music producer will help compose the perfect soundtrack for you. Publish: Share your creations with the world, or keep them for your private sound pond. 2. Lip Sync Battles Compete: Engage in lip-sync battles or team up with AI co-stars for fun performances (suitable for those who are camera shy or can’t sing). Choose Your Style: Sing with your voice and face. Use an AI face with your voice. Pair your face with an AI voice. Climb the Leaderboards: Will you sink or swim to the top and become the next DuckStar ? 3. Community & Social Features Participate in viral challenges. Collaborate with fellow ducks in jam sessions. Earn votes and rewards by getting others to flock to your creations. Vicarious Living through Music When we think of idols and aspirations, actors, athletes, and music stars naturally come to mind. Just as sports fans live vicariously through video games—whether it's football, basketball, or other sports— DuckStar offers a similar experience for music lovers. While designed for non-musicians, it’s equally enjoyable for seasoned pros. DuckStar provides a platform where anyone can experience the thrill of music creation, performance, and competition. With AI-powered features, users can dive into the creative process and bring their musical aspirations to life. How We Built It Here’s the updated list in Markdown format: Amazon Q Developer: We used the Visual Studio plugin to write a lot of boilerplate code, which helped a lot with conforming to strict TypeScript standards, code completion, bug fixing, and refactoring. Some of the Lambda functions were 90% written by Q! Amplify for app hosting. S3 for file and media storage. CloudFront for media distribution and caching (each song consists of multiple MP3 tracks). DynamoDB for user data, song data, and leaderboards. Lambda for serverless operations — FFmpeg and Python functions for pre/post-processing, beats per minute, and other song/track analysis. Node.js is used for coordinating webhooks from jobs, S3 uploads, and AI job routing. Bedrock for lyrics generation (Claude 3.5) and image generation with Stable Diffusion (for AI pop stars, producers, and song/album covers). SageMaker for deploying and inferring with models like AudioCraft and MusicGen. Frontend Vue.js for building the frontend user interface. Backends Node.js for server-side JavaScript execution. Python for data processing, AI integration, and backend services. Key Projects Used AudioCraft for high-quality music generation. MusicGen for AI-powered music creation. Minimax for optimizing decision-making in the creative process. Demucs for high-quality audio source separation. Stable-Audio for high-fidelity sound generation. Stable-Diffusion for creative visuals. Librosa for audio analysis and processing. FFmpeg for multimedia processing and format conversion. Challenges We Ran Into "Waddling Through Webhooks": Had trouble using inbuilt Amplify “functions” for AI job webhooks. In the end, we created a traditional Lambda and updated DynamoDB directly. Audio Drift: Synchronizing audio and video for performances was a challenge, even with AI-generated tracks. Eventually, track "drift" started happening (even ducks drift in a strong current). Existing Music AI/Gen Solutions: Current commercial solutions either lack APIs, offer limited control over editing, or rely too heavily on text prompts. Our goal is to provide users with a more fulfilling and personalized experience by allowing them to be actively involved in every step of the creation process. With granular control over adding, removing, and editing tracks, users can create bespoke content tailored to their vision. We focus on striking the right balance between ease of use, time investment, and effort, ensuring users feel a sense of achievement throughout the creative journey. Creating a Track End to End: The process involves about seven steps: lyric generation, music generation, decoupling the tracks, recreating new "mix tracks," and post-processing. All these steps take time, so working on a UI and user flow to mitigate or obscure long wait times was also a challenge. Accomplishments We’re Proud Of Seamless integration of AI tools for music and visual generation. A fun and intuitive user experience that’s easy for even the most musically-challenged ducks. Building a vibrant community where creativity and competition flock together with the potential to create viral-worthy content (lip sync battles). Beyond a PoC, this is closer to an Alpha release. What We Learned Theory behind music composition and rhythm. First time using Amplify and Bedrock! Due to the amount of time saved using Developer Q, we were able to fulfill our vision within the time frame and build out many more features beyond our initial planned PoC. None of this would have been possible without some amazing open-source projects: AudioCraft, MusicGen, Minimax, Demucs, stable-audio, stable-diffusion, Librosa, FFmpeg. What's Next for DuckStar Polish and Refine: Perfect the user experience and streamline workflows, getting from Alpha to Beta release. Collaborative Features: Improve co-creation and collaboration features for friends, families, and teams. Leaderboards: Add more competitive features to help ducks rise to the top. Social Networking: Enhance collaboration features for a bigger, more quacktastic community. Weekly/Monthly Themed Song Competitions: Sports teams, topical news events, family, and loved ones. AI Improvements: Make the AI more interactive and tailored to your duck personality . Add face, mouth, and head tracking to develop a "charisma" score for the lip-sync battles. Viral Expansion: Time to spread our wings with viral marketing campaigns and get more ducks in the pond! Partner with influencers for VIP Lip Sync battles (Influencer A vs. Influencer B). Potential Music and singing have always been powerful ways for people to connect, and DuckStar amplifies this by making the creative process accessible to everyone. Whether you're making music on your own or participating in a collaborative jam session, DuckStar helps users express themselves in ways that resonate with others. The platform's lip-sync battles have all the ingredients to go viral, making it easy for music to spread like wildfire. DuckStar transforms the excitement of musical expression into an accessible, gamified experience, allowing users to shine and rise through the ranks. DuckStar is not just a game—the real-life creations could mean we may just promote the next real pop star. <div