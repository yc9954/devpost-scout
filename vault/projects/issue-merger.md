---
slug: "issue-merger"
url: "https://devpost.com/software/issue-merger"
title: "Issue Merger"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1116
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Issue Merger

> Are you tired of duplicated issues? Your customer replied from a different email address and created new issue? With Issue Merger you can easily merge many tickets into target issue or create new one.

[Devpost](https://devpost.com/software/issue-merger) · hackathon [[Codegeist 2021]]

## Facets


**stack** atlaskit, custom-ui, forge, jira-cloud, jira-service-management, jira-software, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for issue merger

## Body

Select Issues Summary field prompt Version field prompt Priority field prompt Fill fields Finally step Inspiration In a lot of project, we’ve noticed so many issues, that are similar or even the same. Mostly to find all information we needed, we had to go and find all of this issues that wasn’t linked and then link them to one issue. Even if all issues was linked, we didn't have all information in one place, we had to move around those issues and collect all information. Then we thought, what if we could merge them into one task! What it does Issue Merger has one priority function, merging issues. From selected by user issues user can choose, if application will create new issue or edit existing one. Then in edit view, user have to provide all data, that he want to be populated on target issue. Application will show all values from selected issues so user do not need to type it, just simply click and choose what information are crucial. Additionally Issue Merger offer two actions after merge: linking duplicated issues to parent. removing duplicated issues from Jira (only if user has permissions!). So user can decide what to do with duplication to keep their Jira clean and neat. How we built it Issue Merger is Application that require a lot of data from Jira. To display all view we used custom UI where we could create our own React components. Redux - Application needs to store information about selected issues, their fields and meta data. To create or edit issue we need to know exactly what fields are on view and which of them are required. Also our app is showing all possible value from tasks to user, so he can select them instead of copy pasting, Redux is perfect choice thanks to store that is available for all components, no more need to provide all data in props! TypeScript - This simply app is very complex behind the stage, each data we get from Jira using rest API, comes in certain type, each fields has his specific implementation, all of our states are in different type. With a quick and easy integration with TypeScript we had more control of all our objects and states, so our code end up clean, readable and easy to implement next features. Atlassian Atlaskit - It is not that easy to create advanced user interface that is consistent with Atlassian Ecosystem environment were application is running. We wanted to make users stay in Jira context, so our application should look like uniform piece of site. Because of Atlaskit, all components are same as component in Jira. Challenges we ran into First thing we had to do, was create list of our functions and sketch a user interface. In this moment we had to choose between UI kit and Forge UI. Whole idea behind Issue Merger was to give user as much information as we can, so if user will fill summary field, we want to show him all summary values from issue that he selected, also if he is using e.g. Version fields, app will show witch issues used that value, so user can see all this data in our view. To achieve that, we decided to use Custom UI. All field types are specific and require individual implementation. We couldn’t use regular elements, we had to customize each of them. In Jira almost each action that is related to issue has its own permission. There was a challenge to support all app features and ensure complex security. We decided to make all changes as a user who is making merge action, so Jira is handling permissions out of the box. Another problem we find out was with sending incorrect data to Jira when application was creating or editing issues. If only 1 field is incorrect, Jira will not made any changes. So if user changed few fields, and one of them was incorrect in some way, whole request was rejected. To avoid situations like this, and make all changes we can in one go, Issue Merger is sending each field separately, so one bad value wont screw up whole process. This made work of our application too long, when fields were sending one after another, so we decided to make it asynchronous. Now All changes are made very fast, and if some value isn’t correct, others will be applied. Accomplishments that we're proud of Working application! Issue Merger works, do it's job perfectly! Issue merger has all features and all basic fields we wanted to implement in MVP version, and even more. First thing we aimed in was merging issues into new or existing one, so collecting all fields values, merging them, and send to Jira. Next thing was linking selected issues, so user do not need to do that by hand. As it turns out, Users can even use Issue Merger just to link issues, even without changing fields. We find that useful when we had to link all our issues from this project (: After that, we had some time to add option for remove selected issues. It’s very useful feature, specifically when few people created same task. So all they have to do now, is to select all of them, choose one and merge missing data from other issues. That’s all! Issue Merger will automatically update issue and remove old ones. Also like in linking issues case, this app is just great to bulk remove issues. What we learned The most important thing we learn is developing applications for Jira Cloud using Forge. We mostly created add-on’s for Jira server/DC or using Atlassian Connect for Jira Cloud. Also we learn a lot of how to customize Atlaskit components to our needs, where are limits and how to cross them. We learn more, how to work as a team, and how to split our tasks so everyone can work independently. Also we learned how to mage work, and creating plans for next moves. What's next for Issue Merger We planned some big improvements for Issue Merger: Add Intelligent default fields filling (using AI). Add all standard fields for Jira Software. Add all Jira custom fields. Refactor code to use RXJS. Add fields form Jira Service desk. Create next actions after merge: Transition selected issues to certain state. Create revert merge action - to revert changes made in specific Issue. Show history of changes made with Issue Merger. Place Issue Merger in more spots to give users easier access: In project view, In bulk actions (If it will be possible in Forge). Add retry button to retry action that was invalid when sending data to issue. <div