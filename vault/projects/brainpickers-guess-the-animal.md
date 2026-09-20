---
slug: "brainpickers-guess-the-animal"
url: "https://devpost.com/software/brainpickers-guess-the-animal"
title: "BrainPickers! Guess The Movie"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 615
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# BrainPickers! Guess The Movie

> Guess the movie I'm thinking about from the given clues, pixelated image plus letters revealed with each clue.

[Devpost](https://devpost.com/software/brainpickers-guess-the-animal) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[developer_tools]]
  <sub>weak: developer</sub>
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** alexa, amazon-alexa, amazon-web-services, apl, ask, es6, lambda, mysql, node.js, rds, s3, sql

## Body

In Game Clue APL (small round) 2 In Game Correct Answer APL (small round) 2 In Game Clue APL (small round) In Game Clue APL (mid/large) In Game Wrong Answer APL (small round) In Game Clue APL (mid/large) 2 End Game APL (small round) In Game Correct Answer APL (mid/large) In Game Wrong Answer APL (mid/large) In Game Correct Answer APL (mid/large) 2 In Game Correct Answer APL (small round) Help APL (small round) End Game APL (mid/large) Help APL (mid/large) I find engaging with Alexa to be best when the interaction can be in a quick fire fashion, from the start to the end. This preference extends to gaming experiences on Alexa devices. I wanted to make a series of games that can be used as perfect time fillers. Guess the Movie is a designed for voice-first Alexa skill that allows people to quickly get into game play, play as long as they want and then get back to their other activity. The player must try to guess the name of a movie from clues that Alexa provides. They can give up, ask for a new clue or just guess the name of the movie at any time. Players are seamlessly led from movie to movie and can end the game anytime and see how well they played. I hope to have created a more fun, game-show-like experience for players by incorporating music and SSML speech con's as interjections. Alexa can congratulate a player on a correct answer (or the opposite on a wrong answer) with a random quip that is localised to the player's region. During a session the speech-cons are randomised and unique each time. For example, in the US you could hear 'bada bing bada boom' but in the UK you could hear 'bob's your uncle', in Australia 'sweet as' or in India 'balle balle'! I built the skill with Node.js running on Amazon AWS Lambda using the Alexa Skills Kit SDK. I custom built a database of clues for the skill and offline processed images to build up the questions. I designed the game format to be reusable so that I could quickly develop more 'BrainPickers! Guess the ...' series of games with the codebase requiring slight adjustments to APL documents, code, music, images and a new dataset only. I am a new developer to the Alexa platform and my previous skills have been hosted external services and coded in different languages. This was the first time I was coding using Node.js, using the AWS platform/Lambda and as I was working by myself I had to first learn the development environment and this was the only hurdle! I successfully released and certified this skill as well as four other 'BrainPickers! Guess the ...' series of skills to Alexa Skills stores in the UK, US, India, Canada and Australia. These include 'Footballers', 'Animals', 'TV Shows' and 'Hollywood Stars'. I've also incorporated in-skill purchases to all skills in the US, the can fulfill intents for discovery and the Alexa Presentation Language (APL). I created multiple APL documents to be served from the skill depending on the interaction and each document caters to varying display sizes. Design was based on the smallest form-factor first, with larger displays receiving additional elements to complement. Touch-based interactivity is also implemented so even though the game is perfectly playable voice-only, the player can also progress through the game using on-screen buttons (although the answer to clues must be spoken!). I look forward to adding more 'BrainPickers! Guess The...' series of games with new datasets. I am also expanding the codebase to allow varying clue types so clues can be in audio, video, image or text/spoken formats. <div