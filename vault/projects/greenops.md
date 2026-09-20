---
slug: "greenops"
url: "https://devpost.com/software/greenops"
title: "greenops"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 1576
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# greenops

> Greenops helps to measure the footprints of deep learning models at training, testing and evaluating to reduce energy consumption and carbon footprints.

[Devpost](https://devpost.com/software/greenops) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[researcher]] [[small_business]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** csv, json, php, python, pytorch, sql

## How they structured the write-up

- inspiration 💡
- what it does ❓
- how we built it 🔨
- challenges we ran into 💪
- accomplishments that we're proud of 😎
- what we learned 📘
- what's next for greenops ⏱
- how it works ⚙

## Body

Inspiration 💡 🍃 People think AI will kill us someday, but frankly, it is more likely that we will kill ourselves while developing that AI. The Earth faces different problems like global warming, melting ice caps, ozone depletion and pollution. The carbon footprint of a single big NLP model is more than 250,000 kg.* AI development consumes a lot of electricity, time and money and it has a great carbon footprint. ⏱ Pollution and global warming are really huge problems. As responsible developers, we have to try to reduce the environmental load of AI development. That’s why we created this project. We want to begin a new discussion between AI and ML developers and researchers about environmental protection. Creating more eco-friendly models leads us to a better and livable world. Reducing the running time of a single model by 0.5 second seems nothing. If there are 1,000,000 users worldwide, who use this model, we spare more than 138 computational hours. ⚡ We know there are other things around the world that pollute more, but everybody should do at least a little to save the Earth. Crypto currency miners use heavily loaded GPUs to find new hashes. Just like us, but we iterate and backpropagate our models. Different goals and motivation, with the same result; AI development consumes a lot of energy. This is the problem of today, but frankly, if we had had the chance to talk about it yesterday, it would have been too late. 🔧 Torchscript is a great tool to finetune models, but it is not used as widely as it should be. Our idea provides a tool that opens users’, developers’ and researchers’ eyes. Our vision is a new kind of AI development method where developers focus not just on nodes and layers, but energy consumption and CO2 footprints to create a healthier and better world. 🌎 source https://arxiv.org/pdf/1906.02243.pdf What it does ❓ 📐 Greenops measures the time of model development , in different phases such as training, testing or evaluating, and calculates the energy consumption and CO2 load based on the time and the used device. It provides real-time logging into a csv file to help with any further data visualization technique. So basically greenops is a software, but it is a new mindset at the same time. ✂ With greenops, developers and researchers can deeply understand the energy consumption of models and the train, test or evaluation phases. This proper tool helps to save time and money. How we built it 🔨 🧰 There were more phases of building greenops. First of all we had to look around how to figure out the carbon footprint of artificial intelligence models. It is clear that the time they are running has an important role in their consumption but there are other parameters as well. During the hackathon we succeeded in making a good conception about what we would like to achieve in the long term and we also made a working demo with three examples. We have way too many ideas on how to improve the performance of greenops. It is a question of coding and a question of the data as well. 🔎 There are some competitors out there who try to estimate carbon footprints. As people experienced in data science we know it is more important to have good data than dreaming about the perfect estimator. Therefore we decided to to make a strongly data collection oriented solution. We developed three different approaches to measure time: 1️⃣ The first one is very simple and safe. It can work with any kind of code since it doesn’t really use anything aside from the standard library ’s time function. 2️⃣ The next approach is a thread based solution . It is also very simple since threads get dropped permanently. It utilizes the thread-safe nature of Python’s simple (not only primitive) variables. 3️⃣ The third approach that we developed is a solution that fully integrates with PyTorch , since it registers hooks to the forward and the backward passes. At the moment it registers only one hook to a model but in the future we plan to develop a much more sophisticated solution. The model level approach is very powerful since it can work with any kind of Pytorch or Fast.AI models. ⛏ We think, the amount of the consumed time on its own is just a number. The stat_summary property of a measure (or the str output) contains not only the registered stages but the price and sources of the electricity we used to train, test or inference our models. The reason is that this way the user can see day by day what amount of the consumed electricity comes from sources that never renew. We have in mind great improvements to this feature too. 📑 As we mentioned above, good data is essential to estimate the carbon footprint, energy consumption of a model. Therefore we developed the instant log feature. It logs each data point as soon as possible. The content of data logging is highly customizable but the default is the widest logging possibility. 📊 We also developed a watch feature. The user can add different performance indicators of a model, like loss, weights, biases, etc. The only important thing is, that mutable object should be passed into the watch dictionary. Greenops saves watched objects with the basic data. In the near future we plan to make something similar to tensorboard, a tensorboard implementation or implementation with other libraries to provide instant data visualization. 💾 Since good data is essential, we save our data into CSV files, which can be easily processed with a lot of frameworks familiar to data scientists. 📍 Unfortunately we didn’t publish our project as a PyPi package until the submission deadline but we will do it in the next few days. We plan to publish this package on other Python related frameworks as well. Challenges we ran into 💪 ⏳ It was very hard to decide where to begin our job. The time is so short on a hackathon even when it lasts weeks like this one, since we work aside from this project. But we like what we did and what we achieved so we will sacrifice our time to continue with it since it is very important and our colleagues all over the world have to know how important a role we have in the fight against the global change of the climate even if don’t actually develop the best weather or global warming predictor. 🚀 Since PyTorch is a very current framework, a good integration and an easy-to-use manner is essential. Therefore we decided to develop as high-level code as we can. Since the user can do everything with 3-5 lines of code in a simple use-case, we are somewhat satisfied even if we know we have a lot of to-do in the future. Accomplishments that we're proud of 😎 🟩 we made a working solution from zero, since it is a new idea 🟩 we made 3 different working demo (example) files 🟩 we create an own API service with 3 different endpoints to provide data for calculations 🟩 we learned a lot about carbon footprints, however we considered ourselves green people we figured out we could do much more and much better What we learned 📘 🕵 We learned different things from coding to environmental protection. First of all, we understand how Torchscript works and what it adds as benefits to a model development. This was a cornerstone, since we had to see how developers can finetune their models. We are freelance deep learning developers. When we develop for different kinds of architectures, we use other methods to optimize the models.Since we want to create a code that a lot of users will use, we had to think like other developers. 📚 There is a lot of debate about pollution around the news. However, there cannot be built a hackathon solution on news, gossip and things we heard. It is a deeper topic than collecting waste selectively or turning off the water during brushing teeth. We searched scientific papers and articles in scientific magazines (like Nature and Science) to collect more background information about pollution and global warming. 🔌 Finally, we create our own API service with 3 different endpoints. It was a real challenge, because web service development needs another mindset that we have. What's next for greenops ⏱ 💻 There are two different kinds of future development. First is about the code. We want to add new features to make the code more robust, create a user interface (similar like tensorboard), or provide verifiable log history. Other features will be updated or written based on user feedback. 🧠 The second approach is far away from the keyboard, since we want to make a new discussion, debate or movement within the community of AI or ML developers and researchers about the environmental impacts of AI. There is a real need to form our vision about the future. How it works ⚙ 1️⃣ import import greenops as go 2️⃣ defining the greenops measure measure = go.Measure() 3️⃣ updating the stages measure.update() OR measure.start() and measure.stop() Both start(), stop() and update() can have an argument. It is the name of a stage. Stage can be measured concurrently so if a user runs tasks that have to be measured simultaneously, it is absolutely manageable. 4️⃣ printing the measurement print(measure) OR measure.stats_summary <div