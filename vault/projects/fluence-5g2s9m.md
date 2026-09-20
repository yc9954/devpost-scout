---
slug: "fluence-5g2s9m"
url: "https://devpost.com/software/fluence-5g2s9m"
title: "Fluence"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 732
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/researcher"
---

# Fluence

> A Pytorch based Deep Learning library for Low resource NLP research and robustness

[Devpost](https://devpost.com/software/fluence-5g2s9m) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[researcher]]

**stack** python, pytorch, transformers

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fluence

## Body

Inspiration Transformers are getting bigger and better. The SoTA baseline seems like a never-ending chase. However, this progress raises concerns on two cardinal aspects: How much compute do these models require? The largest transformer (GPT-3) requires 10K GPUs for performing few-shot learning. This is 10x bigger than the previous largest transformer. These models require extensive compute (training time), huge amounts of data to perform well. What are they learning and how it is carried out? These large pre-trained LMs are brittle when distribution shifts during inference. They are biased (for instance, generative models such as GPT-2 will associate nurses with women often). They are treated as black-box models in some aspect, we don't know what impact does finetune has and broadly, what do they look at and how do they perform this reasoning. What it does The main goal is to provide standardized modules for compute-efficient and robust algorithms. Compute efficient methods such as ZSL, Meta-Learning, Adaptive methods, Importance sampling can reduce the amount of data our models need and at the same time provide us competitive performance with standard fine-tuning methods. Another line of research has dived into how we can make these models robust. Debiasing methods aim to provide models with more generalization capabilities. Interpretability methods such as probing classifiers help us study their internal dynamics. Fluence provides standardized API (similar to HF Transformers) to integrate these methods with existing workflows. Almost all the modules require similar arguments as any transformers code would require minimal changes. Thus reducing overhead from the user's endpoint. More details can be found in the video. How I built it This library uses Pytorch for all its functionalities. This library is part of a research project which will be published in the next few months. Being an active user and contributor of Pytorch and Transformers, I realized that there is some form of the gap that can be filled in regards to computing efficiency and robust methods. I looked at many different implementations to understand the issues (different ways of loading data, models expecting different inputs, custom training loops, no standard way to report results) and want to address these issues in this domain similar to Transformers. You can simply feed in any Automodel or nn.Module model, wrap it inside Fluence provided methods and let the rest be taken care of by it. The current functionalities come from what I feel were the essential starting point. Challenges I ran into It took me a lot of time to make some methods work (such as HEX, due to its instability with matrix inversion, MAML for transformers, which now uses higher , integrating these methods with HF Pytorch Trainer ). I had to read many different papers to understand the problems and how they can be better implemented. Some of the methods were implemented in TF which were ported to PT (required me to read TF docs). Accomplishments that I'm proud of I am proud of implementing modules that didn't have a proper implementation. This library going forth will include some of the best practices in research. In the process, I submitted several PRs to the Transformers repo. For instance, adding Pytorch Native AMP in the Trainer . I think Fluence's direction will be determined by the community response. It has always been one of my research goals to create an ML library that makes it easier for researchers to try out their ideas and prototype it with minimal overhead. What I learned I learned a ton about NLI research since this is the task on which I tested out these methods. I learned a lot about the Transformers library such as their standard APIs to instantiate modules and training workflow. I liked it and this is one of the reasons why Fluence integrates with their workflow. I learned about code coverage in general and added it to this library. What's next for Fluence There are a lot of things which will come to Fluence in the coming months. The meta-learning pipeline needs improvement in terms of providing flexibility to users. I hope to add improved pruning methods (inspired by LTH). There are a few sampling methods currently. I hope to make the data order aspect easy to manage. I want to add sparse methods also possibly which integrates well with autograd . Improvements in documentation and the addition of examples will be an ongoing effort. <div