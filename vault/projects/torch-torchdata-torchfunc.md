---
slug: "torch-torchdata-torchfunc"
url: "https://devpost.com/software/torch-torchdata-torchfunc"
title: "torch* (torchdata & torchfunc)"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 799
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# torch* (torchdata & torchfunc)

> 1. torchdata - Implement (and extend) tensorflow.data.Dataset with PyTorch's torch.utils.data.Dataset. 2.torchfunc - improve performance, analyse, plot and make daily life of DL dev easier.

[Devpost](https://devpost.com/software/torch-torchdata-torchfunc) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** css, docker, docker-compose, github, github-action, markdown, matplotlib, photoshop, pytest, python, python-package-index, pytorch, rest

## How they structured the write-up

- torchdata
- torchfunc
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for torch*

## Body

GitHub repo header DockerHub GPU & CPU images (nightly and release) Pytorch style documentation Pip distributions (nightly and release) torch* - all around PyTorch torch* (torchstar, * as in regex) is a WIP ecosystem currently consisting of torchdata and torchfunc . First one is focused on data processing and input pipeline in general, while the second revolves around common tasks one performs in deep learning. Those two are and will be basis to other torch projects I have in mind or are currently developed. Inspiration Minimalism of PyTorch's design and it's flexibility. Many people gave community a lot and I want to take part in open source initiative by providing those tools. Due to my daily deep learning tasks and heavy use of torch I have decided to get some ideas and implementations and make them usable for everyone. torchdata torchdata is PyTorch oriented library focused on data processing and input pipelines in general. It extends torch.utils.data.Dataset and equips it with functionalities known from tensorflow.data.Dataset like map or cache (with some additions unavailable in aforementioned) . All of that with minimal interference (single call to super().__init__() ) original PyTorch's datasets. You can read more at github or check project's documentation Installation Quickest way is to install the library via pip : pip install --user torchdata After that you are good to go and can test the example below. For more instructions, see README . Example Create image loading dataset, map each to Tensor and cache in memory after that: import torchdata import torchvision class Images(torchdata.Dataset): # Different inheritance def __init__(self, path: str): super().__init__() # This is the only change self.files = [file for file in pathlib.Path(path).glob("*")] def __getitem__(self, index): return Image.open(self.files[index]) def __len__(self): return len(self.files) dataset = Images("./data").map(torchvision.transforms.ToTensor()).cache() torchfunc torchfunc is library revolving around PyTorch with a goal to help you with: Improving and analysing performance of your neural network Daily neural network duties (model size, seeding, performance measurements etc.) Plotting and visualizing modules Record neuron activity and tailor it to your specific task or target Get information about your host operating system, CUDA devices and others You can read more at github or check project's documentation Installation Quickest way is to install the library via pip : pip install --user torchfunc After that you are good to go and can test the example below. For more instructions, see README . Example Seed globaly, Freeze weights, check inference time and model size import torch import torchfunc # Inb4 MNIST, you can use any module with those functions model = torch.nn.Linear(784, 10) frozen = torchfunc.module.freeze(model, bias=False) with torchfunc.Timer() as timer: frozen(torch.randn(32, 784) print(timer.checkpoint()) # Time since the beginning frozen(torch.randn(128, 784) print(timer.checkpoint()) # Since last checkpoint print(f"Overall time {timer}; Model size: {torchfunc.sizeof(frozen)}") How I built it On and off creating style. While gathering my deep learning implementations (e.g. from university) I found out those are generic enough to be one day shared with the community. Concept of multiple separate libraries focused on specific tasks seemed good enough so I got to work. Fast forward to today, with pytorch , github , some docker , CI, CD and other I managed to release alpha versions of projects I once dreamed to make. Challenges I ran into Getting the API "to feel right" (I hope I quite got it?) Getting cache functionality of torchdata.Dataset generic enough (handling partial caching, caching to disk and RAM) of those libraries (hopefuly I did quite fine) Reverse-engineering PyTorch's pytorch-sphinx-theme to use with my projects. It's still W.I.P., but functional as you can see by yourself Creating separate nightly and release builds and deployments with GitHub Actions that I've worked with for the first time I will definitely ran into the hardest ones as future maintainer Accomplishments that I'm proud of Releasing alpha versions of both libraries on time and managing to enter this hackathon. Solving challenges listed above (or solving them at least partially). What I learned How to make a sensible (gosh, I hope) presentation video and that it's quite hard to talk to the microphone. :) Oh, and patience, patience and keeping cold blood when deadline is coming. What's next for torch* Maintenance of current libraries Maintaining and fixing bugs of what's been released. You can read plans regarding torchdata in it's roadmap ( here is the roadmap for torchfunc ) Extending torch* ecosystem Developing other libraries (some are currently in development) with torch prefix. Currently on my mind and in production: torchinit - initialization pipelines for neural network models + initialization schemes like LSUV from the paper All You Need Is Good Init torchlayers - reusable small single-purpose layers/modules (instead of whole models which are coded to be run once and never reused) like Squeeze And Excitation or well-known ResNets . torchreg - name W.I.P. but focused on regularization wrappers around cost functions <div