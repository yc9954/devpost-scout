---
slug: "chop-chop"
url: "https://devpost.com/software/chop-chop"
title: "Chop Chop"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 1140
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Chop Chop

> Chop Chop is a handsfree kitchen companion serving up fun, easy to follow video tutorials on chopping fresh produce.

[Devpost](https://devpost.com/software/chop-chop) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**mechanism** [[graph_reasoning]] [[on_device_local]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]]

**stack** alexa-skills-kit, amazon-web-services, final-cut-pro, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for chop chop

## Body

Inspiration This skill came together from a few different threads of inspiration. First off, I think the kitchen is one of the most interesting arenas for voice first exploration. Not only is it a key communal place in a household, but it also lends itself especially well to handsfree interactions. Ever struggled to TouchID unlock an iPhone with food on your hands that went to sleep right before you needed to read step 3 of a recipe? The burners already on, you better hurry! So you peck in your passcode with your knuckle instead only to get a join our email list popup overlay from some janky recipe site. Chop Chop isn’t a recipe skill, but it emerged from a desire for reduced friction with technology in the kitchen. To this point, multi-modal Alexa devices are especially useful in the kitchen. Your hands are tied up while you’re cooking, so a voice-first interaction makes a lot of sense. But the addition of a screen can add a lot of value. Again, recipes are an obvious use case here. But with Chop Chop, a quick visual cue about how to slice up a mysterious piece of produce might be all you need to get an injection of confidence and some direction so you can keep things moving with your cooking. Reading about how to chop something in a recipe can feel super abstract. But when you see someone else doing it, it just clicks. Finally, Chop Chop is an exploration of native voice-first content creation. Sure there are loads of how-to videos on YouTube from all sorts of channels showing you how to chop all sorts of things. But you need to search and click around quite a bit. And once you find a relevant video, you still have to click past the ad and the intro and the chatter to scrub through and find what you need. This is super inefficient when you’re in the kitchen and in the go zone. Chop Chop strips all of that away. It’s designed to give you exactly what you need, when you need it, in the shortest possible time between when you need help and when you get it. What it does Chop Chop is a handsfree kitchen companion serving up fun, easy to follow video tutorials for chopping fresh produce. Users can ask for any fruit or vegetable. From the basics to the exotics, the skill provides entertaining yet highly useful step-by-step instructional videos. Featuring 40+ original videos at launch, we’ll continue adding new fruits and veggies to the catalog over time. There are no menus. No categories. And intentionally minimal navigation. Users are welcomed with, “Hello, what would you like to chop?” If we have it, a video will start playing immediately. If we don’t have it, users are encouraged to submit their requests on a companion microsite, FlavorFriday.com. The intention here, beyond creating a dynamic skill with fresh content, is to develop an understanding and expectation with users to feel like their hands are on the wheel – and that they have a stake in the direction and evolution of the skill. If someone requests a Cherimoya, we want them to find a Cherimoya video next time they return to the skill by simply asking “What’s New?!”. How I built it Chop Chop was built using V1 of the Alexa Skills Kit, leveraging Entity Resolution to handle slot value synonyms within the voice model, DisplayDirective to identify multi-modal devices, Display Interface + BodyTemplate7 for the splash screen and VideoApp for video playback. The backend is written in Javascript/Node.js and hosted in AWS Lambda. Videos were shot on iPhone 7+ in 4K and edited in Final Cut Pro. Logos and images were created in Pixelmator. Alexa dialogue within the video assets was generated using the Alexa Developer Console testing simulator, captured by Audio Hijack, trimmed & normalized in Fission (Rogue Amoeba FTW!) and imported into FCPX for final assembly. Challenges I ran into Even though Echo Show and Echo Spot have different screen shapes and resolutions, they’re powered by shared media assets. So to ensure a good experience for Spot users, we had to frame our shots and edits with a strong center of gravity and maintain a consistent safe zone, especially when using graphics or text. Even though our final exports were 720p, shooting in 4K ensured we had enough headroom to make adjustments and push in on shots as needed. This took quite a bit of trial and error. If you’re serious about multi-modal skill development, you can’t rely on the simulators. Testing on devices is mission critical. Accomplishments that I'm proud of All my previous skills have essentially been static, whereas Chop Chop is my first skill with the technical and creative pieces in place to expand and evolve over time. So I’m really excited to see where it goes and how the audience development and user retention manifests over time. Bringing this skill to life required concurrent creative and technical development. We piloted the format and production process quite a bit in order to bring this to life at scale. Producing native content for voice is an entirely new challenge because the creative development informs the technical development which informs the creative development and around and around we go. In most mediums, the creative is locked and then distributed through technology. Whereas in this context, the two are inseparably intertwined from creation to consumption. What I learned My initial skill architecture didn’t account for the ability to add new video content without the need for re-certification. In this first iteration, I generated a long list of every conceivable type of produce that we didn’t have and made them all synonyms of a single slot value called “Missing Produce.” So any ER-Match to this group would resolve to a message about soliciting suggestions on the microsite. In my second iteration, I moved all of these synonyms to the top level of the voice model and instead now handle them with an if/else gate informed by a match in the video assets array. This way, I can simply add a new video in lambda whenever one’s ready and our voice model will already be dialed in to accommodate that slot value. Through this I realized I’ve only just scratched the surface of Entity Resolution and there is much more to understand and explore here in order to build more complex & robust skills. What's next for Chop Chop More content! Lots more content! In addition to continuing to feed the Chop Chop content engine from user suggestions, we’d like to explore other forms of kitchen-oriented voice first content for potential sister-skills to Chop Chop. And while the FlavorFriday.com microsite gets the job done, I’d like to implement a more elegant in-skill mechanism for soliciting and capturing user requests! <div