---
slug: "indiclp"
url: "https://devpost.com/software/indiclp"
title: "IndicLP"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 664
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# IndicLP

> Indic language processing library, is an effort to make it easy for developers and researchers to build fascinating applications and models in Indian Languages, thus making NLP a more diverse field.

[Devpost](https://devpost.com/software/indiclp) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]] [[legal_professional]] [[researcher]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]]

**stack** gensim, github, html5, hugo, python, python-package-index, pytorch

## How they structured the write-up

- getting started
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for indiclp

## Body

Getting Started NLP is now part of layman vocabulary and also is part of our daily life. With text autocompletes, automated email response etc. we are steadily moving towards a future that's more and more reliant on AI technologies. However, a noticeable amount of corpora and models in NLP are based on English and adjacent languages, making it inaccessible for people who do not speak these. This was the problem statement that we wanted to work on, bringing the world of AI to people who are not familiar with English. IndicLP is meant to achieve exactly this, enabling developers and researchers in AI and NLP to develop models that can help people who speak the native languages on India. What it does IndicLP is an NLP Library, focusing on Indian Languages (currently Hindi and Tamil). With various commonly used functionalities like Tokenizer, Word Embedder, Stemmer and Dataset Loading available at the finger tip of programmers, they can focus on developing their dream projects rather than working on the exhaustive preprocessing steps. Furthermore, through IndicLP we are intending to make it easier for developers to import wide range of open access datasets in Indic Languages and well known corpora like Ponniyin Selvan in Tamil. This is done through the Dataset class present in the IndicLP library. How we built it While building IndicLP library, one thing we were certain from the first was making it easily accessible to any developers. Publishing it as a pip package therefore was a no-brainer for us. Along with making it's installation intuitive to the developers, it also gives us the perfect platform to maintain releases and constantly keep updating it with more features and languages. While having a package is great, it's of no use when the users do not know how to use it. Therefore we have hosted a detailed documentation here , for users to refer to when they hit a roadblock in their NLP journey. Challenges we ran into Any development cycle has ups and downs and the journey for IndicLP was no different. While we had worked on NLP projects before, we never really got into the working of tokenizers, embedder etc. and used the functions provided for granted. IndicLP however was a different journey as we had to build the method we so familiar using. Identifying the right methods, like sentencepiece for tokenizers, word2vec models for embedding etc. took a lot of trail and error and exhaustive code sprints which sometimes were abandoned and reverted in days. Taking a path that has no obstacles is never the road to glory and certainly was the case in indicLP. Accomplishments that we're proud of Living in India and knowing people who eagerly work in NLP and related fields, it certainly is a proud moment when you push your code, knowing that each commit is a step closer to a better life for people who most need it. Moreover talking to friends regarding the same and discussing the possible projects that they can make on top of indicLP, certainly makes the effort worth it. Furthermore, there's no denying, when you finally are satisfied with the code written and push it to pypi and realizing that it's out there for people to use and make fascinating projects with, gives a special sense of accomplishment and pride. What's next for IndicLP IndicLP has a long way to go before becoming what it truly hopes to be, a one stop shop for everything to do with Indic NLP. While it is possible to do other languages robotically by following some step, it is necessary to have people in the team who understand the language to judge the result. We are hoping to add more functionalities to indicLP, making it more robust and usable in a wide variety of tasks, while also including more languages to make it represent the people it is truly meant for. Furthermore we also need to make the existing models more powerful and socially aware. <div