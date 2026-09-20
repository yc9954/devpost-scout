---
slug: "develop-with-aws"
url: "https://devpost.com/software/develop-with-aws"
title: "Develop with AWS (Jira)"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 981
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Develop with AWS (Jira)

> You build it, you run it – integrate your AWS development toolchain with the Jira Software Open DevOps experience

[Devpost](https://devpost.com/software/develop-with-aws) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]] [[housing_homeless]]
**substrate** [[code_repository]] [[geospatial]]

**stack** amazon-eventbridge, amazon-web-services, atlassian, aws-appsync, aws-lambda, aws-step-functions, cdk, forge, graphql, jira

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for develop with aws (jira)

## Body

Develop with AWS (Jira) – pristine deployment data provider Develop with AWS (Jira) – configured AWS environments Develop with AWS (Jira) – various deployment states Develop with AWS (Jira) – issue development dialog Develop with AWS (Jira) – select data provider type and environment via tags Inspiration Ever since starting to use the Atlassian product family we have enjoyed the productivity gains implied with the ability to reference information across the various products and processes. Jira issues have been our standard unit of work accordingly, so we have been delighted to see that this core platform capability is gaining significant additional features via the new Atlassian Open DevOps experience. Given Utoolity's AWS focused app portfolio and recent innovations with the serverless and event-driven AWS offerings, we immediately realized the potential for a foundational integration with Jira that can support any applicable AWS service down the road. What it does Develop with AWS (Jira) allows you to connect your AWS environments (an account/region combination) with the Open DevOps experience provided by Jira Software Cloud. Once connected, any Jira issue keys included in the commit messages, branch names, and pull request titles of your connected Git repositories are propagated to applicable AWS resource types and lifecycle events so that these are in turn surfaced in the new Jira Software code and deployment tabs, and of course also the time-tested issue glance and development dialog. The submitted app version has dedicated support for the Jira Software build and deployment data providers for AWS CodeBuild and AWS CodePipeline. Due to timing constraints we have only rudimentary support for a source code data provider for AWS CodeCommit, though there are no conceptual hurdles for completing this. We have also experimented with a feature flags provider based on AWS AppConfig. Refer to our list of applicable AWS services and resource types for the Jira Software data provider mappings and status of the next candidate services, most notably: CloudFormation, CodeDeploy, ECS, ECR, Elastic Beanstalk, Lambda, and Step Functions To provide flexibility for the not always clear-cut mapping of AWS resource types to Jira data provider schemas, you can already configure aspects of the integration by tagging your resources, for example: override the default data provider type for applicable services, e.g. 'forge deploy' via CodeBuild can be surfaced as type 'deployment' rather than the default 'build' select a specific deployment environment rather than the default 'other', e.g. 'development', 'staging', or 'production' for a Forge app How we built it The app backend is implemented on AWS via a serverless and primarily event-driven architecture based on Amazon API Gateway (HTTP), AWS AppSync (GraphQL), Amazon DynamoDB, Amazon EventBridge, AWS Lambda, and AWS Step Functions. We are leveraging the Cloud Development Kit (CDK) to orchestrate the provisioning of the various CloudFormation stacks. The app frontend is implemented on Forge and primarily comprised of site and project configuration pages, insofar most features are driven by the Open DevOps APIs. Due to Forge still lacking support for Jira Software data providers, we currently use a workaround via the OAuth integration for on-premises tools. Challenges we ran into First and foremost, Forge does not yet support the Jira Software data providers for Open DevOps, which has made the implementation less straight forward than envisioned. Despite the seemingly clean abstractions like AWS resource types, tags, and events, we have also underestimated the complexity of mapping these to the applicable Open DevOps API schemas. We need to implement a custom event mapping pipeline for each supported AWS resource type going forward, which is more work than expected, though also a rewarding task now that the building blocks are in place. Accomplishments that we're proud of We are quite happy that this app is completely serverless and primarily event-driven so that it is scalable and quickly evolvable from day one. We have also managed to significantly improve tenant isolation with CDK driven per-tenant resource provisioning. Aside from the currently required workaround for configuring OAuth credentials, the (unfinished) onboarding experience will refreshingly come down to launching a single CloudFormation stack, plus optionally another one to provision examples. What we learned Even though we have been using and enjoying most facilitated AWS services for quite a while, the event-driven use case and related recent AWS innovations allowed us to explore and embrace respective architectural patterns in a much more comprehensive fashion. Foundational services like Step Functions, EventBridge, and also AppSync, deliver significant productivity gains, which ultimately yields increased team velocity, and more importantly, a highly enjoyable development experience. What's next for Develop with AWS (Jira) Before we can consider a public release, we need to decide how to proceed regarding the missing Jira Software data provider support in Forge. Hopefully the Forge team can deliver this soon, alternatively we might consider publishing it based on the OAuth integration for on-premises tools, or eventually based on a Connect on Forge app (though this workaround is also still blocked due to missing Marketplace support). In the meantime, we'll try to complete the source code and feature flag data providers. The highly interesting remote links data provider is still a beta feature and not yet available via OAuth, so we might explore integrating applicable resources via regular Jira remote issue links instead, for example CloudWatch alerts or Security Hub findings. Obviously we are also keen on increasing our coverage of applicable AWS services and resource types :) Finally, we would like to explore this architecture for other integration points and products, for example to surface AWS resources and events via a dashboard gadget in Jira, or a home page feed and contextual macro in Confluence. It would also be straight forward to use the current OAuth workaround to ingest AWS events as builds, deployments, and code insights via the Bitbucket Cloud API, though this is a tough decision due to the lack of Forge and proper Marketplace support for Bitbucket Cloud apps. <div