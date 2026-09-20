---
slug: "pragati"
url: "https://devpost.com/software/pragati"
title: "Pragati"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 1279
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Pragati

> Web app for underdeveloped but talented women to become financially independent by allowing them to post self-made products/services with Women in News Ask Desk for guidance and Emergency SOS service.

[Devpost](https://devpost.com/software/pragati) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** bootstrap, css, express.js, git, github, google-cloud, html, javascript, ml-model, mongodb, node.js, postman, sentiment-analysis, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pragati

## Body

Welcome to Pragati! Join Pragati by signing in today! Shop classy handmade products by talented artists Post your handmade products on Pragati for sale Opt for services offered by our professionals Post services which you wish to provide This section enables women to ask & solve their genuine queries & get advice on social & personal concerns Stay updated about how women are progressing in different fields through a section of news & articles of the latest success stories Inspiration Rural India has commonly observed that men are the sole earning members in 85% - 90% of the families. Numerous circumstances disallow a woman to go out and make a living, even if she wishes to. The most common reason being, no support or “permission” granted by family; she is often ridiculed and labelled incapable. She is ordered to handle household chores as apparently she’s born to raise children and serve her family. Most can’t fight for rights, out of respect, thus caught under lifetime-domination. Narrow-minded mentality leads to being too conservative to let women go out, interact with strangers, and face the outer world. Scarce jobs for illiterate but talented women, being desperate to earn, leaves them hopeless and dejected. Considering these issues, we thought of innovating a solution, empowering talented housewives to earn independently from home without relocating, and simultaneously attempt to preserve the dying heritage of Indian “hand-made” goods. Thus we bring to you Pragati, a web application that empowers rural housewives to earn money by selling their own authentic self-made products from home & providing reliable services on the go . Our aim is to expand the reach of rural heritage both locally & amongst the urban too, thus bridging the gap between societies. What it does 1. The website revolves around enabling women to post specific home-made products they want to sell like pottery, embroidered materials, paintings, knitted clothing, healthy home-made snacks, etc, or even services like salon services or tiffin services that they can provide. 2. Clients based on their nearby locations, can view their uploaded products/services & contact them if they wish to purchase or seek services by registering their interest on the portal. 3. There is an Ask Desk section that enables women to ask & solve their genuine queries & get advice on social & personal concerns, hence helping them to be future-ready. 4. To stay updated about how women are progressing in different fields, there's a section of Women In News and articles of the latest success stories that act as a source of inspiration. 5. To prevent exploitation of users or misuse of the application, there’s an in-built SOS feature that women can use to connect helplines or police in case of emergency. 6. We have an instant SMS service incorporated at each and every step in our application. Therefore the barrier of internet prevailing in few backward areas do not hamper women from using our application. How we built it We used Figma to design the webpages since we were so keen on making a beautiful UI. The website frontend was made using HTML, CSS, and JS . The website backend was made using Node JS and MongoDB as the database. The backend is deployed on Google Cloud Platform ( App Engine ) and is up and live at https://mindful-ship-302014.appspot.com/ We used Domain.com to register a domain name for our website. risewithpragati.space Overall, it was a great learning experience trying our hands on several new software and building the site from scratch during the weekend. Challenges we ran into Working on various high-level tech stacks was a challenging yet satisfying experience for all of us. We learned to enable SOS service for the guaranteed safety of users by integrating the OpenCage Geocoder API for obtaining their exact location and mapping the women's helpline numbers , which was time-consuming since we were doing it for the first time. In order to preserve the integrity of women, we developed an ML model for integrating the sentimental analysis feature using MeaningCloudAPI while taking inputs. This ensured that any negative sentimental keyword isn't being accepted by the application. It was a tough task to achieve this but we did manage it successfully. As we were building the PWA, working with manifest files and service workers caused caching issues as the new changes weren't being replicated immediately on the site without a hard refresh. After fixing the issue with the help of stack overflow, we learned that adding service workers should be the last step of building an application. The biggest hurdle was the CORS(Cross-Origin Resource Sharing) error that occurred time and again. At first, we could not identify the problem but learned the fix in the process. Accomplishments that we're proud of We are super proud of the fact that we learned various technical concepts from scratch during this weekend and ended up making an efficient and useful web application serving its purpose for society. This project gave us the opportunity to explore and work on something out of our comfort zone. We tried incorporating as many features as we could in this creation of ours, considering every use-case for our clients to get a seamless UX. For the first time, we learned using the Google Cloud Platform to deploy the backend of our web application. It was a bit challenging at first but eventually, we did figure out the whole process. Hosting the website on a different domain using Domain.com was also new to us but enjoyable at the same time. We ended up building a project that would help create a huge difference in the way of living of underprivileged women and of course, getting acquainted with some great development experience which was a bit frustrating but fruitful at the same time. After overcoming numerous hurdles, we are now much more confident as web developers and proud of being able to contribute to society in an efficient way. What we learned We learned how to create a PWA(Progressive Web App) for easy phone accessibility which was needed so that the SOS feature can be accessed from anywhere anytime even without the need for the internet. We learned to integrate several third-party APIs with our front-end for different functionalities. They are as follows : 1. OpenCage Geocoder API - Geolocation services used in SOS 2. MeaningCloud - Sentiment analysis of the questions/descriptions being posted on the portal 3. MediaStack - Women in News API 4. D7 Networks - Instant messaging service 5. Cloudinary API - Products and Services image gallery Apart from the challenges, we successfully managed to incorporate these APIs into our project to make it as efficient as possible for the users. What's next for Pragati As far as future enhancements are concerned, we have planned to incorporate several advanced features pertaining to our user’s experience, and benefit. 1. Language Translation: We have thought of implementing an all Language translation of the website so that there are no language bars for people from different areas. 2. Voice to text: We do not wish to have any barriers to literacy for our application. For increasing the reach amongst illiterate people, we also thought of implementing the Voice to Text using Google voice to text API. 3. Increased User Interaction: We will include more user interaction on the portal such as commenting/liking the QnA on Ask Desk and Rating products and services for a better user-experience. The above features, once incorporated and intertwined, can lead to a one-stop application that would consist of everything one can need when it comes to improving not only the overall economic state of India but also the intellectual and personal growth of women. <div