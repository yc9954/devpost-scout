---
slug: "master-your-garden"
url: "https://devpost.com/software/master-your-garden"
title: "Meet Mr. Garden Gnome"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 1085
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/education"
  - "substrate/video_visual"
---

# Meet Mr. Garden Gnome

> Master Gardeners is an NGO that donates tons of vegetables to fight hunger! Mr. Garden Gnome AI assistant helps them grow more by helping them visualize garden, plant right plants, and fight pests.

[Devpost](https://devpost.com/software/master-your-garden) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[agriculture_food]] [[education]]
**substrate** [[video_visual]]

**stack** bedrock, claude, diffusion, stable

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for meet mr. garden gnome!

## Body

Home page of my App. Inspiration The achievements of the US master gardening community truly amazed me. My firsthand experience with the Dallas chapter revealed a community of passionate senior members. Most had retired after successful careers and now dedicate themselves to gardening and giving back through vegetable gardens, school gardens, and arboretums. These master gardeners use this time to practice earth kind gardening practices and produce fruits, flowers, and vegetables that are donated to families in need and soup kitchens around US. What it does My project caters to gardeners. The application accepts weather conditions, garden style, garden style, and recommends following: Plant selection appropriate for location and intended garden style - Planting right combination of plants which would thrive in the hardiness zone specified is extremely important for gardeners. Flowers attract pollinators which are required for pollinating vegetable garden for producing good yield. Pest control - Master gardeners often come across different kinds of pests which they must control with organic gardening techniques. Using organic methods is an earth kind principle which refrains introducing any harmful chemicals into earth. Expert advice - Often questions these master gardeners have are quite tricky and there are very few right answers. For example, how should I treat a jasmine plant before bringing it in for overwintering. With AI assistant, they get the right answers in a short span. Garden visualization - Application provides sample visualizations of a garden that shows recommended plant combinations. Resources - Gardeners often like reading books that inform them about gardening techniques. How I built it Using Partyrock was really simple. After exploring sample applications, I started typing what I was looking for. By simply typing a paragraph of requirements, I was able to get a good starting point to work from. I spent some time in identifying exactly what would a master gardener benefit from. Once I had identified requirements, I started playing with different widgets to come up with an outline of the partyrock application. Thats when the fun started. I started exploring bedrock console to understand which model can do what. Task 1: Recommended flowers/plants . The task is a combination of Ideation and information extraction task. From the table it was clear that Jurassic-2 ultra, Jurassic-2 mid, cohere, Claude, and Claude 2 instant fit the information extraction use-case. All 5 models, as well as amazon titan models, did a pretty good job at coming with a list of popular vegetables/flowers. However, Jurassic 2 ultra exceeded my expectations and also returned description of the flower/vegetable as well. It was clear that Jurassic 2 Ultra was the model I wanted to proceed with. I also played with the prompt and ensured all the inputs required were incorporated into the prompt. Prompt finalized Based on the USDA Zone [USDA Hardiness Zone - 3a to 11b], [Garden Style] and [Garden plants] entered, generate a list of total 10 recommended plants to grow in a markdown format. Strictly stick to plants that flower and do well in season [Season]. provide separate lists for each plant type listed Claude did a good job of recommending propagation, planting, and harvesting dates for each plant after I provided information about last frost date. Task 2: Identify pests that would affect the garden as well as organic, earth-kind remedies for pests : For the same prompt, I received different kind of results. Llama 2 Chat 70B provided a detailed list of pests that would affect each plant as well as corresponding organic remedies. However, Jurrasic Ultra 2 provided total 5 different pests that I should be concerned with. Similarly, Titan and Claude instant also provided list of 5 pests, however, Claude's output elaborated organic remedies, which is what a gardener would benefit from. Task 3: Show 3 different visualizations of the garden : This task was quite interesting. I wanted to try the Amazon's image generation model here but turns out only stable diffusion is available via Partyrock. I spent some time trying different style preferences such as Analog film, fantasy art but found that they did not serve the purpose. I wanted a realistic visualization. I ended up finalizing 3D model as the style preset. I also tried advanced settings and ended up settling with the cfg = 16 value. Also, Seed = 0 generated most interesting images. Prompt finalized -show mountain, a cottage, sky, tree in background. In foreground display a garden with different plants/trees listed in [Recommended Plants for your garden]. Focus on garden. Ensure at least 60% of area in image shows garden, 15% of the area in image shows a english cottage. Garden should not show any plants not listed in [Recommended Plants for your garden] Similarly, I provided identical prompts for the other two options while asking them to choose plants which were not dominant in previous option(s). Bonus task: I also used Titan Text lite to describe all three options in word format. Task 4: Gardening FAQs and Resources - Claude, titan express, as well command performed well in coming up with list of resources. However, Command's response in resources was more reader friendly. I ended up finalizing Command for FAQs and Claude for recommended reading. Task 5: Chatbot - Llama 2 70B definitely did a great job answering some really tough gardening questions. Challenges I ran into Models require additional metadata - Some tasks required additional metadata to be provided. E.g. I wanted the application to also suggest appropriate date for starting seeds, planting and harvesting and it was clear that none of the models could figure out the right dates without being told about the last frost date in the region. Be careful about tuning parameters - cfg, seed are responsible for controlling model's behavior. Changing values too much can lead to unexpected results. Accomplishments that I am proud of I feel that I have actually built something that master gardeners could use. I would love to explore this idea further. I am really glad that I participated in this hackathon. I got to play with different models for free, instead of having to pay for them with Amazon bedrock. AWS should keep this free forever :) What I learned A ton. this was a great exercise of not only learning bedrock but also an easy way of navigating the realm of generative AI without having to write a single code. What's next for Meet Mr. Garden Gnome! I would love to convert this into an actual application and see if there is a product market fit. <div