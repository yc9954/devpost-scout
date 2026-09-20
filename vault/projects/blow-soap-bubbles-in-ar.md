---
slug: "blow-soap-bubbles-in-ar"
url: "https://devpost.com/software/blow-soap-bubbles-in-ar"
title: "Blow Soap Bubbles in AR"
hackathon: "Facebook Hackathon: AR"
organization: "Facebook"
winner: true
words: 1277
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Blow Soap Bubbles in AR

> In the pursuit of making augmented reality experiences more physical, Data Sapiens have created an Instagram filter that lets you blow soap bubbles. At any time, anywhere.

[Devpost](https://devpost.com/software/blow-soap-bubbles-in-ar) · hackathon [[Facebook Hackathon- AR]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** ar, javascript, sparkar

## How they structured the write-up

- about the creators of this project
- inspiration
- what it does
- how we built it
- challenges we ran into
- outro
- resources

## Body

About the creators of this project Data Sapiens is a creative collaborative, living in the cloud. We are a spare-time collective of creatives from all around the world, specializing in different disciplines. Inspiration For the past months, Data Sapiens have been experimenting on how we can get users to interact with augmented reality experiences not only with touch gestures but also with physical body gestures. We got the idea of detecting if a user is blowing on the phone from watching footage from a trip to the windy west coast of Norway and hearing the wind blowing into the microphone. Using our findings to simulate soap bubbles felt natural when blowing on the display of the device. What it does It enables users to blow soap bubbles in augmented reality. After following three easy steps to calibrate and initialize the experience, the filter will emit bubbles when the user blows on the screen of their device. How we built it Detecting how devices react when you blow on them The moment Spark AR's new audio reactivity features launched, we got to work. We started by seeing how the different frequencies were split and interpreted by Spark AR. We analyzed how sound reacts when a user blows on the screen. Devices have different placement of their microphone, and users hold their phones differently. We noticed that some users use their digitus minimus (little finger) as support when holding their device. If a left-handed user does this on an iPhone, the user might be blocking the microphone, as iPhones have their microphone on the bottom left side of the phone. Google Pixel devices have their microphone on top of the display. These are one of many factors we considered when selecting a sound frequency and threshold value for our custom "wind on the screen" trigger. In our lab, we managed to test on five devices from different manufacturers. To test our detection, even more, we decided to release an early prototype of our filter and ask the community for help, so we could map how different phones behave. We learned that our detection works nicely on most phones, but some old Huawei and Samsung devices are not always working as there are some bugs in the core, and not in the filter. Positioning and triggering a particle emitter We linked an emitter that is a child of a plane tracker to share the same world coordinates and rotation as the camera. objEmiter.worldTransform.position = objCamera.worldTransform.position; objEmitter.transform.rotationX = objCamera.rotationX.sub(Math.PI); objEmitter.transform.rotationY = objCamera.rotationZ.sub(trackerPlane.worldTransform.rotationZ); objEmitter.transform.rotationZ = objCamera.rotationY; With the emitter positioned, we used our findings from our research on audio reactivity, to trigger the emitter to emit particles that were to end up as out bubbles. Making it look like bubbles One of our main goals was to make our filter as authentic as possible. To learn more about how soap bubbles behave, we shot many videos of real soap bubbles in slow-motion and systematically analyzed the recordings. Some factors we were looking for include bubble life span, acceleration, velocity, size, and how the color change based on the backdrop. Using the data from our analysis, we managed to use set forces in the emitter, to move the bubbles in a way that feels natural. We thought that bubbles reflect the environment like a 360-degree photo in a sphere. We were surprised when we saw soap bubbles reflect 180-degree of the environment in a semisphere that is inverted to create a full sphere. Richard Heeks has documented this really well in photo series, Zubbles . We used this opportunity to use the camera texture to recreate the same reflection feeling instead of loading an environment texture. Using the camera texture has two advantages. The look of the bubbles will change based on the environment, and be more relevant to the user's lighting conditions. We had to fake the reflection look by using pincushion distortion as the angle of view on devices is not wide. The camera texture is also pointing in the wrong direction of what would be the texture, so only used the high luminance areas and blended these with our gradients ramps for iridescent. The second and biggest advantage of not using environment textures is size. Our filter is fully procedural, meaning we are not relying on any assets besides our patches and scripts. The size of the export is only 14kb making the filter fast to load and more accessible for users in locations with a bad internet connection. Involving the community Filters need to be tested, and we believe the best way to do this is involving the community. After 3 days of development, we released a prototype and asked the community for feedback. You can read the post here . 253 captures were made on the first day, and people from the community trying the filter gave us feedback. One of the common feedback was to make better instructions. So we did, we also saw the opportunity to create a feature request to the Spark AR team to get better audio reactivity instructions such as, "Start recording and make some noise". Another feedback was to have the bubbles pop more randomly, which resulted in the research we did on soap bubble behavior. The community has helped and pushed us making an augmented reality experience we are truly proud of. Challenges we ran into Plane tracker stability Since we rely on plane tracking to position the bubbles in world space we needed the tracker to the stable so the bubbles don't jump around when the user moves around. To solve this we disabled auto-start on the tracker and added an instruction for the user to look around for 3 seconds before tapping a surface to track. This resulted in a lot more stable tracking across different environments, even in low light. Scale bug after Instagram update The prototype broke on Instagram after an update. It turned out to be Reactive.scale() not working anymore. We rely on inverting the plane tracker scale to keep a constant scale for the bubbles. To solve this we scaled each axis separately. We also submitted a bug report on this. Instructions for audio reactivity Today we can't show instructions while recording, and the user has to record for the audio reactivity to work. This makes it tricky to make the user understand that they need to make some noise or blow on their phone to trigger the emitter. We have submitted a feature request with a proposed solution for this. To work around this we made sure to have a clear demo video. This seems to be working as we can tell from the stats that people are using and sharing the filter. Outro We are really proud of the realistic look of the bubbles, and even more proud to be able to do this in such a small filter size. As a creative collaboration with a focus on building bidirectional bridges between the analog and digital worlds, we are thriving to make experiences accessible for everyone. Having a filter of this quality that will load in an instant, even on bad network connections is a milestone for us. We are looking forward to seeing more users use our filter, learn from them, and improve our filter. We are also proud of the process of building this filter. We learned a lot from the community, a lot about world space in Spark AR, and how we can make AR experiences more physical. We are already looking forward to the next challenge. Resources Link to the filter on Instagram Case study video on Vimeo Project on Github. Data Sapiens on Instagram Data Sapiens Website. <div