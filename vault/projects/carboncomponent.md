---
slug: "carboncomponent"
url: "https://devpost.com/software/carboncomponent"
title: "CarbonComponent"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 1161
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# CarbonComponent

> Use this CI/CD component to track and even offset the carbon emissions for requests made to your website for different usage scenarios. Show the world you use green web hosting with a snazzy badge!

[Devpost](https://devpost.com/software/carboncomponent) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** chrome, docker, git, gitlab, lighthouse, python, thegreenwebfoundation

## How they structured the write-up

- inspiration
- what it does
- green webhost badge
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carboncomponent

## Body

Inspiration Tracking the carbon emissions of requests to your web app or project as part of your CI/CD pipeline is crucial for promoting sustainability in software development. As the digital landscape expands, the environmental impact of internet usage grows significantly. By integrating carbon emission tracking into the CI/CD pipeline, developers can gain real-time insights into the environmental footprint of their applications. This awareness enables them to optimize code and infrastructure to minimize energy consumption and carbon emissions, contributing to a more eco-friendly digital ecosystem. Moreover, it aligns with corporate social responsibility initiatives and helps organizations meet their sustainability goals while fostering a culture of environmental consciousness within the tech industry. CarbonComponent is a free CI/CD component you can drop into your GitLab CI/CD pipeline and immediately get insights about your project. You also get access to an exclusive Green Webhost badge that lets you proudly show your website or app runs on renewable energy, which encourages other teams to also begin tracking their project's emissions. What it does CarbonComponent is CI/CD component for keeping track of the emissions per request made to your website or webapp! This component will give you a detailed report on each run and metrics on merge requests so you can keep tabs on if deploying your latest update will release more or less carbon into the atmosphere. This component also gives you access to a Green Webhost badge which you can use to display that your project is hosted by a web host that uses fossil-fuel free energy. Data about web hosts is provided by the Green Web Foundation's dataset . Finally, this component also lets you offset your website's emissions. In each CarbonComponent report, a link to Wren is generated allowing you to offset a given number of requests to your website using a carbon sequestration project of your choosing ! Green Webhost Badge The Green Webhost Badge is an artifact from running the Carbon Component that you can use to proudly show your website is hosted using renewable energy. It looks like this: It will also appear red, with a "False" if your web host changes their energy mix. You can embed it in your README like so: ![Green Webhost](https://gitlab.com/api/v4/projects/<YOURPROJECTID>/jobs/artifacts/<BRANCH>/raw/badge.svg?job=carboncomponent) where the project ID can be found in "General Settings" for your repo (or by following these steps ) and the branch is your branch of choice. How we built it This CI/CD component uses our modernized fork of Carbon Calculator , which in turn uses Lighthouse and Python to implement the algorithm used by the popular Website Carbon Calculator . Our container hosts a Chromium browser which allows us to use Lighthouse and the Greenhouse plugin to characterize data transfer over the wire, the energy intensity of the website's data, and using information from the Green Web Foundation's webhost dataset the energy source used by the data centers for returned URLs to determine the carbon intensity of electricity used to respond to a request to the target website. It also will check carbon.txt, if available, and use that data in lieu of the data from the dataset. We referenced GitLab's existing examples for CI/CD components and their documentation to make sure we were using best practices. In particular we found the Container Scanning and Secret Detection repos useful in learning how to craft a GitLab component. They showed how to craft our component template and how to write a complete README so it was easy for users to integrate our project. Challenges we ran into As my first GitLab container repository and CI/CD component project, I had a learning curve to publish my container and define how the component works. The documentation and examples were extremely valuable in this effort, as well as third-party tutorials . Characterizing emissions of a web request is more difficult than it sounds. There are many variables to consider, such as how to account for cached assets (which of course won't be re-transmitted and shouldn't penalize the webpage), the carbon emissions based on the energy mix of the web host, how much energy is used in transmission versus by the server, and how exactly do we know the energy mix of the web host. There is not one answer for how energy intensive sending a byte actually is. You can see how these are estimated, weighted, and quantified here , using values from the Green Web Foundation and the Website Carbon Calculator. Lighthouse provided the raw information about bytes transmitted and their types and The Green Web Foundation's dataset let us quickly answer the hardest question we had to answer- does the web host use renewables? The Green Web Foundation has thorough criteria for determining and verifying a web host is green, and frequently updates their dataset as the hosting landscape changes. We believe the combination of these tools provides the most accurate insight into the environmental impact of a web project currently available for one's CI/CD pipeline. Accomplishments that we're proud of Originally the ability offset emissions right from your GitLab pipeline was a stretch goal, so I am proud that this functionality made it into our first release. I am also proud of the thoroughness of our output reports, that we are able to include these metrics in pull requests, and that we were able to accomplish this without burdening a user with a number of complicated inputs. The goal was always to allow a user to simply point our component at a URL and get insights right away, which we accomplished. I am also proud that the component runs quickly and that we were able to optimize the container so that it is as close to lightweight as it needs to be to simply accomplish the carbon estimation task. Finally, I'm proud of our component page on the CI/CD catalog as it provides a thorough description of how to add the component to your pipeline and interpret the results. What we learned More webhosts than we thought are green! This includes, happily, GitLab. We learned how GitLab components work, how to build them, and how to publish them. I learned a great deal about how to characterize a web request in size using automated tools. I made my first GitLab CI/CD pipeline and published my first container to GitLab's container registry. I also learned how powerful badges can be in creating viral tools in the Git ecosystem, which I hope encourages more people to use our component as more users include Green Webhost buttons in their READMEs. What's next for CarbonComponent Additional flexibility in user scenarios as well as the ability to offset running the CarbonComponent container's emissions after running it are on the roadmap for the future. In the long term, being able to highlight for developers which requests are the worst offenders in terms of energy usage will be valuable. Integrating Wren's API would allow users to configure their GitLab pipeline to automatically offset emissions when they merge to production, for example. <div