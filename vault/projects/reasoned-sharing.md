---
slug: "reasoned-sharing"
url: "https://devpost.com/software/reasoned-sharing"
title: "Crithink App"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 596
team_size: 7
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "substrate/video_visual"
---

# Crithink App

> Defeating fake news starts from people. Think critically before sharing!

[Devpost](https://devpost.com/software/reasoned-sharing) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[media_journalism]]
**substrate** [[video_visual]]

**stack** adobe-illustrator, java, photoshop, swift, xd

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for crithink

## Body

Inspiration The majority of approaches to fight fake news focus on the "supply" side of the news and try to automatically spot fake news, limiting the actions of its creators. Given the overwhelming amount of information uploaded every second on the internet, such approaches may fail to evaluate all the contents. For its reason, we think that solution resides in the "demand" side of news, that is people. So we asked ourselves the fundamental question: why does fake news exist? Probably because in nowadays digital media ecosystem people spend little time and efforts in evaluating news credibility. Probably we are not completely aware of the dangers we expose people around us when sharing fake news, especially during the Coronavirus outbreak. Probably we are not ready to behave responsibly in the digital world, yet. That's why we think that we need to step back and reason more before sharing contents. The key to limiting the spreading of fake news is empowering people! What it does Crithink helps you in evaluating the information you want to share on your social networks (notice that Crithink HELPS you, it does not evaluate the credibility of information for you!). When you read an article you would like to share, you can do it through the Crithink app. This will give you a context about: the source of the article (whether it is reliable or not); the content (it nudges you to read the entire article and evaluates the lexical correctness of the article); the artefacts in the article (it discovers whether the images present in the article have been previously used in other contexts). Crithink gives you an indication of all these features, but the sharing decision is still up to you! How I built it The application will be developed for both Android and iOs. All data processing is performed by a microservices infrastructure hosted in a Kubernetes cluster (it may be AWS or GCP for example). The deep neural network which provides all the information needed for the “context before share” will be designed and implemented with Keras. We have particularly focused on user experience and user interface. Specifically, we built the information architecture by developing a user-friendly workflow and usability-based scenarios. Mockup realization and interfaces rendering was elaborated with Adobe Photoshop, Illustrator and XD. Challenges we ran into The main challenge was to find an efficient approach to deal with fake news spreading and create a tool to help people thinking and sharing critically. Accomplishments that I'm proud of Defining the key features of fake news, we developed a clear idea that can benefit the entire society. On the one side, with Crithink, we can create fake news awareness and provide individuals with instruments to identify and limit fake news spreading. On the other side, we value the role that fact-checkers and journalist play in giving us reliable information, giving prominence to their work in fighting fake news. What we learned We learn to join efforts and use a common language to solve a problem. Our team is made up of expert in the field of engineering, sociology, design, marketing, business developing and information technology. Regardless of the different approaches we have to address an issue, we learned how to turn such differences in strengths. What's next for Crithink The further next steps are three: To keep in contact with potential investors and find partnerships with institutions and private entities working in the information world, such as newspapers and journalists To develop the App Start our communication campaign to raise awareness about fake news and the app <div