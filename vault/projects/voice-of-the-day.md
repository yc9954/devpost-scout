---
slug: "voice-of-the-day"
url: "https://devpost.com/software/voice-of-the-day"
title: "Voice of the Day"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 985
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Voice of the Day

> Test your memory and see if you can put a name to the voice in this daily trivia challenge!

[Devpost](https://devpost.com/software/voice-of-the-day) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** amazon-web-services, apl, ask-sdk, azure, gameon, javascript, node.js, s3, sql

## Body

Intro screen Answer screen Hint screen Inspiration The format used to work well on the radio, so we wanted to recreate those memories on Alexa. What it does Players can listen to up to three voice clips of well-known people and/or celebrities talking every day, as well as view a blurred image of the celebrity. After each clip, Alexa will ask you who you think is talking, and you must try to answer correctly. This will earn you a score for the monthly and all-time leader boards. The player can ask Alexa for hints, or to skip that voice clip to move onto the next one. Users scores are awarded depending on how many incorrect answers they gave for that voice and whether they used a hint or not. Users can also ask to hear yesterday’s answers, in case they couldn’t get the answers on that day. How I built it To create the structure of the skill, we used the Alexa Skills Kit CLI. We used Amazons S3 storage for all our in-game assets such as the audio clips and images. We used the Alexa Presentation Language to create the visual interface for the skill. We used the Amazon GameOn SDK to create monthly and all-time leader boards for all users to enter without any sign up. Every day, free users will be given the ‘easy’ clip to answer. The set of clips each day will be selected dependant on the day of the year. Users who have purchased premium gain access to the ‘medium’ and ‘hard’ clips every day, as well as being able to ask for hints for the voices, skip a voice if they are stuck, and enter scores onto the leader boards. The user can say the following: “Play the clip again” “What were yesterday’s answers” “Skip” “Give me a hint” “Show me the leader boards” “Help” “Skip” “Repeat” “What is my score” ⭐ In Skill Product ⭐ The ISP for this skill is called Voice of the Day Premium. This allows you to access two additional voice clips per day on top of the daily voice clip, these are a medium and hard clip. It also gives you access to new intents: "Skip", allows you to skip a question and come back to answer it later. "Give me a hint" gives the user a hint for the current question Premium users also get points for each question they answer, which are posted onto a GameOn leader board. There is both a monthly and yearly leader board to compete on. Challenges I ran into It was very important for this skill that the quality of content was the focus, and so it was essential that high quality and good voice clips were used for the skill. We found it was quite a challenge to not only find high quality audio of the people we wanted for the game, but also clips that did not have other people speaking or have any background noise. As well as gathering all the voices, we then had to categorise them into easy, medium and hard categories. This proved difficult as different generations of users may find different clips easy or harder than others. We ended setting the medium and harder clips as voice clips that might be shorter, or lower in quality, and by who we thought might just be less well known overall. A more technical challenge encountered was developing with the Alexa Presentation Language (APL), which I had to learn whilst developing the skill. Though since the game has a very sole focus, solving the voice clips, almost all the APL views within the skill are identical. So, I was able to focus more time on perfecting one screen, and then using this across the project and just put the appropriate data on the screen. Accomplishments that I’m proud of As well as creating a high-quality voice-only experience, we developed the skill to be very APL focused, which we are very proud of. The visual assets we used for the project were very high quality and we were able to dynamically display the appropriate data for each screen within the skill. The content loaded depends on who is talking, as well as the difficulty of the voice that the user is answering. APL also allowed us to blur and unblur the celebrity images, as opposed to having separate blurred and unblurred images for each person. We were also very pleased with how we implemented the GameOn SDK SDK into the skill. When the user submits a score, they have a random avatar created for them, and their score will be submitted under this avatar. This avoids any sign up to use the leader boards, allowing all users to use it easily. GameOn SDK also allows us to create monthly and all-time competitions/leader boards which all users are automatically entered. What I learned I have learnt how to develop APL as well as better practices for structuring it more efficiently. For example, there are many APL views in the project, all of which are almost identical, what I have learnt that would be more effective in future projects would be to condense these down into one primary view that I would use for each screen and just use the appropriate data. I have also been able to hone prompts to the user for upsells and showing the leader boards. Testing has shown that constant prompts on each play for these things can become tedious to the user, and so we have reduced the frequency of these for a much better user experience. What’s next Voice of the Day We plan to add further voices of celebrities to the skill, to create a continuing user experience with new content every day. We would like to implement a multiplayer experience for Voice of the Day that will allow users to play with each other. <div