---
slug: "temp_name-y3s98f"
url: "https://devpost.com/software/temp_name-y3s98f"
title: "The Commanders"
hackathon: "Global Power Rankings Hackathon"
organization: "Amazon"
winner: true
words: 380
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# The Commanders

> Fans want to know which teams are the best but other rankings are often subjective. Our project provides a data-driven approach to ranking teams based on their performance in game to create a ranking.

[Devpost](https://devpost.com/software/temp_name-y3s98f) · hackathon [[Global Power Rankings Hackathon]]

## Facets

**user** [[developer]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** .net, c#, lambda, postgresql, python, sqs, supabase, svelte, vercel

## How they structured the write-up

- who we are
- what we learned/challenges
- documentation

## Body

Who We Are Our group stems from a small discord community where we have formed over the year through happenstance. Ironically, the team members of this project are also the major nodes that created the discord we all use today. Originally, we were three separate discord communities that would then join each other's discord for League games. However, we soon started using one in particular. That is when we decided to then cut everything and restart a channel as the all in one place for us to group. It was League of Legends that brought us together and what drove us to participate in this Hackathon. Something that became apparent from the start was that in our group, we had all the necessary tooling and knowledge to actual participate and compete in this event. We had, by profession: Data Scientist Data Engineer/Architect Software Engineers Each person had their respective role and did their part to contribute to the project. What we Learned/Challenges One of the biggest things to overcome initially was the data challenge itself. Although in the Hackathon post they gave a script that could round up all the data, it was a mess. I think initially when we pulled and processed the data, it was ~2TB of data. Furthermore, the format of it was incredibly agonizing to work it. This was the first challenge and step: Figure out the data and what data is actually useful for our methodology. The methodology and data scrunching can be found below and goes into more detail there. From there, after the data set up and exploration, came the methodology itself. Again, more detail can be found below, but to highlight the idea, we wanted something that didn't take into account bias or personal feelings. We all wanted to build something that we would stand by and if push came to shove, give in-depth reasoning into why we believed in our ranking system. Documentation On our website, we have markdown files that document the methodology of the ranking system, the testing instructions, and the AWS tooling we used to build out our final project. They can be found below. Testing For a walk through of our project and testing documentation, see this link: https://ranking-ui.vercel.app/docs/testing The Methodology Journey: https://ranking-ui.vercel.app/docs/methodology AWS Tooling: https://ranking-ui.vercel.app/docs/aws-architecture <div