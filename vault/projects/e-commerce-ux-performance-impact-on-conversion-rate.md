---
slug: "e-commerce-ux-performance-impact-on-conversion-rate"
url: "https://devpost.com/software/e-commerce-ux-performance-impact-on-conversion-rate"
title: "e-Commerce UX Performance Impact On Conversion Rate"
hackathon: "AWS Deep Learning Challenge"
organization: "Amazon"
winner: true
words: 601
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/simulation_digital_twin"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# e-Commerce UX Performance Impact On Conversion Rate

> Amazon study says 100ms slowness page load time cost 1% in revenue. Built a Deep Learning ML model to prove UX Performance impact on Conversion rate and which UX Performance KPIs matters most.

[Devpost](https://devpost.com/software/e-commerce-ux-performance-impact-on-conversion-rate) · hackathon [[AWS Deep Learning Challenge]]

## Facets

**mechanism** [[measured_ablation]] [[simulation_digital_twin]]
**domain** [[retail_commerce]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-ec2, habana.ai, python, pytorch, sagemaker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that i am proud of
- what's next for e-commerce ux performance impact on conversion rate

## Body

Inspiration Being a Performance Engineer for last 15+ years , any sort of performance be it frontend or backend is very critical for me. Though its always very hard to map the performance impact to business outcome mainly when it comes to eCommerce platform. As part of this project I am trying to establish this relationship , so it will becomes easy to present a case to any business when questions come down to why performance matters so much ? What it does This model analyze all historical sessions information mainly focused on UX &Backend performance KPIs to find out the KPIs which matters most when it comes to conversion /non-conversion of sessions. It helps to identify top critical performance KPIs , simulate a slow % improvement into those KPIs as part of experiment and understand the impact of that on conversion rate. It takes non-converted session to prove the hypothesis by running experiments and see how non-converted sessions changes to converted sessions as we improve the performance of those KPIs one at a time. How we built it This is built using Deep Learning Binary Classification model using PyTorch framework. It uses around 80k+ data rows and 45+ parameters. As it progress , the model focused on only the KPIs which matters most. These rows are one line per user session with final outcome of converted vs non-converted session. Once the model trained with 95% of data with 505 sessions of 50% mix of converted & non-converted session data which are not used for training or testing is used to run experiments. Trained model work on 505 sessions by reducing (simulating performance improvement) one KPI value at a time (by 5%,6%,7%,8%) and running predictions to see if we observe any shift from non-conversion sessions to conversion sessions as part of binary classification. Post that overall change from non-converted to converted sessions are calculated and based on that the model provide which are critical KPIs can have impact on overall conversion rate and by how much? Challenges I ran into Getting session level data , used a real data set adding masking where needed. Accomplishments that I am proud of Manage to use DL1 Habana Gaudi accelerators which reduced training time by 75% compared to 6 GPU platform. Conversion rate is very critical for all businesses but issue is they struggle to understand which are those critical KPIs needs to tune/optimized to drive to increase it. This model is POC which focused on UX Performance to start with but its not limited to using those KPIs only , we can push any KPIs which are business critical to understand and simulate the scenarios rather than spending time and money on these A/B experiments in production. What I learned For comparison purpose i trained the same model using Sage maker Studio Lab running with 6 GPU vs DL1 Habana Gaudi accelerators. Found that running on DL1 Habana Gaudi accelerators model took 75% less time to train for same amount of data and same number of epoch. What's next for e-Commerce UX Performance Impact On Conversion Rate Hyperparameter tuning to increase accuracy further of the model at least to from 81% to 90% though 81% accuracy in e-Commerce business is good enough to prove the case ( as even 0.1% conversion uplift in high volume business can have massive impact on revenue increase)​. Present this outcome to business to create a case , so that these improvement can be implemented ​ Once the improvements are in place carry out A/B Testing to verify actual conversion rate uplift with real user in production​. <div