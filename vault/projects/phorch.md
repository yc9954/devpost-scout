---
slug: "phorch"
url: "https://devpost.com/software/phorch"
title: "Phorch"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 384
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "substrate/web_dom"
---

# Phorch

> Don't be a victim of phishing attacks!

[Devpost](https://devpost.com/software/phorch) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**domain** [[scientific_research]] [[security_privacy]]
**substrate** [[web_dom]]

**stack** geoip2, heroku, python, pytorch, sqlite, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for phorch

## Body

Inspiration A malicious website is a foundation of criminal activities on the Internet. This link enables partial or full machine control to the attackers. This results in victim systems, which get easily infected allowing attackers to utilize systems for quite a number of cyber-crimes such as stealing credentials, spamming, phishing, denial-of-service, and many extra such attacks. The rising issue related to spamming, phishing and malware, has created a requirement for a solid framework solution that can analyze the extracted features, classify and further recognize the malicious URL. Therefore, the methodology and technique to detect such crimes should be fast and precise with the additional capability to detect new malicious websites or content. What it does Adversarially attack the data using FIGA (Feature Importance Guided Attack) and create 3 different attack sets of data based on certain parameters We utilize these data features to implement adversarial training as a defense against FIGA using neural net architecture in PyTorch Web application demonstrates URL prediction in 2 forms where it serves as a standalone URL checker and also fetch random topic-based tweets to identify any malicious redirection How we built it What is FIGA FIGA is model agnostic, it assumes no prior knowledge of the defending model's learning algorithm, but does assume knowledge of the feature representation. FIGA leverages feature importance rankings; it perturbs the most important features of the input in the direction of the target class we wish to mimic. Creating an adversarially hardened model We train the defending model using unmodified data and correctly labeled adversarial samples. The expectation is that training the model with adversarial samples will improve its performance. Challenges we ran into Deciding on the parameters for data perturbation Improving model for decent predictions Accomplishments that we're proud of Creating something that can be utilized right away for cyber security purposes What we learned Learning about PyTorch and its capabilities Reading through various research papers and increasing our knowledge in the field What's next for Phorch We aim to make a package out of it so that the model can be utilized by social media and similar applications to moderate content such as promotions and offers which may lead to unethical data extraction by fooling people with phishing urls. Further, improve on the model to generate better results and predictions <div