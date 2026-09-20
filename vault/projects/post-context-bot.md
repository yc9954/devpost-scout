---
slug: "post-context-bot"
url: "https://devpost.com/software/post-context-bot"
title: "Post Context Bot"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 595
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Post Context Bot

> Porting the code behind u/mmm-submission-bot that is written in Python to a "Devvit" app.

[Devpost](https://devpost.com/software/post-context-bot) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]]

**stack** devvit, github, moderator, reddit, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for post context bot

## Body

Inspiration Combatting spam is hard on Reddit - especially on a subreddit such as " r/maybemaybemaybe " where all the post titles are the same. Some sort of automated function was needed to combat the bots that would post irrelevant content; the idea for a submission statement bot was born. This then evolved to not just combat spam, but also to provide additional context to users - why was this post submitted to this subreddit? What did it bring to the community? Submission statements became more about post context, and so the concept evolved to where we are now. What it does Posts a comment on every new submission requesting a context statement. If the poster doesn't reply in time, or doesn't meet the length or keyword criteria, the post is removed automatically. If they do, the bot confirms it and tidies up (at least from the user perspective, moderators can see the original comments that get removed) the request message. Everything is configurable to how moderators want to operate their subreddit; timings, character limits and keywords, even the exact message that posters will receive. How we built it I already had a Python/PRAW bot that I wrote for this purpose, so for this hackathon I ported that existing codebase to Devvit Web using TypeScript and Hono. Post submission fires a trigger, and a scheduled job handles the deadline check - meaning it doesn't have to continually poll and keep an in-memory list of posts anymore. Redis is used to prevent duplicates as a fallback. The trigger-based activation means the app now responds instantly, whereas before it was polling the subreddit every few minutes to check for new posts or submission statements to handle. Challenges we ran into Documentation is limited! Getting the reply lookups working and debugging to ensure the devvit.json schema was correct took a big chunk of time with some trial-and-error required. It was also important to ensure we didn't just read the settings at app-startup, as they could be changed at any time - which required a shift in approach. Accomplishments that we're proud of The shift to Devvit means no self-hosting by a subreddit on external infrastructure is needed, making it massively more usable. No self-setup on a hosted server somewhere, it's a "click and go" install from the App Directory. I've also provided a default configuration out of the box so it really does just work from the moment it's installed. The main accomplishment is that every feature that was previously in the Python-based bot has been ported across to Devvit, with settings now configurable through the Devvit site rather than needing to edit a config file. So not only did we not lose any functionality, it in fact has become significantly easier to use. What we learned There was a different mindset needed from polling to scheduling, removing loops and sleeps and replacing with triggers. It's resulted in a much more usable app, IMO. I'd also never written a TypeScript application before so there was a personal challenge to get the context and syntax right in some cases. What's next for Post Context Bot The bot is complete for what I needed it to do, but if other moderators have feature requests (one that comes to mind would be to skip "approved" posters) then I can always build these in. I hope that it can be used to reduce moderation overhead and provide improved user experience to subreddits - I know from experience how helpful the Python version has been and this just makes it even better. <div