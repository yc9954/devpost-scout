---
slug: "pystiche"
url: "https://devpost.com/software/pystiche"
title: "pystiche"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 1234
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# pystiche

> The pystiche project is a free, open-source framework for Neural Style Transfer (NST) algorithms. Roughly speaking, pystiche relates to NST algorithms as PyTorch relates to deep learning.

[Devpost](https://devpost.com/software/pystiche) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[scientific_research]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[video_visual]]

**stack** ajax, django, javascript, jquery, matplotlib, numpy, python, pytorch, requests, torch, torchvision

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pystiche

## Body

pystiche frontend after selecting a content and style image pystiche frontend during the NST pystiche frontend displaying the result image after the NST Inspiration I (Philip Meier, main author) started my research in the field of Neural Style Transfer (NST) in July 2018. Having little prior experience with deep learning, I thought was in for a steep learning curve. Fortunately, the first link after typing "neural style transfer tutorial" into DuckDuckGo directed me to the official PyTorch tutorial for NST . Having worked with Caffe and TensorFlow before, I instantly fell in love with PyTorch, because I understood the implementation in mere minutes without having ever heard of PyTorch before. Writing my first paper in the field of NST earlier this year, I painfully learned that it is hard to benchmark your own results, if everyone uses different deep learning frameworks, implementation strategies and so on. I realized, while there are frameworks for deep learning, there is no such thing for the field of NST. Having never written a framework before, I decided to give it a try if "I have some time left over". Needless to say, there was never time left over. Fast forward to August when I read the announcement of the PyTorch Global Hackathon 2019. It was the perfect opportunity for me. Especially the price of being featured by PyTorch sold it to me, since a framework is no use for anyone, if no one knows it is there. As pun on the word pastiche I started to develop pystiche . What it does As explained above, pystiche is a framework for NST algorithms. Roughly speaking, it relates to NST as PyTorch relates to deep learning. After an initial shock how many different variants are out there, I learned that at the core the methods overlap greatly. Many building blocks can be reused. Basically, most papers varied a single component, which sometimes lead to drastically different results. I realized that having a flexible Operator most of the surroundings are static. Thus, the goal was to design a framework, that allows other researchers to rapidly prototype their inventions without sacrificing the quality. Since in science the comparison between multiple methods is vital part of the development process, I implemented the approaches of three major papers within pystiche . Furthermore, I gathered download links for commonly used images, saving other researchers the time to download them on their own. With these two parts, a replication study of these papers is easily accomplishable. Since the results of NST are visually appealing, the techniques might also be interesting for recreational use. Some web servies already offer simple NST functionality, but the results are often watermarked or not freee obtainable. Furthermore, the use has little to no control over the actual algorithm, leading to a lot of wasted potential. Thus, I wanted an easy to use frontend for the pystiche project, that enables interested user to create art without explicitely knowing how the algorithms or work and how they are implemented. How I built it I structured the pystiche backend in three steps, which are aligned with the tasks one has to perform in an NST: Encoder NST algorithms heavily rely on CNNs or more precisely the feature maps they generate. A standard way to implement this, is to include transparent layers into the CNN, which pass the input right through, but save some information about it within the nn.Module . This information, usually torch.Tensor s, is later extracted and further processed. I got rid of this practice by designing the Encoder class, which subclasses an nn.Sequential , but gives the option to extract one or more feature maps within a single pass. Operator As stated before the used Operator s are the center pieces of every NST algorithm. I designed it so that a researcher who wants to write their own has to answer some very basic questions: Should the operator compare the input image to a target image or does it work as a regularizer? Should the operator work on feature maps or directly in the pixel space? Should the operator work on the whole image or just on some region of it? According to the answers, you can simply pick an abstract Operator form the selection an implement only the actual logic need for the approach. This allows the user to focus on the important things, just like you only implement the forward() method of an nn.Module without worrying about about the rest. NST The actual NST is performed by an ImageOptimizer and basically implements the "training loop". Given an input image, it - generates the necessary feature maps with the help of the encoders, - calculates the scores of every operator, and - updates the image accordingly for every iteration step. In the current state the frontend is based on django , JavaScript , and Ajax . It features two dropzones, which enable the user to pick or drop two images to use. With a click of a button the frontend spins up the pystiche backend, which performs a basic NST. Subsequently, the result is displayed. Challenges I ran into Having never worked in web development before, I recruited Christopher Koch to help me with the frontend. Together we got it working, but the result lacks behind what I had envisioned to accomplish within this hackathon. Accomplishments that I'm proud of Having said that, I'm very proud that we got frontend working at all without any prior knowledge. Furthermore, I'm very proud that the design I finally chose after many revisions, should cover most of the papers within the field, thus making pystiche general enough for other researchers. Finally, I'm most proud of myself that I put in the hours to bring pystiche to life after never "having time left over" to implement it. What I learned I learned late but not too late to not try something like this on your own. I partially was so focussed on implementing "this one feature" that I lost the big picture. Having no formal CS background, I learned that for me it is very important to talk to someone else about your design choices before you blindly implement them. Thus, I'm very grateful to Christopher Koch providing me with that "sparring partner". By asking him for help earlier, I could have saved some sleepless nights. What's next for pystiche My great wish for the future is that other researchers adopt pystiche for their own research making it the first and commonly used framework for NST. Even if this does not happen and regardless of the outcome of this hackathon, I plan to continue developing the project. I will start my PhD within the field of NST soon and even if other researchers don't, I want my results easily reproducible. Furthermore I will try to submit it to pyOpenSci and if that works maybe write a paper about it in JOSS . Some features I plan on adding in the (near) feature: Fast Neural Style Transfer. This should not be a large step, since the only difference to the classical NST algorithms is that instead of optimizing an image you train an generator to do it with a forward pass. Implementing more functionality of the backend within the frontend. If successful, this could also be a good starting point for new researchers to get an intuition about NST before diving into the backend. <div