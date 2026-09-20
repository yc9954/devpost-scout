---
slug: "civo-x-pyroscope"
url: "https://devpost.com/software/civo-x-pyroscope"
title: "Civo x Pyroscope Continuous Profiling"
hackathon: "Civo Hackathon 2021"
organization: "Civo"
winner: true
words: 708
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Civo x Pyroscope Continuous Profiling

> Writing code without using a profiler is like driving a car with no dashboard. Civo x Pyroscope allows you to see an interactive performance profile for each PR that you create!

[Devpost](https://devpost.com/software/civo-x-pyroscope) · hackathon [[Civo Hackathon 2021]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]] [[transportation]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[video_visual]]

**stack** pyroscope, ruby, ruby-on-rails

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for civo x pyroscope

## Body

Inspiration My cousin and I decided to enter this hackathon because both of us wanted to learn more about Kubernetes. Although I've been coding for several years now, the jobs that I've had have been either ruby/rails or python/django so I haven't used Kubernetes very extensively in a professional context. My cousin joined me last week at Rubyconf in Denver and so we wanted to find a way to bring the power of Kubernetes to the world of Ruby! We used the abalone project which is part of Ruby's "rubyforgood" organization and was used in a workshop on performance by Jade Dickinson at Rubyconf last week. With that being said, I've also been working on open source performance monitoring tooling for about a year now so I thought it would be a good exercise in combining everything together! What it does This project does two things: It allows you to preview your application before the PR gets accepted into the main branch It allows you to understand the performance impact of the current commit vs previous commits using continuous profiling What this project does is allow for you to profile your test suite and use an open-source continuous profiling tool called Pyroscope to inspect the profiles over time and understand which parts of your application are consuming the most resources. We also added the ability to tag profiles based off commit and commit author for easier/further analysis (especially in the profile diff view) How we built it We build this using Github actions fairly extensively. When someone creates a PR the following steps happen: Checks out the repo Creates a docker image with a tag for the particular commit Deploys kubernetes manifests which contain pods for webserver, tests, and pyroscope Creates ingress to access webserver (to view the staged changes before merging) Creates ingress to access pyroscope server (to view profiles of webserver / tests before merging) Posts a comment to the PR with a link to the webserver / pyroscope server Challenges we ran into One of the biggest challenges here is that debugging github actions was extremely difficult. Especially when we are trying to create something that fits into the workflow we have to go through that entire workflow ourselves to test that it is functioning correctly. Another issue is that with neither of us being experts in kubernetes there was a lot of trial and error to get things like ingresses to work the way we wanted them to. It seems as though a lot of kubernetes examples and documentation have quickly become outdated so we found ourselves in situations where we were trying to make old code work instead of using the new code. Accomplishments that we're proud of I ultimately learned a lot about how to effectively debug kuberenetes issues and William became an expert on Git (and is going to make his first open source contribution soon!) What we learned In trying to follow some tutorials that are purely for kuberentes, we started to understand how much simpler Civo made the process. We spent a good couple of hours trying to understand all TEN of the files needed to create an application with an ingress from this article: https://medium.com/kubernetes-tutorials/deploying-traefik-as-ingress-controller-for-your-kubernetes-cluster-b03a0672ae0c Only to eventually realize that 80% of it was necessary because Civo has abstracted / simplified much of that. All we needed was two file for the Ingresses and it worked great! What's next for Civo x Pyroscope There's a couple of additions we'd like to add here, but didn't have time: Create a plugin in the https://github.com/civo/kubernetes-marketplace to simplify adding a Pyroscope server to Civo — Going to be Williams first open source contribution! Publish our Github action: This will allow people to create this staging server + profiler combination as long as they've set up a Kubernetes cluster with Civo Add a load testing tool (i.e. K6). The impact of performance issues in flamegraphs become more apparent as the server is under heavier load. It would be cool to add a service that sends fake traffic (or mocks of real traffic) to make the profiles more realistic The web app is a little slow right now so sometimes the link to that will break (ran out of time to fix) <div