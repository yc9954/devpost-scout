---
slug: "cloud-native-movie-catalogue-web-app"
url: "https://devpost.com/software/cloud-native-movie-catalogue-web-app"
title: "Cloud native Movie Catalogue Web app"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 396
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
---

# Cloud native Movie Catalogue Web app

> a cutting-edge, user-friendly platform where movie enthusiasts can effortlessly explore, discover, and curate their favorite films.

[Devpost](https://devpost.com/software/cloud-native-movie-catalogue-web-app) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[code_repository]]

**stack** apim, cloud, grafana, gravitee, prometheus

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for movie catalogue web app

## Body

Inspiration Our inspiration stems from the impressive capabilities of the Gravitee APIM tool and its feature. Witnessing the efficiency and flexibility of these technologies sparked our ambition to apply similar principles to the realm of movie cataloging. What it does Our Cloud Native Movie Catalogue Web App revolutionises the way users interact with movie data. It provides a seamless platform for users to effortlessly add, search, and delete movies from the catalog. Drawing inspiration from Gravitee APIM and its monitoring tools, our web app incorporates robust features and a user-friendly management tool to secure and monitor the overall movie catalogue application. APIM[Gravitee APIM] -->|manages| GW[Gateway API] GW -->|serves| WebApp[Movie Catalogue Web App] APIM -->|monitored by| Prometheus Prometheus -->|visualization with| Grafana How we built it We built the Movie Catalogue Web App by leveraging the power of cloud-native technologies. Our development process involved the careful integration of Gravitee APIM principles and its functionalities, ensuring a scalable, efficient, and dynamic movie cataloging solution. Use cases: curl -X POST https://trial.apim.trial-devex.gravitee.xyz/movie -H 'Content-Type: application/json' 'X-Gravitee-Api-Key: 7c2c924d-a949-46e6-8466-6df5988b7a12' -d '{ "title": "Avatar III", "year": 2024, "cast": ["Sam Worthington"], "genres": ["Action"] }' curl --header "X-Gravitee-Api-Key: ec7dab14-3e70-4cf9-9545-a6d32e7fea35" https://trial.apim.trial-devex.gravitee.xyz/movies/year/2023 [{"cast":"Robert Downey, Jr., Chris Evans, Chris Hemsworth","genres":"Action, Drama","title":"Avenger War Cry III","year":2023},{"cast":"Tom Holand","genres":"Action, Drama","title":"Uncharted II","year":2023}] curl --header "X-Gravitee-Api-Key: ec7dab14-3e70-4cf9-9545-a6d32e7fea35" https://trial.apim.trial-devex.gravitee.xyz/movies/name/Av [{"cast":"Robert Downey, Jr., Chris Evans, Chris Hemsworth","genres":"Action, Drama","title":"Avenger War Cry III","year":2023},{"cast":"Sam Worthington","genres":"Action","title":"Avatar III","year":2024}, Challenges we ran into Throughout the development process, we faced challenges in aligning the Gravitee APIM and monitoring elements seamlessly with Grafana. Overcoming these hurdles required creative problem-solving and collaboration among the team members. Accomplishments that we're proud of We take pride in successfully translating our inspiration into a functional and user-friendly Movie Catalogue Web App. The seamless integration of Gravitee APIM principles and prometheus into the cloud-native environment showcases our dedication to delivering an innovative solution. What we learned The project provided valuable insights into the intricacies of combining Gravitee APIM and its other features. We gained a deeper understanding of cloud-native development, API management, Gateway API, and container orchestration, further expanding our technical expertise. What's next for Movie Catalogue Web app Looking ahead, we plan to enhance and expand the Movie Catalogue Web App. Future iterations may include features such as user profiles, advanced search capabilities, and integrations with popular streaming platforms. We are committed to evolving our app to meet the evolving needs of movie enthusiasts in the cloud-native landscape. <div