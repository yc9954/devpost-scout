---
slug: "enterprise-architecture-manager-for-compass"
url: "https://devpost.com/software/enterprise-architecture-manager-for-compass"
title: "Enterprise Architecture Manager for Compass"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 892
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Enterprise Architecture Manager for Compass

> Turn Compass into an indispensable tool for Enterprise Architects! Answer questions like: "Is this application fit for its purposes?" and "Is our business well-supported by our current applications?"

[Devpost](https://devpost.com/software/enterprise-architecture-manager-for-compass) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]

**stack** compass, forge, graphql, javascript, svelte, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for enterprise architecture manager for compass

## Body

Inspiration Since our lead architect saw a demo of Compass at Team ’22, we’ve been Compass obsessed and started using it the same month. Even though we realized pretty quickly that we, as a five person team, aren’t the target demographic, we loved it and started documenting our software architecture in it. Doing so was a) a delight and b) extremely informative because we realized our architecture was much bigger than we had thought. Even though Polymetis Apps is a small team, we all have experience working in large, growing organizations. We found that, as organizations grow, the way architects think about architecture also expands. There are more questions being asked of architects. Having a dedicated tool, rooted in engineering, that can answer those questions would be amazing! What it does Enterprise Architecture Manager enables you to group your Applications into Business Capabilities. A Business Capability encompasses a function that a business might be able to carry out and lists all IT applications required to execute that function. Adding a layer of Business Capabilities allows architects to answer novel and different questions about the general software landscape. For example: Is application X a good fit for its purposes? How widely is application Y used? Which areas of our business would be affected by replacing or sunsetting application Z? While Compass components can show an architect what exists today, they cannot answer questions like “Why do we need this?” or “What does this application allow us to do exactly?”. With Enterprise Architecture Manager, we record how well an application is suited for a Business Capability. Since Compass components can be generated from code, an architect using Enterprise Architecture Manager can be reasonably sure that application-level data and below are sound and up-to-date. This minimises the data quality issue that you typically encounter with completely detached enterprise architecture tooling. Of course, we all want to avoid the trap of becoming an “Architecture Astronaut”, so we decided that the Business Capability layer should not stay simply within Compass. We, therefore, made Enterprise Architecture Manager a cross-tool application and included Confluence macros to allow users to put always up-to-date reports into Confluence documents – where a broad set of users can see them. How we built it As by the codegeist rules, this was going to be a Forge app. And of course, we had built Forge apps before, but this year we wanted to do something different. So instead of rushing to build yet another label app, we wanted to push ourselves in true hackathon style. What did we want to exist and how much can we bend current technologies to make it happen? So, we started with a customUI application template for Compass but threw out the React-based UI in favor of a Svelte-based one. Much to our surprise and delight, using @forge/bridge just worked right from the start. We later added the Confluence macros, as we found during internal testing that users would screenshot a report and paste it into Confluence. With macros, there's no need for that anymore and data in Confluence is always up-to-date. Challenges we ran into The biggest challenges for us were learning GraphQL and cross-product sharing of data. Especially the GraphQL Compass API was a challenge, as not only Compass features are supported by ready-made functions in the API, so we had to figure out how to call the GraphQL API directly to get information about application scorecards. Accomplishments that we're proud of Being able to build cross-tool applications in Forge is a fantastic feature, but unfortunately, it is still in its infancy. Having Confluence macros that show live data from Compass is something we are quite proud of, as it is both: ground-breaking (for us) and really useful for users of this app. What we learned GraphQL – as mentioned above that was quite a challenge for a team that has been so focused on REST before. On a more technical level, we had expected that building an app with Svelte instead of React in the frontend would lead to all sorts of difficulties. Instead, however, this has been one of the best Developer Experience we had in the ecosystem in quite a long time. The combination of Svelte, vite and forge/bridge and forge tunnel worked seamlessly from day one and allowed us incredible productivity gains by shortening our dev loop substantially. What's next for Enterprise Architecture Manager for Compass For now, EAM for Compass will stay an internal pet project. Since Compass itself is still in beta, there is no way (yet) to turn it into a real product. However, we will keep watching Compass and hope it soon grows into a live product with an app Marketplace. Feature-wise, there is still a lot to build. On our shortlist are more visualisations of the various capabilities, their application components, and dependencies, as well as filtering options. We would like for EA Manager to be able to produce answers to questions like: If we need to sun-set X which applications and capabilities will be affected? Which area of our business deals with PII data? Especially with Compass' custom fields, we could add more information about the application lifecycle, operating costs, etc. Given that Compass also knows about the corresponding repository of an application, we would also love to show lists of dependencies and/or their respective licenses. <div