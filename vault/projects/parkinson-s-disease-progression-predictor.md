---
slug: "parkinson-s-disease-progression-predictor"
url: "https://devpost.com/software/parkinson-s-disease-progression-predictor"
title: "Parkinson's Disease Progression Predictor"
hackathon: "Determined AI Model Training Hackathon"
organization: "Determined AI"
winner: true
words: 650
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/developer"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Parkinson's Disease Progression Predictor

> Predict a Parkinson's patient's UPDRS-3 score

[Devpost](https://devpost.com/software/parkinson-s-disease-progression-predictor) · hackathon [[Determined AI Model Training Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[developer]] [[patient_family]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[structured_db]]

**stack** determined-ai, keras, pandas, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for parkinson's disease progression predictor?

## Body

Best metrics Model on Determined Cloud Loss and validation loss plots Inspiration How often do you go for a walk? Or use a utensil to eat? Unfortunately, these everyday tasks happen to be a burden for many patients with Parkinson’s disease. Parkinson’s disease is a brain disorder that affects your nervous system. It causes patients to lose control of their muscles and nerves. While symptoms may start slowly, there’s no known cure for Parkinson’s disease, so the symptoms only worsen over time. Parkinson’s symptoms are measured using the Unified Parkinson’s Disease Rating Scale (UPDRS). Patients are scored across multiple categories based on the severity of their symptoms. In particular, UPDRS-3 measures a patient’s motor skills, with a higher score indicating more severe symptoms. However, a UPDRS score only measures the current status of a patient. How would the patient’s symptoms be projected to worsen over an extended period of time, for example, in one year? This was the question that we aimed to address. What it does By leveraging a neural network learning algorithm, our model uses a patient’s current protein levels along with the protein’s associated peptide data to predict their UPDRS-3 score a year from their first visit in order to determine how their condition might decline in the future. How we built it We used Determined AI’s Cloud service and Tensorflow Keras libraries to build our model. We also used Python libraries like scikit-learn and pandas to organize and visualize our data. To train our model, we used the AMP®-Parkinson's Disease Progression Prediction dataset from Kaggle. Challenges we ran into Determined AI unfortunately doesn’t support Windows machines, which happens to be what we both use. As a result, we both struggled with setting up Determined AI locally, before switching over to Determined Cloud, which was much easier to use. We also struggled with managing our project timeline. We found out about the hackathon in late March and had internship deadlines and final exams to worry about, so we were pressed for time and had to reprioritize our tasks to finish the project. In particular, our model’s validation loss suffered a lot – tuning our model’s hyperparameters to improve its performance turned out to be much more time-consuming than we anticipated. It was also challenging (but rewarding) to learn all these new tools and concepts in one project, between the Determined AI platform, TensorFlow Keras, and learning how to create a machine learning algorithm. Accomplishments that we're proud of This was our first time working on an ML-focused project, so we’re proud that we created a working model that integrates with Determined! We’re especially happy about our organizational skills while completing the project. We created a schedule for ourselves and frequently revisited and reprioritized tasks so that we could complete our project on time. What we learned Over the past three weeks, we dove into the complete life cycle of a machine learning project. We learned how to apply machine learning concepts including feature engineering, regularization, and optimizers to our own model. We also learned how to use ML tools such as Keras API and scikit-learn, as well as Determined AI to run training jobs and visualize our results. While figuring out how to engineer our model to perform better, we learned about different diagnostics and error analysis strategies and applied them to bring our loss function down. What's next for Parkinson's Disease Progression Predictor? We’d like to spend more time reducing our loss metric! Currently, our loss and validation loss values are very close to each other, which indicates that our model generalizes well. However, we’d like to bring both values down to improve our model. We’d also like to build a larger multiple regression neural network that can predict multiple UPDRS scores. This might allow us to identify broader trends in protein abundance that relate to Parkinson’s disease and provide further insights into its progression. <div