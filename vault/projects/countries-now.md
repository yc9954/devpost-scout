---
slug: "countries-now"
url: "https://devpost.com/software/countries-now"
title: "Countries Now"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 527
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Countries Now

> Integrate Geo-classification into your websites and web applications fast.

[Devpost](https://devpost.com/software/countries-now) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** cloudflare, express.js, handlebars.js, heroku, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for countries now

## Body

landing page Postman Documentation GIF Random countries Example app GIF Country Code Checker Example App GIF Country Cities Viewer Example App Postman Monitor Inspiration The inspiration to build Countries Now came from the recurring need to have a plug and play solution to having countries and states related data in applications. With the rise of Jamstack and Serverless applications, there has been a need to provide different open source "No-backend" solutions for different use cases. One of them is Countries Now. Countries Now is an Open source API that provides countries, states, cities information, including, population, location, number of states, latitude, and longitude of each country and so much more. I had searched for services offering similar data for free but didn't find anyone sufficient enough. There was always one or many issues - terrible documentation, poorly formatted or complex response data, etc. Another major challenge was, libraries tried to make the process of integrating this data into your application seamless, but then came the problem of application size. Libraries like this have an unpacked size of 51.9MB , and in the era of fast websites, this is a drawback. When users have to wait to download large javascript files before they can interact with your website, you tend to lose users and customers. What it does CountriesNow provides open-source data of countries, their respective states, as well as cities within states. It also goes further to provide the location of countries and states by coordinates, flags of countries, country and dial codes, currencies, and a whole lot more. This eliminates the need to install yet another library into your application just for this data, thus increasing page load speed and reducing application build size. How we built it CountriesNow was built using Node.js and Express on the server-side. For proper documentation of API endpoints, I used the Open API specification and Swagger. The API was deployed to Heroku and a custom domain name was purchased on Hostinger . Cloudflare was used for SSL protection and optimization. Challenges we ran into One major challenge we ran into was updating the data source. Most of these data were curated from open source repositories where we have people working tirelessly to update the data every day. We need an efficient and less manual way of updating the data. Accomplishments that we're proud of CountriesNow repository was one of the top Hacktoberfest repositories, we had people contributing tirelessly to make it better. We also recorded a total of 244,451 Monthly requests and a total of 3GB of data served. We were also able to build open-source mini Jamstack applications using the CountriesNow API. We also recorded over 30 stars , 15 Forks, and 8 contributors on the CountriesNow repository. We have also recorded a 100% Average success rate and an average response time of 1.1kms. What we learned We learned how important data is to application development and all the processes involved in efficiently serving data to users and developers. What's next for Countries Now We intend to plug CountriesNow into other third-party data providing services like data-hub and increase the types of geoinformation served to developers and users. <div