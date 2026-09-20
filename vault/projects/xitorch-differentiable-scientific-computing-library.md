---
slug: "xitorch-differentiable-scientific-computing-library"
url: "https://devpost.com/software/xitorch-differentiable-scientific-computing-library"
title: "xitorch: differentiable scientific computing library"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 567
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# xitorch: differentiable scientific computing library

> Just like scipy but differentiable! xitorch provides functional routines (e.g. rootfinder, optimization, ODE solver) with first and higher order gradients

[Devpost](https://devpost.com/software/xitorch-differentiable-scientific-computing-library) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[video_visual]]

**stack** python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for xitorch: differentiable scientific computing library

## Body

GIF A simple differentiable molecular dynamics written with xitorch GIF Neural mirror design with a simple ray-tracing calculation written with xitorch Inspiration It was started with an ambitious project of writing the first differentiable quantum chemistry simulation. Writing a scientific simulation from scratch is already a daunting task, let alone make it differentiable. Although libraries such as Tensorflow, PyTorch, and JAX provide automatic differentiation, their use in writing differentiable scientific simulations is much rarer than their applications in neural networks. One of the biggest challenge is the lack of functional (i.e. function that takes other functions as inputs) routines that can give first and higher order gradients, such as optimization, rootfinder, and ODE solver. In the non-differentiable Python world, scipy is a great library to do this. However, in the differentiable Python world, there was no library like scipy that can do the work. This is what motivates me to start writing xitorch: differentiable scientific simulation library . What it does It provides first and higher order gradients of functional routines, such as optimization, rootfinder, and ODE solver. It also contains operations for implicit linear operator (e.g. large matrix that is expressed only by its matrix-vector multiplication) such as symmetric eigen-decomposition, linear solve, and singular value decomposition. Although some people have implemented differentiable functional routines, such as deep equilibrium network , they typically provide only first order gradient and not capable of providing higher order gradients. The capability of xitorch in providing higher order gradients is what makes it really useful in writing differentiable scientific calculations or simulations. How we built it xitorch is built mostly using python with numerical stability and speed as the top priorities. It is hosted in github ( https://github.com/xitorch/xitorch/ ) with github actions to keep the code quality high. As xitorch requires programming and math, writing it could improve your programming skill and sharpen your math skill. Challenges we ran into Implementing higher order gradients for the functionals were very difficult. It took us a few weeks to get the trick in getting the correct higher order gradients. Other than that, some gradient calculations were also tricky mathematically. For example, gradient calculation for symmetric eigendecomposition with degenerate (i.e. duplicate) eigenvalues can provide numerical instability. We have provided the solution in xitorch to avoid the numerical instability in those gradient calculations. Accomplishments that we're proud of xitorch has enabled us to write the first differentiable quantum chemistry simulation: DQC which was published in Physical Review Letters here . Thanks to xitorch and DQC, I was invited to several seminars (e.g. SciML by CMU-MIT, ALP seminar by University of Oxford, and MLDG seminar by University of Cambridge) about differentiable simulations and quantum chemistry. Besides DQC, with xitorch you can easily write a very simple differentiable ray-tracing and differentiable molecular dynamics (see the images or our github page for demo). What we learned During the writing of xitorch, we have found several problems with PyTorch at that time and the solutions. Some of the examples are wrong grad of torch.symeig for degenerate eigenvalues , numerical instability in gradient calculation of a simple division operation , and memory leak . So, by contributing to xitorch, you might be able to contribute to PyTorch as well! What's next for xitorch: differentiable scientific computing library The next step for xitorch is to implement more algorithms to provide users more options. The to-do list can be found here <div