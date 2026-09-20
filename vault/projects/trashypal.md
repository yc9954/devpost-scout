---
slug: "trashypal"
url: "https://devpost.com/software/trashypal"
title: "cleanclik"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 1117
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/supply_logistics"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# cleanclik

> Sick of litter? Turn cleanup into a game! Scan trash with your cam, our app sorts it from recyclables to e-waste. Earn points for disposal, compete on leaderboards, share eco-badges, and make it fun!!

[Devpost](https://devpost.com/software/trashypal) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[supply_logistics]]
**substrate** [[video_visual]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** flutter, mlkit, python, supabase

## How they structured the write-up

- inspiration
- what it does
- how to use cleanclik (demo version)
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what i learned
- what's next for cleanclik

## Body

Sign up Login Dashboard Trash detection Maps for finding nearest bin After scanning QR code on bin Disposing Leaderboard Profile Inspiration We've seen it: a plastic bottle on the sidewalk or a coffee cup in the park. And we've walked past it. Why? The answer is usually the same. We think, "It's not my job," or "That's what the city pays people for." It feels gross, it's certainly not fun, and ultimately, there's no incentive for us to clean up public spaces. This is where my inspiration began. I realized that to get people to act, I had to answer the question: "What's in it for me?" I was inspired by the power of gamification in apps like Pokémon GO to turn the mundane into the magical. It led me to ask a new question: What if I could make cleaning our city fun, rewarding, and something you could actually win at? This idea is the heart of CleanClik. I set out to build a tool that transforms a civic chore into an engaging adventure, reframing our relationship with public spaces and empowering everyone to make a tangible impact. What it does CleanClik is a mobile application that gamifies urban cleanup. Scan & Detect: Users point their phone's camera at a piece of litter. The app uses machine learning to identify the object and suggests its waste category with a simple on-screen label. Pick-up & Score: Once the user picks up the item, the app remembers it and adds points to their profile. It's a fun activity that makes you feel good about cleaning your neighborhood. Level Up & Share: As you collect more points, you can level up and share your progress with friends on social media. How to Use CleanClik (Demo Version) 1. Install the App For this demo, you can download and install the Android APK directly from our website at Cleanclik.com . (We plan to publish on the Google Play Store and Apple App Store in the future). 2. Create Your Account Sign up with your email. You will receive a verification message to confirm your account. 3. Verify and Sign In Open the verification email and click the confirmation link will navigate to app, and you should be automatically signed in and ready to go. 4. Scan and Collect an Item Open the camera view in the app and find an item to clean up. Pro Tip: For the best results with our current ML model, we highly recommend starting with common objects like food items, plastic wrappers, or small electronic gadgets. Point your camera at the item. When the app recognizes it and shows a label, simply reach out and grab the item. The app will detect that you've picked it up and add it to your inventory. 5. Find and Scan a Demo Bin Since we haven't installed physical QR codes on city bins yet, we've set up virtual demo bins on our website. On a separate device (like a laptop or tablet), visit Cleanclik.com to find the QR code that matches the category of the item you just collected. Use the app's QR scanner to scan the code directly from the website. 6. Dispose and Earn Points After scanning the correct QR code, tap the "Dispose" button in the app. 7. Check Your Rank! That's it! Watch as you're awarded points for your cleanup effort. Head over to the leaderboard to see your rank climb in real-time. How we built it CleanClik was built as mobile application Core Framework: We used Flutter to build the user experience. Backend: Supabase serves as our complete backend, handling user authentication and profiles. Machine Learning: We are currently using Google's ML Kit for general object detection. We plan to replace this with a custom-trained model designed specifically for accurate trash categorization. Challenges we ran into On-Device ML Models: We tried a variety of trash detection models to run on-device, but couldn't get any of them working reliably or performantly. We finally decided to just use Google's ML Kit for this initial version. Pickup Detection: Recognizing when a user has physically picked up a detected item was a tricky interaction to design and implement effectively. Backend Migration: Replacing our entire dummy user management system and integrating a full Supabase authentication backend was a significant challenge. Guiding the AI: It was sometimes frustrating to tell the AI exactly what to implement and when, requiring very specific and careful instructions. Accomplishments we're proud of Building a Complete App with Kiro: Our biggest accomplishment is the project itself. We successfully built a feature-rich, complex mobile application from scratch, almost exclusively using Kiro. This includes the architecture design, service implementation, testing, and documentation. Seamless ML Integration: We are proud of the core user experience. The real-time object detection is fast and responsive, providing an intuitive interface that is magical to use. What I learned I learned how to guide an AI by breaking down the work into smaller, manageable building blocks instead of asking it to build everything at once. I gained experience in integrating multiple ML models into a mobile app and getting them to work seamlessly. Details Matter: I learned this lesson well, and while I focused on the core loop, I know I still missed out on a lot of smaller details that can make an app feel truly complete. What's next for CleanClik We have a clear vision for making CleanClik a real-world solution for cleaner cities. Production Readiness: Our top priority is to make the app production-ready by integrating a real, custom-trained trash detection and categorization model. Real-World Bin Integration: We plan to work with communities to stick QR codes on existing public bins or, where needed, install new ones to create a reliable network for disposal validation. Real-World Rewards: We plan to partner with local businesses to introduce actual rewards for top players, such as discounts or gift cards. Deeper Gamification: We plan to introduce more compelling game mechanics, such as daily quests, collection streaks, and special time-limited "Trash-storm" events in designated city zones. Community & Team Features: We want to empower collective action by allowing users to form local cleanup teams, challenge other neighborhoods, and visualize their team's combined impact. This includes adding features to capture "before and after" images of large trash dumps, with a system to allocate points among the community members who helped clean it up. Environmental Impact Dashboard: We will develop a web dashboard that aggregates anonymized data to showcase the tangible, real-world impact of the CleanClik community, celebrating milestones like "10,000 plastic bottles recycled." The future could even move beyond the phone....imagine people wearing AR glasses, truly turning their city cleanup into a live-action game. <div