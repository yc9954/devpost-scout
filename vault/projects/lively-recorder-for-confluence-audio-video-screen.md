---
slug: "lively-recorder-for-confluence-audio-video-screen"
url: "https://devpost.com/software/lively-recorder-for-confluence-audio-video-screen"
title: "Lively Recorder for Confluence"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 970
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Lively Recorder for Confluence

> Create audio, video and screen recordings directly from within Confluence!

[Devpost](https://devpost.com/software/lively-recorder-for-confluence-audio-video-screen) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** amazon-web-services, atlassian-connect-spring-boot, aui, connect, java, javascript, spring-boot, typescript, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lively recorder for confluence

## Body

Simply insert the recorder macro to start a new recording! Using the recorder pop-up, recording everything from screencasts to audio is a breeze! After you're done, insert your recording and share it with your colleagues! Yes, we've got data locality! You can choose the region of the S3 bucket where we will store your recordings. Never fear running out of attachment space again. With the Lively Recorder you can get up to 5 TB of storage, just for your recordings! Inspiration In our internal Confluence instance we document a lot of our processes in the format of “How we do X” articles. This works great for simple stuff, but for more complicated workflows we have found screen recordings to be much more useful than plain text. As a result, we started adding screen recordings to these pages. After some time, this turned chaotic as different team members were using different operating systems, tools and settings. Less tech-savvy team members also had trouble correctly setting up a recording tool on their machine, so they weren’t able to participate. At the same time, we noticed that these videos were taking up valuable attachment storage in our Confluence instance. We were afraid that we would soon run out of attachment storage if this continued. We needed a simple unified way to create and share screen, audio and video recordings in Confluence, without using our attachment storage. This is how the idea for our Lively Recorder App was born! What it does Upon inserting the Lively Recorder macro, you can choose what type of recording you want to create. Currently our app supports the following types: Audio Video Screen After choosing a type, our recorder pop-up opens. Here you can choose the correct microphone, camera, or screen for the recording. From there, everything is quite simple: Start the recording. Stop it once you’re done. Give it a name and possibly a description. Upload your recording! Once the recording is fully uploaded, the pop-up will close automatically and insert the recording into your page! Now your colleagues can listen to your charming voice, look at your beautiful face, or watch you delete the production database - all in your Confluence page! Now, here’s the icing on the cake: for all EU-based folks and those who value data locality, we have implemented a special feature! When first using the recorder, an admin can decide where in the world your recordings should be stored. Or in more technical terms: you can choose the region of the S3 Bucket that we will create for you! As we are partly EU-based ourselves, this was quite important to us. How we built it We started by building a frontend-only proof of concept that allowed us to make simple video recordings in the browser. After we got that down, we implemented a prototype of our backend that locally stored recordings, so we could test uploading and viewing them. This was later replaced by a mechanism that stores the files in an S3 Bucket. After that we implemented screen and audio recording and focused on improving the UX. Challenges we ran into Because Connect apps live in iframes and those iframes are sandboxed strictly, we had trouble gaining access to the user’s camera and microphone. We solved this problem by using a pop-up, which also turned out to serve the usage flow of our app very well. It also wasn’t easy to come up with a good solution for storage quotas. We wanted to give every user as much storage and flexibility as possible while keeping the price of the app low. We initially wanted to provide different tiers/plans, so that each customer could choose exactly the amount of storage that they need for their instance. This, however, turned out to not be possible on the Atlassian Marketplace. Consequently, we decide to give every instance 100GB for the start and increase that depending on the amount of paid users in the instance (up to a maximum of 5TB). Accomplishments that we're proud of Of course, we are happy that we were able to develop a cool app that solved issues we were facing internally. But we are even more proud of how we worked together as a team to make this happen. We are a small team split across Munich, Germany and Vancouver, Canada and every member was working from home due to the current global situation. Using tools like Confluence, Jira and Slack to coordinate and synchronize ourselves across time zones, we managed to work together just like we were in the same office. This definitely strengthened our bond as a team. :) What we learned Pop-ups can give you access to browser APIs that might otherwise be blocked in Connect iframes. With the right tools fully remote teams can have a great team experience! Not to underestimate the amount of work required for a presentation video, starting early pays off! What's next for Lively Recorder for Confluence We are super excited about our new app and have lots of ideas for it moving forward: Add a simple editing/trimming tool so unwanted parts of your recording can be removed easily. Automatically set storage quota depending on amount of paid users (up to 5TB per instance). Page-level recordings overview page (similar to the attachments overview). Space-level settings and overview (e.g. allow/disallow recordings in this space, see storage used in space, etc.). More player options (force mute, colors, play speed, etc.). Track views of recordings and display them if desired. Volume level indicator for microphone device selection. Allow direct upload of video and audio files. Improvements to the global settings page (more details about what spaces/pages use how much storage, set max recording length, restrict usage to group, clean-up tools, etc.). Continuous improvements to the overall look & feel of the app. <div