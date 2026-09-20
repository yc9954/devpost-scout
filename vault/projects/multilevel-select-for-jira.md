---
slug: "multilevel-select-for-jira"
url: "https://devpost.com/software/multilevel-select-for-jira"
title: "Multilevel Select for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 922
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Multilevel Select for Jira

> Use cascading lists that have infinitely many nested levels. Thanks to our custom field, issue creation in Jira enters a new level.

[Devpost](https://devpost.com/software/multilevel-select-for-jira) · hackathon [[Codegeist 2021]]

## Facets


**stack** atlaskit, forge, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration Our inspiration, as in all our projects, was brought by the need that arose in everyday work. While working on tasks in Jira, we noticed that the cascading select custom field is often not enough for us. Two levels are not enough to meet our expectations. For example, in a marketing project, we would like to have a field in which we select which of our products the issue for writing an article relates to. It quickly turned out that cascading select with two lists: app and hosting is not enough for us. We also wanted to be able to determine whether it is a Connect or Forge version of the app. In addition, we would like to indicate whether the article will concern the area of Jira Software or Jira Service Management. We had to multiply custom fields in Jira (and every Jira administrator knows that this is not a recommended practice) to meet our requirements. That's why we decided to make our cascading custom field. What it does This app provides a new custom field called Multilevel select. It is an extended version of the cascading select custom field known to Jira users. The field provided by our application has no limit to the number of nesting levels. You can create so many levels. You are only limited by your imagination. Additionally, each option can be translated into any language available in Jira. Thanks to this, you do not have to duplicate the custom field and create a separate one for each language. Thanks to this, you keep your Jira instance clean, and field management and maintenance is child's play. How we built it We use the following Forge modules: Forge Custom Field Type Forge Custom UI Forge Storage In the configuration, we use a component from Ant Design called Tree . We manage the entire project using Jira Cloud and Confluence. We have prepared the interface graphic designs in Figma. Challenges we ran into It was extremely important for us to take advantage of the possibility of creating custom fields on Jira Cloud. First, it was a custom field. Then the custom field Type. Later we created a translated select in Forge UI. Finally, it became a multilevel translated select written in Custom UI. Over the past month, we've been rewriting everything multiple times as there are new modules in Forge. Extending the custom field capabilities in Forge gave us more work, but also increased the value of our app. It was important that we keep pace with these changes and implement them in our product on an ongoing basis. Accomplishments that we're proud of It is a great joy for us that the app that we previously released on the Atlassian Marketplace as Translated Select for Jira, thanks to the new capabilities of Forge, could be developed into a completely new one during Atlassian Codegeist 2021 as Multilevel Select for Jira. And all this is thanks to updates in the Forge Custom Field Type module. In the MVP version called Translated Select for Jira, it was possible to create a custom field, but its configuration was in the global configuration in the Apps section on the app's page. It was quite rudimentary: you could add an option and translate it into any language. Apart from not very intuitive configuration placement (it is not natural that it is not in the Custom fields section in Jira), we could not implement the idea of ​​cascading on the custom field editing dialog on the issue. Forge UI didn't make it possible for us. This was not enough to guarantee interaction and dynamically render selects. Fortunately, thanks to the introduction of the Forge Custom UI, we were able to implement it all! Now it is possible to do some wonders in the custom field edit rendering mode :) What's more, we are glad that the action of editing the custom field from the issue glance and the way of configuring this field do not differ from Jira standards. We believe this is an important value for the end-user who does not feel like he is using an external application. We can even boldly say: our app fits perfectly into the products provided by Atlassian. What we learned While working on the app, we got to know every little detail of the Forge Custom Field Type module. No part of it is a mystery to us anymore. Besides, it took a lot of effort from us to write a customizable tree to handle the configuration of our custom field options. What's next for Multilevel Select for Jira The most important point in the further development of the app for us is the change of the model from List to List. It will allow a user-friendly search for this field in the issue navigator (both in Basic search and Advanced search (JQL)) and export these values to a file. Thanks to this, it will also be possible to conveniently use this field on the gadget on the dashboards. Besides, we would like to implement the following ideas: setting a default value for the field improve the custom field configuration from the user experience aspect add a field to request type so that customers can use it on the request form (this requires adding support in Forge for Jira Service Management) We are also waiting for Atlassian to enable using global custom fields in team-managed projects. Thanks to this, it will be possible to use the field provided by our app in them. <div