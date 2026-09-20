---
slug: "the-grenadians"
url: "https://devpost.com/software/the-grenadians"
title: "Meltingpot"
hackathon: "Pixel Forge AI Hackathon ($18,000+ in Prizes)"
organization: "Pixel Forge"
winner: true
words: 1228
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Meltingpot

> Everyone in the class takes notes. Meltingpot turns them into one shared vault for students, and builds flashcards and practice tests from it.

[Devpost](https://devpost.com/software/the-grenadians) · hackathon [[Pixel Forge AI Hackathon -18-000- in Prizes-]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** css, gsap, javascript, plpgsql, supabase, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for meltingpot

## Body

Six characters and you are in, no account needed to look first. Open source, MIT licensed, and built for the Pixel Forge AI Hackathon. Students type however they want and the AI does the tidying. The teacher's admin view, showing what is waiting on their approval. Flashcards built from the notes the class already shared, not from a textbook. Practice tests are marked on the server, so the answers are never sitting in the page. Teachers can see how the class is doing on practice tests and flashcards, listed alphabetically because a class is not a ranking. Every shared note keeps the messy original alongside the tidy version. One class space, organized into weeks, built entirely from what students wrote. Every correction is kept, so you can always see what changed and who fixed it. The landing page, where a class code is all you need to get in. The AI was down while we recorded, so the demo shows the fallback. Fixed version is in the media. Settings keeps the full picker, so anyone who wants dark or wants to follow their device can say so. A student's home: their drafts, their class, and what their classmates just shared. Inspiration This project was inspired by one of our group member’s experience taking a human biology class. The professor went over a lot of material each lecture and very quickly, which caused our group members to have trouble keeping up and to have very disorganized notes that were barely legible. The solution was an all-in-one app that would generate legible summaries from messy notebook pages. What it does MeltingPot is an AI-powered notes analyzer that collects notes from multiple students in the same class, mixes their common themes and ideas, and generates summaries with corrected English, facts, etc. Additionally, MeltingPot can take the notes inputted and use them to create flashcards & full practice tests. It tracks version history, contributions by person, and allows for editing in case of error. It uses roles to enable teachers or hosts to control the submission of edits, notes, and admission of users. How we built it MeltingPot was developed as a full stack web app with NextJS, GSAP, TypeScript and Tailwind CSS. We are powered by Supabase for our Postgresql database, user authentication and private files. For database access control, we implemented rules at the database level to provide separate access to student draft notes versus public notes as well as to enable varying levels of permissions for students, maintainers and pot owners. All of our AI features are accessed via authenticated server-side routes to Google Gemini. The output from Gemini will be structured in a way that allows us to validate its format prior to displaying it to users. As a fail safe we have implemented a deterministic organizational fallback so that even if the AI providers are down or unavailable the primary organizational flow will continue to work. We host the application on a Netlify subdomain at Meltingpot . Challenges we ran into One of the most complex problems we had to confront was ensuring that AI did not end up directing the learning while remaining very useful for students. There is a fear that the model filters information but can get it wrong as it might not decipher unclear or incomplete notes. Therefore, we came up with a way to review the material that would keep the text visible and would not allow publishing of anything without a human review. Another important challenge dealt with creating a secure multi-user system. Private documents have to be carefully differentiated based on the permission rules of sharing notes, teachers, and students along with version history. We soon realized that those rules need to be dealt with on the database level instead of just in the interface. The process of creating a perfect multi-user application was one of the major challenges we encountered at the beginning of the development. It encompassed multiple problems such as doing simultaneous saves, editing notes during corrections, speed of responses, network issues, file management, and responsive design. Testing the whole process allowed identifying problems that would not be visible in tests with single users. Ultimately, the live lecture recording idea turned into a bigger challenge than anticipated, producing the need for reliable streaming transcription, which consists of issues such as microphone permissions, connection recovery, recording consent, privacy and other provider costs, as well as how to deal with the final remarks of the recording. Although we developed and prototype the feature, we did not want to release it as a complete one until testing was done. Accomplishments that we're proud of We take pride in the fact that we achieved serious improvement in our product MeltingPot which transformed into an advanced note generating platform. Now, the system covers the entire process from generating rough notes to completing them, having them acknowledged by a professional human expert, and completing the course. We are proud of the fact that our system allows recording the authorship, so the users know what material is theirs and what information was given to them by other people. We also developed a full range of studying tools extracted from the knowledge base of the class, such as just summaries, flashcards, tests, and the like. The notable achievement is that we managed to avoid creating separate materials for each student. Besides, our main achievements include searchability of the class spaces, file attachments, dashboards, tools for moderation, and a lot of other features. Meltingpot is unique from other source-to-material study apps, since it also carries a social and collaborative aspect that are inexistent in other apps. What we learned The conclusion we reached was that the role of AI in education should be primarily to assist and not to replace the students' judgment. Students are more inclined to trust the organized notes created by the AI if they can see the original wording and how the AI changed the content. Furthermore, it is vital to pay attention to provenance. It is more useful for the students to have a flashcard, summary, or practice answer that they can trace back to the original note, and keep digital notes saved rather than being discarded. The construction of the MeltingPot application has shown that collaborative applications have to be developed for different situations that do not enter the ordinary demos. Many people might be altering the information, and network requests might fail at inconvenient times or content can change while being reviewed. Database restrictions, state management, and realistic testing become as mandatory as one can see. Of utmost importance is the understanding that there are serious privacy obligations attached to educational technology. Features that process information such as student files, voices or classroom recordings should include prior consent, retention controls, deletion options and full disclosure of the way the data will be processed. What's next for Meltingpot We were working on implementing features that allow for live lecture recordings and allow the user to upload recordings of lectures, from which it would transcribe and create notes of, as well as a feature to import and connect the app to both Google Classroom and Canvas LMS. These features were not pushed to the website due to time constraints. Additionally, we would improve the notes that are created through having the AI add visual diagrams and pictures to the notes. <div