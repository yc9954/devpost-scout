---
slug: "sutrobath-ar-tour"
url: "https://devpost.com/software/sutrobath-ar-tour"
title: "Sutro Baths AR Tour"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 574
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Sutro Baths AR Tour

> Our AR tour guides you around a reconstruction of the Sutro Baths historic landmark at the site of its ruins in San Francisco. Learn, view photographs, and interact with the 3D model as you explore!

[Devpost](https://devpost.com/software/sutrobath-ar-tour) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** arcore, blender, c#, geospatial, map-tiles, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sutro baths ar tour

## Body

Sutro Baths AR model seen through Google Pixel 7a In-app view of a user viewing the entrance in AR Unity render of the glass dome In-app view of a user viewing Sutro's Museum in AR Tour marker and content in Unity In-app view of the baths Bird's eye view of the tour route Render in Unity of the full Sutro Baths Unity render of the 1930s art deco entrance Inspiration We are inspired by the opportunities that mixed reality will bring for enhancing experiences and interactions in tourism, real-estate, and entertainment. In particular, we saw the Geospatial Creator as a tool that we could use to build engaging tours at historic sites. The Sutro Baths ruins seemed like the perfect place to create an educational experience on some San Francisco history. What it does Our application guides the user through the Sutro Baths historical landmark using an illuminated walking path, information panels with text and images, and a 3D rendering of how the Sutro Baths swimming pool complex would appear to those attending. Simple sliders and toggles in the app allow users to interact with the 3D models, revealing hidden components and changes over time. How we built it We built the application using Unity 2022 LTS and the Geospatial Creator and Map Tiles SDK. The tour path uses a Bezier spline plugin, and the tour stops are activated by distance. We modeled the 3D assets in Blender and created textures in Photoshop, using historical photos as reference and source material. Geospatial Creator allowed us to anchor the AR experience to the historic site. Challenges we ran into We were hoping to deploy the application to an iOS device but the Mac computer we have access to was too old to deploy to modern iPhones, since Apple routinely deprecates O/S against iOS versions. The mobile device requires a very accurate GPS signal in order to render the anchored content in the exact location where is was placed within the Map tiles. Otherwise, the content drifts away slightly from the correct position. We also had trouble getting the vertical positioning of the content to line up automatically, so we decided to include an in-app slider for adjustments. Accomplishments that we're proud of We are proud of building and deploying an engaging and fully functional application on our Android devices that tourists can use to enhance their visit to the Sutro Baths landmark. We've created an immersive and educational experience that can be widely enjoyed. We're also proud of the quality and accuracy of the 3D models we created in limited time. It took some detective work to find good reference photos for model shape, scaling, and textures. What we learned We learn how to use Geospatial and Map Tiles SDKs to build location-aware mixed-reality experiences on mobile devices. We also gained skills using reference photographs and 3D tools to build historically accurate models. Configuring these models to render correctly in Unity was also new to us. What's next for Sutro Baths AR Tour The mobile phone is an intermediary device for us. We would eventually like to deploy the application to AR glasses and mixed reality devices like the Meta Quest 3. We'd also like to add more content to the tour, including indoor components of the model. If there's interest in this project, we'd love to create similar tours for other sites like the Ancient Roman Forums, which have already been intricately modeled. <div