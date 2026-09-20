---
slug: "theo-k1enau"
url: "https://devpost.com/software/theo-k1enau"
title: "theo"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 864
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
---

# theo

> a cognition copilot that distills your thoughts from pen to perspective

[Devpost](https://devpost.com/software/theo-k1enau) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** agents, ai, elasticsearch, embeddings, firebase, google-cloud, mistral-large, rag, react-native

## How they structured the write-up

- overview
- problem
- solution
- why theo
- accomplishments that we're proud of
- how we built it
- challenges we ran into
- what we learned
- what's next for theo

## Body

Overview Problem Solution Architecture App homepage Annotations Agent scheduling Overview theo is a cognition copilot that distills your thoughts from pen to perspective. You can think of theo in two ways. In buddhist thinking, papañcha is the word for conceptual proliferation — when you’re overthinking about the world and have a swirl of thoughts attacking you from all directions until you’re stressed but don’t know what to do. theo helps you take this swirl of thoughts and distill them into understanding and action. From the perspective of an “epidemic of busyness”, we are constantly surrounded by stimuli and noise that prevent us from taking 5 minutes to take a step back. theo is a cognition OS that analyzes your written notes, prompts you for reflection, sparks connections with your earlier thoughts, and suggests actionable steps in your calendar. A lot of people are building a second brain for productivity — we are building a second brain for cognition. Problem Everyone is in a constant swirl of work, studies, and chores, with little time in a day to step back and process emotions and feelings, reflect on actions and priorities, and identify values and goals. On top of that, with social media, informational noise around us, and pressing global challenges, making this conscious step to recap your day became only more difficult. In the midst of these modern factors, people end up feeling overwhelmed, lost, or anxious, without the means to truly understand why or how to work through it. Helping people understand themselves better is a key to a more lucid, productive, purposeful future for humanity. Solution theo is an AI-powered cognitive workflow that helps users clarify their thinking through writing. When a user inputs journeys – whether scattered ideas, reflections, or unstructured thoughts – theo extracts valuable insights, identifies patterns across past entries, and asks intelligent follow-up questions to spark self-reflection. For every thought journey you write down, theo can leave three types of annotations: connections: relations between the current journey and your previous web of thoughts; questions: focused questions based on the recent notes to spark reflection; actions: suggestions for calendar events to take actionable steps to work on your goals -- one click integration with calendar apps. Additionally, it can prompt you with personalized questions to start your journeys. Why theo Unlike a standard note-taking app, theo transforms raw cognition into structured insight. Unlike a typical agent, it aims to gently guide rather than overcorrect and oversuggest. For example, in annotations, theo first and foremost shows the user their previous thoughts, but deliberately does not give its own analysis on top of them. Additionally, the number of question annotations is kept to be low to not cause a feeling of overwhelm. We assist the user in distilling their thinking instead of thinking for them. Accomplishments that we're proud of We’re proud of building an AI tool that doesn’t just optimize for efficiency but also for depth of thinking. Seeing theo make successful connections between separate thoughts and building valuable insights was a major win. We also prioritized user experience, making sure theo feels like a natural extension of the user’s mind rather than an overwhelming AI assistant. How we built it For this hackathon, we tried incorporating a myriad of new and exciting frameworks into our tech stack. We relied on a React-Native frontend as well as Firebase’s Cloud Functions for our backend, as we wanted our users to be able to journal on the fly. We used Firestore as a general-purpose no-SQL datastore and ElasticSearch to run vector search on our embeddings. Finally, we used Mistral’s fast models for our agentic behavior. This combination of frameworks enabled us to achieve flexible functionality when it came to meeting our app’s functional requirements. Challenges we ran into The architecture of the foundation – the full stack app itself was smooth sailing. However, as many developers who work with AI agents know, we quickly learned that AI agents are unreliable, with LLM output outright hallucinating inconsistent behavior. In particular, we struggled with querying elastic search for semantically similar journals using a vector search, as Elastic search’s semantic search function returned to us different output every time we called one of our HTTP endpoints. Getting the annotations working proved an enormous difficulty as well, requiring us to design an entire mental module associated with indexing the characters on screen. What we learned We gained deeper insight into how AI can facilitate cognition rather than just automate tasks. Through testing, we saw firsthand how prompting users with the right reflection questions can unlock new insights, giving us a glimpse of how AGI might go about functioning. On the technical side, we learned a lot about embeddings, vector similarity, and how to design an effective note-retrieval system. What's next for theo We see theo evolving into a more personalized and adaptive cognition copilot. Future iterations will include improved contextual understanding, allowing theo to better detect a user’s current mindset and tailor its prompts accordingly, and orienting user within their complex web of thoughts by visualizing connections between different journeys. theo is more than a productivity workflow — it’s a thinking partner for a clearer mind. <div