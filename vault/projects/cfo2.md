---
slug: "cfo2"
url: "https://devpost.com/software/cfo2"
title: "Indigenous Stewardship and Tech to Reduce Wildfires"
hackathon: "Amazon Sustainability Data Initiative (ASDI) Global Hackathon"
organization: "Amazon"
winner: true
words: 1324
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Indigenous Stewardship and Tech to Reduce Wildfires

> Reducing the risk of wildfires and emissions is highly relevant. This project assists indigenous stewards to do this while creating renewable energy, offsets, fertilizers, biodiversity and jobs.

[Devpost](https://devpost.com/software/cfo2) · hackathon [[Amazon Sustainability Data Initiative -ASDI- Global Hackathon]]

## Facets

**domain** [[agriculture_food]] [[climate_energy]] [[disaster_emergency]] [[finance_payments]] [[supply_logistics]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, boto3, cuda, gdal, invest, jupyter, matplotlib, numpy, python, sagemaker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- data used and connection to un goals
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for this project and initiative

## Body

GIF Presentation slides also used in the demo video. Fuel map showing an area in northern Alberta Inspiration Climate change, energy crisis, fertilizer crisis, poverty, less biodiversity - These things can trigger something more akin to a panic attack and paralysis rather than inspiration. But sometimes connecting with certain individuals and groups can change that. This has been, and still is, the case for us. We got to know a team consisting of indigenous elders, knowledge keepers, trappers, a forester and their network with both NGOs, researchers and actors in the forestry and insurance industry. What stood out was that this group wanted to change the way certain things are done around forestry, energy and products coming out of the forest. Their ambition was (still is..) to preserve indigenous way of life and knowledge, tackle climate change, energy crisis, fertilizer crisis and poverty by building an economic, sustainable and climate positive ecosystem with the forest at heart. In this submission, we especially got inspired by one part of this that would reduce wildfires by combining western technology with indigenous knowledge. The representatives of this group talk about creating balance, and how, by working with forest fuel levels in different ways, we can have the following impacts: Reduce wildfires, and thus emissions from these Create a sustainable business on offsets Produce renewable energy sources Produce fertilizer that sequesters carbon (biochar) Create jobs in socioeconomic areas with poverty Preserve indigenous way of life and knowledge Protect, and support biodiversity and forest communities (to break negative trends in this area), where in this case is adjacent to a UNESCO site and the home of a genetically unique herd of wood buffalo that may even be linked to the last Ice Age. This group has skills, knowledge and access to large areas of forest, know their way around the forest industry and the logistics side of this business. They do not have as established knowledge in technology and data analytics. This is where our project and group come in. As colleagues having worked with remote sensing and vegetation, this project is about doing something supporting, and showcasing, how we can use data to help this greater initiative by working together across silos. Thus, the inspiration of this project comes from supporting this group and their very ambitious, planet positive goals. What it does Our solution will provide a fuel map showing the amount of carbon and amount of mortality rates in forests in an area in northern Alberta, Canada (where this indigenous community lives, which is also very close to a UNESCO site). The solution will also provide a table with a weighted index combining the calculated carbon stock and mortality rate per area, which becomes a way for the trappers and their team to prioritize where wildfire reduction activities will have the most effect. So, in short, this is a solution showcasing how technology can support more effective wildfire reduction activities with indigenous knowledge - which in turn can reduce emissions, produce biomass for renewables, create new jobs and protect biodiversity and wildlife. How we built it We built this by first uploading a "dead tree" map model output via Sagemaker. This is from a deep learning model we have developed recently outside of this project which analyzes Sentinel-2 imagery. Our solution can take other images than our own specific output. Having the dead tree map uploaded, we download and match that area with the same area from the open ground classification dataset from ASDI. After this, we use the ground classification and run it through our implementation in of the InVEST in Sagemaker. This gives us a calculation of the carbon stock in the selected area. Our next step is by using the ground classification to cut away all except the class forest from the dead tree analysis output. Then we fuse together the remainder (dead tree hits in the class forest and carbon stock map) to create a type of "fuel map" which will show the amounts of carbon and dead trees in the area. We then create two images of this fuel map, one sampled to a resolution of 500m per pixel and one with 2000m per pixel. The former shows a more detailed picture of the fuel map (viewing purpose), while the latter is used for the creation of a priority area list. Finally, we create a table combining the values of carbon stock with the values of the tree mortality into a priority index for each 2000m sized pixel, sorted from high to low. Thus providing an example of how we can use this type of technology to enable wildfire reduction work and efficiency! Data used and connection to UN goals We have used Sentinel-2 imagery, Ground Classification (from ASDI), carbon pool data (collected and collated for use), forest mortality map (proprietary/external model but other sources can be used). We have also used carbon data from https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/4_Volume4/V4_04_Ch4_Forest_Land.pdf as well as the data provided by the InVEST carbon model project itself. The connection to the UN goals are several if used as intended in the described project. We can connect this to goals 7, 8, 9, 10, 11, 12, 13, 15, 17 and even more. The main ones we would argue are clean, affordable energy, climate action, sustainable cities and communities, life on land and partnership. Short video mentioning datasets and data used: https://youtu.be/zlUD5e_zPzg Challenges we ran into Trying to understand wildfires. This is a huge field of research, and after concluding that there really are no simple models, and after talking to the indigenous led team, we came to realize that everyone knows that wildfires emit, the prioritization is the important part, to have an effect. Accomplishments that we're proud of In a very short time, manage to understand which variables we can calculate, and which activities we can support that have backing in science, as well as in a real life application in a real project. Getting cuda to behave... Our speedily understanding of remote sensing data and models - without this, and getting into this project so fast (we got started quite late...). Working as a team, and breaking barriers across silos - We are based in Sweden and India, while our friends in forestry are in Canada and in France where we all have different cultures but a common goal. What we learned That wildfires, forestry, carbon stock and emissions are all very complicated topics, often affected by factors such as soil composition, earlier burns, canopy type, species composition, undergrowth, humidity and more. But we also learned that there is a very real and exciting opportunity to make use of the fuel that today just burns in wildfires today, where we can use technology to make this work easier and more efficient. We learned a bit more on how we can combine some of our own previous work with open datasets to create new value and usage. What's next for this project and initiative CFO2 is in a sense a simple version of something needing more variables for more precision and better priorities. However, we also think it should not be underestimated what proven indexes and simpler solutions can provide in terms of hands-on value. This is also one cog in a bigger machinery and ecosystem which can be a climate positive engine providing energy, offsets, fertilizers, biodiversity, jobs and much more. What CFO2, and our greater ambitions can do, is to gather more insights on a country-sized scale, to know the composition of a forest (we can do parts of this today), a better biomass assessment (better data is coming next year!), factor in water/humidity to make decisions where to go better and better, and be part of the team driving this, to see it scale and have a real positive impact on our planet. As a team, we would be immensely proud to be part of such an effort (and it is a lot of fun!), <div