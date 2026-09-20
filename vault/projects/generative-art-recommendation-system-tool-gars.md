---
slug: "generative-art-recommendation-system-tool-gars"
url: "https://devpost.com/software/generative-art-recommendation-system-tool-gars"
title: "Generative Art Recommendation System Tool (GARS)"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 774
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Generative Art Recommendation System Tool (GARS)

> Explore generative image creation like never before with our custom recommendation system and tool built for generative diffusion models.

[Devpost](https://devpost.com/software/generative-art-recommendation-system-tool-gars) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]]

**stack** gradio, milvus, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for generative art recommendation system tool (gars)

## Body

Inspiration Prompting generative art models is critical in ensuring output aligns with what a user wants. This requires careful prompt engineering and understanding which parts of the prompt effects output. Due the vast possibilities of prompts this can be overwhelming and lead to frustration for a user. What if we can apply principles of recommendation systems to alleviate to issue and allow a user to explore generated images that are created to their preferences? This eliminates the need of careful prompt engineering at each iteration of design saving time for a user to explore more of the output space in a more efficient matter. What it does Our project seeks to develops a novel integration of recommendation systems and generative art models. GARS provides a custom recommendation system that captures users preferences quickly and effectively. GARS allows a user to start a recommendation session in which fast inference SDXL Lightning models are loaded locally (works fully on consumer grade Nvidia 3070 Ti). We were able to do this by offloading parts of the diffusion model that are currently in use to the CPU. Users can optionally state their preferences to better guide the recommendation system, choose a specific step SDXL Lightning model, and an iteration count. After that a user gives a rating from (-1 to 1) for a generated image and allow the system to generate more images. A user can optionally control movements of various image characteristics through adjusting weights of each element or freezing them entirely. Once the recommendation system reaches the final iteration, all the images can be shown within a gallery. How we built it For our user interface, we chose Gradio because of its seamless integration with the diffusion models we utilized. This allows for quick and efficient interactions, enabling users to easily explore and refine image generation in real time. Gradio's flexibility made it simple to display results and manage inputs, streamlining the entire user experience. For our recommendation system, GARS uses Milvus, an open-source vector database, to manage and search through a database of embedding vectors that represent image characteristics. As users interact with the system, their preferences are adapted using the collection of vector embeddings stored by Milvus. Finally, as our recommendation system suggests new art by adjusting the prompt-based representation of the artwork, we needed a text-to-image model to generate the corresponding artwork from the prompt. It is also critical to ensure inference time is fast, as recommendations are created on the fly in real time. To achieve this, we ran SDXL Lightning and allow for user configurable option of running 2,4 and 8 steps of inference. This allows the user the option to sacrifice quality for speed. Challenges we ran into Accomplishments that we're proud of Our recommendation system is able to consistently converge on a specific topic and/or style of an image by the end of a recommendation session. Achieving this level of accuracy in suggesting content that aligns well with the user’s preferences is one of the more challenging aspects of building a recommendation system. However, our system manages to do this within just a few iterations, making it both effective and enjoyable to use. What we learned We learned how to take an idea and transform it into a product that people can use. We never envisioned that we could take our recommendation system and turn it into a design tool. It was initially made as a proof-of-concept that such a recommendation system could be created and function well. However, after completing this hackathon, we believe that the potential for generative recommendation systems is vast, with applications far beyond what we initially imagined. These systems could revolutionize how users discover and create content, offering personalized and innovative solutions across various fields, from design to entertainment and beyond. We also learned that locally hosting model's provides flexibility and control that an online API does not provide. Exploring diffusion pipelines and seeing how custom ones can be built provided both a fun and fulfilling learning experience. Nvidia's AI workbench aided in the process of quickly getting the environment up and running with the possibility of quickly shifting to a remote server if we need to ever run bigger models or for training. What's next for Generative Art Recommendation System Tool (GARS) The main application for GARS is still under development, but what we have developed for this hackathon will likely become a feature within our broader design tool. We aim to transform GARS into a fully functioning application within the next year. If you have any questions/concerns/suggestions or would like to try a demo of our app, please email clevergars.info@gmail.com . <div