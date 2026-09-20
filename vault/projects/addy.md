---
slug: "addy"
url: "https://devpost.com/software/addy"
title: "ADDY"
hackathon: "Junction 2016"
winner: true
words: 1435
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ADDY

> ADDY is a revolutionary fun way to advertise. It takes wishes of both the users and the companies into account.

[Devpost](https://devpost.com/software/addy) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]] [[health_clinical]] [[retail_commerce]]
**substrate** [[structured_db]] [[video_visual]]

**stack** html5, javascript, love

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- meet the team
- what's next for addy

## Body

ADDY's logo Demonstration Design process Meet the Team Old version of ADDY Old version of ADDY The scarf that was retrieved from the Zalando API Inspiration At first, we didn't really know what kind of track would be the most suitable one for us. We started walking around at the venue until we stumbled upon JCDecaux's bus stop. Seeing the endless possibilities of providing entertainment to bored waiting people, we immediately knew this was the right challenge for us. We were still spurring out ideas about the bus stop while we walked on to the very other side of the building, where we found out about the presence of Zalando. Combining the many high tech impulses around us with the technological views of Zalando really opened our eyes. We were facinated by the fact that the challenges of JCDecaux and Zalando could be combined, which we think is a very strong cornerstone of Junction. Our society is rapidly changing and the traditional way of advertising clearly can not keep up with it. We saw an opportunity to shift from static advertising to dynamic advertising. The idea of ADDY was born. What it does We are introducing ADDY, a revolutionary way of advertising. ADDY is a smart screen that invites passers-by to interact with its technology, in order to bring a new fun way of advertising to the market. At the moment someone walks past the screen, the camera shifts on and ADDY seeks to get attention from the person. Whenever attention is gained, ADDY tells the person to come closer. If they do come come closer, an outline of a face is shown. Should the person fit their head in the outline, they will be told that it is soon getting cold and that they should be wearing a scarf. Before they even know it, they're suddenly wearing an actual scarf from Zalando! Well, not actually, of course it is projected like that on the screen. Nice comments like "looking good!" are popping up and the users will be stunned by their own looks, they have become the Zalando models they have always aspired to be. Besides experiencing this fun and unexpected turn, people will have more incentives to actually buy the scarf. The price is shown thanks to the Zalando API. After a countdown of 3 to 0, a "picture" is taken, meaning the screen will freeze for a moment, after which you can step back and enjoy what you had just been through. How we built it We faced multiple technical challenge when developing ADDY. We used a C-based Computer Vision library written in Javascript (source: https://github.com/liuliu/ccv ) in combination with an HTML5/CSS3 web interface. We had to distinguish between moving people (who walk past the screen) and watching people (who actually look at the screen). For this, we used motion detection and face recognition. When motion is observed, certain (tracking) overlays are added to a live webcam feed (designed in a HTML5 canvas element) which trigger the attention of the person. When a face is observed, another (tracking) overlay is added. The overlay, in this case, will be a product which needs to be advertised. Our plan was to integrate the ESA API so different scenario's could be chosen according to the weather (so, if it is cold in 1 week, a scarf will be shown; if it the sun will shine, sunglasses will be shown) but we didn't have any time left. For now we have integrated the Zalando API to fetch a scarf from the database and overlay this so that it seems like the person is wearing it. Challenges we ran into To make the concept as clear as possible since we found that it added value to both the customer and the businesses which will be using ADDY. The biggest challenge is to convey a clear message. A technical challenge we ran into: We've found that the JS library are quite useful to develop an MVP (Minimum viable product) to do some tests and show a demo. However, when developing for production faster and more reliable libraries are needed. JS wasn't enough to make all the complex calculations which left the overlays rather jerky. Another technical challenge we ran into was the amount of light that was displayed in the testing space around the bus stop. Because of all the lights, it was difficult to recognize faces and thus place the scarf correctly. We tackled this by turning as many lights off as possible, and therefore creating an environment in which it was possible to film the interaction at least once. Accomplishments that we're proud of We have noticed that at a lot of hackathons, many of the ideas are incredibly fun or amazingly programmed but simply not feasible. We are proud of the fact that we have taken lots of time to work out the business model of ADDY, and that it is actually very clear to see how ADDY can be a valuable addition to the world of marketing. During the process, we spoke to people from JCDecaux and Zalando regularly. They made us realize that the business model is very important as businesses need viable ideas in order to survive in the market. We are also very pleased to have a working prototype of a concept we've been brainstorming on for a very long time during the hackathon. The idea we are presenting seems quite futuristic, we believe. One partner we spoke to about our concept proclaimed he had never heard of anything like it, maybe only once in a science fiction movie in a distant memory. What we learned The number of people that are reached by an advertisement is enormous, yet they are perceived as boring or worthless. This made us wonder why such an innovation as ADDY has never been done before. And frankly... we don't know? We do know that a fairly simple technological solution may have a massive impact on society. ADDY may change the marketing world as we know it, simply because the scene can use a lot of improvements. Last but not least; we have learned a lot about the Finnish culture. We are all from The Netherlands and we've been accepted warmly (I wish this was about the weather) into the community. Some culture differences had sent us on the wrong track at the beginning. We have learned that Finnish people are shy out in public, which has forced us to make decisions that have turned out to be quite okay actually! For example we heard that Finnish people would not do big interactions in front of a big screen when other people are around. This is why we also decided we did not want to make use of the touchscreen, even though it's an amazing addition to the specifications of the screen. Meet The Team Bas Schleijpen - Bas likes to jump into the shower when deadlines are near. When he is dried up, he's a skilled code writer. Joris van Rijn - This man's smooth jacket and classy shoes say it all: Joris is ready to rock the hell out of Junction. And he sure will. Corné van Son - Corné had successfully infiltrated the Junction crew prior to the event. He's a man who sets out goals, and then crushes them. Gustavo Leal - Gus loves to sleep. A lot. Whenever he is awake though, he's an amazing artwork and interface designer. Bert van Gestel - Bert loves to walk around, talking to all sorts of hackers and relevant partners. This slimy talk results into slimy pitches. What's next for ADDY We will see where it goes after this hackathon; hopefully our idea will be recognized by the companies we ought it valuable for. In this way we can for example integrate the ESA API to create content to give very accurate weather predictions along with products that might protect people from bad weather. Our demo was just about Zalando, however there's an endless list of all sorts of companies, whether they are local or global, that can severely profit from ADDY's services. But there's even more purposes for ADDY to serve than just companies: think about charities, raising awareness for issues, educational purposes. Again, the possibilities are beyond imagination. The demo was also just limited to bus stops. But why only bus stops? These screens can be placed anywhere. Busy shopping areas, airports, hospitals, schools, supermarkets, and the list goes on and on. This is an idea that could grow out to be a very important player in the world of marketing. <div