---
slug: "circle-lhf970"
url: "https://devpost.com/software/circle-lhf970"
title: "Circle"
hackathon: "FigBuild 2026"
organization: "Figma"
winner: true
words: 940
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Circle

> Belonging: the invisible force behind every child who thrives, and every one who doesn't.

[Devpost](https://devpost.com/software/circle-lhf970) · hackathon [[FigBuild 2026]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[education]] [[immigration_refugee]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** figma, material-ui, motion, react, react-dnd, recharts, shadcn/ui, tailwind-css, using-react-18-with-vite, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for circle

## Body

Inspiration When we were in elementary school, neither of us was the kid who caused problems. We finished our work, we were polite, we were fine. But there were stretches of weeks, maybe longer, where we felt invisible. Not bullied, not struggling in any way a teacher could see. Just not quite included. We never said anything. Neither did our teachers. There was nothing to say. There was nothing to see. We built Circle because we think that should no longer be true. The research made it impossible to look away. Loneliness at age seven predicts suicidal ideation at fifteen at nearly \(19\times\) the rate of connected peers. Teacher accuracy in assessing student wellbeing is described in the literature as low to moderate . And 52% of K-12 teachers report burnout, the highest of any profession, meaning the people responsible for catching these kids are themselves running on empty. The problem isn't that teachers don't care. It's that caring is not the same as seeing. What it does Circle gives elementary school teachers a new sense: the ability to see which students feel like they belong, and which ones are quietly drifting, before weeks become months. It tracks participation events across group work and classroom discussion: who speaks, who gets responded to, who is never drawn into conversation, and surfaces patterns no teacher can see while managing 28 kids at once. A teacher with 28 students has \(\binom{28}{2} = 378\) possible pair relationships to track across a semester. Circle tracks all of them. The core features: Classroom setup : create a classroom, import students via CSV Grouping configuration : set group size and optimization goal: diversity of ideas, participation balance, or pure belonging Groupings map : student nodes colored by participation signal; tap any two to see their full relationship history and belonging trajectory Student profiles : longitudinal participation graphs, written summaries, a web graph of their six strongest peer connections End-of-day summary : what happened today, who needs attention tomorrow, and action items. How we built it We built Circle entirely in Figma Make. This turned out to be the hardest part of the project: closing the gap between the product we could see clearly in our heads and what the tool would actually produce. Getting there required a level of prompt engineering we didn't anticipate. We had to articulate our design vision with a precision that most design briefs never demand: exact color values pulled from reference images, why certain typographic choices mattered emotionally, the difference between a node that feels like data and one that feels like a child . Every screen went through multiple iterations. The craft bar we hold ourselves to is high, and meeting it inside Figma Make meant developing a real fluency, learning not just what to ask for, but how to describe taste. Challenges we ran into Restraint. The temptation with data tools is to show everything. But a teacher mid-lesson doesn't need a dashboard. She needs one signal. Designing a tool that does significant analytical work invisibly and surfaces only what matters was harder than building a tool that shows more. Honesty in the use cases. Early versions of the stories we told about Circle were vague: belonging signals , interaction patterns , language that sounded meaningful but didn't explain what Circle was actually measuring. We kept asking: why this student? Why this pairing? The answers had to be specific and causally clear, or the tool wasn't real. Getting there forced us to sharpen the product itself. Craft inside a generative tool. Figma Make is powerful, but it defaults toward the generic. Getting it to produce something that felt warm, considered, and intentional rather than another SaaS dashboard required us to develop a precise visual language and communicate it in prompts with a level of specificity most designers never have to make explicit. Accomplishments that we're proud of A design that feels like a tool , not a product: every visual decision made to respect the weight of what teachers are actually looking at Use cases that are causally honest: Circle doesn't just flag a student, it explains why Tom specifically , grounded in a semester of participation data across \(378\) relationships Safeguards we actually believe in: no permanent labeling, trajectories that reset each year, data that never leaves the device What we learned The asymmetry is the product. A teacher with 28 kids cannot hold \(378\) pair relationships in her head across 180 school days. Circle can. Once we were clear about that, once we stopped hiding behind vague language and said plainly what the tool sees that a human cannot, everything else became cleaner. The design, the stories, the feature set. Honesty turned out to be the best design constraint. We also learned that taste is a technical skill. Describing the emotional register of a typeface, the exact warmth of a color, the weight of a border that reads as care rather than structure . These are things designers usually leave implicit. Building in Figma Make forced us to make them explicit, and we are better designers for it. What's next for Circle The version we built is speculative: it imagines a future where passive classroom sensing is possible. But once the right sensing technology is here, the next step would be to pilot with one teacher, one classroom, one semester. We want to know whether the end-of-day summary changes what the teacher does the next morning. We think it will. We were both the kid who was fine. We both know what fine actually felt like. Circle is for that kid. There is one in every classroom. <div