---
slug: "foodi-copilot"
url: "https://devpost.com/software/foodi-copilot"
title: "Foodi Copilot"
hackathon: "Microsoft Developers AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 950
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/mental_health"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Foodi Copilot

> Foodi Copilot:Your AI-powered food assistant. Get personalized recipe suggestions, nutritional insights, and food product information using text or image queries. Powered by Azure OpenAI and Cosmos DB

[Devpost](https://devpost.com/software/foodi-copilot) · hackathon [[Microsoft Developers AI Learning Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[finance_payments]] [[mental_health]] [[retail_commerce]] [[scientific_research]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[genomic_bio]] [[structured_db]] [[video_visual]]

**stack** azure, azure-openai, cosmosdb, fastapi, gpt4o, python, react, typescript

## How they structured the write-up

- the spark
- what i hoped to create
- the build: a learning adventure
- the "what did i get myself into" moments
- small wins that kept me going
- lessons learned (the hard way)
- the "maybe someday" list
- what's next: the "definitely after hackathon" plan
- the azure toolkit that made this possible

## Body

identify ingredients feature gluten free aware search Foodi Copilot: A Solo Developer's AI-Powered Nutrition Adventure The Spark I'm just a developer who loves food but struggles with health. Deciphering food labels and balancing my diet has always been a challenge, especially with my digestive issues. I can't count how many times my wife called asking where I was when she sent me for groceries - I'd be hopping between stores, desperately trying to find products that fit my health needs and calorie goals. It was during one of these marathon shopping trips that the idea for Foodi Copilot was born. What I Hoped to Create I dreamed of an AI assistant that could: Suggest recipes tailored to individual dietary needs Break down nutritional info in a way that actually makes sense Analyze food products from text or images (because squinting at labels is no fun) Answer all those random food questions we all have The Build: A Learning Adventure Armed with more enthusiasm than expertise, I dove into Azure services: Frontend: Wrestled with React and TypeScript, somehow made it look decent with Fluent UI Backend: Python and FastAPI, containerized in Azure (sounds fancy, right?) AI Magic: Azure OpenAI Service (still amazed this works, big bow to gpt4o) Data Home: Azure Cosmos DB for MongoDB vCore (vector search was a game-changer) AI Conductor: Langchain (because one AI wasn't complex enough) The "What Did I Get Myself Into" Moments Past attempts felt like trying to build a spaceship with duct tape. Vector search finally made it possible. Integrating Azure services solo? Let's just say I have a love-hate relationship with documentation now. Training food recognition models made me question my life choices more than once. Balancing personalized recommendations with not accidentally poisoning someone was... fun. Solo development: Turns out, being a one-person team means a lot of talking to rubber ducks. Nights and weekends became my new "work hours." My family started to wonder if I'd been replaced by a coding zombie. (Spoiler: I kind of was.) Small Wins That Kept Me Going The day vector search actually worked felt like winning the lottery. Building an interface my mom could use without calling me for help. Creating an AI system that doesn't just say "I don't know" to every question. Getting Azure Computer Vision to recognize a burrito (it was the little things). My cousin Al using an early version and not immediately giving up on it. That moment when my wife realized why I'd been glued to my computer every evening - and actually thought it was cool. (Don't worry, I'm as surprised as you are.) Lessons Learned (The Hard Way) Vector search isn't just a buzzword - it's a lifesaver for AI apps. AI agents, LLMs, and databases can work together... after a lot of coaxing. Cloud services are amazing, once you figure out how to use them without breaking the bank. Solo development requires the patience of a saint and the caffeine tolerance of a college student. Azure and Langchain are powerful, but they won't do your dishes or walk your dog. The "Maybe Someday" List Expand the database to include foods my grandma would recognize. Integrate Azure Health Bot (because clearly, I enjoy complex integrations). Mobile app development - because who doesn't need more screen time? Add voice interactions, so I can argue with my phone about calories. Partner with health experts who can validate that I'm not completely off track. Build a community feature, turning my solo project into a group therapy session for health-conscious devs. What's Next: The "Definitely After Hackathon" Plan Look, I'm not stopping just because the hackathon ends. This thing has become my digital baby, and I'm committed to helping it grow (unlike my actual muscles... yet). Here's what's cooking: Adding user authentication: Because apparently, not everyone wants to share their burrito cravings with the world. Implementing user preferences: So Foodi Copilot can remember that I've been trying to bulk up (spoiler: protein shakes are involved). Expanding diet profiles: My cousin's keto journey needs all the low-carb, high-fat support it can get. Weight loss tracking: My sister's on a mission to shed some pounds, and Foodi Copilot's going to be her new best friend (sorry, sis). I'm basically turning my family into guinea pigs for this app. They're thrilled. (Okay, they're tolerating it, but that's basically the same thing, right?) The Azure Toolkit That Made This Possible Azure Cosmos DB: Turns out, databases can be more than just boring tables. Azure OpenAI Service: Because sometimes, you need an AI smarter than you to figure things out. Langchain and LLM Agents: For when you want to feel like an AI orchestra conductor. Azure Computer Vision: Teaching machines to see food so I don't have to squint at labels. Vector Search: The unsung hero that turned this from a pipe dream into something almost useful. Foodi Copilot isn't just an app; it's my diary of late nights, coding frustrations, and small victories. It's far from perfect, but it's a step towards making healthy eating less of a puzzle. Every time I use it and don't immediately reach for takeout, I count it as a win. This journey has been humbling, exhausting, and incredibly rewarding. I'm still learning, still improving, and still amazed when something actually works as intended. If this project helps even one person make healthier choices (besides me, my protein-obsessed self, my keto cousin Al, and my calorie-counting sister), I'll consider it a success. Who knows, maybe one day Foodi Copilot will help someone else navigate the nutritional maze without losing their mind in the cereal aisle. A developer can dream, right? And hey, maybe I'll even get my weekends back... eventually. <div