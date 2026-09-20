---
slug: "a-qeysp1"
url: "https://devpost.com/software/a-qeysp1"
title: "FairTorch"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 590
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/labor_employment"
---

# FairTorch

> FairTorch provides tools to mitigate inequities in deep learning. A unique feature of this tool is that you can add a fairness constraint to your model by simply adding just a few lines of code.

[Devpost](https://devpost.com/software/a-qeysp1) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[education]] [[labor_employment]]

**stack** python, pytorch

## How they structured the write-up

- inspiration
- what it does
- challenges i ran into
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for fairtorch
- references

## Body

Overview Theory Inspiration n recent years, machine learning-based algorithms and softwares have rapidly spread in society. However, cases have been found where these algorithms unintentionally make discriminatory decisions(e.g., the keynote by K. Crawford at NeurIPS 2017). For example, allocation harms can occur when AI systems extend or withhold opportunities, resources, or information. Some of the key applications are in hiring, school admissions, and lending. [1] Since Pytorch didn't have a library to achieve fairness yet, we decided to create one. What it does FairTorch provides tools to mitigate inequities in classification and regression. Classification is only available in binary classification. A unique feature of this tool is that you can add a fairness constraint to your model by simply adding a few codes. Challenges I ran into In the beginning, we attempted to develop FairTorch based on the fairlearn’s reduction algorithm. However, it was implemented based on scikit-learn and was not a suitable algorithm for deep learning. It requires ensemble training of the model, which would be too computationally expensive to be used for deep learning. To solve that problem, we implemented a constrained optimization without ensemble learning to fit the existing fairlearn algorithm for deep learning. How we built it We employ a method called group fairness, which is formulated by a constraint on the predictor's behavior called a parity constraint, where X is the feature vector used for prediction, A is a single sensitive feature (such as age or race), and Y is the true label. A parity constraint is expressed in terms of an expected value about the distribution on (X, A, Y). In order to achieve the above, constrained optimization is adopted. We implemented loss as a constraint. The loss corresponds to parity constraints. Demographic Parity and Equalized Odds are applied to the classification algorithm. We consider a binary classification setting where the training examples consist of triples (X, A, Y), where X is a feature value, A is a protected attribute, and Y ∈ {0, 1} is a label.A classifier that predicts Y from X is h: X→Y. The demographic parity is shown below. E[h(X)| A=a] = E[h(X)] for all a∈A ・・・(1) Next, the equalized odds are shown below. E[h(X)| A=a、Y=y] = E[h(X)|Y=y] for all a∈A, y∈Y・・・(2) We consider learning a classifier h(X; θ) by pytorch that satisfies these fairness conditions. The θ is a parameter. As an inequality-constrained optimization problem, we convert (1) and (2) to inequalities in order to train the classifier. M μ (X, Y, A, h(X, θ) ≦ c・・・(3) Thus, the study of the classifier h(X; θ) is as follows. Min_{θ} error( X, Y) subject to M μ (X, Y, A, h(X, θ)) ≦ c To apply this problem to pytorch's gradient method-based parameter optimization, we make the inequality constraint a constraint term R. R = B |ReLU(M μ (X, Y, A, h(X, θ)) - c)|^2・・・ (4) Accomplishments that we're proud of We confirmed by experiment that inequality is reduced just adding 2 lines of code. What we learned What we learn is how to create criteria of fairness, the mathematical formulations to achieve it. What's next for FairTorch As the current optimization algorithm is not yet refined in FairTorch, we plan to implement a more efficient constrained optimization algorithm. Other criteria of fairness have also been proposed besides demographic parity and equalized odds. In the future, we intend to implement other kinds of fairness. References A Reductions Approach to Fair Classification (Alekh Agarwal et al.,2018) Fairlearn: A toolkit for assessing and improving fairness in AI (Bird et al., 2020) <div