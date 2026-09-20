---
slug: "world-mathematics-league"
url: "https://devpost.com/software/world-mathematics-league"
title: "World Mathematics League"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 843
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# World Mathematics League

> An energetic, exciting and challenging national level mathematics competition, that puts your skills to test.

[Devpost](https://devpost.com/software/world-mathematics-league) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** alexa, amazon-api-gateway, amazon-cloudwatch, amazon-dynamodb, amazon-lambda, amazon-web-services, google, java

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for world mathematics league

## Body

Logo Question Screen Rankings Screen Opening Screen Inspiration STEM education and excellence is a worldwide pursuit. Why then, should we limit our learning to an isolated singular experience? I felt the need for a skill that would rekindle our competitive spirit and help us compete at a global level. With this skill, my hope is that we inspire and challenge each other in a healthy way but still be unified by a regional and national spirit as we would be contributing not only to our own learning but to the greater good of each of our regions and country. The following are the primary motivators of my skill ideation and creation: Learning - Fun interactive way to accelerate STEM learning. Competition - Success at the National and Global level will provide an incredible morale boost to the users encouraging them to learn and practice more. Gamification - With each user motivated to earn the top spot for their state or country on the leaderboard, will not only bring them back to work with the skill each day but will also encourage them to promote it among their friends and neighbors to help the overall board. Thus each of them become 'Champions of STEM education' by helping drive broader awareness and love for the subject in the community. While science and technology continue to grow at breakneck speeds, it is very critical that we plant the seed of love and interest for STEM learning in our community in a fun, interactive, inclusive and competitive way, all at the same time and my skill 'World Mathematics league' is one such effort to achieve that. What it does World Mathematics League is a national level mathematics competition, where every day you will get 15 minutes to solve simple to complex mathematics problems. Based on your device location, you will be auto-enrolled into your regional team and your individual score will be added to your overall team's score. You can check your team's progress throughout the day, and the winning teams will be announced at the end of the day. By recruiting more friends in your region, you will improve your team's chances of winning the daily competition. If you choose, not to share the location, you can still play the game but your points won't be added to your regional score. Skill can be enabled by visiting the page : https://www.amazon.com/dp/B07HH96SWZ The questions vary from as simple as adding two numbers to solving algebraic expressions. So, this could be a great family outing where both adults and kids can work together and helps increase the bonding in the family. How I built it Challenges I ran into One of the microservices was taking more than 7 seconds to respond, and this was causing the skill to time out. This was happening because there are few IO operations performed by the microservice on initial load which was taking a long time. By implementing a CloudWatch Rule and sending a request every minute to the Lambda function, I was able to avoid the Lambda cold start problem that was causing the overall response to go over 7 seconds. This was a good learning for me personally. Having written Alexa skills using the first version of Java SDK, it was total relearning for me to write with the new V2 SDK. It makes me feel good, to be up to date with the latest version! Accomplishments that I'm proud of Leveraging API Gateway to create microservices. This allows me to create different experiences ( skills for future ) based on the same service. Building a multi-modal Alexa skill leveraging different Display templates and directives . Used BodyTemplate1, BodyTemplate2, BodyTemplate7, ListTemplate1 and ListTemplate2. Implemented the CanFulFillIntent to give the skill a chance, to be invoked without using its name. Implemented the FallBackIntent to capture out of domain utterances. Leveraging Alexa Sound Library What I learned Alexa Device Address API to retrieve the device location. This helps me to auto-enroll the user in his regional team. Alexa User Settings API to retrieve user's timezone so that I can administer the test in a 24 hour time period in the user's timezone. Google Geo API to retrieve the user's city and state if they are missing in the Alexa Device Address API response. Alexa Java SDK 2.5 to build the skill. What's next for World Mathematics League I would like to explore the opportunities of providing users the ability to create groups and challenge each other. After testing in the US, I plan to expand the skills to other countries, and it would truly become a world league then. Extend the skill to individual gameplay, and provide feedback on how the user is doing with respect to everyone in the world. Extend or create a new skill ( experience ) with Echo Buttons Explore the option of Account Linking to provide customized analytics to the user. A weekend challenge where users pay an entry fee to participate. Integrate Alexa In Skill Purchasing. Refactor code to use Elastic Cache to calculate leaderboards <div