---
slug: "tunetangle"
url: "https://devpost.com/software/tunetangle"
title: "Tune Tangle"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 1377
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Tune Tangle

> Want to break out of the monotonous loop of music that you can't seem to escape? Look no further! Tune Tangle gives you a curated playlist based on your existing taste to spice your music life up!

[Devpost](https://devpost.com/software/tunetangle) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, flask, html, javascript, python, react, spotify, sql, typescript

## How they structured the write-up

- track 5 // music discovery
- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for tune tangle

## Body

Welcome to Tune Tangle! Tune Tangle: How we do it Using extracted song features, we further tailor the Spotify Recommendation system to return songs similar in style and viral potential. TikTok Music Recommendations, Just for You! The DB of songs user's have already liked/added for cross referencing with our recommendations What's next? Track 5 // Music Discovery Current State of Issue: Many talented music artists struggle to break through noise and gain exposure to their music on TikTok. The Desired Outcome Enhanced Exposure: Artists, particularly emerging and independent musicians, should experience increased visibility and exposure to their music on the platform, leading to greater recognition and potential career opportunities. Viral Potential: The platform should facilitate the organic spread of music through viral trends, challenges, and user-generated content, enabling songs to gain traction and popularity quickly. Inspiration The world of music seems limitless, and yet sometimes, it feels hard to break free from the monotonous music loop that many of us experience. We often find ourselves stuck in a cycle where attempts to discover new songs lead us back to familiar tunes. Tune Tangle aims to solve this by leveraging the viral potential of TikTok and the extensive catalog of Spotify to introduce users to fresh, niche music that aligns with their tastes. By integrating sound recognition and recommendation algorithms, we envisioned a tool that not only surfaces new music but also makes the discovery process enjoyable and seamless. What it does Tune Tangle is a song recommendation system designed for discovering new music on TikTok . With Tune Tangle, users can find their next favorite tune or viral hit from videos curated just for them. It can take inputs in many forms: ranging anywhere from short video clips to user playlists. And if a song is just that good, just its name will do the trick. Whatever melody is presented, Tune Tangle finds other songs just like it, ensuring the perfect discovery method. Listeners can easily access these recommendations through a simple and secure Spotify connection, viewing them in a user-friendly environment. How we built it Apportioning tasks was critical for our success. We split the project up so that one person worked on the backend, one on researching recommendation systems, and two on the frontend because we prioritized an appealing user experience, attempting to mimic TikTok’s engaging and impactful UI design. 1. Sound Recognition First, we wanted to implement a sound recognition system to complement the search bar because many sounds on TikTok are “original” sounds that use existing songs without a known tag to identify said song. To do this, we used Python and ShazamIO, an open-source song recognition system, enabling users to not only find the name of the song they like but also find other similar songs. 2. Music Recommendation System On the backend, the Spotify for Developers API was used once the name of a song was passed in. We use the open-source recommendation system to find sonically similar songs. Then, we cross-reference the recommendations with users’ personal playlists to try and maximize the chances that the songs we recommend are actually new discoveries instead of just popular songs. Finally, we returned TikTok videos pertaining to the song in order to promote new potential viral videos using the unheard sounds. We also added functionality once the recommended songs were given so that users can easily add songs to their “Liked Songs” in Spotify with a click of a button. This furthers our integration with one of the largest existing music platforms. Additionally, we know from personal experience how disappointing the Spotify recommendation system can be, so we tried to fine-tune the system as much as possible by taking data from the user-inputted song such as danceability and liveness and giving a specific range around those values for our recommended songs. 3. Designing the Frontend On the frontend, we utilized a React framework and used Chakra UI and Typescript to make our code as robust and maintainable as possible. The combination of these technologies allowed us to create a responsive and visually appealing user interface, ensuring that users have a smooth and enjoyable experience while discovering new music through TikTok. By having a modular design, future developments would be easy to implement with little of the original code being affected. 4. Catering to User Experience We aimed to have a modern style user interface with a sleek yet comfortable appearance. Thus, we opted for a dark and muted website background with an intentional high-contrast color palette for user accessibility, highlighting actions and the cursor. Smooth transition animations were added for a responsive UI feeling, and large buttons and wide input fields were used to draw user attention. We imitated the TikTok experience with our video recommendation results by creating a vertical feed of cards with TikTok videos embedded. Additionally, we designed the website navigation to be as intuitive as possible, allowing for straightforward usage of the app. 5. Client ↔ Server The communication between the Flask endpoints and the frontend initiates by providing the user’s Spotify authentication token to generate music recommendations. After processing the request and calling various APIs such as Spotify, TikAPI, and ShazamIO, the server returns information that is then processed and displayed in an engaging format. Challenges we ran into We dedicated a significant amount of time to planning a friendly user experience. On the backend, we debated how to utilize the results of our TikTok video search after determining music recommendations. Decisions such as downloading the videos versus embedding them were crucial, as they would ultimately dictate the flow of the app. Additionally, we aimed to replicate the TikTok environment as closely as possible, which led us to question the validity of TikAPI. To ensure practicality in a future integrated environment within the TikTok application, we settled on providing a realistic result by embedding TikTok videos. Even more difficult decisions were essential in creating a seamless and intuitive experience for users, aligning our app closely with the TikTok interface they are familiar with. Displaying video in a feed-like format was essential to mirroring prior experiences. Additionally, we dedicated lots of effort to make the application more efficient timewise. Since searching playlists to create a better recommendation result requires more time, we aimed to use SQL to index Spotify user data and eliminate duplicate fetching. What we learned The importance of presentation for user interactions can make or break a person’s experience (for example, a list of songs vs. list of TikTok links vs. TikTok video feed). Subsequently, this impacts virality and engagement with the media. Accomplishments that we're proud of Anyone can make a get or post request on an API. What makes projects, however, is how a team can put those pieces together in a cohesive manner that can help people in a way they need. First and foremost, we’re proud to have solved a problem that we personally experience in our lives today, and this product is something that we will use even after this TechJam. In addition, creating a complete user experience is something that we never prioritized in our own personal projects until now. After countless iterations and brainstorming, the satisfaction when using our UI is something we are definitely proud of as a team. What's next for Tune Tangle We all know the AI buzzword has been flying around the tech space a little too loosely in the modern day. However, we truly believe that utilizing AI in our music recommendation systems can lead to more tailored results that is better than whatever is behind the Spotify API. Perhaps aggregating information that TikTok has aggregated on user music privileges could be helpful as it allows for an analysis of key moments of virality of songs (for example a catchy hook or a funny line) and predict what songs would appeal to audiences sooner. Additionally, integrating into the TikTok platform would allow for a much more streamlined experience for users, allowing them to perhaps press a Share->See Similar Songs button instead of having to go to a website and search for songs or download it to their local device to share. All in all, the possibilities for Tune Tangle are endless , and we are excited to push the possibilities of Artist Discovery! <div