---
slug: "page-classifier"
url: "https://devpost.com/software/page-classifier"
title: "Page Classifier"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 698
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Page Classifier

> Use AI to automatically categorize pages in your Confluence space and create relevant content labels.

[Devpost](https://devpost.com/software/page-classifier) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** custom-ui, forge, google, google-cloud, javascript, love, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for page classifier

## Body

Inspiration I should probably say that I've built something I needed myself. To be honest, I've never felt this need. But as the idea came up, I told myself: I don't care that I don't need it, I want to play with it and have it in my Confluence! I am a software developer and Cloud enthusiast. It started with Atlassian Connect, which was my first real experience with Cloud. This little avocation soon expanded to many other fields and technologies. Nonetheless, working on Atlassian apps gives me a feeling of home. The topic of my app was clear: let's combine some technologies I love and create something powerful out of them... Or if it won't be powerful, it can be funny... And if it won't be funny but only bad, let's at least learn something new! In my case, the idea was clear: let's mix Confluence, Forge, React, Artificial Intelligence, and polish it with some childish animations, which is my specialty. I love the fact that Artificial Intelligence is now accessible for everyone. I find it very exciting to see that we don't have to build our own models and be AI professionals. Basic engineering knowledge is enough to use existing models. And they are already very powerful! What it does It provides hooks that respond to page created and page updated events. When such an event occurs, the page content is automatically analyzed and categorized. The page receives some properties (in this version, there is a limit of 30 keywords). These properties contain some text highlights. Moreover, the page receives content labels that represent the main text topics. This can be utilized in many ways, I demonstrate it using a content action module that allows comparing the page to other pages in the same space. Additionally, there is a Confluence space page module that allows filtering of pages in the space based on their categories. How we built it I love React. Therefore, in terms of technology, the choice was not that difficult. I also like fiddling around in Cloud and trying out interesting APIs. So once I had more or less the idea, I considered different options and tried to find the best match between what Forge allows and what Cloud offers. During the development, new and new challenges were constantly coming, but I did not hit any 'showstopper'. Whenever I wanted to cry, I was making CSS animations, that’s why you can find that many of them in the app. Challenges we ran into Most of the problems were either caused by scopes (because of which I could not use the whole potential of the Confluence REST API) or by Forge resolver limits. I had to separate all the tasks into as small units as possible and parallelize some jobs (e.g., simultaneously prepare both properties and labels). It would be also awesome, if it was possible to create indexed properties in Forge. It was difficult to find a solution, that effectively replaces this feature. Accomplishments that we're proud of I am proud that I was able to turn a small idea and huge amount of enthusiasm into something ‘real’. What we learned I've learned a lot about Forge and about FaaS in general. It's exciting to see how powerful this technology is. What's next for Page Classifier Independently on the Codegeist result, the Page Classifier is already too deep in my heart to let it die. It will be either listed on the Atlassian Marketplace or the source code will be published for everyone. In terms of features, there are many ideas and possibilities. Indexed content properties, currently not supported in Forge, would open many possibilities for how we can utilize all the data we have. Property value compression or usage of more properties to represent highlights. I ran into a property size limit, which prevented me from storing all page highlights the classifier finds. This could be partially solvable by splitting the result into multiple properties. Vision API and attachment analysis. Google provides an API that classifies pictures/photos, this could be utilized to categorize page attachments. Google Charts to create some fancy statistics based on content labels we have. And much more! <div