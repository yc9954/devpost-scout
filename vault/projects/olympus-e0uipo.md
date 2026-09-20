---
slug: "olympus-e0uipo"
url: "https://devpost.com/software/olympus-e0uipo"
title: "Olympus"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 1341
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Olympus

> Student online learning

[Devpost](https://devpost.com/software/olympus-e0uipo) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** pipelines, quickbase, webhooks

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for olympus

## Body

Inspiration Coronavirus has hit a few industries particularly hard, and being in education, I would argue education is one of the most affected. Seemingly overnight, teachers, students, and administrators had to figure out a way to do everything online. As one of those administrators, I’m proud to report that our teachers and students did indeed turn in their paper and pencils quickly in favor of solutions they found online, such as Google Classroom. In doing so however, the administrators still struggled to track student progress, lesson plans, grading, and parent-teacher relations. Google Classroom had some excellent tools for providing course materials and grading, but without an avenue for sharing data with the schools and the students’ parents, we needed something more. So we turned to Quickbase. We dreamt up an app that would seamlessly link into what our teachers were doing in Google Classroom and dig out data useful for our schools, such as students grades, attendance, and more. Further, we wanted administrators to set up courses and sections for our teachers to use so we could normalize our data and the teachers’ experiences. With lots of related tables in our minds, and a few pipeline steps planned out, my team got to work. What it does The Quickbase App, affectionately named Olympus , does a few things: Tracks students' progress, courses, and attendance district-wide Automates Google Classroom creation for Teachers to prepare courses and invite students Synchronizes with Google Classroom so that Teachers can create new coursework in the suite that will reflect on administration reports Behind the scenes most of our core data is going back and forth between Quickbase and Google using Pipelines. How I built it The app follows the basic administration structure in our district. There are Schools that have Teachers , Students , and Staff , which are reflected as related tables in QB. There are Classes that represent the student groups as they progress each year, and there are Courses they can take in their school year. These are the basic tables in the app that drive our data and reports. We had some big ideas for the app, so it helped to map everything out in a Relational Diagram (I used LucidChart). That way, when we got into other items that a course should have, like class announcements, topics, and assignments, it was easy to set up the relationships in Quickbase. The sticky part was planning out the link between Google Classroom and Quickbase. We wanted to support teachers as much as possible without getting in the way of their newly acquired workflow, but since most educators' workflows were turned on its head this year, we still needed a district-wide system. Thanks to Google, there is a 3rd party API primed and ready to push and pull all the data we need to Quickbase. So now it was a matter of learning their API and making the requests in Quickbase Pipelines. As fortune would have it, this was actually trivial once the authentication was understood. Google uses a variety of authentication methods to access services from a GSuite account (which includes Google Classroom). We opted for a service account and unexpiring refresh token. The Auth API returns temporary credentials for Pipelines to use later in calling things like Create Course or Invite Student Data out We decided that Quickbase should control the creation of courses, teachers, and students, since we are already tracking that as a district. Teachers would then control the course, topics, assignments, and grading from within Google Classroom. That way, they can focus on educating instead of data entry. So, we decided certain tables ( Courses , Course Students and Teachers ) should trigger creating and updating records in Google Classroom. This was simply a matter of triggering a pipeline with the HTTP requests. In short this meant that our pipelines mostly looked like this: Trigger on record create/update/delete Do a Fetch JSON to the Auth API With the access token returned, create/update/delete a record in Google Classroom If there are any IDs or metadata that google creates, add them to the record from the trigger Data in On the flip side, ingesting data into Quickbase needed to be frequent. While Google Classroom didn't have a nice trigger functionality like Pipelines, we could check regularly for any updates. So for course Topics for example, we actually scheduled a pipeline to run every half hour. The pipeline will use a Bulk Record Update and a Merge Key to automatically decide when to update and when to delete topics. More on that later. This way, our administrators would get near real time updates of what's happening in our "virtual classrooms." Challenges I ran into The Quickbase side was pretty easy. It's really beneficial to take some time before developing an app and think about what tables are needed and how they relate to one another. The tricky part was working on syncing data with Google Classroom. At first authentication seemed like witchcraft, and bringing data into Quickbase by polling isn't always as straightforward as it sounds. Authentication For those of you with insomnia, reading API documentation might be your cure. Doing the actions in Google Classrooms is as easy as formatting a JSON object, but learning the authentication method was much more complicated. From what I've learned from their documentation, for every API call I needed an acces token . I learned that service accounts are the way to go when linking to Quickbase. A service account can be set up to perform actions automatically, so in our case, things like adding a student to a class when a button is clicked. Google allows you to limit what things the service account can do. If you want to get technical, this essentially means permissioning, and I am able to grant limited access for this "user." Once that has been set up, I had to generate a refresh token which is a string of text I can use to get an access token. Once I have the access token, I can do whatever I need to in Google Classroom, and everything was downhill from that point. Regular Updates At first, we were debating whether this was viable because Pipelines can only be scheduled hourly. We wanted more frequent updates. By using callable pipelines, however, we could set up the pipeline to be called by 2 or more scheduled pipelines. So now we get our updates every hour on the 15 and 45. Syncing For data going out of Quickbase, I could tell Google whether it was a "Create", "Update", or "Delete" depending on the trigger I picked in Pipelines. For data coming in, "Merge Key" is the magic word. Topics are fetched as a list of records in a JSON object. Instead of creating new topics every hour, we set the Topics table Key Field to be the Google Topic Id field. That way when the records are fetched, Specifying a merge key tells Quickbase to update a record instead of create it. Accomplishments that I'm proud of I am proud of the Quickbase link with Google Classrooms. Educators have had to move at lightning speeds this year. Teachers have worked so hard to make sure our district's students are still getting the education they need and the education their parents expect. I like that we didn't really have to get in their way while still innovating better business practices than ever before. What I learned I learned how to use pipelines better. I was familiar with using them for HTTP requests, but I had to learn about Bulk Record Updates, Merge Keys, and Callable Pipelines. What's next for Olympus Next up on our list is configuring pipelines to automate syncing class assignments, student submissions, and grades. We can create some pretty cool reports with this data, and the reports will be even better than if we were still doing classes in person. Parents also play a critical role in a child's education, and we hope these reports will help them too. <div