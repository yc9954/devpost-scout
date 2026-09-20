---
slug: "ecg-analyzer-btza69"
url: "https://devpost.com/software/ecg-analyzer-btza69"
title: "ECG Analyzer"
hackathon: "Alameda Hacks"
organization: "AlamedaHacks"
winner: true
words: 1090
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ECG Analyzer

> An explainable deep learning system that detects cardiac arrhythmias from Lead-II ECG signals and translates predictions into clear, actionable insights using AI.

[Devpost](https://devpost.com/software/ecg-analyzer-btza69) · hackathon [[Alameda Hacks]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** claude, cursor, gemini, python, pytorch, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the ecg classifier model

## Body

Grad-CAM Visualization SHAP Visualization Training and Validation Curves Confusion Matrix Inspiration Our project was inspired by a research paper that demonstrated the use of deep learning to detect multiple arrhythmias from Lead-II ECG signals, achieving near-perfect performance across seven classes. That work clearly showed the powerful potential of neural architectures to automatically extract clinically meaningful physiological patterns directly from raw ECG data; patterns that traditionally require years of expert training to recognize reliably. We saw a real, pressing problem: while high-performing ECG classification models exist in research settings, most remain black-box systems that offer little insight to clinicians, are difficult to trust in high-stakes medical environments, and are rarely designed with practical deployment constraints in mind. This creates a significant gap between academic state-of-the-art and real-world clinical utility especially in resource-limited settings where explainable, fast, and interpretable ECG analysis could make the biggest difference. Motivated by this gap, our team set out to build a system that not only classifies major ECG diagnostic classes (NORM, MI, STTC, CD, HYP) with solid performance, but does so within the tight constraints of a hackathon timeframe while placing strong emphasis on interpretability, human-readable explanations, and practical deployment considerations. As this was our first deep dive into ECG signal processing, we deliberately chose to prioritize understanding the model's decision-making process using Grad-CAM and SHAP to produce visual explanations that show clinicians which parts of the recurrence plot (and thus which temporal patterns in the original signal) the model is attending to when it makes a prediction. We believe this combination of good classification performance + strong explainability addresses a meaningful real-world need: helping overburdened healthcare professionals gain faster, more trustworthy second opinions on ECG readings, potentially accelerating diagnosis of life-threatening conditions (such as myocardial infarction or conduction disturbances), particularly in settings where expert cardiologists are scarce. By making the model's reasoning transparent and visually intuitive, we hope our work contributes even in a small way to building greater trust in AI-assisted ECG interpretation and moves the needle toward more practical, clinically actionable deep learning tools in everyday cardiology. What it does Our project is a Lead-II ECG Cascaded Dense Neural Network capable of predicting five different types of cardiac arrhythmias from ECG signals. The model takes raw ECG input, processes it through a series of mathematical and neural transformations, and outputs a predicted arrhythmia class. After inference, the prediction is passed to Gemini, which analyzes the result and generates a natural-language explanation describing what abnormality was detected, what it means clinically, and what actions or next steps may be appropriate. The entire workflow is deployed through a Streamlit interface, allowing users to upload or process ECG signals and receive both model predictions and explanatory feedback in real time. How we built it We built the system using Python as our primary language and PyTorch as our main machine learning framework, relying heavily on the torch.nn and torch.nn.functional modules. We utilized the The PTB-XL ECG [ https://physionet.org/content/ptb-xl/1.0.1/ ] dataset that contains 21837 records of clinical 12-lead ECGs from 18885 patients of 10 second length. The model pipeline begins by transforming one-dimensional ECG signals into two-dimensional representations using an RPM (Relative Positioning Matrix) transform. This transformation enables convolutional layers to better extract spatial and temporal relationships from the ECG signal. The transformed data is then passed through a cascaded dense neural network optimized for feature extraction and classification. To improve interpretability, we integrated Gradient Class Activation Mapping (Grad-CAM), which captures activations and gradients to show how strongly different regions of the signal influence class predictions. We also incorporated SHAP (Shapley values), a game-theory-based approach that treats each feature as a contributor to the final prediction and quantifies its average impact. Together, Grad-CAM and SHAP allow for post-training analysis and insight into the model’s decision-making process. Since this was our first time working with ECG data, we used Claude and Cursor extensively throughout development to validate outputs, sanity-check assumptions, and receive guidance on appropriate modeling strategies, signal-processing techniques, and architectural decisions. These tools were especially valuable for refactoring code, improving pipeline structure, and confirming that our approach aligned with established ECG analysis practices Challenges we ran into One of the biggest challenges we faced was achieving strong generalization. While training accuracy improved over time, the model averaged around 60 percent accuracy and showed signs of overfitting, where it began memorizing training data rather than learning transferable patterns. This issue became particularly evident during validation. Another major challenge was dataset imbalance, as approximately 59 percent of the data belonged to a single class, introducing bias and limiting real-world applicability. We also encountered difficulties with input sizing for Grad-CAM, requiring careful handling of sensor dimensions and intermediate feature maps. These challenges reinforced how sensitive deep learning models are to data quality, balance, and preprocessing, especially in biomedical contexts. Accomplishments that we're proud of Our greatest accomplishment as a team was successfully designing, training, and deploying a research-grade ECG classification model within a very limited timeframe. We built a complex pipeline capable of processing gigabytes of ECG data and making inferences across thousands of signal files. Integrating explainability methods such as Grad-CAM and SHAP, alongside real-time deployment and natural-language interpretation through Gemini, allowed us to move beyond a black-box classifier and toward a system that prioritizes transparency and usability. Achieving this level of complexity and integration during a hackathon was a significant milestone for our team. What we learned The most important lesson we took away from this project is the critical role of data selection, balance, and monitoring throughout training. Subtle changes in how data is processed or distributed can drastically affect how a model learns and generalizes. We also learned the importance of tracking how information evolves through each layer of a network, as these transformations reveal whether features are being meaningfully captured or distorted. Lastly, working with ECG data emphasized the value of interpretability, especially in healthcare-related applications where understanding a model’s reasoning is just as important as its accuracy. What's next for the ECG classifier model The next step for this project is to perform a detailed post-mortem on the model to identify exactly where and why it failed to generalize effectively. We plan to dissect the architecture, training process, data pipeline and use detailed datasets to uncover opportunities for improvement. Beyond refinement, we also intend to explore how this cascaded architecture and RPM-based transformation approach could be applied efficiently to other domains and industries where structured time-series data plays a critical role. Track 5. Healthcare & BioTech Track 2. Artificial Intelligence & Machine Learning <div