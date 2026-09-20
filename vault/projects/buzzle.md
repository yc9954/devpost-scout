---
slug: "buzzle"
url: "https://devpost.com/software/buzzle"
title: "Buzzle"
hackathon: "AWS Presents: Breaking Barriers Virtual Challenge"
organization: "Amazon"
winner: true
words: 1120
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
---

# Buzzle

> A screenless educational toy. Powered by AWS generative AI and connected to global telecom networks to help kids anywhere learn anything, in a fun, hands-on way.

[Devpost](https://devpost.com/software/buzzle) · hackathon [[AWS Presents- Breaking Barriers Virtual Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[education]]
**user** [[educator_student]] [[general_public]]

**stack** amazon-cloudwatch, amazon-dynamodb, amazon-web-services, arduino, awsbedrock, hardware, lambda, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for buzzle

## Body

Buzzle Demo 3D CAD Model Virtual Demo Buzzle on my 3D printer I made a virtual demo version of buzzle so you can test out the product without any of the hardware components. Turn your sound up to play! https://master.dkacxx6d0omvo.amplifyapp.com/ Have Fun! Inspiration In a world where kids are drowning in screens—or left behind without them—we saw a growing divide. While some children are overwhelmed by digital noise, others in rural and low-income areas lack access to digital learning altogether. But, what if learning could be joyful, screen-free, and accessible anywhere? That’s when Buzzle was born—a voice-interactive, AI-powered learning toy that turns screenless play into smart learning. What it does Buzzle is a screen-free educational game system that uses RFID-based tokens and voice interaction to teach kids core subjects like math, language, and music. Here's how it works: Step 1: Pick a character. Each token has an RFID tag and a distinct voice powered by Amazon Polly . Step 2: Choose a subject. Tokens launch themed lessons or games. Step 3: Select a mode. “Learn” mode explains concepts; “Game” mode challenges the learner. Step 4: Talk to Buzzle! Using an onboard mic + LTE module, kids respond out loud. Their answers are analyzed in the cloud using AWS Bedrock, AWS Lambda and AWS API Gateway , and difficulty is adjusted in real time via AWS DynamoDB . Buzzle works without Wi-Fi and is built to operate over cellular networks via a 5G module, making it usable even in remote or underserved regions. How we built it We built Buzzle as a hybrid of physical and digital systems: AWS Software: Amazon Polly - Voices for Princess Emma, Liam, etc. AWS Lambda- Processes user input, calls Bedrock, Polly, and DynamoDB Amazon Bedrock - Creates game content, lessons, and dialogue Amazon DynamoDB - Stores session history and adjusts difficulty level Amazon CloudWatch - Observes system flow, error alerts, debugging AWS Amplify Hosting - and deployment of the virtual web demo Amazon API Gateway - Manages HTTP request/response to Lambda AWS IAM - Controls access to Bedrock, Polly, DynamoDB, etc. Hardware: ESP32 Dev Board to read RFID tokens and trigger actions INMP441 microphone for capturing voice input 4G LTE module to transmit/receive data without Wi-Fi 3D-printed shell designed for kids, with tactile buttons and slots Challenges we ran into First up: CAD modeling. Designing a toy that’s both kid-friendly and functional was way harder than it seemed. Our first few 3D prints were either too bulky, too fragile, or didn’t fit the electronics properly. We had to go through multiple redesigns just to make sure the NFC reader could sit in the right spot and that kids could interact with it easily. Then came the 5G challenge. We designed Buzzle to be 5G-ready, but in reality, we used a 4G LTE module for the demo due to hardware access limitations. To be transparent: it worked, but bandwidth and latency weren’t always consistent. Still, we built the architecture to scale with full 5G, and the LTE fallback helped us test in real-world network conditions. And while AWS gave us incredible building blocks—like Polly, Bedrock, Lambda, and DynamoDB—it wasn’t plug-and-play. We had to deeply understand how each service worked, especially how to optimize Bedrock latency, manage Lambda timeouts, and handle DynamoDB queries without slowing things down. Bedrock is insanely powerful, but it requires really clean prompt engineering and solid flow control to get consistent results, especially with kids involved. And of course, there were voice UX issues. Our mic setup (INMP441) would pick up ambient noise, or not hear kids clearly if they spoke too softly. On top of that, younger kids don’t always speak in full, clean phrases—so we had to rethink how we handled voice parsing and start prototyping on-device keyword detection to make things smoother. Accomplishments that we're proud of We are super proud that we didn't just slap together a software product. Instead, we built a full hardware product that reads tokens, speaks with AI Voices, connects to AWS software, and can run educational games without a screen or wifi! Specifically, I'm super proud that I: got voice working on a tiny toy, using AWS to generate custom learning challenges in real-time. made a demo that works in the browser, so even in a virtual hackathon, people could try it out. figured out how to make it accessible to kids without internet, because tech should work everywhere, not just where Wi-Fi is strong. We got voice working on a tiny toy, using AWS to generate custom learning challenges in real-time. We made a demo that works in the browser, so even in a virtual hackathon, people could try it out. And maybe the biggest win: we figured out how to make it accessible to kids without internet—because tech should work everywhere, not just where Wi-Fi is strong. What we learned Voice-only design is hard! Without visuals, every word and pause has to do more work. We spent hours rewriting prompts to feel natural and clear to kids. The voices from Amazon Polly helped a ton here; they gave each character personality right out of the box, which made everything feel more alive. AI is powerful but unpredictable. Sometimes it nails a question. Other times? Not so much. So we had to learn to shape prompts carefully and set guardrails. Using AWS Bedrock with Claude Sonnet gave us flexibility, but we still had to steer it carefully to keep things age-appropriate and on-topic. Also, hardware always breaks at the worst time. Our mic setup glitched mid-demo, and our RFID reader randomly stopped working. We learned (painfully) to always have backups, and to build with resilience in mind! What's next for Buzzle We’re moving Buzzle from prototype to product—building a sustainable, scalable business around affordable hardware and cloud-powered learning. Product strategy: We're developing subject packs aligned with grade-level curricula (starting with early reading, math, and science), bundled with character tokens. These packs make Buzzle modular and upgradable, enabling recurring revenue through direct-to-consumer and school sales. Business model: Sales in developed markets will fund subsidized distribution in low-income regions through partnerships with schools, nonprofits, and governments. We're also pursuing IP licensing deals (e.g. Disney, PBS Kids) to boost engagement and create branded revenue streams. Technical roadmap: Latency + reliability: Optimize AWS Bedrock prompts and implement edge caching to reduce delays and enable offline play in low-connectivity areas. Voice input: Integrate TensorFlow Lite for on-device keyword detection to improve speed and reduce cloud dependence. Progress tracking: Build a real-time parent/teacher dashboard using DynamoDB Streams + AppSync. Multilingual support: Start with Spanish and Mandarin using Amazon Translate and customized prompt pipelines. Buzzle is now a connected learning platform—not just a toy—built for accessibility, adaptability, and scale. <div