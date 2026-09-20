---
slug: "semantic-segmentation-with-horvod-raytune-and-transformers"
url: "https://devpost.com/software/semantic-segmentation-with-horvod-raytune-and-transformers"
title: "Semantic Segmentation with Horvod, RayTune and Transformers"
hackathon: "AWS Deep Learning Challenge"
organization: "Amazon"
winner: true
words: 262
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# Semantic Segmentation with Horvod, RayTune and Transformers

> We build and train a transformer based semantic segmentation model for DL1. We adapt RayTune for use on HPU and run distributed training with Horvod.

[Devpost](https://devpost.com/software/semantic-segmentation-with-horvod-raytune-and-transformers) · hackathon [[AWS Deep Learning Challenge]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[video_visual]]

**stack** horvod, python, raytune, tensorflow

## How they structured the write-up

- potential value and creativity
- project goals

## Body

Potential Value and Creativity Demonstration how to use RayTune for Gaudi for parallel hyper-parameter optimization Demonstration of Horovod on Gaudi Implementation of Vision Transforms based semantic segmentation on Gaudi Demonstration of Gaudi cost benefits Demonstration of usage of Habana model reference building blocks Project Goals Implement a semantic segmentation model in TensorFlow for DL1 which is powered by Gaudi (HPU) accelerators. Use the vision transformer block as a backbone. Attention based transformers originated in the world of NLP, in the paper: Attention is All You Need . The use of tranformers for vision tasks was introduced in the paper An Image is Worth 16x16 Words: Transformes For Image Recognition at Scale . Transformer models are large networks that can be difficult to train. To address this it is common to employ methods of transfer learning to accelerate convergence. For example, you can take weights that were trained for object classification and reuse them as pretrained weights in a semantic segmentation model. Here I use weights from a transfomer based imagenet classificaton model . Demonstrate the steps for building/porting a model for Gaudi. Demonstrate parallelized hyperparameter tuning on Gaudi processors using RayTune. RayTune is a popular framework for hyperparameter tuning. While it does not officially support HPU accelerators, it can be adapted to run on Gaudi as I demonstrate. By using parallel hyperparameter tuning one can discover the best combination of parameters for training. Demonstrate distributed training on Gaudi processors using the Habana Horovod framework. Compare price performance of training Segmentor model on dl1 (Habana Gaudi) instance compared to p4 (NVidia A100) <div