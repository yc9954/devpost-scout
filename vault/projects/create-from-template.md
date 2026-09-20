---
slug: "create-from-template"
url: "https://devpost.com/software/create-from-template"
title: "Create from Template Pro"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 991
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/supply_logistics"
---

# Create from Template Pro

> A revamped Create from Template Macro with advanced options like setting a parent page, adding custom variables, formatting the look and feel of the button and more.

[Devpost](https://devpost.com/software/create-from-template) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[supply_logistics]]

**stack** confluence, forge, forgeuikit, jest, node.js, rest, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for create from template pro

## Body

Macro Configuration in the Confluence Editor Create Form with Parameters defined in Macro Inspiration At K15t, we absolutely love using Confluence Templates. In fact, we love them so much that we we have made this video about it to share our learnings and best practices. Our intranet runs on Confluence and we use templates to standardize our content across the various team spaces. We've also created dozens of custom templates that drive a lot of our internal processes. For instance, we use an Idea Template to encourage everyone to record their ideas for new products or processes within the company. We also use templates to share Weekly Team Updates with the whole company. This means we're constantly making use of the Create from Template Macro. But having pushed the macro to its limits, we realized that in many cases, it just doesn't work well enough for us. Some of the things we struggle with include: Inability to Set a Parent Page The button always creates a new page as the children of the page it is placed on. While this is useful in many cases, it's limiting when we want to use the macro as a CTA in a blog post to for example, create a new Idea Page, or placing it on the team space's home page to collect feedback using a Feedback Template. Limited Options for Page Title Templating The current macro provides limited options when it comes to setting the title of the new page. E.g. You can only use @currentDate, @spaceName or @spaceKey to have those values inserted for you. While these are useful, we have found them to be limited. At K15t, we have established an extensive prefix system for creating and organizing content. We need to add user names to page titles when creating Quarterly Check-in pages, and use different date formats for project pages, e.g. YYMM, Project Name instead of the default format YYYY-MM-DD . You can learn more about the naming conventions we use in this video. No Button Formatting Options While this is not a blocker, the lack of formatting options for buttons prevents us from adding more context to the action and also limits creativity. Inability to Add New Labels While we can add labels to a template, it is not enough in the case of a global template. E.g. We have a global Customer Feedback Template with label: customer-feedback . But we also need to add team specific labels when creating the pages so that we can generate more granular reports later on. This is currently not possible. So, taking all these limitations into consideration and the fact that we recently migrated our intranet to Confluence cloud, we decided to build a simple Forge app that helps us – and hopefully your team too! What it does In addition to the basic options that you get with Confluence’s Create from Template macro, you get the following additional configuration options: Set a Parent Page for the new pages created with the macro. This is particularly useful when you don’t want to create the new pages as a child of the page where the macro is added. Advanced Page Title Templating with the option to define custom variables. These variables are then prompted to the users when they click on the create from macro button. Button Formatting Options like button types and icons to add more context to the action and to endorse creativity. Add New Labels in addition to the labels already added to the selected template. This enables you to have more granular control over labeling the new pages based on specific use cases. How we built it Both the macro and the macro config use forge UI Kit. Challenges we ran into UI Kit limitations: no automatic forwarding to a target page no onChange hooks in form fields (to validate user input) the macro config auto save can be unpredictable (a form field has to loose focus for it to pick up changes and update the config) Others no async loading of select field options No support for custom macro icons in Forge right now. No provision for linking to documentation No way to 'activate' the macro in edit mode Users that use the macro for the first time have to insert it into a page, publish the page, confirm that they allow the macro to change data and then got back into edit mode to configure the macro Accomplishments that we're proud of Building a production-ready app in such a short time complete with a getting started video and documentation. Working with a cross-functional team where no one had prior knowledge of Forge. What we learned Development flow using forge Deploy an app with forge to production and share it with others Use forge UI kit to create confluence extensions Forge manifest scopes and permissions What's next for Create from Template Pro We will upload the app to the Atlassian Marketplace and distribute it for free. We also want to move the front-end to Custom UI so that we get have greater flexibility when implementing new features and improving the existing ones. Here are some features we would like to prioritize - Forms for Variables in Page Templates - Prompt users to enter the variables defined in a template using a form when they click on the Create from Template Button. Scheduled Page Creation - Create a schedule to automatically create pages from templates based on the configuration similar to the ones available for the button macro. Variable Types for Custom Variables in Page Titles - Enable users to define types of variables when defining them in the page title field and display the correct fields in the create form based on the types. More Pre-defined Variables - We also want to support a larger array of pre-defined variables to give our users more power over the customization of the titles of the pages to be created. <div