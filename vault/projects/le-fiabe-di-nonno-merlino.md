---
slug: "le-fiabe-di-nonno-merlino"
url: "https://devpost.com/software/le-fiabe-di-nonno-merlino"
title: "Le fiabe di Nonno Merlino"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 1216
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Le fiabe di Nonno Merlino

> An ancient wizard called Grandpa Merlin reads traditional fairy tales, where users can interact with the plot.

[Devpost](https://devpost.com/software/le-fiabe-di-nonno-merlino) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for le fiabe di nonno merlino

## Body

Home menu Interactive mode: select the story to play or get a brief description of it Story selection: drink the potion or eat the cookie Story selection: choose whether to answer the Wolf Story action: call the Jiminy Cricket! Story action: light the fireplace! Story action: follow the stones! Interactive mode: start over, go on or exit Golden Dreams mode: play the saved playlist or create a new one Golden Dreams mode: add fairy tales to the playlist Goodbye illustration 1 Goodbye illustration 2 Work in progress 1 Work in progress 2 Work in progress 3 Work in progress 4 Work in progress 5 Work in progress 6 Inspiration We all love fairy tales: they go straight to the heart because they are intimately connected to our childhood and, in most cases, to people we love, as our grandparents. I remember well when I sat down on my grandpa legs and, enchanted, listened to all that beautiful stories he recounted to me. Then, I grew up with two passions: technology (I’m a software engineer) and writing. When I realized what Alexa was able to do I thought to put both the pieces together and create something special for kids. The character of “Nonno Merlino” (Grandpa Merlin) is exactly this: the archetype of all our beloved grandparents telling us wonderful stories. What it does In the skill an ancient imaginary wizard, named Grandpa Merlin, reads traditional fairy tales with the involvement of the audience, who becomes an active part of the story. This is the skill main mode, called interactive mode. There is also a continuous mode, called Golden Dreams mode, where interaction is disabled and more than a story at a time can be read in a continuous fashion. In interactive mode the user gets involved in the story through requests called "actions" and "selections". An action is a brief speech, as “do a magic”, or a screen touch, performed by the user in order to let the story continue. For example, kids could be asked to help the story protagonist to escape from a dangerous situation. A selection is instead a brief speech (or a screen touch) that allows to choose between two possibilities. For example, in the famous novel Alice in Wonderland, included in the skill, the user can select whether Alice have to drink the potion or eat the cookie. Each choice makes the story continue in a different way and then both the possibilities are brought back to a common plot. In the Golden Dreams mode, that can be enabled both through a voice command and touching the moon and stars icon on the screen, users can select stories to include in the active playlist, or reuse an existent playlist. Once a playlist has been set up, all stories in the playlist will be narrated by Grandpa Merlin in a continuous fashion, without interaction requests, and then the skill silently shutdown. This mode has been thought both for bedtime, when interactions are a distracting factor, and for children that are too young to interact verbally. Before the beginning of each story, Alexa and Grandpa Merlin interact with each other through short fun sketches, in order to increase the audience participation and reinforce the characters’ personality. How I built it The skill is coded in TypeScript and makes use of the Alexa Skills Kit SDK for Node.js. For the backend, I’ve used the following AWS services: Lambda, S3, CloudFront, DynamoDB. Moreover, the skill uses APL, Playback Controller and Audio Player interfaces. Challenges I ran into The skill has required a lot of work, a considerable economic investment, and, before all, the involvement of many people, that I’d like to thank for their great contribution. The development of the project, that took over seven months, has been organized in four main tasks: skill development, stories selection and texts writing, voice recordings and graphic artworks. The skill includes ten (!) stories, selected among the most beautiful and renowned with the help of a friend who’s a child psychologist. For each story, together with my wife (who’s a teacher), we wrote the script, in order to identify the story actions and selections. We had to invent from scratch all story forks and the related plot, that does not exist in the original story. Then, I rewrote all the texts from scratch with a language style and terms appropriate for the intended audience (mainly but not limited to children between 3 and 9). Each story has been carefully reviewed three or four times with the help of a workgroup (made up of friends who are psychologists and teachers), and the whole process alone took about three months. For what concerns the Grandpa voice, I was especially demanding: I listened to over a dozen of professional voice actors, looking for a great talent that could well interpret my Grandpa Merlin. At the end, I found this special artist able to interpret seven different characters in the same story with an incredible expressiveness. Voice recordings took another two months, and the stories received a further review to adjust them for the voice. Coming to the graphic artworks, I collaborated with an illustrator who made all illustrations by hand! She used a mixed technique (ink, markers, pencils and watercolors). I requested her not to use a vector graphics editor as for the skill I wanted the look and feel of these old children's storybooks, and not the perfection of computer graphics. Please consider that each story has at least two actions and one selection (which in turn has two illustrations), and moreover there are illustrations for the rest of the skill and all the icons. So it is easy to understand why these creations and the digitalization process took another two months. Finally, there was the coding process, that since design to testing took over seven months for the first release. Obviously, this is an ongoing process. Accomplishments that I'm proud of First of all, to be able to manage all the project complexity and to bring it to completion. In my professional career, I managed complex projects with many people and activities but getting a project completed should be never taken for granted. I designed the skill with the ease of use in mind: I wanted to hide all the skill complexity behind an intuitive, child-proof, vocal interface and I think I got this objective. The skill has an extended contextual help, with a lot of managed states, so kids should never remember all commands but can use this intelligent help system. Moreover, in the first sessions, the skill presents three simple tutorials that smooth the learning curve for using the application. At the end I think the skill is very simple to use yet powerful! What I learned Well, a lot of things! First of all, that you should beware of artists! Joking apart, in these months I had the opportunity to collaborate with a lot of people and I feel that each of them has enriched me. So it was and will be a great adventure! Then obviously I learned also a lot of technical things, like APL. What's next for Le fiabe di Nonno Merlino The skill evolution has been carefully planned and will bring in a lot of new features. Stay tuned! <aside class="large-3 columns"