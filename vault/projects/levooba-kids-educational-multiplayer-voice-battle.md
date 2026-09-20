---
slug: "levooba-kids-educational-multiplayer-voice-battle"
url: "https://devpost.com/software/levooba-kids-educational-multiplayer-voice-battle"
title: "LEVOOBA Kids: Educational Multiplayer Voice Battle"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 1272
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# LEVOOBA Kids: Educational Multiplayer Voice Battle

> The first voice only live online multiplayer learning quiz for kids

[Devpost](https://devpost.com/software/levooba-kids-educational-multiplayer-voice-battle) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** alexa, amazon-cloudwatch, amazon-dynamodb, amazon-web-services, dynamodb, lambda, mysql, php, rest-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we've learned
- what's next for levooba kids: educational multiplayer voice battle

## Body

GIF APL during Quiz Round Pick a Quiz, touch enabled, kids-friendly graphics LEVOOBA Kids on the new Echo Show 10, motion-capabilities added Multiplayer voice battle How LEVOOBA looks on an Echo Show 10 Learn school topics with Alexa Kids are having fun with LEVOOBA Table of Contents Original description on submitting to the DevPost challenge by November 2020 Added on January 3rd 2021: Updates to the Skill after Finalist announcement December 2020/January 2021 Description Inspiration The Amazon Alexa Voice Experience Skill was created as part of the Amazon Alexa AWS EdTech Challenge 2020 EMEA. With LEVOOBA we wanted to do our part in creating a fun and educational voice experience to support Kids schools education by using the most natural form of communication: Voice. What it does LEVOOBA Kids is a child-directed skill. With LEVOOBA Kids students can train their current school subjects at home. They virtually get together for multiplayer voice challenges - even if they don’t live in the same neighbourhood. LEVOOBA turns students into players and classmates opponents. Teachers select fitting topics either from our LEVOOBA database or they supply their own material in our backend for their students. They follow up on the students' results and learning progress, so they can circle it back to their own teaching. LEVOOBA is meant for personal use and will enhance the learning situation of all students while they are at home. Parents will need to set up the LEVOOBA account for their kids by using the Alexa App and link the account with a code. No reading or writing is necessary – and LEVOOBA is absolutely screen-free! Kids will learn just by voice-battles. When one player challenges another, the preferred opponent will receive a notification. So you’ll always know when someone is challenging you. Ask your parents to guide you through the process of accepting a challenge. LEVOOBA is our contribution to diverse learning approaches. We also encourage physical activities in breaks and waiting periods. How we built it Our LEVOOBA Kids product is based on a) the Amazon Alexa Skill which is built in the ASK-SDK v2 (node.js) and also uses AWS Services (Lambda, Cloudwatch, DynamoDB, S3). Our Skill is just a frontend for our educational learning plattform (backend). Our backend b) is based on our own created user and content management system written in PHP with a MySQL database. In our CMS we create user profiles, classes, quizzes and questions which kids (our users) then can answer in our Alexa Skill. We're using APL-A for our audio-branding, APL to support display-devices and also Motion Support (Follow on Wake Word) to make sure the screen follows the user. Challenges we ran into Obviously LEVOOBA Kids pushes the Alexa capabilities very far. It is the first ever real live multiplayer Alexa Skill where you can play against other players that are not in front of the same Alexa device but where they are sitting in front of their own devices at home, or using the Alexa app on their Smartphone. So it was very hard to create this kind of multiplayer experience as Alexa isn't able to push game updates of your opponent to your own device, so we made it round-based where each player plays 5 questions and after that you can start playing another round Accomplishments that we're proud of We're so proud that we were able to pull off creating the first ever real live multiplayer Alexa voice experience. It was hard, tough, but fun. And kids love playing against their school buddies and compete with them in who is the smartest regarding their current school topics. We were also selected as Finalists on the AWS EdTech Challenge 2020 EMEA. What we've learned We've learned that voice is great for fun and educational experiences and adding features beyond voice will help and make an even better experience for kids. What's next for LEVOOBA Kids: Educational Multiplayer Voice Battle We're currently in certification for our German Alexa Skill. We will look into all possible options to further increase our Skills multimedia capabilities and add more features, more questions and start approaching schools to get started on LEVOOBA. Updates December 2020 / January 2021 Video: https://www.youtube.com/watch?v=bbxdgeDJCg4 Over the last days since being named a finalist we've been working hard on improving LEVOOBA Kids. So here is what we've added during the holidays! Table of Contents Content. Content. Content Improved APL support for display devices 2.1 Touch enabled menus for kids 2.2 Visual and motion responses during a quiz Added multiple Motion-Capabilities Future 4.1 More motion and display support 4.2 More content 4.3 Monetization Details 1. Content. Content. Content. LEVOOBA Kids is available in US, UK and Germany with now 6 different quizzes and over 1200 questions. We've added 2x more content than available before and also newly classified the content to be found more easily. LEVOOBA Kids now offers kids-friendly content created by professional educators in the following areas: Addition, Multiplication, Social Studies, Letters, Space and a special Christmas Quiz Edition. We're also working with teachers and educators to further improve and add more content. (see 4. Future) 2. Improved APL support for multimodal Alexa display devices 2.1. Kid-friendly touch-enabled graphical menu to choose your quiz Once the kids start training mode they can now not only choose a quiz via voice but are also presented a graphical kids-friendly menu on display devices like Echo Spot, Echo Show 5 and the all new Echo Show 10. There they easily and intuitively choose a quiz type via touch. This feature will soon also be available for multiplayer mode. See it in action ( this is a gif, so please wait a few seconds to the action to happen ) 2.2. Visual responses during a quiz During a quiz round in single- and multiplayer mode kids will now get acoustic, visual and motion-enabled feedback once they have answered a question. We are using APL Pagers to first show the either positive (for correct answer) or negative (for wrong answer) response using a kids-friendly emoji. Then we display the next question to be answered as a text. This is also timed with the acoustic response and positive/negative audio jingle response. 3. Added Motion-Capabilities To welcome the kids to our skill we will play the LEVOOBA Kids jingle via APL-A . We also use APL-A when the kids exit the skill experience. During the start of our skill we've now added Motion-Capabilities and will start a timed PlayChoreo just after the jingle has ended. We're also playing the Choreo when a kid is giving a wrong answer for adding motion to our acoustic and visual feedback, because the PlayChoreo feels like the Echo device was shaking like saying "no-no". 4. Future 4.1 More motion and display support We plan to integrate motion sensing for some quick in-between games to prepare for a round to start (move left/right). We're also planning on integrating a new round based mode for two players on one moving Echo Show 10, where the screen moves between 0° and 180° so that the players on one device can play against each other with the screen moving between both. But as this command "move to position XY" is not possible yet, this will be implemented later on. 4.2 More Content Here's the content we have planned for Q1/2021: Cyberbullying Healthy Diet Subtraction Division Also we're working with a German Publisher to add an educator certified Math Multiply Trainer to LEVOOBA Kids. 4.3 Monetization Once we have added more content and gained a user-base we will also include In-Skill-Purchases ISP to allow users to purchase more content packs to choose from. <div