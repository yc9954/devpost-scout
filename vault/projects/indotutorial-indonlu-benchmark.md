---
slug: "indotutorial-indonlu-benchmark"
url: "https://devpost.com/software/indotutorial-indonlu-benchmark"
title: "IndoNLU: Finetuning Tutorial IndoBERT using PyTorch"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 711
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# IndoNLU: Finetuning Tutorial IndoBERT using PyTorch

> In this tutorial, you will learn how to use PyTorch to implement IndoNLU IndoBERT models for sentiment analysis to guide you to be a good deep learning scientist. Have fun and enjoy the tutorial!

[Devpost](https://devpost.com/software/indotutorial-indonlu-benchmark) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[scientific_research]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]

**stack** albert, bert, docusaurus, github, huggingface, numpy, pandas, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i build it
- challenge i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for indonlu: tutorial finetuning indobert using pytorch

## Body

IndoNLU: IndoBERT Finetuning using PyTorch Tutorial Inspiration Our goal in this project is to enable Indonesian NLP researchers and enthusiasts to access latest trend of deep learning technology in NLP with large pre-training corpus and large pre-trained model. By doing so, we believe that it will bring Indonesian NLP research to the next level. Furthermore, we envision that our work can enable future collaboration between Indonesian NLP researchers and resonate even further by inviting more and more people to collaborate in the advancement of Indonesian NLP research. What it does In the IndoNLU project, we introduce the first-ever vast resource for training, evaluation, and benchmarking on Indonesian natural language understanding (IndoNLU) tasks. IndoNLU includes twelve tasks, ranging from single sentence classification to pair-sentences sequence labeling with different levels of complexity. The datasets for the tasks lie in different domains and styles to ensure task diversity. We also provide a set of Indonesian pre-trained models (IndoBERT) trained from a large and clean Indonesian dataset (Indo4B) collected from publicly available sources such as social media texts, blogs, news, and websites. We release baseline models for all twelve tasks, as well as the framework for benchmark evaluation, thus enabling everyone to benchmark their system performances. How I build it We built IndoNLU framework along with benchmark, large-scale pre-training dataset, and large pre-trained models. We build the framework from scratch by using PyTorch and HuggingFace. We collect 12 tasks for the benchmark from multiple published sources. For pre-training dataset, we collect dataset from 15 sources that is publicly available. For large pre-trained model, we train BERT and ALBERT models with the official code and convert the weight into PyTorch model format and host the model in the HuggingFace platform. Challenge I ran into We found a lot of challenges in the process of making this project. First, in terms of model, we lack of computational resources for building large pre-trained models, and we managed to solve it through collaboration with many parties. Second, in terms of the benchmark tasks and pre-training corpus, we had issues with collecting tasks and pre-trained corpus for Bahasa Indonesia, because the data is scattered and some sources are hard to access. Accomplishments that I'm proud of This IndoNLU benchmark has helped and will continue to help a lot of Indonesian researcher to do research on NLP in Bahasa Indonesia. The resources provided, the models and the datasets has also inspired others to build better models and assemble more Bahasa Indonesia dataset. Moreover, the documentation of this research has been accepted in the AACL-IJCNLP 2020 to be published as the one and only Indonesian research paper in that top conference. In short we are proud to contribute to Indonesian researcher as we also proud to represent Indonesia in presenting the research paper: IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding the AACL-IJCNLP 2020 What I learned While developing this IndoNLU benchmark and IndoTutorial, we learned many things, that is to build bert model from scratch, to create a large scale pretrained corpus, and we actually knew and learned more about many Indonesian NLP downstream tasks, such as emotion classification, sentiment analysis, aspect-based sentiment analysis, textual entailment, part-of-speech tagging, span extraction, and named entity recognition tasks. Most importantly, we learned alot about PyTorch and how easy it is to use it in our usecases and to implement the concepts that we've had in mind. Moreover, also learned to use the PyTorch Hugging Face library and the modelling functions they've built that is related to BERT and ALBERT. What's next for IndoNLU: Tutorial Finetuning IndoBERT using PyTorch We are open for collaborations and improvements. We planned to create NLP competitions and thus we prepared our leaderboard section in our indobenchmark.com homepage and also prepared the submission portal using CodaLab. Other than that, we are planning and opening ourselves to do series of seminars and promotions on NLP researches using Bahasa Indonesia, and also we are expecting to give more help and guidance and also collaborate with many (if not all) NLP Indonesian researcher out there, to help them to build and compare their NLP model performance with the baselines in the IndoNLU benchmark. What's next for us, is the advancement of NLP research especially in NLP task using Bahasa Indonesia. <div