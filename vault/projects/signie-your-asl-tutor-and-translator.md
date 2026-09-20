---
slug: "signie-your-asl-tutor-and-translator"
url: "https://devpost.com/software/signie-your-asl-tutor-and-translator"
title: "Signie - Your ASL tutor and translator"
hackathon: "XR Design Challenge"
organization: "immersive insiders"
winner: true
words: 815
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Signie - Your ASL tutor and translator

> Learn sign language effortlessly and communicate seamlessly with real-time translation into ASL. Breaking down communication barriers and making the world more inclusive — one sign at a time.

[Devpost](https://devpost.com/software/signie-your-asl-tutor-and-translator) · hackathon [[XR Design Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** blender, c#, dollars-mono-(motion-capture), shapesxr, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for signie - your asl tutor and translator

## Body

Choose a level Learning the basics Real time feedback Interactive knowledge check Inspiration One of our team members has been doing some research on ASL. We learned that the hearing impaired struggle to communicate because many people don't know sign language. We also learned that learning ASL can be challenging because you have to see yourself from a third person perspective to know if you're signing correctly. Additionally, for the hearing impaired, when they watch videos and content reading closed captions feels like a second language to them, ASL is actually their primary language for communicating. After some deep conversations about how XR could address these issues, Signie was born. What it does Signie is a concept app that serves two purposes. Its primary purpose is to help people learn ASL in a more effective manner than can be done today. Secondarily we showcase a future state where Signie will be able to translate audio into ASL. For the app we demonstrate the first use case, creating both a ShapesXR prototype and then a working app that shows how we could leverage XR technology to more easily learn ASL using avatars and motion cues to help people learn the signs. In a future state, we could train an AI model to recognize the gestures and provide even better feedback for signs in addition to converting spoken text into ASL movements that would allow hearing impaired to watch movies without captions and also have a virtual avatar overlay in a MR environment. How we built it We first prototyped the concept fully in ShapesXR to validate the use cases and flow. We used ShapesXR holonotes to mimic a 3D avatar and to record third person POV. Once we had enough of the concept figured out we pivoted to building working code. Not all of us knew how to code so we also continued to fully build out the ShapesXR prototype in the event the working code wouldn't be ready. Challenges we ran into Having an avatar that could show the signs was crucial to our product. We experimented with different ways to create them, but eventually found a motion capture tool that could use a camera and translate those movements onto a rigged character. This meant we had to learn ASL ourselves in order to do the motion capture for the avatar character! We also found that a single camera motion capture system has trouble with ambiguous hand orientations (such as palms facing up or down), so we had to craft the phrases to use signs that avoided those gestures. We also had to find a way to create an embodied feel to our product because it was critical that the user can not only see the sign but also see how their movements align with it. We originally wanted to have a model trained on ASL movements and then use the cameras to track the hand and arm motions. That proved prohibitively time and resource intensive so we settled on fixed animations for a few key phrases and then used an transparent shader so the user could still see their hands and arms in relation to animation. Accomplishments that we're proud of We created a functional prototype in ShapesXR, overcoming the limitation of not being able to add an animated virtual avatar by replacing it with holonotes. This substitution made the prototype more immersive and realistic. Additionally, all parts of the video showcasing the user interacting with the UI were recorded using the Quest 3 in ShapesXR's MR mode. This approach brought our envisioned app closer to reality." We used the prototype to guide our development effort. We are so proud of all the effort that we even created two 60s videos, one for the prototype and one for the working app. They both came out so good that we really struggled to decide which one to use as the final main video! What we learned Character rigging is super time consuming, but the motion capture was the savior. If we had to manually pose the avatar for each sign we would not have been able to complete the project. Creating a working prototype was critical for our shared understanding of how the app should function. Communication among team members was critical to a successful project. What's next for Signie - Your ASL tutor and translator The list of enhancements is long, but the primary ones would be: Add rigged facial features to the avatar so it can making proper face and mouth movements, which is really important when learning, especially for hearing impaired. Train an ML model to understand ASL which would allow better real time feedback when learning signs and also the ability to do real-time translation into ASL. Conduct product research to better understand which features are more useful for the hearing impaired and for those wanting to learn sign language. <div