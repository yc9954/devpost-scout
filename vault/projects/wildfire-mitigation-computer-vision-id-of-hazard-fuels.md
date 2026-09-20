---
slug: "wildfire-mitigation-computer-vision-id-of-hazard-fuels"
url: "https://devpost.com/software/wildfire-mitigation-computer-vision-id-of-hazard-fuels"
title: "Wildfire Mitigation: Computer Vision ID of Hazard Fuels"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 1181
team_size: 12
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Wildfire Mitigation: Computer Vision ID of Hazard Fuels

> To aid land managers in quickly identifying and responding to tree disease and mortality, we developed a computer vision model to ID diseased and dead trees from open-source available Landsat data.

[Devpost](https://devpost.com/software/wildfire-mitigation-computer-vision-id-of-hazard-fuels) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[climate_energy]] [[disaster_emergency]] [[supply_logistics]]
**user** [[government_staff]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** esri, forest-service-insect-&-disease-detection-survey-data, python, r, sagemaker, usgs-landstat-data

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for “wildfire mitigation: computer vision id of hazard fuels”

## Body

example model output train test split mask model metrics training mask transfer learning Sagemaker screenshot Inspiration We were inspired to develop a computer vision (CV) model to identify dead and diseased trees in near real-time using Landsat from our work with Federal, state, and local land managers. From our research of the United States Forest Service (USFS) , we have seen that relying on the Annual Insect and Disease Detection Survey to address hazard fuels and contain invasive species limits the capacity of land managers to rapidly detect tree mortality over large land areas. Routine monitoring of the timing, location, and magnitude of tree mortality is critical for Federal, state, and local land managers to rapidly respond to forest disturbances and risk of future mortality. Land management groups such as the Tree Mortality Task Force of California rely mainly on the Annual Insect and Disease Detection Survey performed by the USFS to identify areas with tree mortality (Jin & Byer) . However, the Annual Insect and Disease Detection Survey is infrequent, has a limited coverage area, and does not have a known accuracy from ground truthing. Our computer vision model addresses these issues by providing consistent, spatially extensive measurements of tree mortality. The Annual Insect and Disease Detection Survey’s forest mortality estimates are based on a surveyor’s visual interpretation of canopy conditions and are thus subjective to some degree. According to research by Jin & Byer, the Forest Service’s process of manually labeling aerial imagery does not have known accuracy from ground truthing (Jin & Byer) . Our computer vision approach has the potential to free up Forest Service resources to ground truth the accuracy of our model and manually inspect areas when the model exhibits uncertainty. Additionally, the current manual approach to evaluating tree health happens asynchronously at national forests around the county. We wanted to develop a model that allowed for near real-time assessment of tree health across the United States and provide a comprehensive assessment of tree mortality in a single snapshot. The current technique used by the Forest Service covers the area of the Annual Insect and Disease Detection Survey (Jin & Byer) . While survey regions contain many major forested regions within national forests, many forested areas on the wild land urban interface are not included in the survey. This creates the potential for forest managers to overlook areas of tree mortality outside of survey regions where tree mortality poses the greatest threat to human lives and livelihoods by increasing the risk and severity of forest fires. By providing a spatially extensive measurements of tree mortality, our model equips land mangers with insight into tree mortality in areas where it has the greatest potential to increase the cost of wildfires. Our computer vision model also has the potential to reduce tree mortality through early detection of invasive insects that accelerate tree mortality. Early detection and continuous monitoring of established species such as the Western Pine Beetle are critical to slowing their spread (USFS) . However, the low frequency and limited coverage area of the Insect and Disease detection survey reduces the capacity of USDA’s Animal Plant Health Inspection Service to rapidly detect tree mortality caused by outbreaks of invasive species. Due to the scalability of our CV model, Federal, state, and local land managers can rapidly detect and monitor tree mortality over large land areas, leading to faster treatment of affected areas and containment of invasive species. Through faster identification and monitoring of tree mortality, our CV model has the potential to reduce the risk of power outages and forest fire outbreaks due to tree-conductor contact. On distribution systems, it is common for tree related outages to comprise 20%-50% of all unplanned outages. The vast majority of tree-related outages stem from tree failure. Tree mortality exposes a power line to a high risk of tree incidents over time (Guggenmoos) . By continuously identifying dead trees over a large land area, our model will enable utility foresters, asset managers, arboriculture consultants, and regulators to improve tree risk assessments and line clearance programs through automated detection of tree mortality. The potential of computer vision to reduce wildfire risk and tree mortality through continuous motoring inspired us to take on this project. Computer vision has the potential to reduce tree death through the early detection of invasive species that accelerate tree mortality. Wildfire risk and severity can also be reduced through computer vision identification of tree mortality in areas not currently surveyed by USFS such as areas on the urban-wild-land interface and areas adjacent to power lines. We hope to work with federal, state, and local land managers and utility companies to help them leverage computer vision to reduce wildfire risk and severity. What it does Our model uses 30m Landsat satellite imagery at any time interval to identify dead and diseased trees over time. This approach is extendable to any resolution or region of imagery. How we built it We trained a computer vision model using 30m Landsat satellite imagery as our feature set. We labeled the level of tree mortality in each pixel of the Landsat imagery by converting shape-files from the Forest Service Insect & Disease Detection Survey Data into a Geo-tiff and transferring the labels to the Landsat imagery. To pretrain the model, we created the Image Net feature representation for classification using an image representation of the Landsat bands and time. The representation's pixels are randomized. The pixels are then classified as containing an area with or without tree mortality using a logistic regression with partial fit. Finally, we visualized our model output, error and ground truth using matplotlib and wrote the asset as a Geo-tiff. This approach is extendable to any resolution or region of imagery, aiding Federal, state, and local land managers in the identification and treatment of tree mortality. Challenges we ran into A challenge that we ran into deploying this model on sage maker was storage space and the ability to access other AWS tools such as s3. Accomplishments that we're proud of We’re proud to have developed a completely open-source model that will aid Federal, state and local land managers in the identification and treatment of tree mortality. Furthermore, our interactive dashboard provides and easy to use interface for USDA’s Animal Plant Health Inspection Service to rapidly detect tree mortality caused by outbreaks of invasive insects and for land managers to assess what areas of tree mortality should be targeted for tree removal. What we learned We developed a better understanding of multifaceted risks created by tree mortality and the factors driving tree mortality: climate change, drought, and invasive insects. We applied transfer learning and Landsat data, something that we have not yet explored in a production model. What's next for “Wildfire Mitigation: Computer Vision ID of Hazard Fuels” We plan to meet the USFS and other land management stakeholders to share our model and dynamic tools. We look forward to working with USFS and other forestry professionals to further refine the model and implement a seamless satellite image to tree mortality dashboard pipeline for land management professionals. <div