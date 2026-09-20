---
slug: "childgrowthmonitor"
url: "https://devpost.com/software/childgrowthmonitor"
title: "ChildGrowthMonitor"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1250
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/revocation_withdrawal"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ChildGrowthMonitor

> Quick, accurate data on malnutrition

[Devpost](https://devpost.com/software/childgrowthmonitor) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[provenance_signing]] [[revocation_withdrawal]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[housing_homeless]] [[labor_employment]] [[mental_health]]
**user** [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** azure, flask, java, python, tensorflow

## How they structured the write-up

- problem
- solution
- data
- scanning process
- what you have done during the weekend - hackathon completion
- the solution’s impact to the crisis
- the necessities in order to continue the project
- the value of your solution(s) after the crisis

## Body

Child Growth Monitor We provide quick and accurate data on child malnutrition in the most ethical way for frontline healthcare workers and organizations sharing our vision of Zero Hunger Problem Hunger or malnutrition is not simply the lack of food, it is usually a more complex health issue. Parents often don't know that their children are malnourished and take measures too late. Current standardized measurements done by aid organisations and governmental health workers are time consuming and expensive. Children are moving, accurate measurement, especially of height, is often not possible. During the current COVID-19 pandemic the situation has become worse. All manual measurement of children is suspended, because it would not be possible to keep a safe distance. Bottom line: accurate data on the nutritional status of children is unreliable or non existent PROBLEM FOR HACKATHON: Our AI algorithm needs clean data to produce good-quality results. During Covid-19 our partners in the field (frontline healthcare workers) can’t collect data any more. So, we’re building a tool that our partner scan use whilst locked in at home. This tool helps to enrich our image data with additional information (e.g. quality of scan, pose of child, light conditions, etc) also after Codiv-19. These information will speed up the process of our AI algorithm development. Solution Our users do a quick scan of a child, similar to recording a video. We use the data from the smartphone camera and further sensors to measure the child using machine learning and artificial neural networks. Therefore we provide a quick and touchless way to measure children and detect early warning signs of malnutrition. Our app is still in development mode. A first prototype will be available within 3-6 months. A tech solution that diagnoses children for their nutrition status via image data does not exist yet. From a technical, data science side this challenge is big but we are on a good way to tackle this task. Mobile App https://github.com/Welthungerhilfe/cgm-scanner The mobile app provides authenticated users an interface to scan children in 3D with consent of the parents and upload all collected data to the secure backend. Because of the limitations of mobile connectivity in rural areas and in slums with tin roofs offline first is a major goal of the project. While the app already works fine in offline environments, results from the scans are currently produced in the cloud. Providing predictions directly on the device is the next big step we are taking, as it would also improve privacy by not having to upload every scan. We guide the user to scan the child in a way that a quick, accurate measurement can be taken. This will involves data of the camera pose, point clouds and RGB video. App Backend Backend is implemented in Azure and uses Authentication with B2C Tenant OAuth Vue.js Frontend Flask Backend Custom Python ETL processes AzureML Storage Accounts are used with Queues and Blobs for structured data and scan artifacts PostgreSQL for structured data Grafana for visualization Database PostgreSQL is used for structured data. Storage Storage Blobs are used for large objects such as rgb video and maybe point clouds. Storage Queues are used for transfering structured data from app to backend. Machine Learning Backend Development of the machine learning backend happens at https://github.com/Welthungerhilfe/cgm-ml and on our DevOps project Data Please refer to our data description Scanning Process Before any data is accessed or added our trained team explains in simple terms that the data belongs to the children and parents, they give us the rights to store and process the data for a limited time this right can be revoked any time and the data deleted we are using the data only for the achieving the UN goal of Zero Hunger by 2030 Lastly, the informed consent with the caregivers signature is scanned to document compliance. The scanning process is broken down into three parts for each standing and lying children. We evaluate scanning results to find the best way of scanning to gather necessary data. Children are wearing underwear. front scan The child is scanned from the front. Scan from back The child is scanned from the back. 360° scan This scan gathers more information about the volume of the body and could lead to a more accurate prediction of the weight of the child. For children that can stand upright, the user asks the child to spread the arms slightly of the body and turn around on the spot 360 degrees. For children that are lying down the user leads the smartphone left and right around the child to get a more detailed 3D image. What you have done during the weekend - hackathon completion We have been able to meet the goals of this hackathon to 100%. We have produced a prototype of the backend and the frontend of our data enrichment tool. This prototype will enable our users to do data cleaning allow data scientists to work on our data provide a protopye notebook for body part segmentation With a few adjustments we will be able to go live with our data enrichment prototype, i.e. the tool can be used by frontline healthcare workers whilst they are locked in at home. We were able to complete the goal that we set for the hackathon. The solution’s impact to the crisis Measuring malnutrition has been stopped in many developing countries due to Covid-19. Traditionally, children need to be touched to be measured. Our app offers a no-touch solution. The hackathon results allow us to to optimize our data quality develop the accuracy of our AI algorithm improve understanding of our users This prototype of our data enrichment tool allows our users to look at their scans and understand which way of handling the smartphone produces accurate results. Through their data inspection we gain more clean data for our machine learning which will improve the accuracy of our results The necessities in order to continue the project Our Child Growth Monitor app is still in development mode. Due to Covid-19 we want to release a „Child Growth Monitor beta“ product as soon as possible. Big International Organisations like the World Food Programme have urged us to release such a beta version. The value of your solution(s) after the crisis The no-touch feature is not the main feature of Child Growth Monitor. We have not developed our app because of Covid-19. The main advantages of our solution compared to traditional measurement methods are that the Child Growth Monitor: delivers better measurement quality eliminates the lack of measurements since it turns anyone with a smartphone into an expert for anthropometric measurements gets rid of unreliable, bulky and expensive hardware eliminates the possibility to manipulate data The impact of Child Growth Monitor can be huge. We assume that we will be able to help millions of children into food extension programs. Thus, possibly saving these lives. The economic impact of getting rid of malnutrition is potentially gigantic as well. Our project partner The Boston Consulting Group has calculated an additional GDP of €100 billion for India alone. BUSINESS SIDE We will set up the Child Growth Monitor as a non-profit, open source Social Business. Our goal is to maximize impact (i.e. get children out of hunger), not revenue. We have developed a business plan and will test the hypothesis of our business plan with the lean startup method. We are doing this process together with our partners Boston Consulting Group, WFP and Unicef. Additional links: https://childgrowthmonitor.org/ https://github.com/Welthungerhilfe/ChildGrowthMonitor https://www.youtube.com/watch?v=FfYxIkp_vw4 <div