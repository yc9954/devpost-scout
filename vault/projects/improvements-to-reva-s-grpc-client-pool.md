---
slug: "improvements-to-reva-s-grpc-client-pool"
url: "https://devpost.com/software/improvements-to-reva-s-grpc-client-pool"
title: "Improvements to Reva's gRPC client `pool`"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 510
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Improvements to Reva's gRPC client `pool`

> This project aims to improve the client `pool` of Reva's gRPC client by reducing the technical debt, using design patterns and adding security configurations with necessary documentation.

[Devpost](https://devpost.com/software/improvements-to-reva-s-grpc-client-pool) · hackathon [[Go Hack]]

## Facets


**stack** go, grpc

## How they structured the write-up

- improvements to reva's grpc client pool

## Body

CERN Collaboration Track: Reva Project - Go Hack, 2022 Improvements to Reva's gRPC client pool About Me Name: Amal Santosh Thundiyil GitHub: @amal-thundiyil LinkedIn: @amal-thundiyil Gitter: @amal-thundiyil Contributions Use functional options for client gRPC connections - #2801 Make grpc.MaxCallRecvMsgSize call option configurable - #2872 Make hard-coded HTTP "insecure" options configurable - #2775 Enable TLS for gRPC connections - #2791 Add cato tag for Insecure configuration - #2873 Others: RFC3339 as layout for parsing time - #2744 Bump copyright date to 2022 - #2846 Draft: Update linters - #2770 Description This project aims to improve the client pool of Reva's gRPC client by reducing the technical debt, using design patterns and adding security configurations with necessary documentation. Technical Debt: Previously making changes such as adding options or customizations to the gRPC client pool meant passing primitive arguments from the all the references where the gRPC client was being called from which resulted in an unnecessarily large diff. With the changes in this project, adding any new configuration will result in a very small and easy to review diff thus decreasing the technical debt. Design Pattern: The client pool was refactored to make use of functional options pattern. This makes the code more explicit and extensible. With this pattern the order of arguments don't matter allowing for flexibility and ease of testing which is certainly an improvement. Security: Security problems of the kind where Reva made use of insecure connections (HTTP and gRPC) in many places were also addressed in this project. To address this I added a configuration for using insecure connection which defaults to false . For gRPC, I added security configurations to enable and use TLS for secure endpoints with user configuration for using TLS certificates instead of setting up a proxy to use Reva with secure endpoints. I also added a Makefile recipe to generate local certificates for testing and development. Configuration: Now any user will have the option of setting insecure , skip_verify and other new security configuration values in the shared table. Example: [shared] insecure = true # other configuration The user can also set the same new configurations for the individual interceptors, services etc. This kind of configuration will have a greater precedence over the previous type of configuration. Example: [grpc.services.authregistry] insecure = true # other configuration Documentation: The documentation for the new configurations is added using cato . Related Links to Issues: How to run revad with TLS enabled - #1962 Some "insecure" options are hardcoded to true - #2216 Use colon : for timezone layout when parsing dates - #2322 Conclusion I would really like to thank the Go Team for maintaining such a helpful community of coders and the CERN team at Reva for taking the time out for reviewing my code and suggesting relevant and useful code changes. Looking forward, I plan to continue my contributions to the Reva project and other related repositories (ownCloud, CERNBox) to forward the grander vision of the project and also help new contributors and users get started on using and contributing to the project. <div