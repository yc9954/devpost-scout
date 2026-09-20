---
slug: "dpancestry"
url: "https://devpost.com/software/dpancestry"
title: "DPAncestry"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 478
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "domain/civic_government"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/genomic_bio"
---

# DPAncestry

> Ensuring genomic data privacy with cutting-edge local differential privacy algorithms

[Devpost](https://devpost.com/software/dpancestry) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[privacy_tech]]
**domain** [[civic_government]] [[scientific_research]] [[security_privacy]]
**user** [[researcher]]
**substrate** [[genomic_bio]]

**stack** javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dpancestry

## Body

Inspiration Genomic data is unique in that it is both incredibly personal and near impossible to change. Companies that store genomic data for analysis are vulnerable to data breaches, both traditional direct breaches and indirectly revealing insights into their data via the AI tools they develop. What it does DPAncestry is a platform that uses state-the-the-art local differential privacy algorithms to securely process genomic data while maintaining individual privacy. By adding a layer of obfuscation to the data, DPAncestry ensures that sensitive information remains confidential, even when analyzed for ancestral insights. While many top companies and organizations such as Google, Microsoft, Apple, and the U.S. Census Bureau have already adapted differentially privacy in their models, our platform is, to our knowledge, the first to pioneer this idea for the genetic testing sphere. To learn more about the research we referenced while developing our platform, check out: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9073402/ How we built it DPAncestry leverages local differential privacy (DP) algorithms, which work by adding controlled noise to individual data points before any analysis occurs. This approach ensures that the true values are obscured, but useful aggregate information can still be derived. We built our platform based on the methods detailed in the paper we cited, which provides a comprehensive framework for implementing differential privacy in genomic data analysis. Challenges we ran into One of the major challenges we faced was choosing a focus for the project that utilizes this advanced technology while still being impactful. Additionally, we had to carefully select the most suitable differential privacy algorithm that balances privacy with data utility, ensuring meaningful insights without compromising individual privacy. Our project additionally required parsing through academic research papers on privacy algorithms, which presented a substantial challenge for converting to a concrete implementation. Accomplishments that we're proud of We are proud of successfully integrating local differential privacy into a user-friendly platform that can handle data as complex as genomic data. It provides a simple, powerful and most significantly, anonymous service for ancestry determination. We also linked an LLM model, Anthropic’s Claude, which guides the user to interpreting their genomics results, and help understanding the privacy mechanisms behind the model. What we learned Throughout the development of DPAncestry, we gained a deeper understanding of the intricacies of differential privacy and how it can protect personally identifiable information. We also learned about the challenges of balancing privacy and data utility, and the importance of user trust in handling sensitive information. What's next for DPAncestry Once our project acquires additional investment, we aspire to accelerate our company into the first DP genetic testing company. We’ll develop our platform into a more cohesive product for seamless usage. Another proposition deliberated by the team was selling our software to genetics testing companies like 23andMe, to recover share prices after their major 2023 data leak, which leaked the sensitive data of over 6 million clients. <div