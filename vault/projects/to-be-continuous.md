---
slug: "to-be-continuous"
url: "https://devpost.com/software/to-be-continuous"
title: "to be continuous"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 1031
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/video_visual"
---

# to be continuous

> "to be continuous" is an open-source project defined by opinionated principles, offering a collection of GitLab CI templates crafted by DevSecOps experts to construct cutting-edge CI/CD pipelines.

[Devpost](https://devpost.com/software/to-be-continuous) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[video_visual]]

**stack** bash, cicdcatalog, component, gitlab-ci.yml, pages

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we've learned
- what's next for to-be-continuous

## Body

TBC in GitLab's CI/CD Catalog: 45 components TBC's opinions: differentiated CI/CD pipeline behavior TBC's opinions: the adaptive pipeline behavior TBC's composability in action: a pipeline made of 5 templates Inspiration Orange's journey with GitLab CI began in 2017, captivated by the platform's architecture – a perfect blend of simplicity and versatility such as 1 job for 1 container, no API to implement, no nightmare upgrading the product and its plugins, decoupling of runners, etc. The decision to transition from Jenkins to GitLab CI was immediate and transformative. Over two years of dedicated practice, we've cultivated expertise, enabling the sharing of GitLab CI knowledge and code snippets within the community. In January 2019, the introduction of the "include" feature in the Community Edition marked a turning point. It allowed us to transcend mere code-sharing, enabling the creation and sharing of ready-to-use templates. During these two years, we not only developed templates but meticulously polished them, enhancing our GitLab CI expertise. Our journey also involved progress in our semantic representation of what a pipeline should be, understanding the nature of tasks, and delving into the profound differences between CI and CD, as well as Git workflows. What it does "to be continuous" is more than a collection of GitLab CI templates; it's a comprehensive project developed and maintained by DevOps and technology experts. This initiative streamlines the creation of state-of-the-art CI/CD pipelines, encompassing tasks such as building, testing, code analysis, infrastructure management, application deployment, and acceptance testing. These templates are also accessible on Self-Managed GitLab instances through the gitlab-sync tool, ensuring your self-managed instance stays up-to-date. Similar to Maven or Gradle, "to be continuous" follows conventions (default configurations) while remaining open to customization. Users can either overload configuration variables or overwrite YAML code to tailor it to their specific needs. How we built it The project's foundation was laid in 2019, leveraging GitLab CI's "include" feature. From the outset, the templates were designed as a honeypot, attracting newbies who wanted to set up their continuous integration without spending hours on GitLab CI, natively implementing all the killer-features offered by GitLab, and facilitating the adoption of modern tools and practices. The focus was on creating a system that not only streamlined development but also acted as a catalyst for the adoption of best practices in DevSecOps, consistent workflows, and efficient CI/CD pipelines. In short, "to be continuous" modestly aims to lay the foundations for the standardization of CI/CD through semantic modeling, integrating Git workflows, environment management, the nature of tasks in a pipeline, and understanding the differences between CI and CD. Challenges we ran into While being avid supporters of GitLab products, building a DevOps pipeline from scratch demanded significant time and expertise. The constant evolution of GitLab CI and the challenge of integrating new features with each release represented recurrent burdens for projects. And finally, the most problematic point in our opinion is the lack of semantic framework provided by GitLab CI. GitLab CI is mainly a sophisticated scheduler, allowing to define technical tasks and their sequence, but GitLab CI cares little about the nature of these tasks, and does not give any clues as to the "right" way to build a DevOps pipeline. The consequence of this, is a lack of standardization from one project to another, from one company to another. This is a criticism that can be formulated against the majority of CI/CD tools today. Accomplishments that we're proud of What started as an initiative at Orange evolved into a recognized inner source project, with a community of nearly 2250 members and offering 47 templates. "to be continuous" has laid the groundwork for CI/CD standardization within Orange. Orange , like many IT companies , is a substantial consumer of opensource, sharing in return what we do well is just obvious. The logical continuation of this story was going opensource, which happened in May 2021 under the name "to be continuous". Since becoming opensource, "to be continuous" has gained widespread adoption, extending beyond Orange to include several major international companies. These organizations have embraced "to be continuous" based on its principles, finding them convincing and aligning with their needs. "to be continuous" has been recognized as a valuable solution, and these companies have successfully integrated and adapted it within their own organizational frameworks. Recently we've recently updated our templates to seamlessly integrate with components, and they are now accessible through CI/CD Catalog. "to be continuous" support both types of includes include: project: and include: component: For now, "to be continuous" has 46 templates of 6 kinds: Build & Test: Angular, Bash, dbt, GitLab Package, Go, Gradle, Maven, MkDocs, Node.js, PHP, Python, Scala/SBT, Sphinx Code Analysis: DefectDojo, Gitleaks, MobSF, SonarQube, Spectral, SQLFluff lint Packaging : Cloud Native Buildpacks, Docker, Source-to-image Infrastructure (IaC): Terraform Deploy & Run: Amazon Web Services, Ansible, Azure, Cloud Foundry, Google Cloud, Helm, Helmfile, Kubernetes, OpenShift, S3 (Simple Storage Service) Acceptance: Bruno, Cypress, Hurl, k6, Lighthouse, Playwright, Postman, Puppeteer, Robot Framework, Test SSL Misc: GNU Make, Renovate, semantic-release "to be continuous" is thoroughly documented, covering basic notions and philosophy, general usage principles, and individual documentation for each template. To facilitate a quick start, "to be continuous" provides an interactive configurator (a.k.a "kicker") that allows generating the .gitlab-ci.yml file simply by selecting the technical characteristics of your project. Additionally, "to be continuous" exposes several example projects, illustrating how to use the templates in production-like projects by combining multiple templates. What we've learned The journey from individual GitLab CI usage to a standardized framework imparted valuable insights. The importance of semantic modeling, nuances of CI/CD standardization, and the need for a more opinionated framework in the CI/CD tools landscape were key takeaways. What's next for to-be-continuous "to be continuous" aims to be a dynamic, community-driven project, responsive to emerging needs and technological advancements. The roadmap includes: AI enhanced CI/CD project configuration, share our experience with GitLab team to enhance the CI/CD catalog features, expand project visibility beyond developer profiles, continue enriching GitLab's CI/CD catalog with new templates: new languages ( Rust ...) OSS compliance ( Fossology , ORT ) SBOM management ( Dependency-Track ) DevSecOps ( Semgrep , Snyk Open Source , OWASP ZAP ...) deployment technologies ( Heroku ...), <div