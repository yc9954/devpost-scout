---
slug: "spottr-ef3kgb"
url: "https://devpost.com/software/spottr-ef3kgb"
title: "Spotter"
hackathon: "Junction 2017"
winner: true
words: 950
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/researcher"
---

# Spotter

> Stupid simple matching of new music talent to interested and relevant music curators. Goodbye radio, hello Spotify

[Devpost](https://devpost.com/software/spottr-ef3kgb) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[researcher]]

**stack** cloudflare, dokku, koa, lightsail, mlabs, mongodb, node.js, passion, redis, redislabs, spotify, statistical-analysis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for spotter

## Body

The artist receives their recommendations Inspiration Traditionally for an artist to get their music heard, they would have to send their music physically or digitally to local or national radio stations, or to record labels however, Spotify and other streaming platforms have opened up the playing field for new artists to get their music heard easily. One of the few caveats to these platform being so open – from an artist’s point of view – is that they can easily be drowned out by all the noise because there is so much music available to the end user, and only a few means of getting their tracks into the spotlight. Yet there’s hope. Spotify has an incredibly strong social network integrated into its system and with the platform being open to all users (and free to use), the sharing capabilities have become one of Spotify’s critical pillars for attracting users and artists to the platform. From this, an ecosystem has grown where popular users who lovingly curate good quality playlists, garner huge numbers of followers, and therefore can provide a spotlight for a new artist’s tracks. Curators generally have means for artist’s to submit their tracks to them from outside the platform, however what often happens is that artist’s will spam many curator’s and their playlists despite the playlist not being appropriate. So we have a few problems: Curators get many demo submissions, many of which aren’t suitable for their playlists; There is no way within the spotify platform for an Artist to submit their track to a Curator; An Artist might struggle to find appropriate playlists from Curators to submit their work to. From this, we have been inspired to create a platform that tackles each of these issues one by one. What it does Spotter allows music artists on the Spotify platform to search for and submit to curated music playlists to get their new music into the headphones of as many people as possible. It's not enough to just send the tracks to any old playlist though. Spotter uses sophisticated search algorithms to determine which Spotify playlists will be the most relevant and the most likely to accept the artist's track as a new entry. Spotter subverts the existing practice of an artist mailing out track samples to as many people as they can find by ensuring that artists can only find curators who match the intrinsic qualities of their music. It brings the people that can make things happen to the makers of things that can happen How we built it As an already established team, we had the advantage of knowing each other's strengths and weaknesses so our first step was to plan out the stages of development and delegate the work appropriately. By initially designing common interfaces to develop against, we also cut down on integration time when it came to merging units of work. While members of the team had various language abilities, the common denominator was Node.js and so we began with a basic Koa framework skeleton and starting working from both ends of the chain: exploring the Spotify API to determine how we could gather our data as well as starting to implement our slick user experience. The data scientist on our team went about designing a search and ranking algorithm that took advantage of the audio statistics made available via the track analysis api while the devops guru set about creating the infrastructure that would allow our team to work quickly (and hopefully not break things). The result was a development environment where all of our data storage (Mongodb, Redis, etc) was in the cloud, removing an otherwise significant bottleneck to development. With regular but short progress meetings, we were able to keep everyone on the team up to date with the progress and feed back any concerns about how development was going. Communication is incredibly important and as a result these quick discussions were very important to the achievement of our goals and the completion of our hack. Challenges we ran into We discovered that the Spotify API wasn't necessarily designed for the sorts of things we were asking of it. In reality, we needed a way to search through playlists in a much more targeted manner, but we could only perform a full text search against the playlist names and descriptions. Ideally, we would have spent the time to index all of the playlists on Spotify, but that wouldn't have been viable given the rate limits and time available. Instead, we devised a way to structure our data requirements (genre/category/feel) as a full text search to get reasonably accurate results. Accomplishments that we're proud of The main aspect of Spotter that excites us is the genuine utility and legitimate business value that it provides. We're very proud to have designed a system that would fill a real niche. We're also quite happy with the level of polish that we achieved, developing the full end to end experience in about a single day's worth of development time. What's next for Spotter Spotter is just the beginning of the journey to make getting discovered simple and easy. Given the constraints of the hack, we focused on just music and Spotify. But we believe that there are many more industries that this idea applies to directly. After some time polishing and streamlining, it would not be unreasonable to see Spotter expand into, for example, indie movies - analysing video as well as audio, and recommending directors as well as curators. To take the idea even further, crossing industries could prove to be incredibly valuable (Curators of great movie soundtracks being recommended to directors, allowing new talent to thrive and prosper. <div