---
slug: "3-layer-quantum-data-classification"
url: "https://devpost.com/software/3-layer-quantum-data-classification"
title: "3-Layer Quantum Data Classification"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 353
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/document_pdf"
---

# 3-Layer Quantum Data Classification

> An ML data classification model that integrates a complex quantum circuit as a neuron layer. Built for the CANSOFCOM quantum classification challenge.

[Devpost](https://devpost.com/software/3-layer-quantum-data-classification) · hackathon [[Hack the North 2022]]

## Facets

  <sub>weak: legal_professional</sub>
**substrate** [[document_pdf]]
  <sub>weak: financial_record</sub>

**stack** jupyter, numpy, pennylane, python, tensorflow

## How they structured the write-up

- important for cansofcom judges
- challenge statement
- the hybrid model
- the quantum circuit
- the results
- challenges and learning!

## Body

Important For CANSOFCOM judges Since the challenge document was made for an old hackathon with an online submission portal, we took some liberties in changing how we showed off our model. It is built on a Jupyter Notebook, with the input string read from a input.txt file. We made Y_test vectors for quick testing, but the string outputs are printed at the end of the program in console. Please let us know if this is appropriate for model evaluation! :) Challenge Statement Given a set of data points sorted into and labeled with three different classes, design a variational quantum classifier that can classify test data from the same distribution with an accuracy of > 95%. The Hybrid Model Layer 1 -> Classical 3 Neuron Layer with ReLU activations Layer 2 -> 3 Qubit Quantum Circuit, packaged into a QuNode object which can be used as a layer Layer 3 -> Classical 3 Neuron Layer with Softmax activations, for multi-class classification The Quantum Circuit Built with 3 Qubits or Quantum Bits, which use superposition (0 and 1 at the same time!) properties to perform multi state calculations, then record measurements. Features are first encoded into each Qubit given size of input, then sublayers are added with tuneable parameters. These sublayers apply “rotations” to Qubits, using parameters for tuning values. Finally, the final sublayer output is measured using a PauliZ matrix. The entire QuNode object is packaged into a Keras layer. Thanks to PennyLane, we can integrate the layer with our model pretty easily, and it works with various Tensorflow optimization and loss functions! The Results The model will always train towards 100% test accuracy on two epochs of training! Try it yourself using the notebook in the Github link below. Challenges and Learning! We didn't know anything about quantum computing and had limited knowledge of machine learning going into this weekend. It was a blast to learn about the cool applications of Quantum Bits in models! We had issues with long computation times with our quantum circuit, and had to go through some iterations and ideas before settling on a separate circuit. <div