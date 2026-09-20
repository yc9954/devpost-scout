---
slug: "integrate-with-aws-for-jira"
url: "https://devpost.com/software/integrate-with-aws-for-jira"
title: "Integrate with AWS for Jira"
hackathon: "Codegeist 2024"
organization: "Atlassian"
winner: true
words: 885
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "substrate/code_repository"
---

# Integrate with AWS for Jira

> Link and track your AWS resources – integrate Amazon Web Services with your DevOps workflows in Jira

[Devpost](https://devpost.com/software/integrate-with-aws-for-jira) · hackathon [[Codegeist 2024]]

## Facets

**domain** [[developer_tools]] [[housing_homeless]]
**substrate** [[code_repository]]

**stack** amazon-eventbridge, amazon-web-services, atlassian, aws-cloudformation, aws-lambda, aws-step-functions, cdk, forge, jira, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for integrate with aws for jira

## Body

Integrate with AWS for Jira – Linked AWS resources (project w/ query) Integrate with AWS for Jira – Linked AWS resources (issue sidebar) Integrate with AWS for Jira – Linked AWS resources (issue details) Integrate with AWS for Jira – Project configuration flow Integrate with AWS for Jira – Project configuration Integrate with AWS for Jira – Connected AWS environments Integrate with AWS for Jira – Connect AWS environment(s) Inspiration As a partner focused on AWS integrations for the Atlassian platform, we've long wanted to bridge our own DevOps workflows across both platforms with conceptually cross-product integrations for Jira, Confluence, Compass and Bitbucket. While the Atlassian Marketplace does not support cross-product integrations, the notable uptake of our sibling app Integrate with AWS for Compass validated the concept and encouraged us to make it a reality with technically separate yet conceptually overlapping apps for Jira, Compass, and soon also Confluence and Bitbucket. What it does Integrate with AWS allows you to link and track your Amazon Web Services (AWS) resources right from your DevOps workflows in Jira – you can connect one or more AWS environments (an account/region combination) via a CloudFormation based onboarding process, and once connected, it currently allows you to: Link AWS resources to Jira projects by configuring AWS Resource Explorer views that match your workloads Link AWS resources to Jira issues by tagging them with an issue key, e.g. when provisioning environments per pull request Follow contextual deep links to AWS resources and audit resource health and compliance How we built it The app backend is implemented on AWS via a serverless and primarily event-driven architecture based on Amazon API Gateway (HTTP), Amazon DynamoDB, Amazon EventBridge, AWS Lambda, AWS Step Functions, and AWS Resource Explorer. We are leveraging the Cloud Development Kit (CDK) to orchestrate the provisioning of the various CloudFormation stacks. The app frontend is implemented on Atlassian's Forge app development platform and uses the Jira Cloud REST API to drive the relevant Jira integrations. Challenges we ran into Launching the sibling 'Integrate with AWS for Compass' app in time for the Compass GA required us to take on some technical debt. As every so often, our expectations on how long we might need to pay off this debt have been vastly off due to the paramount need to avoid impact on existing users and added several months to our release schedule. On the flip side, besides the many involved learnings, this allowed us to submit the app for Codegeist :) Accomplishments that we're proud of Overcoming the aforementioned technical debt required us to carefully upgrade our data schema and CDK-based backend architecture to avoid any disruptions for existing users. We leveraged advanced AWS capabilities like DynamoDB streams and Lambda triggers as well as CloudFormation resource import to achieve this, and these will remain useful competencies for the evolution of our apps. We are quite happy about our vision for a cross-product AWS integration finally coming to life. The Jira and Compass apps share a backend and applicable tenant resources like the connected AWS environments, which eases onboarding and administration for end users. This has been made possible by a completely serverless and primarily event-driven approach that ensures the app is scalable and quickly evolvable from day one. What we learned We continue to learn our way around ever-growing distributed architectures, which remains a significant challenge despite the quickly evolving DevOps practices and serverless toolkit. The evolving integration between Jira and Compass allows us to leverage both products for our own DevOps workflows, and to evolve our AWS integrations in parallel to cover our AWS-specific requirements atop the Atlassian platform. What's next for Integrate with AWS for Jira Marketplace release First and foremost, we'll submit Integrate with AWS for Jira to the Atlassian Marketplace. We'll provide an update here once it's approved and published, so if you spare a like for the app, you'll get notified about the app being generally available. Single sign-on (SSO) enabled deep links The AWS Identity Center recently gained shortcut links , which doesn't sound too exciting until you realize that it solves the long-standing problem of single sign-on (SSO) enabled deep links to the AWS Management Console. This will significantly increase the usability of our integrations and is our most important roadmap item accordingly. Confluence & Bitbucket support With the app already being available for Jira and Compass , expanding to Confluence and Bitbucket will be fairly straight forward, so we'll prioritize these releases based on your feedback for the existing apps. Additional Jira integrations We're considering to add an AWS resource custom field and/or custom field type , an AWS resources dashboard gadget , and we might also support remote issue links to complement the AWS resources issue panel. Further onboarding improvements While we already provide onboarding flows to guide users towards configuration and usage of the app, there are still a few obvious improvements unlocked by recent UI Kit and AWS innovations, most notably the ability to browse for and select AWS resources right from the app (rather than having to copy an ARN from the AWS Management Console). We'd love to get your feedback! Let us know which AWS integrations for Jira would simplify the management of your distributed architecture via a comment below, or directly via our help center . <div