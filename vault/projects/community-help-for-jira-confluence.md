---
slug: "community-help-for-jira-confluence"
url: "https://devpost.com/software/community-help-for-jira-confluence"
title: "Community Help for Jira & Confluence"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1007
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Community Help for Jira & Confluence

> Enable users & admins to be able to get the help they need, by searching the Atlassian Online Community directly from the products they are using.

[Devpost](https://devpost.com/software/community-help-for-jira-confluence) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** atlassian, bitbucket, confluence, forge, jira, khoros, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for community help for jira & confluence

## Body

Confluence Content "more actions" menu option. Main dialog with link to Online Community. Example input for searching. Search results page with hyper links to article on the Atlassian Online Community. Jira Issue "more actions" menu option. Main dialog with link to Online Community. Example input for searching. Search results page with hyper links to article on the Atlassian Online Community. Project Kickoff Jira Roadmap view. Project Kickoff Jira Sprint Backlog. Project Kickoff BitBucket Repositories. Project Kickoff BitBucket Skeleton. Week 1 - Jira Roadmap progress Week 1 - Jira Velocity Report Week 1 - Jira Sprint Burndown Week 1 - Jira Software Insights Week 1 - ButBucket App code changes Week 1 - BitBucket Pipelines YAML Week 1 - BitBucket Pipeline build results Week 1 - App Menu Option Progress Week 1 - App Main Dialog progress Week 2 - App Main Dialog Progress Week 2 - App Search Results Progress Week 2 - Midnight inspiration - Include "Search Snippet" to make articles more relevant. Get Community Help for Jira - App Icon Get Community Help for Confluence - App Icon Inspiration This started from me wanting redemption from not making a submission for Codegeist 2020. When I heard from Bridget on the Atlassian Community team that Codegeist was returning for 2021, I knew I wanted to actually make a submission this time. While walking the dogs in the morning, I was thinking about what business challenge or need I could solve, and it hit me. One of the most powerful resources Admins and End users have at their disposal is the Atlassian Online Community. There are tons of people asking and answering questions every day. "What if I could write an app that would bring the Online Community closer to the tools people are already using?" After a brief conversation with one of the Community managers to see if there were public APIs I could access (which there are), I had my idea! I also summarized this in an intro video I posted on youtube for this project: link What it does What I have created is a "more actions" menu option from either a Jira issue, or a Confluence page that will display a modal dialog box. From here you can input a search term for an issue you are having and click a search button to have it return the top 25 results from the Atlassian Community, with a short snippet from each article relevant to your search. The article titles are hyperlinked so you can go to the article on the Community to read more. How we built it I started by following the Atlassian Forge UI kit templates. Once I had a skeleton template I made heavy use of the Atlassian Forge resource guide to find the visual elements I wanted to use. From there build the app was about putting the pieces in place until I was happy with them. As for the API call itself. This took a bit of investigation as I needed to use a generic node "fetch" since I wasn't accessing information form one of the Atlassian products. Challenges we ran into I ran into a number of challenges throughout this process. From the beginning, I had it in my head that I wanted a top level menu, not a "more actions" menu. But, I discovered through the developer community that top level menus are not yet supported in Forge. Also, when I was using the node "fetch" api command. I ran into permissions issues that aren't very well documented. This took a significant amount of trial and error before I was able to figure out not only the permissions I needed to grant but also where I needed to define this. The last challenge I had was that I would have liked to generate a dynamic list of tags to include in the search instead of the static list I ended up using. However, I don't have access to the APIs that would allow me to search for and generate a checkbox list of tags. Accomplishments that we're proud of The most important accomplishment for me is actually finishing and submitting this time. I'm also really happy with the end product. It isn't very flashy, but I think it will be something very useful. I was also really proud that even though I had a full time job and other life commitments, I still managed to stay relatively on track while completing this project. What we learned I learned SO MANY things! First, I got to dive into the Khoros platform APIs (this is the product powering the Atlassian Online Community). While one of the Atlassian Community Developers posted a nice article about some simple search api calls you can make, my deep dive helped me discover that "search snippets" are something the platform supports. Up until now I have dabbled a bit with Atlassian Forge for work, but my setup is on a MAC. My home computer is on windows, so I needed to re-learn how to setup my forge development environment. My previous experience with BitBucket is using the server version as well as Bamboo. So it was also really cool to have the opportunity to experiment with YAML build files and BitBucket Pipelines. What's next for Community Help for Jira & Confluence First, I will be writing an article on the Atlassian Community to share my experiences with Codegeist 2021 and the app I developed. I'm part way through submitting it as a free app in the marketplace, and as long as it doesn't get rejected in a way that will cause me too much effort to resolve, this will likely be available for free to anyone that would like to have easier access to the Atlassian Online Community. I also included/posted a "final thoughts" video on youtube documenting how I felt about this wonderful process: link Finally, I also took this entire experience and summarized it in an article on the Atlassian Community, titled: How I Accidently Became a Marketplace Vendor link <div