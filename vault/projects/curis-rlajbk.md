---
slug: "curis-rlajbk"
url: "https://devpost.com/software/curis-rlajbk"
title: "Curis"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 606
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Curis

> Our project seeks to keep physicians informed about the best course of action for their patients. The project specifically focuses on Cancer patients and finds relevant medical trials for the patient.

[Devpost](https://devpost.com/software/curis-rlajbk) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]] [[medical_record]] [[structured_db]]

**stack** embeddings, fastapi, huggingface, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for curis

## Body

Curis Logo Inspiration Clinical trial matching identifies eligible patients to be considered for clinical trial enrollment, which is essential for clinical discovery and drug development. For diseases such as cancers where standard of care often fails, clinical trials are also a last hope and represent an important treatment option. The standard process for clinical trial matching, however, is extremely inefficient. Most information needed for accurate matching is scattered in vast amount of unstructured text, such as elaborate eligibility criteria of a clinical trial or patient information in longitudinal electronic medical records. For example, in the United States (U.S.) alone, there are two million new cancer patients every year and, at any given moment, there may be hundreds of active oncology trials (Siegel and Jemal, 2022; U.S. National Library of Medicine, 2023). Manually evaluating all oncology trial-patient candidates is infeasible. Consequently, less than 3% of patients were able to participate in a trial (Unger et al., 2019), whereas 38% of trial failures stemmed from insufficient recruitment (Stensland et al., 2014). What it does Our project seeks to give Oncologists a tool to locate and enroll their patients in life-saving trials. Curis starts with a DNA sample from the patient and classifies their Cancer with a 99.6% accuracy. It does this using a variational auto-encoder (VAE) based on Cancernet, which is a cutting-edge technique for Cancer diagnosis. It then gives the result to the oncologist to aid them with Diagnosis. Once the Oncologist has diagnosed the patient, the model uses the patient's information to search through a dataset of all FDA-approved clinical trials and finds the trials that are the best match for the patient. This allows Oncologists to easily locate trials that have a higher likelihood of working for their patient and prevents them from having to dig through Medical Journals, Articles, and Research Papers. How we built it Curis contains 3 separate AI models for aiding Oncologists in the diagnosis and treatment of patients: A VAE for Cancer classification, a vector embedding model for searching through trials, and a GPT-based model for determining trial eligibility. We built the front end in NextJS with Tailwind. The front end communicates with our FastAPI backend, which coordinates all of our models. The FASTApi communicates with the VAE, which we uploaded to Hugging Face and is built with TensorFlow, as well as the Vector embedding model, which is built with Chromadb and MongoDb. After the FastAPI gets the Trials from the Vector embedded model, it does an API call to GPT-4, which determines if the patient fits the Criteria for the Trial. The FastAPI uses Docker and is hosted on Google Cloud. Challenges we ran into DOCKER!! Docker worked locally but refused to work when uploaded to Google Cloud. There were also some versioning issues with our Python environment, which meant that we had issues when going between machines. Accomplishments that we're proud of We are very proud of the cutting-edge research that we managed to implement for Curis. The model successfully classifies cancer and determines treatment, which requires us to implement two very complex systems. What we learned We learned how to use Hugging Face, which most of our team members had never used before. Hugging Face ended up being an incredibly useful tool for implementing the VAE. None of us had every successfully used Docker for us, which was an essential part of our project. What's next for Curis Curis is not currently HIPPA compliant, but we plan to fix that using in the future encryption of patient information. We would also like to implement a keyword search of the trials that our program provides the Oncologist. <div