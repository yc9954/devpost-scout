---
slug: "freshair"
url: "https://devpost.com/software/freshair"
title: "freshAir"
hackathon: "AWS Data Exchange Challenge"
organization: "Amazon"
winner: true
words: 1325
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/immigration_refugee"
  - "user/general_public"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# freshAir

> Track air pollution across the world and see its impact instantly. How can we keep our air FRESH?

[Devpost](https://devpost.com/software/freshair) · hackathon [[AWS Data Exchange Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[immigration_refugee]]
**user** [[general_public]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, css3, html5, javascript, python, react, sagemaker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for freshair
- sources
- data

## Body

Intro Page Our Mission and Tips section Interactive World Map The gradient bar highlights the countries with the selected color + each country has a link to each of their detail pages. Ranked countries based on the number of tonnes polluted Detail page for each country On hover shows a graph of the pollutant's emissions throughout the years Shows the the countries' total progression of pollution Category: Data Visualization Inspiration Severe air pollution has been prevalent in our world since the Industrial Revolution. In recent years, however, scientists have revealed that humans started emitting greenhouse gases over 2,000 years ago after finding trapped air within Greenland’s glaciers [1]. After these many years, how has our atmosphere taken in all these harmful pollutants -- and how has air pollution been a major contributor to global warming? Not only is our environment getting damaged, but the public health too, in major ways. For example, contact with smog (when fossil fuels react with air) and soot (airborne pollutants) can irate the eyes and damage the lungs. As well, polycyclic aromatic hydrocarbons (PAHs) in large amounts have been linked to blood/liver problems, eye/lung irritation, and cancer [2]. Inspired by the recent Covid-19 pandemic and the viruses' damage to the lungs, we wanted to encourage countries to improve their air quality and focus on air pollution reduction. Although air pollution has gotten significantly better over the years, particularly the United States thanks to the Clean Air Act, there's still much to improve on. This 1963 act made a huge advancement in the reduction of air pollution and is one of the most influential modern environmental laws. Even more, this further validates that leading countries like the United States are serious in making a change in regards to air pollution. Change and improvement will happen in the industrial industry if we look back in our past and the data we collect, to define the next steps for our future. Our solution does just that and visualizes the air pollution in a unique way, one that has not been done before. Taking inspiration from https://www.worldometers.info/ and air quality visual maps such as https://aqicn.org/map/world/ , we created freshAir, a unique air pollution visualizer and tracker. What it does Visualizes and ranks the air pollution for countries throughout the years to provide analysis and access to visual trends across the world. FreshAir’s features include an air pollution index to track the tonnes of pollutants emitted each year per country, a map color-coded with colors from white to the black gradient to uniquely represent the pollution, and graphed trends across the years for each pollutant per country. To summarize, our platform shows the progression of air pollution across the years around the world. Unlike other air pollution indexes, or maps, who use AQI ( Air Quality Index ) to rank and measure the severity of air pollution in real time , we used the number of tonnes emitted to show the progression through time , courtesy of the CRUX OECD - Air Emissions by Source dataset. It's important to not only focus on the now but also the past, so we can learn from our mistakes and our uprisings to improve how we approach the issue of airborne pollutants in the future. As well, we used Amazon's SageMaker to graph those trends for each of the main pollutants, Carbon Monoxide, Nitrogen Oxides, Non-Methane, PM10 / PM25, and Sulfur Oxides to describe these trends and the history of air pollution. Through tracking, visualizing, and representing, we believe that we can get a better idea on how one can approach the issue in the future, and what countries need the most work in reducing their waste. How we built it The technologies/languages we used include: Amazon SageMaker: To interpolate the data and create graphs that would show the progression of tonnes of pollution emitted for each pollutant per country across time. AWS Amplify: To host our react application. React/Javascript: To complete the front-end of our platform and all the functionalities, including the interactive SVG map. Python: The language we used for creating the graphs on Amazon Sagemaker. Some highlighted features: Color gradient - white to black For each country, we labeled its air pollution intensity with a color between white and black- representing the colors of smoke and smog. We decided to do this to give a better visual on our map and ranking list so it's easier to understand compared to confusing AGI values and unclear labels other pollution maps have. These hex color values were calculated based on the number of tonnes the country emitted that year. The more tonnes emitted, the darker the shade is. The visual below shows a clear explanation of how it was done: Using Sagemaker for Interpolation We have created Notebook instances for AWS Sagemaker. Using Python 3.6 we imported the CRUX Air emission dataset and wrangled it. We dropped unwanted rows and columns and finally with the dataframe we made lineplots based on trends. We used Tonnes and the unit and plotted time series graph for value vs year for each country for each pollutants. For example, this graph shows Australia's air emissions in tonnes versus time: Interactive Map SVG To be able to highlight the country borders, colors, and hovers, we decided that a sufficient way to do this is with an SVG. The world map is constructed through loops in our react app and each SVG path is inserted separately. When a border color or background is changed, the react state variable causes a reload and the SVG re-creates itself again. This allowed us to make seamless transitions while interacting with the map but also maintain a lot of design control. (The map was taken from https://simplemaps.com/ ). Challenges we ran into Merging SageMaker results with our react application - and the best way to showcase both in our final product. Finding the best way to display the map while having control over the display, colors, and highlights. Changing the year variable throughout all navigation links and through the state. It was challenging to make the updates seamless. Deploying the site on AWS Amplify because of our large files causing ‘Javascript heap out of memory’ errors. Accomplishments that we're proud of Overall, we’re glad we participated in this challenge and created a fresh idea that is different from similar counterparts (air pollution maps). We created a simple interface that’s easy to use and displayed the trends created with SageMaker in unison with our site. We used the CRUX dataset to its fullest potential since we incorporated almost all the data from it. Finally, this project is rather large for only a 2 person team, so we’re definitely proud of the work we have done in quantity and quality. What we learned During the development of this project, we use a couple of new technologies for us. Amazon SageMaker and AWS amplify were new, so we learned how to use them and integrated them with our React app. As well, we got more familiar with React and its differences between javascript (especially with SVG's). We learned how to solve merge conflicts and to make sophisticated decisions regarding the design, idea, and functionality of our project. What's next for freshAir Access to the full database, so we can report data on all the countries. Calculating the percentage each sector contributes to the pollution and displaying it in a simple way on our country detail page. Machine learning predictions of future air pollution. More information on the ranking table such as the country’s improvement from the previous year and the projected number of tonnes the country will emit the following year. Zoom in feature on the map- to have a better view of the air pollution per country. Graph the trends worldwide, not just per country (easier to see the progression of pollution). Sources [1] https://www.smithsonianmag.com/history/air-pollution-has-been-a-problem-since-the-days-of-ancient-rome-3950678/#:~:text=Before%20the%20Industrial%20Revolution%2C%20our,at%20least%202%2C000%20years%20ago . [2] https://www.nrdc.org/stories/air-pollution-everything-you-need-know#sec3 Data OECD - Air Emissions by Source -CRUX Informatics https://aws.amazon.com/marketplace/pp/prodview-dfw7buzlknvzw?qid=1595129067836&sr=0-1&ref_=srh_res_product_title#overview <div