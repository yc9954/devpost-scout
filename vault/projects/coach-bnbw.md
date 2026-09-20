---
slug: "coach-bnbw"
url: "https://devpost.com/software/coach-bnbw"
title: "Coach BNBW"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 1079
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/developer"
  - "substrate/code_repository"
---

# Coach BNBW

> Avoid psychological burnout by analyzing developer's behaviour based on their commits. Powered by AI

[Devpost](https://devpost.com/software/coach-bnbw) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**domain** [[developer_tools]] [[mental_health]] [[scientific_research]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** git, gitlab, ollama, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coach bnbw

## Body

Inspiration Plamen and Angel are colleagues, both in the SRE department of their company. They both started when there was a migration ongoing within the company, and that migration proved to be quite a big task to undertake for such a small team. Some of their colleagues were facing a lot of stress, because they were working extra hours, working through a huge backlog, getting frustrated when things didn't turn out in time and so on. This worried both of them, so they started talking with their manager to get an idea how they could tackle this issue. Together with their manager, they implemented strategies such as workload distribution, setting realistic timelines, and introducing regular check-ins to gauge the team's well-being. This really boosted the team's productivity and lowered their stress levels. Coach BNBW is the embodiment of their experience. A way for developers to have a guard rail, a coach for then to keep them nice and well. What it does Coach BNBW analyses the user's git commits. It takes the messages and the timestamps and performs analysis by running the information through a few formulas created to measure the behavior of the developer, these being: Sentimental analysis of the commit messages Repetitiveness of the commit messages Velocity of the messages (how quickly new commits are pushed) Within or outside of working hours These analysis produce results that have specific info tied to them. The results are then passed on to an AI to give out a comprehensive assessment of the developer's antics. If the results show that he's performing well, Coach gives him encouragement, if he's performing unwell, i.e., he's overworking himself, Coach gives him a suggestion or a reminder for him to take a break or relax a bit and call it a night. How we built it Coach BNBW was built with Python 3.10. It utilizes a Ollama instance for anything AI related. There are snippets in the code like this where you can see what role the AI plays in the code. def prompt_gen(s: str) -> str: """ Generate a prompt for sentiment analysis. Args: s (str): The input sentence for sentiment analysis. Returns: str: A formatted prompt for the Ollama service. """ return """ Give me a sentiment analysis of the following sentence, ONLY output the result with options: "Negative", "Positive" or "Neutral", nothing else no explanations, no comments, nothing more, return it in a md formatted json as a list of objects like {"result":result} Have in mind that this is a commit message in git, so whenever you have curse words count it as a negative, otherwise consider mostly the level of respectfulness, dont mistake for negative things that are neutral, your threshold of negative should be high except for when curse words are used. --- """+s Challenges we ran into The first challenge that we ran into was figuring out what formulas we were going to do performance measuring. What were the thresholds we were going to implement, what part of the information we were going to use in what way? We went out and did our research, read a few research papers on best practices with dealing with stress for programmers, and of course, drew from our own personal experience. The second challenge that we ran into was a design flaw. Before implementing the AI into the program, we used libraries for sentiment analysis, but we found out they were not really that accurate when it came to sentiment analysis. We had to figure out what we were going to do, so we stopped at AI. It performed pretty consistently and close to our expectations, so we decided to go with it. * The third challenge that we faced was the unexpected workload that we had to face. Creating a project from scratch and using your creativity to develop something unique is a very different experience than our daily work lives. We've both created projects for fun, but never for a hackaton, where you essentially have a deadline pushing you for a passion project. The final challenge we faced is the presentation. We are very confident in the viability of our product - it works as intended and we have tested it with some of our colleagues and have received positive feedback, but it's one thing when you're presenting it to people you know and you work with, and another when you're presenting it to a hackaton. It took us some time to built something good looking, but we did manage to do it in the end! It is certainly a part of development that you usually don't run into frequently. Accomplishments that we're proud of This whole project is an accomplishment that we're proud of. It was hard, it took time, persistence, and maybe even a tad bit disregarding the advice from the Coach, but we created this whole project from scratch. We're proud of the way that we integrated AI into the project, we're proud of the feedback we received from the people that tested it. It does look like a simple project, but the simplicity is what makes it viable. There isn't a lot of psychological wellness software out there aimed at developers. What we learned We learned how to do test driven development, how to create an API and create authentication related to the API, how to make something presentable as a product. We learned about best practices related to development when it comes to psychological well being. And we learned some niche commands for git as well. We learned from our experiences and are more than equipped for our next hackaton! We came out with really pleasant experiences from the whole experience! What's next for Coach BNBW A lot. This is our 0.1 release, and we plan a lot more features in the future for our Coach. We plan to allow people to use their own Ollama instances, add a graphical representation of the results, we even might add a GUI. We also want to add persistence - we want users of Coach BNBW to be able to track their own profile, so we can enable them to see how they are progressing, maybe even implement or develop a formula that can predict a burnout! But yeah, we do plan to expand Coach BNBW with some more customizable features as well. We completely understand that everybody has their own personality, so we plan to make the Coach adapt to the habits of the developer. <div