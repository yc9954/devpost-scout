---
slug: "velofuse"
url: "https://devpost.com/software/velofuse"
title: "VeloFuse"
hackathon: "Wix Make-A-SaaS Hackathon"
organization: "Wix"
winner: true
words: 524
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# VeloFuse

> VeloFuse is a platform that lets you generate velo code with a logic builder. You set a trigger, the conditions and the actions, you click Generate Code, and you have your code ready to use.

[Devpost](https://devpost.com/software/velofuse) · hackathon [[Wix Make-A-SaaS Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** prism.js, velo, wix, wix-data, wix-members

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for velofuse

## Body

Inspiration I have worked with many Wix partners in the past, and many of them wanted a way to perform simple tasks without needing to know Velo. For example, clicking a button and manipulating something on the page, or changing text and other simple things that would require knowledge of Velo to do. So, I thought of a way to help them accomplish these tasks without writing a single line of code. If they could just enter their logic of what they want to do, click "Generate Code," and paste the code to their site, it would help a lot of users. What it does The platform lets users build their logic with any element they want (e.g., a button click or text entering the page) or a Wix service (e.g., Wix Stores to apply a coupon to the cart or Wix Location to redirect the user to a different page). The platform has three sections: a trigger, conditions, and actions. A trigger is the event that will trigger the code, such as a button click or a state change on a multi-state box. A condition (or more than one) is a requirement that needs to be met for the actions to run, such as if the input field has the specified value or if the input field is valid. Finally, the actions are the things the user wants to do when the trigger is triggered and the conditions are met. For example, changing the text on the page to something else or changing the multi-state box to another state. There are endless use cases you can build with the logic builder. How we built it We built the entire infrastructure on Wix, using only one outside service, Prism.js, to highlight the code we display to the user. We used a dynamic page for code block management and repeaters for the actions/conditions. To add a condition/action, a separate lightbox was created, each having the required elements like multi-states, repeaters, etc. Challenges we ran into The main challenge was accounting for all possible use cases. When the code compiler generated the user's code, it needed a lot of data to make sure it was possible to generate any kind of code the user wants to generate, and how this code works with itself, such as wrapping around the conditions in an if statement. Accomplishments that we're proud of We are proud that we were able to interconnect all those things together and give users the ability to do basically anything they can think of with any element Wix has, or any service that Wix has, and connect them all together. It required accounting for all use cases, such as different element types and Wix services like Wix Stores, etc. What's next for VeloFuse We want to make the platform bigger by allowing even more Wix APIs to be integrated and allowing users to use those APIs too. We also want to make ready-to-install apps with Wix blocks that will work with VeloFuse in a way that they can communicate with code blocks themselves, and users can create code for a "VeloFuse app" as well. <div