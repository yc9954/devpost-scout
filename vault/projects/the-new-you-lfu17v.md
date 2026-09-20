---
slug: "the-new-you-lfu17v"
url: "https://devpost.com/software/the-new-you-lfu17v"
title: "THE NEW YOU"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1175
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# THE NEW YOU

> YOUR PERSONAL AI STYLIST. UNLEASH THE NEW YOU.

[Devpost](https://devpost.com/software/the-new-you-lfu17v) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[provenance_signing]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[retail_commerce]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** antigravity, firebase, geminiapi, google-cloud, googleaistudio, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the new you

## Body

landing page color analysis it suggests 30 best colors and 10 colors to avoid our simple protocol face shape analysis and it also suggests the best hairstyles account screen it also have body shape analysis where you can also check your size in different brands shop screen which has all the categories with different links across different platforms for virtual try on and chat with ai outfit suggestions with links across different shopping platforms style genie screen for outfit suggestions and selecting the best outfit for an occasion select the best outfit mostly designed for designers our virtual try on results Inspiration The inspiration for THE NEW YOU came from observing a glaring gap in how women interact with fashion tech. When trying to figure out what to wear, women spend hours scrolling through Pinterest or Instagram for outfit suggestions because retail apps fail to understand them. Current platforms are just massive catalogs that overload women with choices, causing intense choice overload and decision fatigue. If color analysis, outfit suggestions, and virtual try-ons are not deeply personalized and connected, the experience completely falls apart. This inspired me to build a platform centered on identity—helping women bridge the gap to the person "they could have been" by discovering a new self through fashion. I wanted to eliminate the need to search external social apps or constantly switch between broken platforms, replacing chaos with a single, deeply personal styling journey. What it does THE NEW YOU is a first-of-its-kind, cost-effective fashion-tech ecosystem designed to help women unlock and embrace their unique style identity without increasing costs. Instead of forcing users to navigate overwhelming, generic e-commerce choices, the app unifies three premium pillars into a single, seamless user journey: Color DNA Analysis: An advanced AI computer vision engine that decodes a user's unique facial canvas (skin undertone, eye contrast, and hair features) from a simple selfie, mapping them to one of the traditional 12-season color palettes. Personalized Body Shape Engineering: An intelligent silhouette calculator that analyzes body aspect ratios to identify their silhouette (e.g., Hourglass, Pear, Rectangle) without requiring intrusive or complex physical measuring tapes. Interactive Virtual Try-On: The ultimate validation layer that generates a high-fidelity digital twin, allowing users to visually experience how a recommended garment fits, drapes, and harmonizes with their complexion before spending a single rupee. How we built it Building the platform required decoupling complex computational color and silhouette logic from the creative AI styling generation. To ensure the fashion science was flawless, I deeply researched the domain and spoke directly with real, professional personal stylists to map out how human experts consult clients.Initially, I tried to handle the entire project by manually writing all the code. However, to handle the deep contextual nuances of high-fashion personalization, I pivoted the architecture to Google AI Studio. By utilizing advanced prompt engineering and integrating external tools, I architected a sequential, multi-layered processing stack:The Core Attribute Extractor: When an anchor garment image is uploaded, the computer vision pipeline extracts its dominant color signature mapped in the HSV (Hue, Saturation, Value) color space, denoted as:$$\mathbf{C} {\text{base}} = (H_b, S_b, V_b)$$The Geometric Color Wheel Engine: Instead of letting an LLM guess matching shades, the backend executes pure geometric transformations on the hue circle to find mathematically perfect color harmonies. For example, a split-complementary harmony generates two target accent hues, $H_1$ and $H_2$, calculated by rotating the base hue $H_b$ (measured in degrees) by $150^\circ$ and $210^\circ$:$$H_1 = (H_b + 150^\circ) \pmod{360^\circ}$$$$H_2 = (H_b + 210^\circ) \pmod{360^\circ}$$The Seasonal Boundary Intersection Matrix: To find colors that simultaneously complement the garment and match the user, the app pulls the user's seasonal sub-palette, represented as a discrete set of allowed color coordinates $\mathbf{S} {\text{user}}$. The engine dynamically calculates the intersection between the geometric harmony vector space $\mathbf{H} {\text{harmony}}$ and the user's seasonal constraints:$$\mathbf{C} {\text{final}} = \mathbf{H} {\text{harmony}} \cap \mathbf{S} {\text{user}}$$This ensures that the final suggested outfits fit precisely within the overlapping sub-space of structural design and personal genetics. Challenges we ran into The absolute hardest challenge was achieving true personalization across every single feature. If the color DNA or the silhouette rules felt even slightly generic, the entire user journey failed. Technically, this manifested as a battle against LLM token frequency bias within Google AI Studio. In standard generative models, seasonal terms are heavily linked with overused cliché colors in the training data. For instance, passing the word "Autumn" to an AI almost always returns an uninspired loop of olive greens and rust oranges, completely ignoring the remaining 80% of the true seasonal spectrum. By taking the insights gathered from real personal stylists, I overcame this by writing rigorous algorithmic prompt structures. I forced the AI to treat the styling canvas as a 360-degree matrix intersection and enforced strict multi-toned canvas rules (where apparel, footwear, and accessories must occupy separate, non-overlapping color domains). This broke the model out of its predictable token pathways, allowing it to generate highly personalized, runway-level outfit coordination. Accomplishments that we're proud of Graduated Idea Validation at WE HUB: Successfully completed the rigorous idea validation incubation phase at WE HUB, graduation from their foundational startup classes, and received critical prototyping support to refine the venture's direction. Google for Startups Recognition: Selected for and validated through the prestigious Google for Startups "Prompt to Prototype" program, proving the technical scalability of our prompt-engineered styling stack. Fully Functional MVP Ecosystem: Engineered and launched a successful, working Minimum Viable Product ("Outfit Match Mate") that maps garment attributes directly against personal color matrices to break the fragmented app barrier. Active Market Validation: Transitioned out of pure development to actively measure user interest, capturing early behavioral insights and real-world feedback from our target demographic. What we learned This project completely changed my perspective on software development. Moving from trying to code every feature manually to leveraging Google AI Studio taught me how to blend traditional system guardrails with generative AI. I learned that AI shouldn't handle foundational mathematics; instead, human engineers must build the structural frameworks (like color wheels and silhouette matrices) and use precise prompt engineering to let the AI act as the creative, empathetic stylist. Ultimately, I learned that fashion tech isn't just about selling clothes—it's about building a seamless journey that reflects a user's true identity. What's next for THE NEW YOU The immediate roadmap focuses on expanding the technical features of THE NEW YOU and systematically moving the platform toward a public launch: Virtual Hairstyling Integration: Expanding the interactive digital twin feature to include personalized hairstyle modifications, allowing users to test different hair cuts and colors that complement their analyzed seasonal color palette and facial structure. Rigorous User Testing: Launching intensive, closed-group user testing phases with our target demographic to capture real-world user experience data, streamline navigation, and eliminate onboarding friction. Perfecting Validation Loops: Iterating on the system backend based on user testing data until the recommendation engine and try-on precision achieve perfect validation metrics. Public Deployment: Transitioning the platform out of its current prototype environment to officially deploy and launch the fully realized application for the wider public market. <div