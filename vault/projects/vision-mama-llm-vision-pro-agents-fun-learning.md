---
slug: "vision-mama-llm-vision-pro-agents-fun-learning"
url: "https://devpost.com/software/vision-mama-llm-vision-pro-agents-fun-learning"
title: "Vision Mama: LLMs + Vision Pro + Agents = Cooking Magic"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1395
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Vision Mama: LLMs + Vision Pro + Agents = Cooking Magic

> Remember Cooking Mama? We turned it into a Conversational Agent for Vision Pro that teaches cooking! We pretrained & fine-tuned recipe making LLMs, made a food ordering agent, semantic recipes,...

[Devpost](https://devpost.com/software/vision-mama-llm-vision-pro-agents-fun-learning) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[finance_payments]]
**user** [[clinician]] [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** cursor, finetuning, github, gpt, intersystems, iris, jupyternotebook, lora, mistral, mixedreality, monsterapi, openai, python, reflex

## How they structured the write-up

- the future of computing 🍎 👓 ⚙️ 🤖 🍳 👩‍🍳
- what we created
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vision mama: llm + vision pro + agents = fun & learning
- impacts
- concerns

## Body

Page through the gallery to PLAY VISION MAMAAAAA!! Keep going to find out what's new! Keep going! Read our detailed Devpost for more! we ran experiments on fine-tuning a 7b model to write recipes! we pretrained a tiny language model that is 4,375x smaller than GPT-3! And it worked kinda ok!! Here's the training loss curve for the LLM if you like that kind of thing! :) No Vision Pro? Check out our web-based AI agent at recipes.reflex.run We use SERP API and a neat optimization algorithm to find the cheapest ingredients for your recipe and with minimal stores visited. Click through our slideshow for a neat overview!! Check out our demo video The future of computing 🍎 👓 ⚙️ 🤖 🍳 👩‍🍳 How could Mixed Reality, Spatial Computing, and Generative AI transform our lives? And what happens when you combine Vision Pro and AI? (spoiler: magic! 🔮) Our goal was to create an interactive VisionOS app 🍎 powered by AI. While our app could be applied towards many things (like math tutoring, travel planning, etc.), we decided to make the demo use case fun. We loved playing the game Cooking Mama 👩‍🍳 as kids so we made a voice-activated conversational AI agent that teaches you to cook healthy meals, invents recipes based on your preferences, and helps you find and order ingredients. Overall, we want to demonstrate how the latest tech advances could transform our lives. Food is one of the most important, basic needs so we felt that it was an interesting topic. Additionally, many people struggle with nutrition so our project could help people eat healthier foods and live better, longer lives. What we created Conversational Vision Pro app that lets you talk to an AI nutritionist that speaks back to you in a realistic voice with low latency. Built-in AI agent that will create a custom recipe according to your preferences, identify the most efficient and cheapest way to purchase necessary ingredients in your area (least stores visited, least cost), and finally creates Instacart orders using their simulated API. Web version of agent at recipes.reflex.run in a chat interface InterSystems IRIS vector database of 10k recipes with HyDE enabled semantic search Pretrained 40M LLM from scratch to create recipes Fine-tuned Mistral-7b using MonsterAPI to generate recipes How we built it We divided tasks efficiently given the time frame to make sure we weren't bottlenecked by each other. For instance, Gao's first priority was to get a recipe LLM deployed so Molly and Park could use it in their tasks. While we split up tasks, we also worked together to help each other debug and often pair programmed and swapped tasks if needed. Various tools used: Xcode, Cursor, OpenAI API, MonsterAI API, IRIS Vector Database, Reflex.dev, SERP API,... Vision OS Talk to Vision Mama by running Whisper fully on device using CoreML and Metal Chat capability powered by GPT-3.5-turbo, our custom recipe-generating LLM (Mistral-7b backbone), and our agent endpoint. To ensure that you are able to see both Vision Mama's chats and her agentic skills, we have a split view that shows your conversation and your generated recipes Lastly, we use text-to-speech synthesis using ElevenLabs API for Vision Mama's voice AI Agent Pipeline for Recipe Generation, Food Search, and Instacart Ordering We built an endpoint that we hit from our Vision Pro and our Reflex site. Basically what happens is we submit a user's desired food such as "banana soup". We pass that to our fine-tuned Mistral-7b LLM to generate a recipe. Then, we quickly use GPT-4-turbo to parse the recipe and extract the ingredients. Then we use the SERP API on each ingredient to find where it can be purchased nearby. We prioritize cheaper ingredients and use an algorithm to try to visit the least number of stores to buy all ingredients. Finally, we populate an Instacart Order API call to purchase the ingredients (simulated for now since we do not have actual partner access to Instacart's API) Pre-training (using nanogpt architecture): Created large dataset of recipes. Tokenized our recipe dataset using BPE (GPT2 tokenizer) Dataset details (9:1 split): train: 46,826,468 tokens val: 5,203,016 tokens Trained for 1000 iterations with settings: layers = 12 attention heads = 12 embedding dimension = 384 batch size = 32 In total, the LLM had 40.56 million parameters! It took several hours to train on an M3 Mac with Metal Performance Shaders. Fine-tuning While the pre-trained LLM worked ok and generated coherent (but silly) English recipes for the most part, we couldn't figure out how to deploy it in the time frame and it still wasn't good enough for our agent. So, we tried fine-tuning Mistral-7b, which is 175 times bigger and is much more capable. We curated fine-tuning datasets of several sizes (10k recipes, 50k recipes, 250k recipes). We prepared them into a specific prompt/completion format: You are an expert chef. You know about a lot of diverse cuisines. You write helpful tasty recipes.\n\n###Instruction: please think step by step and generate a detailed recipe for {prompt}\n\n###Response:{completion} We fine-tuned and deployed the 250k-fine-tuned model on the MonsterAPI platform, one of the sponsors of TreeHacks. We observed that using more fine-tuning data led to lower loss, but at diminishing returns. Reflex.dev Web Agent Most people don't have Vision Pros so we wrapped our versatile agent endpoint into a Python-based Reflex app that you can chat with! Try here Note that heavy demand may overload our agent. IRIS Semantic Recipe Discovery We used the IRIS Vector Database, running it on a Mac with Docker. We embedded 10,000 unique recipes from diverse cuisines using OpenAI's text-ada-002 embedding . We stored the embeddings and the recipes in an IRIS Vector Database. Then, we let the user input a "vibe", such as "cold rainy winter day". We use Mistral-7b to generate three Hypothetical Document Embedding (HyDE) prompts in a structured format. We then query the IRIS DB using the three Mistral-generated prompts. The key here is that regular semantic search does not let you search by vibe effectively. If you do semantic search on "cold rainy winter day", it is more likely to give you results that are related to cold or rain, rather than foods. Our prompting encourages Mistral to understand the vibe of your input and convert it to better HyDE prompts. Real example: User input: something for a chilly winter day Generated Search Queries: {'queries': ['warming winter dishes recipes', 'comfort food recipes for cold days', 'hearty stews and soups for chilly weather']} Result: recipes that match the intent of the user rather than the literal meaning of their query Challenges we ran into Programming for the Vision Pro, a new way of coding without that much documentation available Two of our team members wear glasses so they couldn't actually use the Vision Pro :( Figuring out how to work with Docker Package version conflicts :(( Cold starts on Replicate API A lot of tutorials we looked at used the old version of the OpenAI API which is no longer supported Accomplishments that we're proud of Learning how to hack on Vision Pro! Making the Vision Mama 3D model blink Pretraining a 40M parameter LLM Doing fine-tuning experiments Using a variant of HyDE to turn user intent into better semantic search queries What we learned How to pretrain LLMs and adjust the parameters How to use the IRIS Vector Database How to use Reflex How to use Monster API How to create APIs for an AI Agent How to develop for Vision Pro How to do Hypothetical Document Embeddings for semantic search How to work under pressure What's next for Vision Mama: LLM + Vision Pro + Agents = Fun & Learning Improve the pre-trained LLM: MORE DATA, MORE COMPUTE, MORE PARAMS!!! Host the InterSystems IRIS Vector Database online and let the Vision Mama agent query it Implement the meal tracking photo analyzer into VisionOs app Complete the payment processing for the Instacart API once we get developer access Impacts Mixed reality and AI could enable more serious use cases like: Assisting doctors with remote robotic surgery Making high quality education and tutoring available to more students Amazing live concert and event experiences remotely Language learning practice partner Concerns Vision Pro is very expensive so most people can't afford it for the time being. Thus, edtech applications are limited. Data privacy Thanks for checking out Vision Mama! <div