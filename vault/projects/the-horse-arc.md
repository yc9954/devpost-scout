---
slug: "the-horse-arc"
url: "https://devpost.com/software/the-horse-arc"
title: "The Horse Arc - product evaluation"
hackathon: "Amazon Sumerian AR/VR Challenge"
organization: "Amazon"
winner: true
words: 886
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# The Horse Arc - product evaluation

> Using Amazon Sumerian and VR to remove sales barriers, increase engagement, capture sales leads & usage stats

[Devpost](https://devpost.com/software/the-horse-arc) · hackathon [[Amazon Sumerian AR-VR Challenge]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: labor_employment</sub>
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** amazon-sumerian, amazon-web-services

## Body

Menu and streaming video The Horse Arc - exact scale [+] [-] buttons allow you to scale horses to match your own Set your height in VR or desktop browser mode to appreciate scale more accurately Horse Arc have not funded this development but have provided permission to use their media and product likenesses to use in the case study. Inspiration Having previously created a website for the Horse Arc ( www.HorseArc.co.uk ), I understood the challenges they faced. They have many USPs, so keeping peoples attention long enough to convey them all is important. Customers want to see the product in real life before buying and sometimes travel long distances to see one. This is a barrier to sales. Even then, it's hard to evaluate the size without seeing your own horses inside the Arc. I knew VR could help with these issues, but not many people have VR. This led me to create a solution that works on premium VR devices, mobile VR (that the business owner can take to events) and even on the desktop browser to increase the reach of the experience. I was also interested in how to capture a sales lead without needing the user to exit VR or use a virtual keyboard to slowly enter their details. What it does A streaming video with audio narration plays, directing the customer through various interactive tasks that keep them engaged in the sales process. USP's are conveyed as the customer actually builds the Horse Arc. The customer can set their true height in the experience and teleport in and around the arc to appreciate its size. They can scale two horses to match their own horses and move them through the arc. This allows them to evaluate the suitability of the arc without seeing it in real life. Finally the customer is prompted to record a voice message which is emailed to the company. This quickly captures a sales lead without ever leaving VR or requiring a slow and clunky virtual keyboard. Every interaction is recorded on a database so we can evaluate how well the app is engaging customers. Features Video with audio is streamed from S3 (rather than using HTML3d component) to maintain good performance in VR. The video pauses and resumes at various points driven by your interactions. Jump straight to different parts of the experience using the menu above the video (ideal for returning customers) The experience works on PC-based VR, mobile VR (Oculus Go) or on a desktop browser and is optimised for mobile VR. You can set you height in VR or desktop mode. This is important to help you gauge scale more accurately. Leads are captured by allowing the customer to record an audio message. This is emailed to the company via a Lambda function call and SES. Sample: https://s3.amazonaws.com/horsearc/voicemail.png Usage stats are recorded as the customer navigates the experience. Details are stored on a DynamoDB database via a Lambda function call. These important analytics will allow us to assess the effectiveness of the experience and improve it over time. Duration and the number / type of interactions are recorded. Sample: https://s3.amazonaws.com/horsearc/statsScreenShot.png A fool proof drag and drop technique is used when building the Arc or moving horses. It works the same in VR and when using the mouse and restricts movement between two points on a set plane. Teleport enhancements prevent you from teleporting too close to the arc, and automatically optimises your position when teleporting back to the video screen. How I built it Uses Amazon AWS services with no other dependencies, meaning the solution is robust and scalable. Coded in Sumerian and uses S3 for video streaming, Lambda functions to pass the customers voice message on to the business via SES and DynamoDB (via Lambda) is used to record anonymous usage stats to allow the success of the experience to be measured and improved over time. Challenges I ran into I couldn't get spatial audio working in VR - which is a known issue. Accomplishments that I'm proud of Creating a VR experience that can also be used on the desktop browser. It works consistently across platforms and even allows the user's height to be modified. The desktop version is not as ideal as VR for judging scale, but setting your height makes a significant improvement. Introducing teleporting into the desktop browser version provides a more user-friendly approach to movement.The target market here aren't gamers, so simple controls are required. I'm proud of the finished product - an effective marketing tool, a great way to evaluate products when scale matters and a good demonstration of an optimum lead capture technique and of capturing analytics in VR. What I learned WebVR is not some far off technology and it's not just restricted to VR / AR. It performs well across devices and can deliver real business benefits right now. What's next for The Horse Arc Allow the Arcs to be customised with optional extras and see them on the model. Make available to Horse Arc customers and monitor the stats to measure engagement. Use as a case study to promote the benefits of using WebVR, Sumerian and AWS to present optimised / user driven sales experiences using interaction to increase length of engagement and accurate scale representation to remove sales barriers. <div