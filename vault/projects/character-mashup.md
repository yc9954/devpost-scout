---
slug: "character-mashup"
url: "https://devpost.com/software/character-mashup"
title: "Character Mashup"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 654
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Character Mashup

> Character Mashup is a connected lens that allows users to share custom characters from anywhere in the world and bring them to life through the use of body tracking.

[Devpost](https://devpost.com/software/character-mashup) · hackathon [[Snap AR Lensathon 2022]]

## Facets


**stack** blendshapes, body-tracking, connected-lenses, javascript, persistent-storage, realtime-storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for character mashup

## Body

Early Concepts Early Concepts II Body Bin Inspiration Jye was interested in building a connected lens that allows users to share unique experiences with each other. Meredith was interested in building a customizable character creator inspired by exquisite corpse drawings, and Sallia wanted to build an AR experience centered around user interaction. What it does Character Mashup allows the user to custom-build their own avatar which they can bring to life through body tracking and then share with friends via connected lenses. Join a connected lens session and have a virtual dance party with friends across the globe using your avatar. You can even save your avatar configuration onto your phone and bring it with you when joining your friend's sessions. How we built it Through lots of iteration and sketching, we settled on a group of body parts that would create lots of potential variations. Inspiration came from things like action figures, emojis, and funky characters doodled in a sketchbook. We storyboarded out the experience and discussed the end goals and technical possibilities in the project. Character parts were modeled and rigged onto the body mesh skeleton. We built all the character parts into one texture sheet in order to save space and prioritize the 3D high poly models. All the character parts were then configured to sync over a connected session through realtime storage. The Lens is setup with a custom events system with various events that fire off for easy and agile control over the entire framework. Challenges we ran into One of the biggest challenges was syncing all of the lens data through a connected lens. Making sure all changes to the appearance and tracking of the characters would sync through as many connected devices as possible. Getting the body tracking to look natural on the platform was a little difficult as the body tracking is based from the hip joint, which makes it look strange when the user squats or sits down. Trying to add a lot of variety into the lens whilst still keeping in the lens file size limits was tough. We had to employ lots of tricks to fit everything in (and we did it with space to spare). We also faced the challenge of working across different time zones; with one member on the west coast, another on the east coast and a final member in Australia. Accomplishments that we're proud of We managed to build a lens that features high poly models while keeping the file size manageable. We figured out that texture sheets and shaders can take up a ton of space in the lens. To mitigate this, we built a master shader that features one texture sheet. All the visuals of the lens are driven off of two texture sheets. One texture sheet drives all the base colors including environment and the other is to drive face expressions on the characters. What we learned The biggest lesson learned is about time management and team building. We are all across 3 different time zones and all have different skill sets. We were able to do a 24 hour work cycle on the lens and divide tasks according to our strengths. What's next for Character Mashup We see so much potential for future versions of this lens. We could add in Idle animations so the characters will look a bit more natural when there isn't any body tracking. It would be interesting to add in more character options that extend past human proportions to create weirder and weirder avatars. Another is making the UI more clean and simple so the user feels in control, but isn’t overwhelmed by the amount of options. We'd also like to add some more gamification elements to give the users more opportunity to interact with eachother through the connected experience. We’re proud of the work we did here and we plan on promoting this lens via social media! <div