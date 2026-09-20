---
slug: "learning-assistant-xek9b3"
url: "https://devpost.com/software/learning-assistant-xek9b3"
title: "Learning Assistant"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 1035
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Learning Assistant

> Learning Assistant is a Postman based tool that will help you keep improving as a software engineer, no matter the field you specialize in or your degree of expertise.

[Devpost](https://devpost.com/software/learning-assistant-xek9b3) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[video_visual]]

**stack** dev.to, docker, github, javascript, postman, slack, youtube

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for learning assistant

## Body

Working example Inspiration I decided to create this project because - as a quality engineer - I believe in continuous improvement , not only applied to a project or a product but also to people . There are a lot of passionate software engineers around the world that want to improve the quality of their projects, the way they work in their teams and the value they deliver to the company they work at. In order to accomplish this, we need to keep learning about different topics every day. There are two ways of learning: By own experience. For instance, practicing. By the experience of others - which means reading, studying, investigating... When we learn by the experience of others, we consume resources . We read articles, tutorials, we hear podcasts, we watch talks, etc. We usually find these kind of resources by ourselves, but what if we had someone or something that collected this resources for us based on our interests? This is when Learning Assistant comes into play . What it does Learning Assistant is a Postman based tool that will help you keep improving as a software engineer, no matter the field you specialize in or your degree of expertise. By just providing the areas you're interested on, Learning Assistant will recommend periodically a set of resources for you, your friends or your team to get up to date with the current state of art in software development. This set of resources consists on: A Github repository. A Docker image. An article from Dev.to . A talk streamed in Youtube . A course from Udemy . How I built it I built it using entirely the Postman ecosystem, there are no external tools apart from the APIs that Learning Assistant consumes in order to fetch the resources. To sum up, it consists of a Postman collection with chained and scripted requests that gather the information from all these sites where the resources belong to and dumps it on a Slack channel . A Postman monitor runs this collection periodically so that you get your information of interest whenever you want . It can be every day, every Friday, once a month... Your Learning Assistant, your rules. Of course, a different set of resources will be dump each time the Postman monitor is run. You can read the full description in the Learning Assistant public workspace Challenges I ran into I found some challenges during the process: The first one was choosing the sources of information and checking that they provided good API integrations . Then, I found that the algorithm I used to retrieve random resources from all of these sites was not valid in case of Dev.to and Youtube , because these APIs don't provide the required information for the algorithm to work properly. Instead, I decided to retrieve items sequentially from these two sites. Considering how the algorithm used when retrieving resources from Dev.to and Youtube works, I needed to persist some information in the Postman environment used by the collection. It worked when I ran the collection using the Collection Runner but failed when running this collection with a Postman monitor. This is because monitors don't persist the environment information from one run to another . I decided to retrieve and persist this environment information using a couple of endpoints provided by the Postman API at the beggining and the end of the collection, this way the environment information was persisted successfully from one monitor run to another. Finally, they way used to extract the ID of the active Postman environment from the scripts didn't work properly when running the collection in a Postman monitor, because the UID structure of this environment is different depending on whether you access it from your Postman IDE or a monitor. To solve this issue, I decided to create an auxiliary collection to let the user get the environment UID before setting up the monitor. The user only needs to get this UID once and it is not updated in the monitor run so I thought it was a good workaround. Accomplishments that I am proud of I'm proud of: Managing to develop a tool that I'm sure it will help people to achieve their goals in software development. The tool design , considering I wanted to implement it entirely on the Postman ecosystem. The code itself, it was my very first experience ever working with Javascript. I'm sure it could be better of course, but I think it was a good starting point (mostly keeping in mind that the Postman sandbox does not provide the best flexibility for OOP, since it is oriented to scripting). Finally, I'm proud of doing all this in just a week , working on it after work. It was the greatest handicap. What I learned I learnt how to prioritize design decisions among others in a short time. Also, I learnt better how the Oauth 2.0 protocol works when authenticating on thirdparty APIs. I feel I've started to get confident working with Javascript. In a nutshell, this was a chance for me to keep improving my coding skills , given I'm not a full time developer, and I feel it was a great training for me. What's next for Learning Assistant I would like to engage the community to improve this tool, because I think it can provide value to both single developers and also teams. These are the next improvements I have in mind: Currently, all requests retrieve resources dynamically and randomnly from related APIs except the Dev.to and Youtube ones, which retrieve resources sequentially by following an order because of the way these APIs are built. It would be greate to find a way so that these resources are retrieved dynamically and randomly too. To implement a solution to dump the collected resources to an email address apart from Slack (for example, by using Gmail API), just in case the user does not have Slack or prefers this method. Add new articles sources like Medium (by using Medium API) or personal blogs. Add a way to also recommend Postman public workspaces. Improve the recommendation algorithm so that it delivers most relevant resources more frequently. <div