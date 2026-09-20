---
slug: "kanga-slides-made-easy"
url: "https://devpost.com/software/kanga-slides-made-easy"
title: "Kanga: Streamlining Research Papers into Presentations"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1236
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Kanga: Streamlining Research Papers into Presentations

> We are making research more accessible by automatically generating understandable, concise, and aesthetically clean presentation slides from a research paper with just one click.

[Devpost](https://devpost.com/software/kanga-slides-made-easy) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** bun, canva, llm, node.js, openai, python, sdk, togetherai, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kanga

## Body

Inspiration There’s two fundamental issues we want to address: a) Research is not generally accessible to the public. Most people don’t want to spend hours trying to decipher jargon and figure out why a paper is important. b) Presenting research and making it accessible is a very tedious task. Authors have to compile their research into a presentation, figure out what key points to highlight, and what to present to make it understandable to those without industry knowledge. Plus – no one wants an ugly presentation, so significant time is spent on design too. Put together, this means that researchers spend a lot of time building presentations (our empirical survey found researchers spent ~5.8 hours on average building presentations) if they want to be able to present them to the general public. Yet, research is incredibly valuable in driving forward innovation, ensuring people understand what is happening in society, and helping inspire and educate students currently in school who will become further scientists and leaders. It's not enough for research to simply live in the bubble of academia -- the wider public (which are all impacted by research findings) need to be engaged, and there needs to be a easier way of doing that. What it does The current ways that people create slides: Slidesgo / SlidesCarnival: Tools like Slidesgo and SlidesCarnival only provide templates, rather than content creation. It is very time consuming to add content and design a presentation. Tome.ai / Gamma: These existing AI-powered slide generation tools do not have dynamic content creation and placement. These tools produced slides that look fragmented and do not flow as a full presentation. And neither are suitable for research presentations. Our system takes an URL to the PDF of the research paper, and retreives the research paper in order to summarize and compiled a structured presentation of the key background, contributions, and results of a given study. From there, we organize the data and assign it into logically-ordered slides broken down by purpose and dynamically render visual elements and text onto a Canva presentation. All of this is completed in under 60 seconds, where as most people don’t even have a title slide created during that time! How we built it We built this application onto of the Canva SDK in Typescript, using Bun as our runtime to speed up the backend. To process the PDF, we built an API endpoint using Together AI’s hosted Mistral 8x7B model and Python to provide cleaned text. From there, we stitched together multiple layers of LLM agents in order to analyze the research paper, extract the relevant information, convert the relevant information into slides, and organize the slides and content into Canva objects that are properly spaced and positioned. We also utilized Canva’s images library in order to add and implement dynamic styling of elements based on a user selected theme. Challenges we ran into Learning to use the Canva SDK was quite challenging, especially since it was recently released so the documentation describing various functionality and nuances were not as extensive. It was also very challenging and time consuming finding the most optimal LLM pipeline setup that ensured that any content we had was: Relevant, and concise Accurate and minimzed hallucinations. Finally, figuring out how to best position the content on a slide in a way that can be generalized to all research papers was a major challenge. We attempted to build out a system to generate more advanced / complex elements and layouts on the fly using LLMs, but were not able to complete this in time. Accomplishments that we're proud of We’re very proud of the pipeline we built — it's quite robust, and we’re able to parse essentially any research paper from any journal across any domain. This is no small feat, considering that there are libraries built specifically to parse certain journal articles from specific publications. We’re also quite proud of how coherently we were able to get content – it’s output in a very understandable manner that is simple and accurate. Finally, we’re very proud of the interface we built. A big part of our focus was around simplicity – unlike traditional design tools like Figma or Adobe XD, we aren’t catering our tool towards designers, but rather than researchers who frequently have minimal if any design experience. Therefore, we focused on minimize the complexity and failure cases that researcher would potentially face in the process, to make our tool as easy to use as possible. We're excited to be working on a big problem that has to potential to change the way research is being communicated if our solution works -- the "no-code" design market is ~60B USD (Canva's TAM is ~40B). Universities alone spent ~20B USD on software tools. We estimate that the demand for good design tools at research institutions is at least ~3B USD -- given that there's no other tool on the market doing this, we'd be positioned for significant market capture, and that's before we expand beyond just research. What we learned We learned a lot about working with Canva’s SDK, which we found quite impressive. We believe there’s a lot of potential for AI to be integrated more tightly into the Canva ecosystem through it's SDK to supercharge how people design presentations and event posters. Furthermore, given that accuracy is very important in research contexts, we learned about techniques to minimize LLM hallucination — reducing the temperature parameter of models, and breaking tasks into smaller subtasks that can be processed iteratively. Finally, through the process, we learned how important it was to effectively communicate and delegate tasks – at first, we had multiple team members working on similar sub-projects because while we were all clear on the components we needed to build to make this project work, there was a bit of miscommunication as to the best way to divide up the necessary components to develop, given a lot of components have significant interdependency. What's next for Kanga We plan on applying for the Canva Innovation Fund to further develop this project. We’d also like to refine the various stages of this process. While in 36 hours we managed to build out an arguably-impressive prototype, there’s a lot of room for improvement, especially in terms of designing more presentation-ready papers. Some features we’d lile to implement include: Extracting relevant diagrams and images from papers and positioning them within slides Generating icons and diagrams that present various contributions and concepts discussed within the paper using Dalle / SDXL Building more variety in the positioning of elements and layouts within a slide show Providing for fine grained control over the final result of the presentation Expand beyond just presentations into posters and other graphics Given ample time, we’d also like to fine-tune our own LLM models that are catered towards distilling research information, to ensure that we are capturing the most optimal contributions and key points with maximum accuracy. We want to become the default app for Canva users and become part of their daily workflow, and ideally be integrated fully into Canva as a “design-assist” agent and get acquired by Canva in 18 months. We’d use a variety of per-user pricing plans to generate revenue, primarily catering towards researchers and educational institutions, where we’d be able to close high-value contracts and push our product to a large amount of relevant users (stuents, professors, researchers) very quickiy. <div