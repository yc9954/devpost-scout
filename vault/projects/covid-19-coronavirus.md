---
slug: "covid-19-coronavirus"
url: "https://devpost.com/software/covid-19-coronavirus"
title: "COVID-19 Instagram AR Experience"
hackathon: "Facebook Hackathon: AR"
organization: "Facebook"
winner: true
words: 1298
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/media_journalism"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# COVID-19 Instagram AR Experience

> An educational augmented reality experience about COVID-19 that explores the virus' origin, transmission, structure, effects, prevention measures, and more

[Devpost](https://devpost.com/software/covid-19-coronavirus) · hackathon [[Facebook Hackathon- AR]]

## Facets

**domain** [[media_journalism]] [[retail_commerce]] [[scientific_research]]
**substrate** [[video_visual]] [[web_dom]]

**stack** blender, editor, javascript, patch, photoshop, sparkar

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for covid-19 coronavirus instagram ar experience

## Body

COVID-19 Coronavirus AR Experience - Chapter Showcase COVID-19 Coronavirus AR Experience - SparkAR Patch Editor COVID-19 Coronavirus AR Experience - Photos from Viewers Around the World COVID-19 Coronavirus AR Experience - QR Code Inspiration It's often said that "You should meet people where they are." That's why I created an educational COVID-19 Coronavirus AR experience on Instagram, with the intention of providing some baseline knowledge to a demographic that doesn't watch the news or read a daily paper, but instead stays informed through their network on social media. As this story developed, I found an extremely positive side effect of this experience was that viewers began taking the virus much more seriously (and stopped making it the butt of a joke / meme), as the AR effect helped put a more tangible face to the virus and and this very serious situation. In addition to the cause behind this effect, I also wanted to see how far I could push the platform both technically and in using it for education / journalism, in a way that's not been fully realized on the platform until now. What it does The COVID-19 Coronavirus effect is a 5-minute, 6-chapter, world-based educational augmented reality experience, that informs viewers about the SARS-CoV-2 Coronavirus that’s currently spreading around the world. Beyond just visualizing the virus in augmented reality, the AR effect also teaches viewers about the virus' origins, how it spreads, it's structure, replication, potential economic impact, prevention measures, and more, all communicated through the individual chapters within the experience. How I built it I built the AR effect in Facebook's SparkAR platform throughout most of the month of February (2020), spending roughly 160 hours writing the script, editing audio, Photoshopping textures, creating and optimizing 3D models in Blender, animating components, and designing the AR logic to both run + consistently reset the experience. This is in addition to nearly 100 hours of research starting back in January and continuing alongside development in February. The individual chapters are accessed via Instagram's Native UI Picker, which was patched through to the Patch Editor in SparkAR, where individual scenes were turned on and off based on the chapter selection. Apart from the human sneezing in Chapter 2 (animated in Blender), all animations were created inside of SparkAR, which I have found to be most effective for performance. The script and information contained within the experience is all based on WHO / CDC recommendation or peer-reviewed papers, and even had a handful of CDC and St. Jude employees give me positive remarks on the finished effect. Challenges I ran into The challenges in building this experience were of two very different types; one being technical, and the other being controversial. technical The technical challenge to accomplish this amount of content in a single Instagram AR effect was immense, given the 4MB file size restriction for the entire effect. The effect contains 7x music tracks and 6x narrations, all of which had to fit in just 1.1MB of space. This meant the music loops had to be short but sound convincingly longer than they were, and narration had to be trimmed to just the most important information. On the visual side of things, I had to heavily optimize 3D content, often removing a few hundred vertices at a time from models and replacing them in the project, just to buy back a few precious kbs of space. I was even forced to remodel the virus several times over from scratch, as it was important that it was a very detailed model, but also had to not take up too much of the precious file size allotment. I also find it more challenging to reset every state in any SparkAR experience than it is to animate and build the logic in the first place. You have to be able to anticipate a massive range of user behaviors and then build logic that tries to handle that. For example, if a user navigates off of one chapter and onto another before the first one finished, they can do that at any interval of time, so ensuring both chapters reset fully was fairly difficult. controversial The challenges of creating an experience like this around a developing story is that once the disease starting spreading in the US and Europe, misinformation, poor-taste humor, and minimization of the situation begun to run rampant. Both media outlets and creators publicized a number of negative / misinforming COVID-19 effects to their massive digital audiences, eventually forcing Instagram's hand in severely restricting COVID-19 AR effects on the platform, and limiting the reach and discoverability of effects like mine without an official CDC / WHO endorsement. Accomplishments that I'm proud of I'm extremely proud to have created the first long-form narrative educational / journalism AR experience on Instagram. I think this experience will set a new bar for educational / journalistic experiences on the platform in the future, should they be attempted. I'm also very grateful to have reached a global audience who was genuinely thankful and excited for this experience, as it gave them information they likely would not have received otherwise, and has almost certainly saved one or more people from becoming infected. After hearing the overwhelming, direct-feedback from nearly 100 users around the world, the AR experience seems to have really resonated with people in giving them a better understanding of what this virus really is. What I learned From the controversy around the COVID-19 Coronavirus, my biggest takeaway is that I'm not sure if Instagram as an AR platform is fully ready developing stories or educational experiences (but to be fair, most things on Earth were not fully ready for this virus, how could we be?). One thing that makes it particularly hard to showcase factual information is that you can't write text or direct people to other webpages (per Instagram AR platform rules), so citing sources becomes a tricky and indirect endeavor. The infamous "With great power comes great responsibility" quote comes to mind, as Instagram is a platform with a lot of power (in the number + engagement of your users), and of course a responsibility to them as well. Much of Instagram's community is going to continue to get it's news from the platform, whether it's via an AR experience, or an image, or any other piece of content. In general, I think social media as a whole has a massive hurdle on it's hands in battling misinformation. This was especially evident as so many viewers around the world wrote-in to us and send me pictures, thanking us for making the experience, bringing a non-fear mongering awareness to the situation, but also sharing information they had learned that wasn't discussed in other posts they'd seen. It was also extremely powerful to connect with these individuals and hear their stories about their country's current situations from all over the globe, and empower them to begin preparing for a new (potential) reality of widespread infection. What's next for COVID-19 Coronavirus Instagram AR Experience On a technical level, the effect needs to be updated to reflect the current contagion locations on the globe [Chapter 1], as well the slightly reworded guidelines from the CDC/WHO regarding facemasks ([Chapter 6] change "not a proven preventative measure" to "not a recommended preventative measure"). On a more realistic level, what this AR effect really needs to be successful on Instagram is a fact-checking review (followed by content revision) and then an approval from a CDC / WHO source, so it can be shared through the proper channels (via search, via official partners, etc) on Instagram. I would be more than happy to revise the project with more up-to-date information and messaging, and could even envision another chapter that discusses social distancing / sanitation in more depth. <div