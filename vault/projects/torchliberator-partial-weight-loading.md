---
slug: "torchliberator-partial-weight-loading"
url: "https://devpost.com/software/torchliberator-partial-weight-loading"
title: "TorchLiberator - Partial Weight Loading"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 594
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/scientific_research"
---

# TorchLiberator - Partial Weight Loading

> torch_liberator.load_partial_state automates model surgery. It finds the maximum correspondence between weights in two networks.

[Devpost](https://devpost.com/software/torchliberator-partial-weight-loading) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[scientific_research]]

**stack** cython, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for torchliberator - partial weight loading

## Body

Inspiration When working with pytorch I kept running into issues where I had a pretrained state for a nearly identical model (i.e. the on disk module was saved with/without DataParallel so it has a disparate "module." prefix, or I changed weights in the last layer, etc...) , but I had to manually munge keys in the state dictionary to get it to load. I wanted to find a solution that would load as much of the weights from one model into another as possible. I was thinking about this problem and it dawned on me: Subgraph Isomorphism! I then spent a few weekends / nights researching these graph theory problems and building efficient Python / Cython implementations. What it does Given two model state dicts, torch_liberator.load_partial_state transforms the keys in each state dictionary into a set of "paths", which are then converted into ordered trees. A maximum common subgraph matching algorithm (either the isomorphism variant where the subgraph has to be a "contiguous" subgraph or the "embedding" algorithm - which really should be called subminor or something more distinguishing - where edges within the subtrees are allowed to be collapsed in order to achieve a matching) is applied to find the common structure between the two state dictionaries. Given this matching, the keys in a subset of the second state dictionary are modified to match those in the first. Finally, we copy over the weights from the second state dict into the target model. In the case where the weight Tensor isn't the exact same shape, we copy over as much of the tensor that will fit (e.g. weights for a final linear layer for a 100-class problem might be a 512x100 tensor, and if loading a linear layer 512x1000 tensor from ImageNet, we bring over the classifiers for the first 100 classes only). The load_partial_state function contains parameters to enable/disable this last behavior if desired. How we built it I implemented an algorithm from Lozano, Antoni, and Gabriel Valiente. "On the maximum common embedded subtree problem for ordered trees." String Algorithmics (2004): 155-170. and then applied it to the partial weight loading problem. All slides from the presentation can be found here: https://docs.google.com/presentation/d/1w9XHkPjtLRj29dw50WP0rSHRRlEfhksP_Sf8XldTSYE Challenges we ran into It was initially unclear how to modify the Lozano algorithm to add constraints on the matching procedure, but eventually I figured something out that I'm fairly confident works (although I have not formally proven that it works). Accomplishments that we're proud of This work has led to 3 PRs accepted into networkx: https://github.com/networkx/networkx/pull/4294 https://github.com/networkx/networkx/pull/4326 https://github.com/networkx/networkx/pull/4349 And the core algorithm is awaiting review in another PR: https://github.com/networkx/networkx/pull/4327 What we learned A whole bunch about graph theory and dynamic programming. I nevery fully groked how to turn any recursive algorithm into an iterative one (with a stack) until I implemented these algorithms in Cython. I learned the difference between maximum common ordered subgraph minors (which the Lozano paper calls embedded subtrees) and, maximum common isomorphic subgraphs, and maximum common homeomorphic subgraphs. What's next for TorchLiberator - Partial Weight Loading There are two newer algorithms from Droschinsky, Andre, Nils M. Kriege, and Petra Mutzel. "Faster algorithms for the maximum common subtree isomorphism problem." arXiv preprint arXiv:1602.07210 (2016) . and Droschinsky, Andre, Nils M. Kriege, and Petra Mutzel. "Largest Weight Common Subtree Embeddings with Distance Penalties." arXiv preprint arXiv:1805.00821 (2018). that implement unordered isomorphic and homeomorphic variants of the maximum common subtree matching problem with a theoretical running time that is faster than the current algorithm I have implemented. I would like to add these as additional association algorithms. <div