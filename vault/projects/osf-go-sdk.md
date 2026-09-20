---
slug: "osf-go-sdk"
url: "https://devpost.com/software/osf-go-sdk"
title: "OSF Go SDK"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 1101
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/scientific_research"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# OSF Go SDK

> OSF Go SDK is a library/wrapper for Go built on top of OSF API that enables developers to access features from the OSF API for their Go project in a more predictable and opinionated way.

[Devpost](https://devpost.com/software/osf-go-sdk) · hackathon [[Go Hack]]

## Facets

**domain** [[climate_energy]] [[developer_tools]] [[housing_homeless]] [[scientific_research]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[web_dom]]

**stack** golang, jsonapi, osf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for osf go sdk

## Body

Usage of Generics in our project Usage example The repository on GitHub Inspiration What strikes us as the most amazing thing about humans that enable us to come so far compared to other species is that we are able to distill, crystallize, and manage knowledge, especially on the most pressing issues and problems that humanity faces from time to time. From decreasing maternal mortality to almost ~40% [1], the fall of climate-related deaths to almost 99% [2], the abolishment of slavery [3], to the declining rate of global extreme poverty from 30% in 1998 to below 10% in 2021 [4], it tells us that we can admit that we still indeed have work to be done yet at the same time we can also be proud at the progress that we've made. All those progress are made possible by science (natural, social), arts, engineering and technology as the forefront of innovation to bring solutions to the human's problems, enabled and multiplied by the research done by many people working together. Contrary to what the popular culture tends to show, research is not a one-person solitary journey. It's a joint progress made by many, and is passed down from generation to generation. What we are experiencing right now from housing, food, sanitary system, internet, we are all standing on the shoulder of the giants. Unfortunately, there are several problems that are currently faced by the global science and research community, and one of the biggest is the reproducibility of research [5]. When someone wants to improve or create something, they will look for prior arts and research done by others so they do not have to start it from scratch and are able to continue the research for further improvement. So it is crucial for researchers to leave traces and make their research reproducible so that it can be used and tested by others who will continue their line of research. Alas, this aspect of reproducibility is sometimes overlooked by researchers simply because the overall scientific community and research system in general tend to incentivize more of the other things like numbers of citations, the quantity of publications, and others [6]. This made researchers less and less likely to enforce a rigorous set of research methodology from the process, data, variance, openness, research design, and other various aspects of reproducibility (Research Transparency and Openness guideline [7]) to their research, making it hard for others to test, reproduce, and continue their line of research. Just like how online code versioning platforms like GitLab and GitHub enable thousands of developers to collaborate despite timezone and place through the open source, there are institutions that try to tackle this line of research reproducibility problem, and of the most promising is the platform made by the Center for Open Science (COS) known as the Open Science Framework (OSF). OSF is a website platform that enables researchers to post details of their research from citation, data, materials, research design and analysis, to preprints and preregistrations which not only sustain a better methodology for the science and research community and allow people to conform their research to a better aspect of reproducibility but also make it easier for others to get the details of particular research and replicate it for their own research and improvement [8]. OSF has not been only becoming the home to ~500k researchers [9] with the growing rate to new ~450 users per day [10], but also have its own set of API that enable people to access their feature programmatically [11] which is already used by giants in the research communities like Zotero [12]. What it does Our team provides a Go(lang) library/wrapper for the OSF API to make it easier for Go developer who wants to use the OSF API in a more predictable way as a Go dependency in their Go project and without having to look the explanation of the OSF API docs line-by-line. How we built it One of the biggest reasons that Go is a programming language loved and used by many aside from its fast performance, first-class concurrency, and simplicity is that Go(lang) standard library is packed by features used by developers on a daily basis so that developers don't have to add too many dependencies to their projects. This is what enables us to build the go-osf library with only a few dependencies since most of the features that we need to use are already on the Go's standard library. Challenges we ran into OSF API conforms to the JSON API Spec [13]. We initially used an existing Go library for JSON API. But as we implemented more features of the OSF API, we eventually hit the wall with that library, particularly on results with pagination. We also faced incomplete documentation regarding creating new preprints. We needed to inspect the requests made when we followed the creation procedure through the Web. Accomplishments that we're proud of We finally ditched the existing library and built our own implementation for the JSON API. And we did leverage the Go Generics that was just introduced in Go v1.18. Generics actually made the implementation much simpler than we initially thought. What we learned We work as industrial software engineers so we do not keep in touch closely with the research community. Joining this particular hackathon of Go Hack broaden our knowledge and give us a chance to learn about the science and research community. The process, the state of the art, along with its problems, specifically the problem of reproducibility. This is also the first time we tried to write an API wrapper in Go and made us think from the point of view of others and aspect of the developer experience on how it will be used by other developers, which we were heavily inspired by the similar wrapper of go-github for GitHub API. Furthermore, this library project also become the perfect chance for us to try the newly introduced Generic feature that comes with Go 1.18. What's next for OSF Go SDK Our roadmap consists of implementing other endpoints from the OSF API as we can to enable people to access more of the capability that OSF has to offer through their endpoints, along with keeping it up to date with the update of the API. We are also putting the code open source and MIT License by default so anyone can raise an issue or Pull Request to the repository. [1] https://www.who.int/news-room/fact-sheets/detail/maternal-mortality [2] https://www.humanprogress.org/the-collapse-of-climate-related-deaths-2/ [3] https://harvardlawreview.org/2013/05/human-rights-and-history/ [4] https://www.freethink.com/culture/reasons-for-optimism-2022 [5] https://www.vox.com/2016/7/14/12016710/science-challeges-research-funding-peer-review-process [6] https://www.vox.com/future-perfect/21504366/science-replication-crisis-peer-review-statistics [7] https://www.vox.com/2015/6/27/8854105/new-science-guidelines [8] https://www.cos.io/initiatives/top-guidelines [9] https://www.cos.io/blog/osf-on-track-to-reach-half-a-million-users-by-midyear-2022 [10] https://www.cos.io/blog/continued-growth-in-osf-usage [11] https://developer.osf.io/# [12] https://github.com/zotero/translators/blob/ba3cec3ff790f8017dac3e26582ad015000e15dd/OSF%20Preprints.js [13] https://jsonapi.org/format/1.0/ <div