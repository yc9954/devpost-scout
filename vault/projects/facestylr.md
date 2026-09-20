---
slug: "facestylr"
url: "https://devpost.com/software/facestylr"
title: "faceStylr"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 1297
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/small_business"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# faceStylr

> Polyvore meets Augmented Reality for styling your face. Make meaningful product connections with your customers!

[Devpost](https://devpost.com/software/facestylr) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[retail_commerce]] [[supply_logistics]]
  <sub>weak: immigration_refugee</sub>
**user** [[general_public]] [[small_business]]
**substrate** [[video_visual]] [[web_dom]]

**stack** android, asm.js, dlib, ios, lamp, linux, mac, opencv, realityscript, s3, shopify, tensorflow, unity, visa

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for
- a note exclusively for my “bad fans”: clarification on past work

## Body

Try out a new look designed by the community Apply some filters! Snapshot your look! Save your Look Please show your face to help us thumbnail the looks! Inspiration My mother was a former beauty queen, from another country, who had become completely forsaken to beauty. Though she was once even an Avon lady, she would not teach me anything about makeup. Once, when we were watching a late night beauty pageant, and I looked wistfully at the contestants, my mother told me, “No, you’ll never qualify.” I was not raised in a competitive family, but I had always personally believed in winning contests and at age 12, being told I had no chance meant this wasn’t worth the time investment at all. I learned early on, from my mother, the beauty expert, that I was not pretty. 18 years later, in the streets of NYC and Paris, on my own, I would discover the world of expert fashion stylists, who are able to make anyone look glamorous — they can even make an ugly girl look pretty. For anyone in this modern world, seeing yourself look amazing is transformative. It fosters hope and makes you believe in your dreams again. I want to help spread this magic. My goal in ShopFace is to build an AR product that lets anyone show off the look they want, and even share it so that others can, quite literally, instantly try it out. My aim is to create an innovative yet universal platform to lets anyone express their beauty creativity by becoming a stylist, and by helping them discover and virtually try-on products they did not know could transform their looks. What it does FaceStylr is Polyvore meets augmented reality for styling your face. Users can browse different styles, mix and create their own look sets from a selection of products—and try any of them on virtually! The platform provides Style Analytics to merchants. We track each product the user tries on, how long they try it out for - as well as which product links the user clicks through, and which look set they belong to. For merchants, FaceStylr helps you maximize meaningful user engagement time for more of your products. And for inspiring the creativity of a user-driven community for discovering and sharing looks - to create social media art with their face, based on your products. Onboarding is FAST. Any product online with a front-facing photo can be easily added to the system. Finally, we gather for machine learning on style data for a specific set, relating to combinations of how users put on various face-wear. In the long run, as the inventory grows, the platform will evolve into an AI stylist omniscient of everything you can buy online, recommending the perfect products and look sets for your face. FaceStylr. The Augmented Reality Face Styling Platform. How I built it Semi-meticulous software architecture on the fly for a client-server app that I/Os to server, and on the clientside, is aware of the user’s face pose tensor to be able to virtually apply the products on the user’s face. Stack below: * App: Unity C#/.NET 3.5 Equiv @ .NET 2.0 Subset. AReality3D RealityScript framework, primarily just RS.IO, RS.TrackingBindings, RS.Misc, RS.Rendering (shaders for makeup blending, face mask, LUT for color matching and post processing filters, etc) Tracking: OpenCV 3.4.1/Dlib 19.7 (Free, open source) Webstack: LAMP (because I learned it all starting in 1997) Cloud Storage: AWS S3 iOS, Android, etc via cross platform compile WebGL via asm.js / Emscripten or Unity cross-platform compile * Gitlab for storing giant Unity projects Products featured from Amazon, Zenni, Shopify and other fine ecommence retailers. Challenges I ran into I wish I started this earlier. I wish I had more time. I wish I wasn’t just a one person team. CORs WebGL issues. Ugh. BUGS!!! I could swap in a better tracking SDK, but… Accomplishments that I'm proud of After a decade building AR software for everyone from Autodesk to Intel to Google and more, I feel that I’m past just the technical implementation or even “just rapid prototyping an idea”. I’m onto using my expertise in building software to maximize product design to create platforms that can scale and solve problems that matter to me. I’ve identified and executed on building an AR use-case to help brands sell products to millennials and beyond, and helps people feel better about the way they look. It’s a culture that loves social sharing of everyday creativity — and what better than creatively customizable AR try-on’s of real products? I would be grateful for the TechCrunch publicity to help push this platform forward, beyond the humble small network of this indie dev. What I learned New experiment: I’m trying to launch a real product at Disrupt Hackathon, so unlike my usual iOS TestFlight app, I figured a WebGL link that anyone can access works the best. I’d love to learn from all of your feedback! Help an ugly girl out? What's next for Integrations! If there’s traction/funding… Replace OpenCV/dlib tracking with a commercial face tracking SDK. (Sorry for the lag and everything for this POC!) A Note Exclusively for my “Bad Fans”: Clarification on Past Work FaceStylr is a project I started designing, architecting and building on July 27, 2018 after a week of feeling like an outsider among women in tech at Google Cloud Next (even being rejected from the Women in Tech Social). I’ve designed my own frameworks to build AR apps… fast—and I’ve also used a bunch of other modern programming frameworks. These are a bunch of RealityScript libraries I wrote on top of Unity C#. I built SnapGlass.es Share two years ago, but that was just a simple glasses try-on platform, with a 3x3 look comparison grid inspired by Warby Parker. That was also using OpenCV/Dlib from 2016. Tracking does not make all AR apps the same. Comparing that to this would be like comparing a basic dynamic website to an extensive blogging platform. The amount of work and the insight in software architecture to build the latter from the first is a world of difference. I built FaceShop.io last year before Facebook launched their AR Studio. Despite the similarity in name, for those who understand product, it is clear that my previous project FaceShop.io is very different from FaceStylr. Just in case, I’ll clarify the differences here: FaceShop is more of a “Photoshop for AR” - a general purpose creator software, similar to Facebook AR Studio or Snap Lens, but without relying on either platform. (It also includes a basic Flash ActionScript 1.0-inspired scripting language and a whole lot of things that would only be relevant for a professional creator tool.) FaceStylr is more like a “Polyvore for AR” - primarily a creative platform to discover fashion-related products and share product collections in a personal way that involves AR try-on’s. (Polyvore and Photoshop, though they both start with P, are very different - I hope we agree here!) FaceShop used the old OpenCV Dlib from last year with no stabilization. (And also allows the user to swap other face tracking SDKs, as it is tracking agnostic as a creator platform). ShopFace uses the latest OpenCV v3.4.1 and Dlib v19.7 and may switch to a commercial face tracking platform. Currently, a hackish stabilization with high-pass filters and optical flow is used. ShopFace has a variety of ecommerce and product and even referral link integrations. FaceShop was made directly for iOS on an iPad resolution device; for instant test-ability, FaceStylr was made initially for (desktop) WebGL. Simply summarized, FaceStylr is about creating AR Shopping experiences across the entire ecosystem, with benefits for both consumer and merchants to engage meaningful sales - and not just about creating arbitrary AR filters like FaceShop. <div