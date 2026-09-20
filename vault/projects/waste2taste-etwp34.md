---
slug: "waste2taste-etwp34"
url: "https://devpost.com/software/waste2taste-etwp34"
title: "Waste2Taste"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 1379
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Waste2Taste

> Measuring plate waste in dining halls so chefs serve what students enjoy.

[Devpost](https://devpost.com/software/waste2taste-etwp34) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** depth-anything, groundingdino, owl-vit, python, raspberry-pi, segment-anything, snowflake, snowflake-cortex, socket, supabase, typescript/javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for waste2taste

## Body

Recommendations page. The ranked list of dishes from most to least disliked, with a popup for detailed alternate recipes. Today page. Example of expanding the most disliked dish, with the total mass and an overview of the alternate food options. Today page. Quantified overview of how many dishes were tracked and an introduction to the decision feed. Analytics page. Information especially effective over longer periods of time, including totals, averages, and highest priority items. Recommendations page. The alternate recipes and ingredient lists for the two dishes, including estimated preparation time and names. The Waste2Taste Logo Inspiration The idea for Waste2Taste came from something that we see every day, but barely stop to notice: the endless amount of half-eaten plates on the conveyor belts of the dining hall dish return. Entire scoops of mac n cheese, untouched chicken wings, apples with just a bite or two taken out. The sheer speed of the conveyor makes it easy to overlook, but when you stop to watch, the amount of food wasted is devastating. And it's not just waste, it's a signal that students aren't enjoying the food either. And that dissatisfaction fuels even more waste. We created Waste2Taste to break this cycle, minimizing food waste among university students. What it does Waste2Taste is a Snowflake-powered platform that measures food waste in dining halls and transforms that data into actionable insights for chefs. Here is the process: A mounted camera above the dish-return returns images of the leftover plates. These images are processed by our backend, which identifies the food items and calculates how much food is uneaten. The results are sent to the Waste2Taste dashboard, where chefs are able to view real-time data on grams of food wasted, item by item. Using this data, our system ranks foods from most to least food wasted, indicating how much students like a food, and provides chefs with AI-powered recipes that use similar ingredients to turn unpopular dishes into ones that students are more likely to enjoy. How we built it Backend: Our backend uses segmentation and detection in order to detect and measure how much food is left uneaten on each plate. Using the OWL-VIT open-vocabulary object detection network, we identify the food based on the custom label set that we define. Once the food is identified, groundingDINO localizes items by drawing bounding boxes, and segmentation refines this into pixel-level masks of the leftovers. Using the predefined physical dimensions of the plate, we calculate a pixel-to-length conversion ratio, which allows us to measure the surface area of each masked region in real-world units. To get a 3D measurement, we apply Depth-Anything V2, which generates depth maps of the plate, giving us height information and allowing us to approximate the volume of each leftover portion. Finally, we combine volume with set food density values, and we can estimate the mass (grams) of uneaten food per item. We stored all of this data in Supabase, and used the Snowflake API for many of our other backend processes. Snowflake would be used to process all of this data, and then we heavily utilized Snowflake Cortex to generate the recipe recommendations using Mixtral-8x7b. Snowflake was incredibly important in this project because it allowed us to ingest data automatically from Supabase then immediately process it, all within one easy framework. Snowflake was also crucial in the Analytics section of the website, being used in the Historical Trends Analysis, Frequency Analysis, Waste Reduction Metrics, and Pattern Recognition components. The scalable computing features of Snowflake also came in handy as we were able to configure the warehouse settings depending on the workload. Frontend: We made a React 18 and TypeScript app built using Vite for fast local development. We used React Router for client side navigation across the Today, Recommendations, and Analytics views. Furthermore, we used Tailwind for the styling aspects and shadcn/ui components for building bocks. Also, Lucide provided lightweight icons and next-themes provided easy dark/light mode toggling. Forms were built with React Hook Form and validated with Zod. We made the visualizations for waste metrics with Recharts and used date-fns for time formatting. For content that needed motion, we used Embla Carousel. Challenges we ran into Throughout our journey with Waste2Taste, we encountered many problems, especially with the integration of all parts into a coherent whole. We repeatedly had issues with dependencies and requirements when attempting to run our backend scripts and models on Raspberry Pis connected to the cameras. We were also challenged with estimating depth as our original plan centered around multi-angle camera shots or using a depth camera, however we were not able to get the right materials for that strategy. Accomplishments that we're proud of We are proud of integrating our backend software with our frontend successfully, creating a flow from image capture to insights on the dashboard. Our team built an AI pipeline that not only detects and measures leftover food but also takes that data to turn into clear, real-time metrics for chefs. We are proud of successfully implementing relevant models (OWL-VIT, GroundingDino, Depth-Anything) into a working pipeline, which can be used to accurately estimate the volume and weight of leftover food. Connecting our backend data retrieval to Supabase and Snowflake allowed us to create recipe recommendations from the data that we collected. We designed a clean, intuitive frontend dashboard that chefs can easily use to see food waste trends. In terms of Snowflake, we were proud of how we used a dual system approach by using Supabase to store data and Snowflake to analyze the data and use AI. This allowed us to effectively use Snowflake for what it is known best for, which is analytics and AI processing. We were also proud of how we used Snowflake to build a comprehensive analytics section with real time data processing. Overall, being able to use Snowflake for so many purposes, from ingesting data to AI processing to recommendations to an analytics dashboard, was an accomplishment for us. What we learned The biggest thing we learned is that integration of all parts is always the hardest part. Creating single functions is manageable, but putting all the pieces together is where the challenge lies. We had to carefully connect hardware, backend processing, ML models and integration, and the frontend data retrieval so that data could flow smoothly from plate images to chef insights. Through this process, we learned the importance that clean data flow and API design has in bringing backend computation to a live frontend. We also learned that computation can be delegated to tasks depending on efficiency, For example, tasks that can be run on a Raspberry Pi can be sent to a MacBook to run quicker. For Snowflake, we dug deep into the intricacies of the platform throughout our time here and gained valuable experience helpful for not only this project but for our careers. We had a chance to try a multi-layer architecture design while also using a warehouse based compute model. We additionally learned how to use Snowflake Cortex, which will now likely become our go-to for AI integration. What's next for Waste2Taste To expand Waste2Taste, we would like to first utilize training and classification for food detection instead of generative image matching in order to create a more efficient program that relies on pre-trained information rather than generating images for comparison during runtime. We would also like a more accurate representation of the food on the plate. We want to experiment with multi-angle capture or depth sensors to achieve more precise representations of food height and volume. This would also improve the accuracy of our portion sizes and weight calculations. We also want to train our segmentation and detection models on the Nutrition5k dataset, which focuses on estimating volumes of fully-prepared dishes with many ingredients mixed together, as seen in real life. We want to expand our dashboard to include historical tracking of each item, which would allow chefs to see long-term trends, identify the least-wasted foods historically, and make menu adjustments based on the data. We'd also be interested in continuing to develop our Snowflake API skills through this project, utilizing the predictive analytics side of Snowflake. This includes their time-series functions, which would allow us to predict things such as season trends in food disposal. <div