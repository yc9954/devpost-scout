---
slug: "poppedcorn-word-game-to-guess-blockbuster-from-cryptic-plot"
url: "https://devpost.com/software/poppedcorn-word-game-to-guess-blockbuster-from-cryptic-plot"
title: "PoppedCorn: The Blockbuster Movie Cryptic Anagram Word Game"
hackathon: "Reddit Games and Puzzles Hackathon"
organization: "reddit"
winner: true
words: 1057
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/immigration_refugee"
  - "substrate/geospatial"
---

# PoppedCorn: The Blockbuster Movie Cryptic Anagram Word Game

> Play a Fun Word Game right in your Subreddit with Top Grossing Hollywood Blockbuster movies guessable from Cryptic Word Clues or Emoji. Manually Curated with Bonus Content from r/ExplainAFilmPlotBadly

[Devpost](https://devpost.com/software/poppedcorn-word-game-to-guess-blockbuster-from-cryptic-plot) · hackathon [[Reddit Games and Puzzles Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[immigration_refugee]]
**substrate** [[geospatial]]

**stack** devvit, react, reddit, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for poppedcorn

## Body

Popped Corn - Word Game to guess the movie from the cryptic description Splash screen when the post first loads Guess the movie from the cryptic hint provided Bonus question from r/ExplainAFilmPlotBadly Leaderboard for flex rights Emoji mode as a bonus option Inspiration 🍿 Update: We've run into issues with Devvit 0.11.13 where uploading >1k assets with runAs:APP and userActions:true refuses to upload the app and fails with: Something went wrong... "Create" failed after 3 attempts . We've filed a bug for the same and are waiting for a fix for the final game but this would probably take months We ❤️ Reddit and we 😍 watching movies. We're kinda basic so we watch hits and top grossing movies not cinema. We came across r/ExplainAFilmPlotBadly and we wanted to do something similar, but while the subreddit had mostly classic cinema we wanted to make a game for casual movie enthusiasts featuring blockbuster hits and popular movies and television series. So we made a simple game, which was super duper hard to implement correctly. Reason being: we tried to make it really interesting to guess your favorite movies, while also making it difficult enough that you couldn't guess them immediately. Our code and game are public and we would love any feedback or issues. What it does Guess the movie from anagrammed letters of that movie as well as some letters from similar movies which would also fit the provided hint. Bonus content from r/ExplainAFilmPlotBadly and an Emoji Round that lets you guess the movie from the provided emoji. The features in a nutshell 🌰 🔢 Vector Embeddings for Movie Descriptions - Similar Movies are Hinted Together ⬇️ Server Functions for fetching Game Hints - Keeps the algorithm off the client for both faster processing and code obfuscation ⭐️ User Generated Content - Reddit Client API - Fetches bonus questions from r/ExplainAFilmPlotBadly to keep the game fresh and challenging 😎 Emoji Mode - A limited subset of movies in the list described through only Emoji 💯+0️⃣ - Over a thousand movies and cable or streaming series that we manually hinted and prompted in order to have enough content to make the game last almost forever How we built it We had a little bit of React experience and after trying to build on a custom UI and use a WebView, we realized that using native Devvit UI blocks would be best suited to our purposes. We built the entire thing using only Blocks Components, and assets that we created ourselves. We also manually compiled a list of over One Thousand guessable movies and emoji , and also used User Generated Data from the aforementioned subreddit to keep the content fresh. UI featured useAsync for all our data loading Almost all data was loaded using server functions to process the data, except for the Reddit API data which was loaded on the client side. const { data: message, loading, error } = useAsync(async () => { const user = await _context.reddit.getCurrentUser() ... let moviesSeen:string[] = [] ... const returnedMovie = await getMovie(moviesSeen) //movie user hasnt seen before, or restart after list over ... },{depends: pageIndex}) We used sentence encoding and hashing for movie lookups and similarity const use = new SentenceEncoder(model, use_vocab); function fnv1aHash(str) { ... return Math.abs(hash).toString(16); } async function embedJSON(inputFile){ const arr = JSON.parse(fs.readFileSync(inputFile, 'utf8')) ... for(const item of arr){ const tensor = await use.embed(item.description) ... const hash = item.emoji ? fnv1aHash(item.movie+item.emoji) : fnv1aHash(item.movie) const embedding = vector.map(k=>k.toFixed(8)).join(",") ... results.push(obj) } } Anagram function to include multiple movies for letter hints We make the game more challenging by including movies that might possibly fit the hint. The other movies are those which have similar descriptions to the target movie. We generate letter hints that have the correct solution, as well as possibly making one incorrect solution as well. function findRequiredLetters(thisMovie: string, otherMovies: string[]): string[] { const cleanSentence = thisSentence.toLowerCase().replace(/[^a-z]/g, ''); const mainLetterCount = new Map<string, number>(); ... let bestCombination: string[] = []; let minTotalLetters = Infinity; for (const otherSentence of cleanOtherSentences) { ... const combined = cleanSentence + otherSentence; for (const char of combined) { letterPool.push(char); } if (letterPool.length < minTotalLetters) { minTotalLetters = letterPool.length; bestCombination = letterPool; } } return bestCombination.sort(); } As mentioned earlier we also used RedditClientAPI for User Generated Data and Server Functions for processing and a RedisClient for dynamic leaderboards. Challenges we ran into We had some interesting challenges that we'd like to illustrate below: We ran into some issues with the color schemes on buttons, specifically the caution and bordered appearance on the button component did not seem to display colors correctly We also ran into some issues with logging, where some asynchronous functions would not register logs on devvit logs for a subreddit These two minor issues aside we had a blast developing on the platform! It's really easy to do a lot of things we thought would be super hard, like getting posts and comments, or generating a leaderboard. Accomplishments that we're proud of 🤯 Using Devvit - Honestly this was better than we ever expected. Even though the documentation had a disclaimer stating that it might be incomplete, the docs were leagues better than a few other platforms. 🔎Cryptic Movie Clues - As mentioned before we manually compiled the list. It took us three days of part time work to make the list (and about 13 days of part time work in total for the entire project), but the end result was super rewarding 🍿Vector Similarity for Hints - A Word Game is only as good as its words, and we spent quite a lot of time trying to figure out the best way to allow a user to play. We're happy with the results. What we learned The Devvit platform was an absolute revelation! We went through nearly all the documentation and we realised how incredibly powerful it was. Also building games using the platform is super easy and fun. We will be spending even more time on reddit now thanks to all the cool games that'll be made as part of this hackathon we're sure! What's next for PoppedCorn Hopefully some recognition. We worked hard on this and feel we have a solid mvp, but with a few weeks more work we'll add more emojis, fix more bugs and make the game faster and snappier. <div