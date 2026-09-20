---
slug: "spozzle"
url: "https://devpost.com/software/spozzle"
title: "Spozzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 1349
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Spozzle

> Dash comes to Africa

[Devpost](https://devpost.com/software/spozzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** bloc-architecture, dart, firebase, flutter, material-design

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spozzle

## Body

spozzle on the web - northwest theme spozzle on the web - north theme spozzle on the web - west theme spozzle on the web - littoral theme spozzle on the web - running game - northwest theme spozzle on the web - active language dropdown - northwest theme spozzle on the web - result page - northwest theme spozzle on mobile (ios) - northwest theme spozzle on mobile (ios) - littoral theme spozzle on mobile (ios) - north theme spozzle on mobile (ios) - west theme spozzle on mobile (ios) - running game - west theme spozzle on mobile (ios) - result page - west theme spozzle on mobile (ios) - WhatsApp share - west theme spozzle on desktop (macOs) - northwest theme spozzle on desktop (macOs) - north theme spozzle on desktop (macOs) - littoral theme spozzle on desktop (macOs) - west theme spozzle on desktop (macOs) - running game - spozzle on mobile (ios) - running game - west themewest theme spozzle on desktop (macOs) - active langauge drop-down - littoral theme spozzle on desktop (macOs) - result page - northwest theme Inspiration Spozzle was inspired by our desire to make Flutter more relatable to people across the world, through cultural aspects close to their hearts. We chose to begin with Africa, by showcasing four native attires from Cameroon using Dash (the Flutter mascot) as our model. What it does Spozzle is a slide puzzle that enables users to: Pick their preferred puzzle theme and switch between themes as they wish, through a 3D image slider without losing their current score. Track their game duration through a timer that persists the score of a user while they switch between themes. Pause the game and quickly attend to some pressing issue beyond their control, like opening the door for a guest. Listen to African based tunes before the start of the game and while switching between themes. Select their language of preference (English or French) Experience aspects of the African culture that they can relate to through the Flutter mascot - Dash Interact with the game through multiple platforms (android, ios, web and desktop) Invite friends to play the game by sharing their scores through WhatsApp, Twitter or Facebook How we built it Our goal was to build the most beautiful slide puzzle with an all-around African feel. We used the Very Good Ventures starter app ( https://github.com/VGVentures/slide_puzzle ) as a template to structure our app and took advantage of some already existing features like accessibility, responsiveness and working logic of a generic slide puzzle. We realized the following milestones during the development of Spozzle: 1. Design Designed four African based themes from scratch, with all related design assets for each theme using tools from Adobe Suite. Sourced for free African tunes from Chosic ( https://bit.ly/3J9nPjs ) and integrated into the app Generated app icons and favicons using App Icon Generator ( https://appicon.co/#app-icon ) and Favicon.io ( https://favicon.io/ ) respectively Built a cool app logo using My Free logo Maker ( https://myfreelogomaker.com/ ) Used the Material design guide ( https://bit.ly/3MUOVx5 ) to pick colour variations for buttons, texts and to design the general user interface look and feel of the app Used a few other tools for image editing and miscellaneous. 2. State management and logic Followed the BLOC architecture to structure the app and used the flutter_bloc package to manage the app state Implemented buttons to enable a user to pause or shuffle the puzzle at any point in time and managed the app's state to respond according to the desired feature. Established a custom themed working slide puzzle. 3. Speed Pre-cached all assets using the precacheImage function to load the assets faster Compressed all assets using tools like Tinypng ( https://tinypng.com/ ) and Kraken.io ( https://kraken.io/account/optimizer/uploader ) for the images and Audio converter ( https://online-audio-converter.com/ ) for the audios 4. Animations Implemented sliding and tapping animations using a tweaked version of the GestureDector widget. A user can choose to either swipe or tap to move a tile Implemented an image slider using a 3-D animation using the Flutter Carousel Slider package ( https://bit.ly/3CyN6RD ). This image slider enables a user to select/switch between different themes Added Typewriter animations to the score widgets on the result page using the Animated Text Kit package ( https://bit.ly/3pUPywI ) Used the AnimatedIcons class to animate the pause/play button Implemented scale and fading animations on the puzzle tiles and puzzle timer using the ScaleTransition and FadeTransition widgets. 5. Multi-platform Support Added support for mobile (Android and IOS), desktop (macOS and Windows) and Web Used the ResponsiveLayoutBuilder widget to ensure that the user interface has an appropriate size on each supported platform 6. Translation Translated all strings to English and French. Added a dropdown, to enable a user to select their language of preference 7. Social Sharing Implemented social sharing to WhatsApp, Twitter and Facebook using custom URLs as specified by each developer platform (Twitter: https://bit.ly/3hZDMwr WhatsApp: https://bit.ly/3tO6tSs Facebook: https://bit.ly/36bQ4zp ) Used some cool helper classes and functions like the URI class, openLink(), canLaunch() and launch() functions to open the social share links in new tabs depending on the platform 8. Hosting Hosted the web application on Firebase ( https://spozzle.web.app/#/ ) Hosted the source code on Github ( https://bit.ly/36bJ31c ) Challenges we ran into Initially, we implemented the sliding effect of a tile on the entire puzzle board (board-wise); by detecting gestures on the puzzle board using our customized version of a GestureDetector and responding accordingly. During testing, we noticed that the speed of swiping was very slow, so we had to move the logic of swiping to be tile-wise and we obtained a far better performance. It was quite challenging to compress a ton of assets, so as to optimize the app's loading speed. When testing the responsiveness of an app on the web - by inspecting and switching between different devices, one always has to refresh the page to make the user interface (UI) show up properly. It does not automatically show the desired UI for the selected device. Accomplishments that we're proud of Successfully built a custom slide puzzle that meets all our requirements and brought it to production on mobile, web and desktop. Being able to understand a large codebase and building something original from it. What we learned Designing your assets and user interface is as important as coding the logic of the app. Sometimes design assets are underrated, but they play a key role in the app's speed and overall user experience. The importance of being keen on the features and properties of the widgets a package offers. It's good practice to vividly analyze the properties of a widget in comparison with your requirements and overall goal, before making your pick. Some packages might have high scores on pub.dev and look really fantastic, but when you take a deeper look at their properties, they might not be a good fit for that feature you're trying to implement. You might end up wasting a good chunk of time trying out different packages that seem like a good fit. There are a ton of helpful packages on pub.dev that facilitate development, but a few good ones don't support null safety yet. Flutter makes it a breeze to support multiple platforms and implement responsive user interfaces for each platform. What's next for Spozzle Future updates for Spozzle include: Integrating new themes for cultures in Asia, North America, South America, Europe, Australia and even more in Africa with a more dynamic image slider/theme picker Adding three levels of difficulty to the app and improving on the overall design and logic Creating an AI-based solver that gives a user hints on moves to take that can enable them to solve the puzzle in the fastest time possible. This feedback was inspired by some early feedback we've gotten from a few people who've tried out Spozzle. Adding more interactivity like tactile vibrations that create the illusion of a real game atmosphere Using it as a tool to make Flutter memes more relatable at local events and why not globally too. <div