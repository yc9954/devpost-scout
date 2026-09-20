---
slug: "comment-translation-for-jira"
url: "https://devpost.com/software/comment-translation-for-jira"
title: "Comment Translations for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 901
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Comment Translations for Jira

> Enable a multi-language team to cooperate on Jira issues by offering easy access to the comments in their language. They can also create comments in their language and have them be translated.

[Devpost](https://devpost.com/software/comment-translation-for-jira) · hackathon [[Codegeist 2021]]

## Facets

**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** atlaskit, css, faas, google-translate, html5, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for comment translation for jira

## Body

GIF Create a comment in your language and have it be translated into the project default language Read other people's comments in a language of your choosing GIF Translate portions of Confluence pages into any language Inspiration Looking to the actual world, it is easy to see many teams today that are spread around the world and Jira is helping people to manage the projects in an easy and good way. But this brings to us new issues to face: how can we help people with different languages around the globe to have a better experience about the communication? How can we help people express their ideas better and more comfortably? How can we help people understand better what their colleagues are saying? Keeping this in mind Communication is one of the most important keys to having a successful project Comment Translation for Jira was created to help users to communicate in an easy way providing tools, helping them express themselves in different languages and to understand better what their colleagues are saying. What it does To make this possible, Comment Translation for Jira provides a useful UI, where comments can be posted in the user's native language and automatically translated into the project default language. Additionally, all comments can be translated to whatever language the user wants. The first interface is the editor based on @atlaskit/editor-core which Jira uses internally to create comments. There, the user can type the comment using their native language and in two steps, clicking to "Translate" and "Save", the comment is posted using the default project language. This allows the user to make any adjustment they want before posting the comment (we at resolution GmbH have some experience with company names being translated even though they're used as such 😅) or return to the untranslated version if they wanted to rephrase something. The second interface is a new tab provided by the Comment Translation for Jira where the user can see all comments translated to a language they choose. This is useful if the user isn't proficient in the language used on the project. This is done using a dropdown where it's possible to select the language used to translate the comments. For a native look and feel, we use the @atlaskit/comment component. As a little bonus, if you install the app in Confluence, you can select some text and then use a context menu action to translate it. How we built it To create this, the Resolution team used the Forge Custom UI mixed with Atlaskit-provided React components to create a good and Jira-native-looking UI, where the users can have a good experience understanding the others and expressing themselves. To make the backend, we used the Atlassian API to get the comments and all information necessary to translate. We then convert ADF to HTML, so the Google Cloud Translations API could be used to translate all texts. Challenges we ran into To create the Comment Translation for Jira we have some issues and we see some points to improve like: Initially, we wanted to see if we could convert our existing Translation app to Forge, but it turned out that Service Desk is not supported. Similarly, to mirror that app's functionality, we tried to mirror the ability to edit comments. This would have allowed us to put in the translations without user interaction, but since admin scoped functionality is still broken in Forge this was not possible and we had to create the editor instead Since the Google Cloud Translations API only supports plain text or HTML, we had to develop a way to convert ADF to HTML in such a way that it was reversible. Since Google Cloud Translations preserves the HTML tags, we were able to create a 1-to-1 mapping from ADF nodes to HTML tags, with additional information stored in HTML attributes. The Atlaskit documentation needs some update: During the process, we needed to check some documentation, like the DropdownMenu and DropdownItem and simple things like how can we trigger an onClick isn't there. Looks like there is a problem to use lasted versions of styled-components mixed with DropdownItem. The onClick property doesn't work properly. A workaround to solve this can be found here : The same situation, we mean, lasted versions of styled-components mixed with Atlaskit components could be seen when we use @atlaskit/editor-core . There is no module for a project settings page, so we had to work around that by creating a project page that has view conditions set to only appear to project, product or site admins Accomplishments that we're proud of One thing that the Resolution team is proud of is how the transaction from ADF to HTML was made. Since Google Cloud Translations supports translating within and preserving HTML tags, this makes it possible to translate the text without removing the formatting created by the user. After translation, we recreate ADF from the translated HTML so the translation also has the same formatting in the same places. What we learned Works deeply with ADF format, more about Atlaskit component who we hadn't worked with before, and more about how the Forge Custom UI works. We were also able to gain a lot of information about the state of Forge and its readiness for use in production Marketplace apps. What's next for Comment Translation for Jira We do not wish to share this information publicly. <div