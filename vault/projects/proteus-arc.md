---
slug: "proteus-arc"
url: "https://devpost.com/software/proteus-arc"
title: "Proteus Arc (Student Category/Lower Division)"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 339
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Proteus Arc (Student Category/Lower Division)

> Multimodal Superintelligence for Early Alzheimer’s Diagnosis, 97.3%>(MRI) and 88-95%>(EEG) accuracies for the respective segments.

[Devpost](https://devpost.com/software/proteus-arc) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**domain** [[education]] [[elder_child_care]] [[health_clinical]]
**user** [[educator_student]]
  <sub>weak: patient_family</sub>
**substrate** [[video_visual]]
  <sub>weak: document_pdf, structured_db</sub>

**stack** adamw, amp, argmax, array, autocast, complete-graph, compose, concatenate, counter, crossentropyloss, cuda, dataloader, dataset, draw

## Body

Kaggle link: https://www.kaggle.com/code/harneethguttikonda/multi-modal-diagnosis-for-alzheimer-s-mri-eeg Document link: https://drive.google.com/file/d/1XAWSxB9Tuzph38ClqbYbQES3add2UPEG/view?usp=sharing NOTE WE ARE IN THE STUDENT CATEGORY Inspiration Many MRI-based early Alzheimer’s detection models do not fully leverage modern deep learning architectures, leading to inconsistent accuracy, while EEG-based models often suffer from low interpretability and high data requirements. This motivated us to design a multimodal system that combines accurate MRI analysis with robust and explainable EEG-based reasoning. What it does Proteus Arc uses a deep learning MRI model to classify Alzheimer’s severity from brain scans and a randomized attention-based EEG model to extract stable electrode connectivity patterns. Together, these modalities classify patients into four stages: Healthy, Mild, Moderate, and Severe. This creates our multimodal architecture. You can check out the reproducable notebook through the first tryout link on kaggle How we built it For MRI, we used a ResNet-152 architecture with standardized preprocessing to perform high-accuracy image classification, training it on 31000 images. For EEG, we applied stochastic Graph Attention sampling to fully connected electrode graphs and trained a supervised ML classifier on stable connectivity signatures. Challenges we ran into Ensuring reliable MRI inference while managing large image data was a key challenge, alongside balancing randomness and stability in EEG attention sampling. Preventing overfitting with limited EEG data also required careful design choices. Accomplishments that we’re proud of The MRI model achieved approximately 97.3% accuracy with fast inference, while the EEG model outperformed most EEG-only approaches with strong interpretability and data efficiency, along with an accuracy of around 88-95%. Together, the multimodal system delivers more reliable predictions than either modality alone. What we learned We learned that deep residual networks are highly effective for MRI-based diagnosis and that controlled randomization improves robustness in EEG analysis. Combining complementary modalities significantly strengthens overall diagnostic confidence. What’s next for Proteus Arc We plan to expand validation across larger datasets and refine multimodal fusion strategies to further improve early-stage differentiation. Future work will focus on tighter integration between MRI and EEG predictions. Additionally, we intend to publish, and go into the clinical field with our architecture. <div