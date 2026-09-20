---
slug: "learn2learn-s2dhyb"
url: "https://devpost.com/software/learn2learn-s2dhyb"
title: "learn2learn"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 624
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/structured_db"
---

# learn2learn

> A PyTorch Meta-Learning Framework for Researchers.

[Devpost](https://devpost.com/software/learn2learn-s2dhyb) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[legal_professional]] [[researcher]]
**substrate** [[structured_db]]

**stack** pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for learn2learn

## Body

The learn2learn logo. Example of Omniglot tasks. Test accuracy on Omniglot. GIF Example of meta-learning to control the Mujoco Half-Cheetah after a single parameter update.. Inspiration Meta-learning is not ready for production. The current algorithms suffer from instability and high computational costs and often require an arduous hyper parameter search. Our library is designed with these difficulties in mind. We offer the core functionality needed for those unfamiliar with meta-learning to easily implement it in their project, as well as tools for researchers to create new meta-learning algorithms (or modifications to existing ones) that seek to address these problems. What it does learn2learn is a PyTorch library through and through. learn2learn uses a modular approach and well engineered interface to provide a library that is powerful extension of torch at a high, mid and low level. High level functionality includes implementations of several meta-learning algorithms, as well as a TaskGenerator that allows users to easily create their own meta-learning datasets. How we built it We started working on learn2learn at the PyTorch MPK Hackathon. By the end of the hackathon, all members were enthusiastic to continue working on it, and so we did. Since we were all in different locations, we decided to meet about once a week via video chat, and stay in touch via slack. (Join us at: slack.learn2learn.net !) To build learn2learn, we started with barebone PyTorch, and wrote utilities we thought useful for meta-learning. One such example is the clone_module() function, which replicates the behaviour of Tensor.clone() for nn.Modules. With those low-level utilities, our development routine goes as follows: Replicate results from a given paper. When doing so, we particularly look for general functionalities useful to a wide range of applications/algorithms. Merge those general functionalities in the core library. clone_module() is a good example of such general functionality. Another one is the magic_box function from the DiCE paper (Foerster et al, 2018). We’re planning to continue the development of learn2learn past the Global hackathon. In fact, we’re already using it in our day-to-day research! Challenges we ran into Replicating papers is always tricky; authors don’t always open-source their code, and they tend to use tricks to obtain state-of-the-art results. Those tricks rarely make it into the final paper. This made it particularly difficult to replicate some results. Even when we managed to replicate the results, it was difficult to judge what aspect of the algorithms should be considered “general functionality” to be merged in the core library, and what shouldn’t. A good example is the ProtoNets paper, whose implementation is very simple: once replicated, we really couldn’t bring back anything into learn2learn. As always with libraries, it is difficult to foresee what the users will need, and what the right API should be. It took us a few iterations (e.g. on the TaskGenerator) but we’ve slowly converged on an interface that works well for most (all?) use cases. Accomplishments that we're proud of General API design that works with any PyTorch module, dataset, or library. (including torchvision, torchtext, torchaudio!) Support for supervised and reinforcement learning algorithms. Replicating the results of half-a-dozen papers, and support for about 10 meta-learning algorithms. Well documented and tested code base. The start of a nice community. (200+ stars on GitHub, 3 days after posting on Reddit.) What we learned Meta-learning is extremely fragile in the reinforcement learning setting. Current successes heavily rely on reward shaping, and some results are not replicable at all. (We emailed the authors!) Meta-learning does not work for text -- yet! Despite our efforts, we could not outperform simple pre-training baselines on the News-Journals dataset. (which we introduce with learn2learn) What's next for learn2learn Support more meta-learning algorithms. (e.g. meta-features) Provide more datasets. (e.g. meta-dataset, cifar-fs, tiered ImageNet) Better testing. <div