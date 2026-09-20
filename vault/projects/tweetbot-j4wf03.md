---
slug: "tweetbot-j4wf03"
url: "https://devpost.com/software/tweetbot-j4wf03"
title: "Alexa Tweet Bot"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 493
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# Alexa Tweet Bot

> Tweet using just your voice

[Devpost](https://devpost.com/software/tweetbot-j4wf03) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**domain** [[developer_tools]]

**stack** amazon-alexa, amazon-web-services, heroku, lambda, node.js, sinatra, twitter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for tweetbot

## Body

Inspiration I'm a big Twitter nerd and was shocked to find there was no existing skill to share Tweets via Alexa. I was excited to dive in and build my first Amazon Alexa Skill. What it does Alexa Tweet Bot allows you to Tweet using just your voice. You can add Tweet Bot to your Alexa account with Launch Tweet Bot . Once launched, it will prompt you to link your Twitter account. You can also manually link your twitter account linking by saying: Tell Tweet Bot to connect my Account . Once your Twitter account is linked, you can begin to tweet using Tweet Bot. Every Tweet needs to be prefaced with the word 'tweet'. The following phrase will kick off the Tweet process: Tell TweetBot to tweet hello world . The tweet process kicks off a short conversational flow to ensure the tweet is what you expected. If it is, say yes and the tweet will be sent. Voila! How I built it Tweet Bot was trickier than I expected because the Alexa SDK does not handle open-ended input well. You can define your own custom slot types with custom utterances. For example, you may build a Pizza Ordering Skill that has a custom slot type PizzaTopic . This slot type could have utterances: pepperoni , sausage , anchovies , tomatoes , etc. But when defining a custom slot type Tweet , the utterances for it are boundless. So what I did was built a tool (which I open-sourced that generate random phrases of English words. I used those as my utterances for Tweet and it worked! After that, it was a matter of connecting it to Twitter. Since Twitter still uses OAuth 1.0, I had to stand up a Heroku server that can do the data passing in between. All in all, a great experience that gave me an opportunity to play with cool new technology applying skills I have been honing. :) Challenges I ran into Definitely learning about Alexa SDK and getting it to handle open-ended input was the biggest challenge. Accomplishments that I'm proud of The skill is certified and published to the Alexa Skill Store. I'm excited to have built the first Alexa skill to author and send Tweets listed on the Alexa Skill Store! What I learned I learned about how conversational APIs work and the choices that Amazon made when developing their Alexa Skill API. What's next for Tweetbot First, it should be smart enough to handle @mentions. Most likely this will need to do some smart searching by looking at users who you have some affinity towards. Since vocalizing someone's Twitter handle will be difficult. Simple autocomplete on username would not be enough, would need to be really smart on which are the users you are most likely to mention. Also, new tools like the Amazon Echo Look and Echo Show offer exciting opportunities to share pictures and videos hands-free to Twitter. <div