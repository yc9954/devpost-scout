---
slug: "greeting-arena"
url: "https://devpost.com/software/greeting-arena"
title: "Greeting Arena"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 1071
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Greeting Arena

> Wishing your loved ones was never this easy

[Devpost](https://devpost.com/software/greeting-arena) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: developer, legal_professional</sub>
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** figma, javascript, mysql, php5, replit

## Body

Replit development environment Replit credits consumption Wish email which is sent according to the contact's timezone (GMT offset) Confirmation email is also sent to the user who scheduled the wish Wishy is "error-proof" & covers all edge-cases, thanks to Replit AI search feature to quickly find templates Successful scheduling of a template Contact creation form Plan change error Special case: showing hearts & cakes for a contact who has his birthday & anniversary on the same day Contact's management page Features to be launced in the future Landing page, greeting the logged in user Signup page Verification email sent to the new user Note: In the video, we mentioned it is just an android app, whereas it is a mobile app (works beautifully on both iOS & android, as it is made using the Replit mobile apps feature). Replit judges can read the "how we built in section" to know more about the integration. Also, do go through the image carousel also to get a hold of the entire application. As this app is made using Replit, it can only be accessed on a mobile phone on the Expo Go app. We have somehow submitted the aab file on Google Play Store, but it is pending approval from Google Inspiration In a world racing toward automation, where everyone is building agents to handle our work, we often forget the simplest and most human things: to connect, to care, and to celebrate each other. Wishy was born out of that realisation. It’s not about AI doing more - it’s about us doing what truly matters, better. Birthdays, anniversaries, and festivals are more than dates on a calendar; they’re moments that make life personal and warm. With Wishy, you can remember and celebrate those moments effortlessly, not just as a digital routine, but as a genuine gesture of kindness. Technology should make us more human, not less. Wishy’s mission is exactly that - to remind us to pause, smile, and make someone’s day special, one heartfelt wish at a time. What it does Let's go through the project overview to see how the app works: a. New users have to sign up & verify their email via OTP. Post that the user will be greeted on the landing page, which lists the features of the app, future roadmap along with the beautiful animations. b. On the contacts page, you can see the current plan (free, standard, & premium). As of now, one can just tap on a plan to upgrade. Contacts' carousel is presented in a descending order, so a contact who has his/her special day closest will be shown first (along with the countdown tags at the top left of the card). c. One a particular contact card is clicked/opened, one can see which templates are scheduled for that particular one. Use the tick & delete icon to edit the same, and the error/success messages shown. d. PHP CRON job is running at the background & ensures that the contacts are wished on the very first minute of their special days. But do you wonder, how that happens behind the scene? While creating the contacts, one provide the address (city, state, & nation) for it, so that the Geo-encoding API can grab the GMT offset (there are more than 24 timezones in the world) & store it in the backend. And the CRON job ensures that the GMT offset is taken into account, so that you always are the first one to wish your contacts. How we built it (the Replit way) When we got to know that Replit has this amazing mobile apps feature, we were excited to turn out our idea into reality. We started by giving 2 FIGMA UI screens to the AI agent, and from there on, we witnessed to see that with minimal reference and inputs, the landing and signup pages were made. Tweaking and adding the functionalities took us some time, but once we get used to the platform, we understood the flow better. As we got $25 credits for this event, we used them to code all of the required pages. We used Replit so much, that an invoice was raised (which literally blocked us from coding till we don't clear/pay off that invoice). Post clearing that invoice, we decided that for this event, we will keep a separate database and it's operations on our own PHP server, so that we can offload that from Replit side. So, the Replit APIs are contacting with our written PHP server, which is turn is contacting the mySQL database. Replit agent was awesome, as it did most of the debugging on its own, took screenshots for its own reference, updated its memory as we coded the application on the go. We were just typing in our thoughts, and Replit was building it right in-front of our eyes in an efforltess manner. It was great to see out idea turning into a working application. Challenges we ran into We wrote the PHP server code, designed the database schema, set up the CRON jobs, and the email parts also on our own, so we have to tweak a lot around that, to ensure that the DB is flawless and clean. Apart from this, it took a day or so to get accustomed to use Replit, how the fike structure works for a mobile application, and how to test it out on the Expo Go application. Also, we created our Google Developer account for this event, and somehow got the aab file for our Replit app and sent it for approval (it is still pending as it takes some weeks). We were very well aware of the "app store integration" on Replit, but we thought of spending $5 for the google dev account, as opposed to $99 for the apple dev account (exhausted most of our budget for this event on Replit; and we are happy to spend for such a beautiful utitlity application). Accomplishments that we're proud of From two figma UI mocks, to such an amazing, beautiful, functional mobile application, we are completely awestruck by how accurate Replit Mobile App feature & agents are. The idea behind this app is so serene and divine, that this app feels like a dream come true. What we learned How to code like a pro on Replit, working with PHP for the background and DB operations. What's next for Greeting Arena <div