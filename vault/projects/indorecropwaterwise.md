---
slug: "indorecropwaterwise"
url: "https://devpost.com/software/indorecropwaterwise"
title: "IndoreCropWaterWise"
hackathon: "FuturistFest 2024 X NASA"
organization: "Stem Like Her"
winner: true
words: 825
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/scientific_research"
  - "user/frontline_worker"
  - "substrate/web_dom"
---

# IndoreCropWaterWise

> Empowering Farmers, One Drop at a Time

[Devpost](https://devpost.com/software/indorecropwaterwise) · hackathon [[FuturistFest 2024 X NASA]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[agriculture_food]] [[scientific_research]]
**user** [[frontline_worker]]
**substrate** [[web_dom]]

**stack** lightgbm, numpy, pandas, python, scikit-learn, streamlit, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how does it work
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for indorecropwaterwise

## Body

Introduction page of the app, providing all the necessary instructions to use it. Main page of the app. Enter the required weather data and calculate the irrigation requirement for your crop. Inspiration Growing up, I was surrounded by the world of farming and irrigation, thanks to my father's work in manufacturing drip irrigation systems. My fascination with agriculture was seeded early on, but it wasn't until I witnessed the devastating water crisis in Indore that I felt compelled to take action. Indore, my birthplace, has seen its groundwater levels plummet from 150 meters in 2012 to a staggering 560 feet (170 meters) in 2023. This sharp decline is a direct result of overexploitation and inefficient water use, especially in agriculture. I couldn't stand by as farmers struggled with decreasing crop yields and soaring water costs due to inefficient irrigation practices. Driven by a deep concern for Indore's future and the desire to leverage my knowledge, I embarked on creating IndoreCropWaterWise. This project aims to revolutionize irrigation practices by providing accurate reference evapotranspiration (ET0) predictions, enabling farmers to use water more efficiently and sustainably. My goal is simple: to empower farmers with the tools they need to conserve water, enhance crop yields, and secure a brighter future for Indore's agriculture. What it does IndoreCropWaterWise (ICWW) is a cutting-edge project designed to predict irrigation requirements (IR) for various crops specifically in the Indore region. Using advanced AI models like Light Gradient Boosting Machines (LGBM) and Artificial Neural Networks (ANN) , ICWW produces accurate ET0 predictions based on about 37 years of training data which are then used to predict the IR by running the predicted ET through a series of formulae to calculate the Gross Irrigation Requirement (GIR) which is in mm of water / unit area of the crop field / day. How does it work The app predicts the Gross Irrigation Requirement (GIR) for crops in Indore using meteorological data and machine learning models. The process is structured as follows: Input Data: Enter today's meteorological data, including estimated rainfall. Select your crop type (from 6 common crops), its growth stage (Initial, Mid, Late), and your irrigation method (Drip, Surface, Sprinkler). Model Selection: Based on the selected data, the app automatically chooses the most efficient model (ANN or LGBM) to predict the reference evapotranspiration (ET0). Model Architecture: ANN Model: Input Layer: 3, 4, or 6 neurons Hidden Layers: 4 layers (256, 128, 64, 32 neurons) using ReLU activation. Output Layer: 1 neuron with a linear activation function. LGBM Model: Built using the LightGBM library with default parameters. Calculation Process: Step 1: ET0 is adjusted for crop type and growth stage to calculate the Crop Water Requirement (CWR or ETc). Step 2: Effective precipitation is calculated from estimated rainfall. Step 3: Net irrigation requirement is derived by subtracting effective precipitation from CWR. Step 4: Net irrigation is adjusted for irrigation efficiency, giving the final GIR output. This structured approach ensures that the app provides precise irrigation recommendations, tailored to the specific needs of crops in Indore, thereby promoting sustainable water usage in agriculture. Challenges we ran into ET0 Calculation Challenges: The ET0 was calculated with the FAO-56 Penman-Moneith equation. The equation required specific meteorological data not readily available for Indore. Discovered the NASA POWER website as a key data source. Applied standard assumptions to calculate ET0 values successfully. ANN Architecture Challenges: Identified the optimal Artificial Neural Network (ANN) architecture. Focused on balancing high prediction accuracy with computational efficiency. Conversion Methodology Challenges: Conducted extensive research and experimentation. Determined the correct methodology for converting predicted ET0 values into final Gross Irrigation Requirements (GIR). Accomplishments that we're proud of Creating IndoreCropWaterWise has been a dream since childhood, and realizing this vision fills us with immense pride. We successfully developed a complex application that is not only functional but also accessible to everyone through a dedicated website. We are also thrilled to share that our research paper on using AI models to predict ET0 in Indore is about to be published—marking a significant milestone as the first-ever research in this area. This accomplishment reflects our dedication and hard work. What we learned Through the development of IndoreCropWaterWise, we gained invaluable experience in applying machine learning to real-world agricultural challenges. We learned the importance of data accuracy, especially in calculating ET0 using the FAO-56 Penman-Monteith equation. We also deepened our understanding of optimizing ANN architectures for both accuracy and efficiency. Additionally, we learned how to integrate machine learning models into a user-friendly web application, bridging the gap between complex algorithms and practical, accessible tools for farmers. What's next for IndoreCropWaterWise Expand Crop Types: Incorporate additional crop varieties for broader applicability. Enhance Meteorological Data: Integrate region-specific data to improve ET0 predictions. Improve ET0 Accuracy: Collect data directly from the City Meteorological Department for precise model training. Forge Local Partnerships: Collaborate with agricultural bodies to deliver the tool to farmers. Promote Sustainability: Aim for more efficient and sustainable water use in agriculture. Hi. <div