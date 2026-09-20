---
slug: "ross-42pnvi"
url: "https://devpost.com/software/ross-42pnvi"
title: "ROSS - Remote Operated Semantic Sketching"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 844
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ROSS - Remote Operated Semantic Sketching

> We're making art accessible to the blind by bridging visual ideas with touch, temperature and sound!

[Devpost](https://devpost.com/software/ross-42pnvi) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[geospatial]] [[video_visual]]

**stack** arduino, blood, cohere, gemini, huggingface, python, sweat, tears

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ross - remote operated semantic sketching

## Body

Cartesian Robot Painting by Monet Segmented Edge Extraction Stroke Graphs Vectorization Wiring CAD Model Inspiration Visual art is such a large component of human culture. If you visit any art gallery, you'll notice that many of the exhibits are paintings on 2D surfaces. What if you're blind and looking to experience the art as well? What if you could take a picture of a painting and feel the shapes and curves being drawn on your hands? Our inspiration for this project was based in accessibility, to make the idea of art accessible to the visually impaired by adding the elements of touch, sound, and temperature. The inspiration for the name specifically is Bob Ross, who believed that art should be accessible and joyful for everyone, regardless of skill or background. What it does ROSS takes in any sort of visual art - paintings, sketches, photography - and transforms it into complete touch and sound experiences without losing its creative information. The image is converted into line representations tagged as either warm or cool in color. A two axis robot draws on your outstretched palms using two brushes. One draws with alcohol, the other draws with a heated resistor. These hot and cold brushes convey the color and spacial representations of the art. Narration is then applied for each component drawn, giving detailed descriptions of what is being shown, conveying the semantic information within the art. How we built it On the hardware side, we utilized 2 Nema Stepper Motors (to move the rails), servo motors (to move the brushes up and down), many 3D printed parts, Arduino to control the different motors, a paint brush dipped in hand sanitizer, and a second paintbrush with a 10 ohm resistor (which we used to generate the heat for the second tip). A web camera was also utilized to provide a way for users to capture the painting image by voice. Take an input image and feed it into Meta SAM (Segment Anything model) in order to isolate meaningful elements in the painting (e.g. different objects like a tree, person, or building) For each mask, generate a simplified stroke outline. Convert detected strokes into intelligent graph structures that understand how lines connect, where they start and end, and the optimal way to traverse them, similar to how a human artist plans their drawing sequence Transform pixel-based stroke data into smooth, mathematical curves using algorithms like Ramer-Douglas-Peucker simplification. Convert digital coordinates into real-world millimeter measurements with 1mm spacing accuracy, ensuring the robotic reproduction maintains proper proportions and detail resolution on physical canvas. We categorize parts of the painting as warm or cold depending on how similar the colour is to red or blue. Colours closer to red are labeled as red, and colours closer to blue are labeled as blue. Warm colours paint using a warm paint brush warmed by a resistor, and a cold paint brush has hand sanitizer on it. This way one can distinguish between colours. (This is not working completely, so for demo we are using no colours and just one brush) Take all the numerical outputs and feed it to an Arduino which controls the hardware. While painting, we would also play some music which is relevant to the sentiment of the painting, as well as a Bob Ross voiceover (from this fine-tuned HuggingFace model: https://huggingface.co/drewThomasson/Xtts-FineTune-Bob-Ross ) Challenges we ran into Many issues with making sure the hardware could move the brushes in the right direction We tried to find many free speech to voice APIs to mimic Bob Ross's voice, but we could not find a super good one. Accomplishments that we're proud of Built a complete end-to-end system that connects computer vision, stroke optimization, and hardware control into one seamless demo. Translated complex research models into a functional prototype that can be used in real-world accessibility contexts. Designed and assembled a multi-motor hardware system with custom 3D-printed parts, proving out our concept under tight time constraints. Created a unique multi-sensory art experience by combining touch, temperature, and sound. Overcame numerous technical and integration challenges to deliver a working prototype by the end of the hackathon. What we learned We learned that things that seemed simple can be a lot harder than they seem. We had initially thought that we could use an LLM to do the picture simpliciation, the component labeling, and basically most of the work. However, we figured out that the results were inconsistent, leading us to go with a more mathematical approach. What's next for ROSS - Remote Operated Semantic Sketching Two brush method with warm and cold colours working. We had wanted to do this, but we were unable to get the functionality working in time/ We would do the wawrm and cold colours in a more professional manner, instead of using a resister for warmth and hand sanitizer for cold. A portable camera wearable to make it easier to feed images A larger scale arm setup that could possibly draw on the backs of people Custom music generation to make music unique to each painting <div