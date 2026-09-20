---
slug: "pytree"
url: "https://devpost.com/software/pytree"
title: "PyTree"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 487
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/structured_db"
---

# PyTree

> PyTree, a PyTorch package for recursive neural networks.

[Devpost](https://devpost.com/software/pytree) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pytree

## Body

Inspiration Natural language processing is an extremely prolific research field. The rise of deep learning witnessed the apparition of distinct architectures. The efficiency of such architecture is crucial. Slow or under-optimized implementations might constraint the parameter size or the research of hyperparameters. Therefore, the popularity of architectures is, to some extend, bounded by the efficiency of their implementation. For example, transformers mainly depend on attention and matrix multiplication which can be performed extremely fast on GPUs or TPUs. Nonetheless, other less efficient architectures might be worth exploring. The latter might be more intelligible or exhibit some specific properties. Tree-structured networks are of special interest for NLP applications. Language is indeed often associated with a recursive structure. PyTorch is really convenient to implement recursive neural networks. Indeed, the computation graph is dynamically computed for each input. As trees might present distinct structures and shapes, this makes it easy to adapt to a variety of inputs. However, it is more difficult to compute a whole batch of distinct trees at one. What it does For the hackathon, we implemented tree-structured neural networks in PyTorch. The package, called PyTree, provides highly generic recursive neural networks implementations as well as efficient batching methods. Recursive neural networks are notoriously hard to implement and deploy and although many custom implementations exist, they lack unity. The goal of our implementation is to be as most straightforward as possible: simplify the format of the inputs and outputs and align them with other popular architectures, such as Transformers or LSTM. How we built it The package is built in pure PyTorch and is designed to work with the entire PyTorch stack. Dataset, Dataloader, Datacollator, or nn.Module . As a result, it is compatible with every PyTorch-friendly project. For example, our demonstration uses a Trainer module from another Open Source library. Challenges we ran into We aimed at implementing multiple models with each specific characteristics and architecture specificities. We had to redefine our intermediate variables or functions multiple times in order iteratively to improve the implementation power of generalization. Accomplishments that we're proud of We were proud to be able to reproduce some paper results, which validated our implementation. What we learned We learned a lot about PyTorch build-in functions and develop our intuition about dimensions in Tensors. Eventually, we also had to deep dive into our implementation to fix some bugs. From our point of view, debugging is one of the main strengths of PyTorch. You just have to use the standard Python debugger in the IDE of your choice and you can execute your code step by step to control every line of code. This feature makes it really convenient to debug. What's next for PyTree We like to keep improving the library. In particular, we expect to add other recursive models such as other encoders or decoders. We also aim to extend the number of tutorials and examples, for NLP or other fields. <div