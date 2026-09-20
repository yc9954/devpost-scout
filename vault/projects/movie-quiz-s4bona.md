---
slug: "movie-quiz-s4bona"
url: "https://devpost.com/software/movie-quiz-s4bona"
title: "Movie Quiz"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 616
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Movie Quiz

> Guess the movie by the emoji. We give you hint after hint, you try to guess the movie.

[Devpost](https://devpost.com/software/movie-quiz-s4bona) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**substrate** [[document_pdf]] [[video_visual]]

**stack** jovo-framework

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for movie quiz

## Body

Splashscreen Pagers in MainGame screen GameRoundPagers Cards in the Alexa app Echo Spot Fire TV Stick Inspiration We like watching movies and playing community games. So we decided to create a game for Alexa that connects these two things together, by using emojis. What it does The game principle is very easy. At first, you decide how many players are playing. The game is currently made up to four players. The game starts and on the screen, at first you see two emojis that are describing a movie. If you know the right answer you can say the movie title, if it is correct you will get five points, if you are wrong you can get a hint and on the screen you will see one more emoji. You can get three tips maximum, but with each hint, the points you can get, will decrease. The minimum points you can get by guessing the movie using all hints is two. If you don't guess the movie by using all hints you get zero points. All players play simultaneously, so you need to be faster than the others. How I built it By using the Jovo Framework and the Echo Show (2nd gen) as a testing device. Challenges I ran into APL can be tough :D The first approach was to create an APL document with every request the user makes. It worked, but the game flow felt way too slow. The device rendered every image again and again. The interaction didn't feel natural. The second approach was to create the full APL (for the gameplay) document at the beginning and slide between states and user interactions with Pager components. In detail: When the user answers wrong, the skill doesn’t render the “wrong”-layout, but it switches the layout with APL commands (SetPage) to the required layout. This architecture allowed a smooth gameplay. It was hard because we had to add all possible states for that round into that document. (See image "Pagers in MainGame screen") In general, we like the idea of the Pager components. We were able to add small effects like a countdown, a timer or a kind-of revealing effect. (See image "GameRoundPagers") We used the Open Source emojis by Twitter (twemoji). They are pretty neat but needed an additional effect. We added a “sticker effect” to every (2841) emoji in the set. To improve the loading speed in general we did this for 5 different size types. (64x64, 128x128, 192x192, 256x256, 384x384). Another challenge was to use a UI optimized gameplay in a voice-only device like the Echo Dot. Therefore we used an image processing library to create Alexa home cards for every hint emoji in the right resolution. Image processing steps: Convert SVG emojis to PNG (384, 256, 192, 128, 64) (sharpjs) Add sticker effect to all of them (PS batch processing) Add random rotation to emojis (looks more playful now) (sharpjs) Create Alexa Cards for two different sizes (sharpjs) Accomplishments that I'm proud of Combining many modalities into a gameplay that makes sense for every device: Echo Show/Spot and FireTV (UI with some effects) Voice-only: Special wording + Alexa Cards Echo Buttons: Work with Echo Show/Spot and Voice only devices What I learned I improved my process of building multi-modal voice apps. Start with user testing soon Build wireframes first Don’t get lost in details in the beginning DON’T RECORD A VIDEO RIGHT BEFORE SUBMISSION DATE WITH YOUR MOBILE PHONE :) What's next for Movie Quiz learn from user feedback increase number of movies improve cross-device functionality build a small CMS to add more movies more frequent add more variety to the dialogs add unit tests make the skill open source <div