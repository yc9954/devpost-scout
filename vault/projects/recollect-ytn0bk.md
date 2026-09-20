---
slug: "recollect-ytn0bk"
url: "https://devpost.com/software/recollect-ytn0bk"
title: "Recollect: Leave No Book Behind"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 807
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Recollect: Leave No Book Behind

> Our robot scans, digitizes, and analyzes books with zero intervention.

[Devpost](https://devpost.com/software/recollect-ytn0bk) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** arduino, autodesk-fusion-360, bun, google-cloud, google-cloud-vision-api, gpt-4, next.js, openai, react, supabase, typescript, vercel

## How they structured the write-up

- why build this?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recollect

## Body

Result after prints and cuts Debugging the arm Starting CAD Finishing touches Web UI First diary scan Recollect is a $150 robot that scans, digitizes, and analyzes books with zero intervention. Once a book is placed on the stand, Recollect's robotic arm delicately flips the pages while a high-resolution camera captures each page. The images are sent to a website which merges the images into a PDF and creates AI summaries and insights of the document. Why build this? Only 12% of all published books have been digitized. Historical records, ancient manuscripts, rare collections. Family photo albums, old journal entries, science field notes. Without digitization, centuries of accumulated wisdom, cultural treasures, personal narratives, and family histories threaten to be forever lost to time. Large-scale digitization currently requires highly specialized equipment and physical personnel to manually flip, scan, and process each page. Oftentimes, this is simply not practical, resulting in many books remaining in undigitized form, which necessitates careful, expensive, and unsustainable transportation across various locations for analysis. How we built it Hardware: Recollect was made with easy-to-fabricate material including 3D printed plastic parts, laser-cut acrylic and wood, and cheap, and off-the-shelf electronics. A book rests at a 160-degree angle, optimal to hold the book naturally open while minimizing distortions. The page presser drops onto the book, flattening it to further minimize distortions. After the photo is taken, the page presser is raised, then a two-degree-of-freedom robotic arm flips the page. A lightly adhesive pad attaches to the page, and then one of the joints rotates the page. The second joint separates the page from the adhesive pad, and the arm returns to rest. The scanner was designed to be adaptable to a wide range of books, up to 400mm tall and 250 mm page width, with easy adjustments to the arm joints and range of motion to accommodate for a variety of books. Software: Image processing: On the backend, we leverage OpenCV to identify page corners, rescale images, and sharpen colors to produce clear images. These images are processed with pre-trained Google Cloud Vision API models to enable optical character recognition of handwriting and unstructured text. The data are saved into a Supabase database to allow users to access their digital library from anywhere. Webpage and cloud storage: The front end is a Vercel-deployed web app built with Bun, Typescript, Chakra, Next.js, and React.js. Challenges we ran into We ran into challenges involving getting the perfect angle for the robotic arm to properly stick to the page. To fix this, we had to modify the pivot point of the arm’s base to be in line with the book’s spine and add a calibration step to make it perfectly set up for the book to be scanned. Our first version also used servo motors with linkages to raise the acrylic page presser up and down, but we realized these motors did not have enough torque. As a result, we replaced them with DC motors and a basic string and pulley system which turned out to work surprisingly well. Accomplishments that we're proud of This project was a perfect blend of each team member’s unique skill sets: Lawton, a mechanical engineering major, Scott, an electrical and systems engineer, Kaien, an AI developer, and Jason, a full-stack developer. Being able to combine our skills in this project was amazing, and we were truly impressed by how much we were able to accomplish in just 24 hours. Seeing this idea turn into a physical reality was insane, and we were able to go beyond what we initially planned on building (such as adding summarization, quotation, and word cloud features as post-processing steps on your diary scans). We’re happy to say that we’ve already digitized over 100 pages of our diaries through testing. What we learned We learned how to effectively divide up the project into several tasks and assign it based on area of expertise. We also learned to parallelize our work—while parts were being 3D-printed, we would focus on software, design, and electronics. What's next for Recollect We plan to improve the reliability of our system to work with all types of diaries, books, and notebooks, no matter how stiff or large the pages are. We also want to focus on recreating PDFs from these books in a fully digital format (i.e. not just the images arranged in a PDF document but actual text boxes following the formatting of the original document). We also plan to release all of the specifications and software publicly so that anyone can build their own Recollect scanner at home to scan their own diaries and family books. We will design parts kits to make this process even easier. We will also explore collaborating with Stanford libraries and our close communities (friends and family). Thanks to Recollect, we hope no book is left behind. <div