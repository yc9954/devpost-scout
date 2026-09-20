---
slug: "notation-gx6v9m"
url: "https://devpost.com/software/notation-gx6v9m"
title: "Notation"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 561
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Notation

> A notes marketplace that boosts student scores with high-quality notes from peers, with resources for clubs, competitions, and more!

[Devpost](https://devpost.com/software/notation-gx6v9m) · hackathon [[Funathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]]

**stack** amazon-web-services, chakra-ui, mongodb, nextjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for notation

## Body

Notes Marketplace One of our high-quality notes uploaded to Notation The dashboard for everyone! Inspiration When we participate in competitions like math olympiad, science olympiad, or DECA, we feel that there just aren't many good resources made for our specific event! We also felt that the "resources" that are provided by these competitions don't really work , and often times there are thousands upon thousands of paragraphs that just don't relate to our topic. So, we created Notation, the world's first (to our knowledge) note marketplace that allows students to exchange their notes on any subject in existence! What it does Notation is note marketplace that allows students to upload their old notes (that they don't need anymore), in exchange for points. Then, students can use these points to purchase other notes that they need! Every time someone else downloads your note, you get points! So, if your note is really really good, you'll get many points. However, if your note is pretty bad, then you won't get many points at all! Core Features Tag system (search for notes most relevant to you using tags, allowing you to search by school*, **subject , grade , and many more !) Net-Positive points system (every time a transaction occurs, more points put into circulation, increasing the number of notes on our site!) Review system (people can comment on a note, leaving a review!) Analytics - see download count, points you earned, and much more for each note you upload! How we built it We built Notation using Next.JS for our front and backend, Chakra UI for our front end UI, Amazon S3 for our mass file storage, MongoDB for our document-based, quick access storage, and Disqus for our rating system! Since we were extremely time limited (by the hackathon), we used pre-built Chakra templates (with MIT licenses) for most of our UI Challenges we ran into Collaborating with each other (since one of us was in Hawaii) was a big challenge, so we set it up where only one of us would commit to the Github Repo. Getting Amazon S3 to work was a bit of a pain, as we had to set up some IAM stuff The search engine indices that we made were also challenging to get just right Our front end would often times make unnecessary requests, as we were using multiple React State updates Deploying to Next.JS created so many problems with invalid SSL certificates, random build errors, and so much more (see our Github repo commits, and you'll see the full story :)) Accomplishments that we're proud of Creating a working marketplace system within the time frame! Creating a search engine that actually lets you find stuff that you want Creating a nice-looking UI (with the help of some pre-build components) Creating a points system that incentivizes the exchanging of notes Creating an email-verification system where users will get automated emails with a verification code What we learned We learned how to get Amazon S3 to work, how to create an optimized search engine, better optimize React States, and that deploying to production is a really really big pain What's next for Notation If our users grow, then we'll definitely add a way to buy points (with USD) so we can earn moneyyyyyy. We'll also work on improving our UI, and support more than just PDF uploads. <div