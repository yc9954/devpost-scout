---
slug: "water-quality-prediction"
url: "https://devpost.com/software/water-quality-prediction"
title: "Water quality prediction"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 847
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Water quality prediction

> This project predicts the water quality basing on contamination of certain elements in water.

[Devpost](https://devpost.com/software/water-quality-prediction) · hackathon [[HackSwift 2024]]

## Facets

**substrate** [[structured_db]] [[video_visual]]

**stack** numpy, pandas, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration As our team consists of different people that aren’t really familiar with each other or know each other it was a bit of a challenge to come up with an inspirational topic. So, we started out researching some available datasets that would be interesting and lined up with the topic of the hackathon. This theme being “Streamlining Solutions for Global Challenges.” We came up with multiple different options but quickly agreed and decided to pick and focus on a dataset for water quality classification. This because it fit well with the theme regarding global challenges, as access to clean and safe water is one of most basic the human needs. This is also shown as part of the United Nations sustainable development goals as goal 6: ‘’Ensure access to water and sanitation for all’’. Where worldwide challenges already exist that are only predicted to worsen with an even further increasing demand. The submission may not directly be linked to the scarcity or actual improvement of water quality as it is based on a fictional dataset, we believe it could still help with the understanding and determination of water quality with regards to safety for consumption. This because the dataset consists of many different characteristics or elements in the water that affect the quality and thus the safety if their quantities are too high. The quantity threshold where water is considered to be dangerous and unsafe to drink differs between elements. These are also defined within the project. What it does The project analyses a dataset of elements and attributes across ±8000 samples. These are preprocessed and ran through different models to determine if the sample is safe or not. This is determined based on the measured amount of 20 elements across the sample. They all have their own specific threshold for what is considered dangerous. This means that if the level in one of the elements exceeds this threshold the entire sample would be considered unsafe and thus should not be consumed (without further treatment). How we built it Perhaps not the most efficient way, but we all decided to individually approach the preprocessing process and then later on compared these to come to a final version. As there are different skill levels and familiarities regarding the machine learning aspect of the project some people had an easier time and were able to already expand upon this by utilizing different models as well. After the discussion it there was some uncertainty on how to proceed and further improve the project. We eventually decided to expand by using some more additional models as well as to take good parts from the other codes to improve the most extensive version and also start trying to increase the legibility by making the results more readable for the general public, by also implementing the results in graphs and images rather than just tables or a result line. Ultimately, we presented on a graph how different model cope with this problem and what was their accuracy. Challenges we ran into Challenges were regarding the meetings and discussions where we were often initially not really sure what to pick, do or how to proceed, having a bit of trouble with actually making decisions. This brought down the efficiency as it took up quite some time. Some other challenges were the different skill levels and familiarity regarding the topic, implementation and machine learning in general. Some people worked on something similar before and some never did anything with it. While one of the goals is to also learn from the project and experience this made it more difficult for everyone to participate equally. With the program itself we had some problems with different formats of data in our dataset, but we quickly resolved this issue. We also had some struggles with visualizing the data, but fortunately we came into ideas that we were satisfied with. Accomplishments that we're proud of Despite some initial trouble regarding actual decision making and the different people in the time across different countries and time zones we still worked well together and reached multiple high accuracies across different models. Furthermore, we all learned something new and had a great time working on this machine learning problem. What we learned This depends on and is different from person to person, but we learned more about classification in machine learning and teamwork regarding working together with new and unfamiliar people. We also learned how to use hyper parametrization, data preprocessing and other things that make our models work as good as they can. What's next This is difficult to answer as the project has a fictional dataset and thus is not necessarily a reflection on a real-life problem or situation. But it could be nice if other people look at the project and learn from it, and possibly implement it to help improve the situation and water quality somewhere in the world. In addition, thanks to this hackathon we can have some background information for another machine learning problems and in the future we can solve more sophisticated issues. <div