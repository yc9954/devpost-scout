---
slug: "fashion-speedometer"
url: "https://devpost.com/software/fashion-speedometer"
title: "Fashion Speedometer"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 633
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/web_dom"
---

# Fashion Speedometer

> Helping consumers check the sustainability of online products.

[Devpost](https://devpost.com/software/fashion-speedometer) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[labor_employment]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[web_dom]]

**stack** ajax, css, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fashion speedometer
- how fashion speedometers is sustainable (for most sustainable hack - sponsor track)

## Body

FashionSpeedometer Chrome extension. Rating H&M dress; environmental rating is high due to use of organic fibers (Keywords: "linen", "cotton"). Full Report webpage linked to chrome extension. Each category specifically explains the rating received. Inspiration Fast fashion - the rapid and unsustainable mass production of clothes - is a growing concern that threatens the environmental future of our planet, particularly exploiting developing countries. The $5 shirt you bought on SHEIN because it was trendy on TikTok was likely made by a child from materials that will release microplastics and chemicals into a landfill after you wear it for maybe 3 weeks, tops. While public awareness of unsustainable fashion is increasing, it can be difficult to remember and identify the signs of fast fashion while shopping. We hope to curb the explosion of fast fashion by providing convenient and accessible information about products to better inform consumers. What it does FashionSpeedometer is a Chrome extension that works as a plugin for any shopping website. Using Python, FashionSpeedometer web scrapes the page for relevant information on worker safety, and materials used. This information is then used to develop a comprehensive rating that evaluates both environmental and labor sustainability. The user can access a full report from the extension, which explains the rating of the product. How we built it The Chrome extension and full report website were created using HTML and styled with CSS. The active elements on the extension that interact with the website were created using Javascript. For example, Javascript is used to mine the page URL, and passes this to a Python program to web scrape. Python then filters the page for specific keywords and produces a text file embedded into the full report. Challenges we ran into Although we have limited experience building webpages using HTML and CSS, we were shocked when we discovered how Chrome extensions are actually quite different from webpages, and require a more complex code architecture in order to respond to events and actions on the webpage that it plugs into. As such, there was a bit of an unexpected learning curve for this project. Additionally, we struggled with piecing together the frontend and backend of the product within the timeframe in order to create a fully functional extension. Accomplishments that we're proud of As mentioned above, we really struggled with not only developing a beautiful UI/UX experience and a versatile web scraping backend, but managing to seamlessly piece the two together. However, in the end, with a lot of dedication (and StackOverflow), we managed to do it! It feels great to see our ambitious ideas come to completion. What we learned The more challenging learning experience - by far - was learning how to extract data from the webpage in order to web scrape. We explored many different approaches, and along the way gained a higher understanding of Javascript, Node.js, React, and web-interactive Python APIs. What's next for Fashion Speedometer We hope to expand upon the Full Report website linked to the Chrome extension and implement a GoogleSearch API that can instantly find and rate similar products. As it is now, FashionSpeedometer provides comprehensive and convenient information on any product, making it the perfect shopping buddy. It would be interesting to see if FashionSpeedometer could become its own independent marketplace, where consumers are encouraged to make sustainable choices regarding their clothes. How Fashion Speedometers is Sustainable (for Most Sustainable Hack - Sponsor Track) The Fashion Speedometers allows consumers to reflect on their purchases and consider choosing more ethical and sustainable fashion. Fast fashion is a leading contributor to pollution in the world (Did you know? 85% of textiles end up in landfills every year!). By informing consumers, Fashion Speedometer hopes to reduce the number of fast fashion pieces purchases and inspire ethical and sustainable buying standards. <div