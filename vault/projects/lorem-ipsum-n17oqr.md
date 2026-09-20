---
slug: "lorem-ipsum-n17oqr"
url: "https://devpost.com/software/lorem-ipsum-n17oqr"
title: "Monday Rewards"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 1376
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Monday Rewards

> Monday Rewards is an employee achievement system that cultivates and supports a culture of recognition within an organization

[Devpost](https://devpost.com/software/lorem-ipsum-n17oqr) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** babel-cli, babel-preset-react-app, body-parser, cors, couchdb, css, dotenv, ejs, express.js, html, javascript, jsonwebtoken, milligram, monday-sdk-js

## How they structured the write-up

- context
- what it does
- value proposition
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for monday rewards

## Body

The unique user dashboard shows the current Leaderboard standing, badges earned, XP Points, and Kudos updates The user details page with a tool tip indicating how badges are earned The pop up notification users receive when they unlock a shiny new badge! Unlocked Badges Locked Badges Context In recent months, the current economic crisis has transformed the way we work and do business at an unprecedented rate. Many organizations are instituting mandatory work from home policies, or have already announced a permanent shift to a remote working culture. For many organizations, this abrupt change marks a significant shift in how teams engage, communicate, and interact with one another. As a result of this transition, organizations have started to rethink how team members can be recognized for their hard work and dedication with the days of a “pat on the back” or a kind acknowledgement in passing is no longer as simple as it once was. What it does Monday Rewards is an employee recognition system designed to express appreciation for employees' contributions within your team and organization. Our app has been designed to encourage and incentivize team building, give accolades, celebrate failures, and so much more. We believe everyone in an organization should recognize each other’s hard work and efforts while having fun! Did someone pull an all-nighter to get the project done? Award them with a Night Owl badge and share the success with teammates. Did one of your teammates do something outstanding? Don’t send a boring text message. Praise them with a High Five badge! For each badge and trophy you get, earn XP points and compete against your colleagues for the top spot on the Leaderboard . For every item changed to 'Done', earn more points towards your next XP level and earn milestone badges along the way. Your teammates can see who’s leading or close to overtaking so work hard and work smart to maintain your lead and show them who's boss! But hey, to keep things interesting, we believe failures should be celebrated too! Did someone miss a deadline or ask for an extension? Give them a badge and deduct the points. It’s a competitive world out there! Enough about the teammates, what about the management? Many companies strive to have a rich culture in their organization, but most leaders don’t have time to track their employees good deeds by witnessing and recognizing their efforts, whether remotely or in the office. With Monday Rewards, team members can praise, recognize, and celebrate failures and successes with each other, anytime and anywhere. However, this isn’t just a top down system between managers and those who report into them - it’s about everyone! Managers are people and want some appreciation too! It’s a 360-degree style of recognition which we believe builds empathy and transparency between everyone in the company, while forging fun and meaningful relationships as well. This is Monday Rewards. A fun and engaging app for teams to recognize, praise and appreciate. Value Proposition When designing this app, our primary goal was to ensure that it didn't function as a novelty product, but one that provides value to both the business and user. The badge system we've developed focuses on simple user achievements most rewards systems offer - Birthday badges, Work Anniversaries, XP Points reached, etc. However, we felt that this system could also act as a fun way to incentivize users to discover features throughout the Monday app, such as the Board Owner badge for when someone creates a new board in Monday, or even the Monday Madness badges that users can earn after an item status is changed to 'Done' 100x, 500x, 1,000x, 25,000x, etc. Our goal has been to create a scaleable system that allows ample room for new badges to be added whenever new features are integrated, or even when a new idea comes to mind. We believe this gamified system is a fun and engaging way to help guide the user to different features within the platform and discover new tools to help solve problems and/or manage teams and processes within their organization. How We Built It JavaScript along with HTML and CSS were primarily used with Node.js for the back end and React for the front end. Milligram was used as our CSS framework along with CouchDB for the database and monday-sdk-js for the front end library. For back end dependencies, this app utilizes Express for the web application framework and also used to handle our http server and routing. Babel-cli and Babel-preset-react-app transpiles our React JSX code into standard JavaScript code, Cors helps with cross origin resource sharing, Body-parser helps parse the body of http requests, dotenv has been used for accessing environment variables, ejs (a JavaScript templating language, jsonwebtoken for managing JSON web tokens, monday-sdk-js to build for the Monday.com Work OS platform, nano for managing CouchDB, path for working with file/directory paths, and pino for logging. We are using Ngrok for development with hosting on a linode cloud server. On the Linode cloud server we are using an Nginx server to serve our app. Nginx will be set up as a proxy directing requests from port 80 to the port our app is running on. The Linode server will also be encrypted so the data will be encrypted at rest to meet business compliance standards. Challenges We Ran Into This project certainly challenged us in terms of connectivity issues with the server (because it was only accepting ipv6 traffic), the integration recipes took a little while to understand, and ultimately our own estimation of how long we felt it would take to work on such an ambitious project. In the end, we were able to make it happen, but it definitely wasn't easy. Thankfully, we've had a lot of fun working on this project and look forward to building more apps for the Monday marketplace in the future. Accomplishments That We're Proud of From Hunter... "I enjoyed the process of designing for the Monday.com platform and learning about their API. To me, the challenging part was setting up the integrations and configuration settings. Overall, if we had more time I’d be able to add more features. I have a solid grasp of how apps are built for this platform." From Alina... "I’m glad I had an opportunity to write tooltips and notifications for our rewards system. As outlined in the Design Principles, to delight the user using down-to-earth language, which I enjoyed writing for our badges/trophies. The best part was to be able to celebrate achievements, successes and failures with the user in a friendly and empathetic way through UX writing. I’m satisfied with our product’s outcome and believe it will provide value to the teams." From Kori... "This was my first experience working with the Monday Design System and I absolutely loved it! It's fun, easy to use, and really helped me gain more experience as a Product Designer." What's Next for Monday Rewards As a small team, and one with a single developer, we worked endlessly throughout this challenge to come up with a concept, define how it could work, where there's an opportunity for it in the marketplace, and also begin to create our core MVP. We recognize that not every badge we've determined to be possible is currently set up and running due to time constraints and resources (i.e., 10 year anniversary badge since that wouldn't come up immediately), so our main goal first and foremost is to continue developing the app for it to be marketplace ready with all badges included. In addition, we hope to receive guidance from the Monday team to understand how we can design and integrate a wider range of badges with a focus on introducing and guiding users to features within the platform. From our experience using Monday, we see that the possibilities are endless in terms of the tools available to help teams solve their unique challenges, manage projects, groups, and more. We designed Monday Rewards from the very start to be a scalable app that would allow an endless number of badges to be integrated within, and would certainly appreciate the help the Monday team could lend towards helping us recognize further opportunities to make Monday Rewards even bigger and better. <div