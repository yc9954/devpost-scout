---
slug: "us-law-reference"
url: "https://devpost.com/software/us-law-reference"
title: "US Law Reference"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 322
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/education"
  - "domain/legal_justice"
  - "user/educator_student"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# US Law Reference

> US Law Reference: A fast, offline legal pocket guide with searchable US Code, Constitution, and DMV practice tools.

[Devpost](https://devpost.com/software/us-law-reference) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[education]] [[legal_justice]]
**user** [[educator_student]]
**substrate** [[regulation_legal_text]] [[structured_db]]

**stack** dart, flutter, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for us law reference

## Body

Inspiration Students often struggle to access U.S. legal information in a simple, organized way. Existing apps are cluttered, online-only, or incomplete. I wanted a fast, offline tool that makes learning U.S. laws and DMV rules easy for everyone. What it does US Law Reference provides an offline, searchable library of the U.S. Code, the Constitution, and DMV practice tests. Users can browse titles, read full legal sections, study amendments, take quizzes, and track their progress—all in one app. How we built it I built the app using Flutter and Dart, with a local SQLite database for storing law sections, constitutional text, quiz history, and DMV questions. The UI uses Material Design 3 and follows a clean MVVM structure. All legal content is embedded for offline access. Challenges we ran into Extracting and formatting real U.S. legal text into a structured database Managing large datasets efficiently on-device Fixing quiz randomization bugs and answer duplication Designing a clean UI that still handles long legal sections Ensuring good performance without requiring internet access Accomplishments that we're proud of Fully offline access to 38 U.S. Code titles and the entire Constitution A clean, intuitive UI that makes dense legal text easier to read A complete DMV practice test system with progress tracking Smooth search functionality across all legal sections Successfully publishing a working APK usable on real Android devices What we learned How to structure and optimize large SQLite datasets in Flutter How to manage state and navigation in a growing mobile app How to extract, clean, and format public legal data The importance of UI/UX when displaying long-form text How to design quizzes, timers, and statistics tracking systems What's next for US Law Reference Expanding to all 54 U.S. Code titles Adding case law summaries and examples for easier learning Adding bookmarks, favorites, and note-taking Improving search with filters and keyword highlighting Bringing the app to iOS Publishing to Google Play for easy installation <div