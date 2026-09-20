---
slug: "detection-of-microplastics-in-water"
url: "https://devpost.com/software/detection-of-microplastics-in-water"
title: "Detection Of Microplastics In Water"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 670
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Detection Of Microplastics In Water

> MY PROJECT DETECTS THE MICROPLASTIC ITEMS IN WATER AND DECREASE THE DISEASES CAUSED BY IT .

[Devpost](https://devpost.com/software/detection-of-microplastics-in-water) · hackathon [[Frostbyte Hackathon]]

## Facets

  <sub>weak: realtime_stream, sensor_fusion, vision_ocr</sub>
  <sub>weak: civic_government, developer_tools, scientific_research</sub>
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, html, json, react

## Body

U CAN SEE EACH AND EVERY DETAILS WITH THIS QR 🌟 Inspiration Behind the Project Plastic pollution has emerged as one of the most critical environmental challenges of the modern world. Scientific reports indicating the presence of microplastics in drinking water, marine ecosystems, food, and even human bloodstreams motivated me to explore this issue further. The realization that humans may unknowingly ingest thousands of microplastic particles annually inspired the development of a technological solution to detect these contaminants early. The core idea of this project originated from a simple but impactful question: Can we design an intelligent system that detects microplastics in water before they enter the human body? This curiosity led to the integration of Artificial Intelligence, image processing, and full-stack web technologies to create an automated detection and monitoring system. 🎯 Objectives of the Project The primary goals of the project are: To detect microplastic particles present in water samples. To classify particles using Machine Learning techniques. To estimate contamination levels and potential health risks. To provide a digital platform for monitoring and analysis. The concentration of microplastics in water is calculated using: 𝐶 𝑁 𝑉 C= V N ​ Where: 𝐶 C = Concentration of microplastics (particles per liter) 𝑁 N = Number of detected particles 𝑉 V = Volume of water sample (liters) 🛠️ How I Built the Project The project was developed using a combination of hardware analysis, AI modeling, and MERN stack web development. 1️⃣ Data Collection and Sample Preparation Water samples were collected from various sources such as tap water, bottled water, and local water bodies. The samples were filtered using microfilter paper to capture microscopic particles. The residue obtained was then dried for imaging. 2️⃣ Image Acquisition and Processing Microscopic images of filtered particles were captured using a digital microscope. These images were processed using Python and OpenCV techniques such as: Noise reduction Thresholding Edge detection Segmentation 3️⃣ Machine Learning Model Development A Convolutional Neural Network (CNN) was trained to classify particles into: Microplastic Non-plastic The convolution operation is represented as: Feature=(Input∗Kernel)+Bias The model learned features such as texture, shape, and color variations that distinguish plastics from organic or mineral particles. 4️⃣ Full-Stack Application Development (MERN) To make the system user-friendly and accessible, a web platform was developed using the MERN stack: MongoDB → Data storage Express.js & Node.js → Backend APIs React.js → Frontend interface The platform allows users to: Upload sample images View detection results Monitor contamination levels Analyze historical data 5️⃣ Risk Level Estimation The contamination risk is categorized using threshold logic: 𝑅 𝑖 𝑠 𝑘 { 𝐿 𝑜 𝑤 𝐶 < 50 𝑀 𝑒 𝑑 𝑖 𝑢 𝑚 50 ≤ 𝐶 < 200 𝐻 𝑖 𝑔 ℎ 𝐶 ≥ 200 Risk= ⎩ ⎨ ⎧ ​ Low Medium High ​ C<50 50≤C<200 C≥200 ​ This helps users understand potential exposure risks easily. 📚 What I Learned This project provided knowledge in multiple domains: 🔹 Technical Skills Image processing using OpenCV Deep learning model development (CNN) Full-stack development using MERN REST API integration Database design and management 🔹 Research Skills Understanding environmental datasets Problem analysis and solution design Scientific documentation and experimentation 🔹 Personal Development Team collaboration Problem-solving under constraints Debugging and optimization techniques ⚠️ Challenges Faced Several challenges were encountered during development: 1️⃣ Dataset Availability Obtaining real microplastic datasets was difficult due to limited public resources and laboratory access. 2️⃣ Particle Similarity Non-plastic particles such as sand, fibers, and organic matter often resembled microplastics, reducing classification accuracy. 3️⃣ Small Object Detection Microplastics are extremely small, requiring high-resolution imaging and careful preprocessing. 4️⃣ Integration Complexity Connecting the AI model with the MERN stack backend required API integration and data format optimization. 5️⃣ Model Overfitting Due to limited training data, the model initially overfitted. This was addressed using: Data augmentation Regularization Cross-validation 🌍 Impact and Future Scope This project contributes toward environmental safety and public health awareness by providing an affordable detection method. Future improvements include: IoT-based real-time monitoring Mobile application integration Larger training datasets Government water quality monitoring integration <div