---
slug: "early-alzheimer-s-detection-from-handwritten-drawings"
url: "https://devpost.com/software/early-alzheimer-s-detection-from-handwritten-drawings"
title: "Alzheimer’s Detection from Handwritten Drawings"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 380
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/elder_child_care"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Alzheimer’s Detection from Handwritten Drawings

> Early Alzheimer’s detection from handwritten drawings using attention-based multimodal deep learning.

[Devpost](https://devpost.com/software/early-alzheimer-s-detection-from-handwritten-drawings) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[elder_child_care]]
**substrate** [[structured_db]] [[video_visual]]

**stack** googlecolab, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned

## Body

Inspiration While thinking about real world AI projects that are both accessible and practically deployable, the idea of detecting alzheimer disease from handwritten drawings came to mind. Hand drawn tasks are simple, low cost, and easy to apply in real life screening scenarios. While searching for a suitable dataset for this task, I learned that the DARWIN dataset is suitable for handwriting based alzheimer detection. I looked for ways to access the DARWIN dataset, I found a Kaggle dataset ( https://www.kaggle.com/datasets/tizianadalessandro/darwin-i ) with relatively low interaction that shared a subset of the DARWIN dataset. The dataset was uploaded by Francesco Fontanella, one of the authors of the original DARWIN dataset paper, which increased confidence in the data source. Based on this, I decided to build a project focused on detecting alzheimer risk from handwritten drawings using this dataset. What it does This project detects early signs of alzheimer disease by analyzing handwritten drawings using a multimodal deep learning approach. It specifically focuses on the circle drawing task from the DARWIN dataset. The model combines visual features from the drawings with demographic information such as age and education level to predict alzheimer risk, aiming to provide an effective and accessible screening tool for early detection. How we built it I built a multimodal deep learning pipeline using the DARWIN dataset’s circle drawing task. The drawing images were carefully preprocessed and augmented. During data inspection, i identified and removed a small number of images that were inconsistent with the rest of the dataset and negatively affected model performance. The visual data was processed using an EfficientNet-based convolutional neural network enhanced with an attention mechanism to capture relevant drawing patterns and increase interpretability. Demographic features such as age and years of education were encoded through a separate network and fused with the visual embeddings. Accomplishments that we're proud of I built a multimodal deep learning model for early Alzheimer’s detection from handwritten drawings and improved performance through careful preprocessing, model selection, model architecture finetuning,and data curation. What we learned I learned how critical careful model tuning and well-designed data preprocessing and augmentation strategies are when working with limited medical datasets. Through experimentation, i gained experience with attention mechanisms and saw how multimodal feature fusion and architectural choices can significantly impact model performance. <div