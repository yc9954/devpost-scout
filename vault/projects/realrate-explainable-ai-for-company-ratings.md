---
slug: "realrate-explainable-ai-for-company-ratings"
url: "https://devpost.com/software/realrate-explainable-ai-for-company-ratings"
title: "Causing: CAUSal INterpretation using Graphs"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 848
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/document_pdf"
---

# Causing: CAUSal INterpretation using Graphs

> Causing is a tool for Explainable AI (XAI). We explain causality and ensure fair treatment. It is developed by RealRate, an AI rating agency.

[Devpost](https://devpost.com/software/realrate-explainable-ai-for-company-ratings) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

  <sub>weak: deterministic_policy</sub>
**domain** [[labor_employment]]
  <sub>weak: supply_logistics</sub>
**substrate** [[document_pdf]]
  <sub>weak: structured_db</sub>

**stack** autograd, graphviz, python, pytorch, sympy

## How they structured the write-up

- a real world example
- scientific abstract
- how i built it
- use of pytorch
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next

## Body

Explaing wages for young American workers Causing: CAUSal INterpretation using Graphs Causing is a multivariate graphical analysis tool helping you to interpret the the causal effects of a given equation system. We want to explain AI decisions, ensuring transparency and fair treatment. Causing is explainable AI (XAI): We make transparent black box neural networks. Input: You simply have to put in a dataset and provide an equation system in form of a python function. The endogenous variable on the left had side are assumed being caused by the variables on the right hand sight of the equation. Thus, you provide the causal structure in form of an directed acyclic graph (DAG). Output: As an output you will get a colored graph of quantified effects acting between the model variables. You are able to immediately interpret mediation chains for every individual observation - even for highly complex nonlinear systems. Further, the method enables model validation. The effects are estimated using a structural neural network. You can check wether your assumed model fits the data. Testing for significance of each individual effect guides you in how to modify and further develop the model. The method can be applied to highly latent models with many of the modeled endogenous variables being unboserved. The Causing approach is quite flexible. The most severe restriction certainly is that you need to specify the causal model / causal ordering. If you know the causal ordering but not the specific equations, you can let the Causing model estimate a linear relationship. Just plug in sensible starting values. Further, exogenous variables are assumed to be observed and deterministic. Endogenous variables instead may be manifest or latent and they might have error correlated terms. Error terms are not modeled explicitly, they are automatically dealt with in the regression / backpropagation estimation. A Real World Example To dig a bit deeper, here we have a real world example from social sciences. We analyze how the wage earned by young American workers is determined by their educational attainment, family characteristics, and test scores. https://github.com/HolgerBartel/Causing/blob/master/education.md Scientific Abstract We propose simple linear algebra formulas for the causal analysis of equation systems. The effect of one variable on another is the total derivative. We extend them to endogenous system variables. These total effects are identical to the effects used in graph theory and its do-calculus. Further, we define mediation effects, decomposing the total effect of one variable on a final variable of interest over all its directly caused variables. This allows for an easy but in-depth causal and mediation analysis. To estimate the given theoretical model we define a structural neural network (SNN). The network's nodes are represented by the model variables and its edge weights are given by the direct effects. Identification could be given by zero restrictions on direct effects implied by the equation model provided. Otherwise, identification is automatically achieved via ridge regression / weight decay. We choose the regularization parameter minimizing out-of-sample sum of squared errors subject to at least yielding a well conditioned positive-definite Hessian, being evaluated at the estimated direct effects. Unlike classical deep neural networks, we follow a sparse and 'small data' approach. Estimation of structural direct effects is done using PyTorch and automatic differentiation taylormade for fast backpropagation. We make use of our closed form effect formulas in order to compute mediation effects. The gradient and Hessian are also given in analytic form. How I built it Causing is a free software written in Python 3 . It makes use of PyTorch for automatic computation of total derivatives and SymPy for partial algebraic derivatives. Graphs are generated using Graphviz and PDF output is done by Reportlab . We use PyTorch to perform model estimation. Autograd is used for automatic differentiation of the expert model, giving the indiviual effects of key figures on the financial strenght. I constructed a Structural Neural Network Class (SNN) in order to represent my specail model structure. Graphviz is used to plot easily interpretable dependency graphs. Use of PyTorch Causing uses PyTorch, Autograd, SymPy and Graphviz to explain causality and ensure fair treatment. PyTorch was used for three tasks: Using autograd to compute the effects, being simply the total derivatives of the model. Defining our own NN class: a Structural Neural Network, restricting many weights to zero, enabling identification and interpretation of single neurons ("explainable AI"). Using optimization algorithms like Adam or RProp for estimation of real-world causal effects. Challenges I ran into Autograd cannot be used for cyclic models yet. So I restricted myself to directed acyclic graphs (DAG). Masking via PyTorch, ie restricting certain coeffients to zero is was not flexible enough for my purposes. Accomplishments that I'm proud of I am proud of having made even quite complex models easily interpretable. This is the base for fair treatment by AI. What I learned PyTorch was easy to start with. But I had to build my own customized neural network. I wa happy to learn that PyTorch is tailor-made for those individual customizations. What's next Scalability for big data. Use maksing of model weights to speed-up the model <div