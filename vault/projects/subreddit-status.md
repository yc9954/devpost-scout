---
slug: "subreddit-status"
url: "https://devpost.com/software/subreddit-status"
title: "Subreddit Status"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 599
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
---

# Subreddit Status

> App to monitor subreddit modqueue, modmail, community stats, etc. in Discord or Slack to help mod teams keep a pulse on their subreddit status from the comfort of their private subreddit-mod spaces.

[Devpost](https://devpost.com/software/subreddit-status) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets


**stack** devvit, discord, slack, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for subreddit status

## Body

Subreddit Status Main Board ModQueue Warning and Priority Report Alert - Slack Example Discord Setup w/ Stale Modmail Alert Inspiration They say necessity is the mother of invention, and that couldn't be more true here. The inspiration for Subreddit Status was the need for my co-moderators to keep a pulse on the status of the subreddit. Prior to the creation of Subreddit Status, this required checking the subreddit directly to see if there was anything in the ModQueue or in Modmail. Since our internal communications occur within Discord, this meant that there was a obvious shortcoming in our ability to stay on top of things. By creating a status board that monitors the status of the community for us, we can easily glance at the status board to know if increased moderator activity is required. We can also be directly notified via role mentions/pings when things get too out of hand. What it does Subreddit Status monitors a subreddit's subscriber count, modqueue, and modmail and displays these stats in a condensed manner that is easily digestible for mod teams. It updates every minute, and can be configured to post messages when the subscriber count reaches a milestone, when modqueue backs up to a predetermined number, when modmail messages go too long without any action, and more. How we built it Originally built in Python, it was converted to TypeScript and migrated to the Devvit platform. Originally it was just the basic monitoring, updating every minute to show how many subscribers there were, how many items were in ModQueue, and if there were any in-progress Modmail conversations. Over time, it grew to what it is today. Challenges we ran into The primary challenge was integrating Slack support. Built originally only with Discord in mind since that is where my moderation team communicated, I wanted to expand to support Slack for the moderation teams on Reddit that may utilize the platform. The issue with supporting Slack is that it is very different from Discord, and what works for one platform does not necessarily work for the other. The challenge was reviewing both to find common ground in order to minimize the amount of logic needed to support each platform individually. Accomplishments that we're proud of Built before Devvit, Subreddit Status was never intended to be used by other moderation teams. It was the first app I released on the platform, and is now used by moderation teams in 175+ communities. Providing a tool like this that so many other people find useful is one of the best accomplishments I could ask for. What we learned Over the course of development, I found that scope creep is an ever present variable. While it can be easy to add to the to-do list, this prolongs releases and can add unnecessary bloat. I needed to constantly remind myself that the app can do a lot, but it doesn't need to do everything. Too much of a good thing can be a bad thing. This is especially true as more and more apps get released on the Devvit platform. I have to be careful not to look like I'm trying to copy other apps or take their place. What's next for Subreddit Status The next major update to Subreddit Status will likely include externally triggered actions. If a post/comment receives a priority report for example, implementing buttons to allow the moderation team to approve/remove the content from Discord or Slack would mean quicker response times to said reports. Adding an interactive layer to the app will further bridge the gap between Reddit and Discord/Slack. <div