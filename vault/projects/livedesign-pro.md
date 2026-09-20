---
slug: "livedesign-pro"
url: "https://devpost.com/software/livedesign-pro"
title: "LiveDesign Pro"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 1008
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LiveDesign Pro

> A streamlined event page design platform integrating ChatGPT and Midjourney for effortless image generation, smart copywriting, and interactive features to enhance TikTok live stream engagement.

[Devpost](https://devpost.com/software/livedesign-pro) · hackathon [[2024 TikTok TechJam]]

## Facets

**domain** [[retail_commerce]]
**user** [[small_business]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css3, firebase, flask, heroku, html5, python, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what we learned
- building the project
- challenges
- conclusion

## Body

PublishPage: Click "create" to get into LiveDesign Pro FrontPage: Choose existing or generate eventpage GeneratePage Creation: Create eventpage by prompt GeneratePage Examples: Check eventpage examples and apply ChatPage: Get eventpage generated from Midjourney and edit DesignPage: Add interactive components on eventpage and publish PublishPage: Check your published eventpage here Inspiration 1. Product Overview As event pages increasingly become the core of live stream engagement, we aim to create a simple yet efficient event page design platform to maximize their advantages. Through market research, we identified distinct challenges faced by small and large brands in leveraging TikTok for live stream engagement. 2. Current Challenges TikTok is a crucial marketing platform for small businesses. Data shows that 77% of small businesses reported increased sales through TikTok marketing last year. However, small businesses often lack sufficient design, development, and marketing teams, resulting in poorly designed and interactive event pages that ultimately impact live stream engagement. For large brands, even with professional teams, the complex processes (such as coupon distribution, live stream reservations, and link sharing) require users to navigate to the website for registration and verification. This increases operational difficulty, leads to user drop-off, and reduces live stream engagement. 3. Our Solution To address these challenges, we designed "LiveDesign Pro". This feature is integrated within TikTok, incorporating ChatGPT API and Midjourney API, allowing users to effortlessly create stunning marketing posters, copywriting, and intelligent tags directly within TikTok. LiveDesign Pro By adding button components, it enables TikTok's built-in functions, such as one-click coupon distribution, live stream reservation reminders, and automatic generation of QR code and link for live stream sharing. This significantly lowers the production cost for businesses, improves live stream promotion, optimizes user experience, and stimulates interest in live shopping, meeting the goal of our project. What We Learned 1. Product Development Process Our greatest achievement was successfully navigating the entire product development lifecycle—from ideation and implementation to iterative enhancement and final deployment. This comprehensive experience provided us with a profound understanding of the product development process. 2. Team Collaboration and Plan Execution As the team leader, I prioritized balancing development difficulty and implementation effectiveness when making the plan, ensuring that everyone could perform at their best within their capabilities. Additionally, team members actively executed the plan, continuously learned new technologies and solved coding issues, which was crucial to the project's success. 3. Skills Enhancement The completion of the project relied not only on technology but also on design, market analysis, user research, product planning, etc. This process significantly enhanced our comprehensive skills, aligning better with the market demand for versatile talents. Building the Project 1. Market and User Research We first focused on low live stream engagement and purchase rates and identifying the main problem in creating event pages. We used related functions on TikTok and analyzed how event pages can boost live stream activity. We also studied the successful live stream shopping strategies of TikTok's Chinese version. Ultimately, we aimed to create a simple and efficient event page design and interaction platform to maximize their advantages. 2. Product Design Based on our research findings, we decided to build new features directly within TikTok for seamless integration, focusing on two main functional pages: GeneratePage and DesignPage. Generate Page integrates the ChatGPT and Midjourney APIs. Users input descriptions, select models, and page sizes, which are then processed by ChatGPT for prompt optimization before being sent to Midjourney for image generation. For users unfamiliar with this process, we provided some examples as a reference. After submission, users can access the Chat Page to interact with Midjourney AI, enabling partial modifications or image regeneration to ensure the design meets their requirements. Once the image is finalized, it transitions to DesignPage. Design Page emphasizes interactive design features for event pages. Users can add promotional slogans, key information, themed stickers, upload images, and add background music to enhance visual and auditory appeal. They can also add buttons to leverage TikTok's built-in features, such as one-click coupon distribution, live stream reservation reminders, and QR code generation for sharing. To ensure optimal dissemination, we used ChatGPT to intelligently optimize the caption and tags, ensuring the content aligns with TikTok's style and marketing strategy. Once complete, users can click the "Publish" button to automatically publish the event page. Finally, we selected colors based on TikTok's design guidelines and created prototypes in Figma for development reference. 3. Technical Implementation We followed an efficient and actionable plan for product development. Task allocation was based on the team's expertise: front-end development utilized React, TypeScript, JavaScript, and Tailwind CSS, while back-end development was handled with Flask. For the user interface, we selected Ant Design to ensure consistency in style and expedite feature implementation. Additionally, we integrated ChatGPT and Midjourney APIs for AI-driven text and image generation. 4. Testing and Optimisation In the final phase, we performed rigorous testing, deployed code on GitHub, and undertook report writing and demo video editing. We ensured seamless code execution and clear operational processes, completely demonstrating our product concept through detailed reports and engaging demo videos. Challenges During the development processes we had a couple consideration for which AI to use. Our choices were between MidJourney, GSAP or Dalle2. From our tests, the Dalle2 API produced results quickly, although, we believed that the quality and design were not up to standards for the user to be able to generate an event page. We also considered incorporating GSAP for special effects, but the high learning curve led us to abandon this idea. Hence, we decided to go with the MidJourney API, which produced excellent results, however, the average user wait time was around 90 seconds which is significantly longer compared to Dalle2. While it was regrettable that the product couldn't be perfectly realized, we learned that rapid development involves constant trade-offs and compromises to achieve our goals. Conclusion In conclusion, we are grateful for the opportunity to complete an entire product development cycle. This experience allowed us to acquire new knowledge and skills. We hope our efforts will be reflected in a positive outcome in the competition. <div