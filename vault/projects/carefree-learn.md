---
slug: "carefree-learn"
url: "https://devpost.com/software/carefree-learn"
title: "carefree-learn"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 988
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# carefree-learn

> A minimal AutoML solution for tabular datasets based on PyTorch

[Devpost](https://devpost.com/software/carefree-learn) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

**mechanism** [[benchmark_measured]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[sensor_telemetry]]

**stack** numpy, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for carefree-learn

## Body

Inspiration I've been working on tabular datasets in the past few years, and managed to build a rough AutoML system that beat the 'auto sklearn' solution to some extend. After I met PyTorch, I was deeply attracted by its simplicity and power, but I failed to find a satisfying solution for tabular datasets which was 'carefree' enough. So I decided to take advantage of my knowledges and build one myself, and here comes the carefree-learn , which aims to provide out of the box tools to train neural networks on tabular datasets with PyTorch. What it does Here's the documents that covers most of the following statements. carefree-learn provides high level APIs for PyTorch to simplify the training on tabular datasets. It features: A scikit-learn-like interface with much more 'carefree' usages. In fact, carefree-learn provides an end-to-end pipeline on tabular datasets, including AUTOMATICALLY deal with: Detection of redundant feature columns which can be excluded (all SAME, all DIFFERENT, etc). Detection of feature columns types (whether a feature column is string column / numerical column / categorical column). Imputation of missing values. Encoding of string columns and categorical columns (Embedding or One Hot Encoding). Pre-processing of numerical columns (Normalize, Min Max, etc.). And much more... Can either fit / predict directly from some numpy arrays, or fit / predict indirectly from some files locate on your machine. Easy-to-use saving and loading. By default, everything will be wrapped into a zip file! Distributed Training, which means hyper-parameter tuning can be very efficient in carefree-learn . Supports many convenient functionality in deep learning, including: Early stopping. Model persistence. Learning rate schedulers. And more... Some 'translated' machine learning algorithms, including: Trainable (Neural) Naive Bayes Trainable (Neural) Decision Tree Some brand new techniques which may boost vanilla Neural Network (NN) performances on tabular datasets, including: TreeDNN with Dynamic Soft Pruning , which makes NN less sensitive to hyper-parameters. Deep Distribution Regression (DDR) , which is capable of modeling the entire conditional distribution with one single NN model. Highly customizable for developers. We have already wrapped (almost) every single functionality / process into a single module (a Python class), and they can be replaced or enhanced either directly from source codes or from local codes with the help of some pre-defined registration functions provided by carefree-learn . Full utilization of the WIP ecosystem cf* , such as: carefree-toolkit : provides a lot of utility classes & functions which are 'stand alone' and can be leveraged in your own projects. carefree-data : a lightweight tool to read -> convert -> process ANY tabular datasets. It also utilizes cython to accelerate critical procedures. To try carefree-learn , you can install it with pip install carefree-learn . How I built it I structured the carefree-learn backend in three modules: Model , Pipeline and Wrapper : Model : In carefree-learn , a Model should implement the core algorithms. It assumes that the input data in training process is already 'batched, processed, nice and clean', but not yet 'encoded'. Fortunately, carefree-learn pre-defined some useful methods which can encode categorical columns easily. It does not care about how to train a model, it only focuses on how to make predictions with input, and how to calculate losses with them. Pipeline : In carefree-learn , a Pipeline should implement the high-level parts, as listed below: It assumes that the input data is already 'processed, nice and clean', but it should take care of getting input data into batches, because in real applications batching is essential for performance. It should take care of the training loop, which includes updating parameters with an optimizer, verbosing metrics, checkpointing, early stopping, logging, etc. Wrapper : In carefree-learn , a Wrapper should implement the preparation and API part. It should not make any assumptions to the input data, it could already be 'nice and clean', but it could also be 'dirty and messy'. Therefore, it needs to transform the original data into 'nice and clean' data and then feed it to Pipeline . The data transformations include: Imputation of missing values. Transforming string columns into categorical columns. Processing numerical columns. Processing label column (if needed). It should implement some algorithm-agnostic methods (e.g. predict , save , load , etc.). It is worth mentioning that carefree-learn uses registrations to manage the code structure. Challenges I ran into Most of the challenges I ran into was to build a system. I need to make sure that users can use it easily, and developers can also extend it without spending too much efforts. This took me days to design & refactor. The second challenge was the data processing module ( carefree-data ). Since the target of carefree-learn is to fit (almost) any tabular datasets with high performance, I need to implement a whole bunch of data processing methods into carefree-data , in an automatic manner. This again took me days to design & optimize. Another challenge was the multiprocessing part. Using CUDA and multiprocessing is not easy, especially when I needed to do some fine grained logging within the multiprocessing process. This aaagain took me days to experiment & resolve. Accomplishments that I'm proud of I've made training NNs on tabular datasets really easy now: import cflearn m = cflearn.make() # fit np.ndarray m.fit(x_np, y_np, x_cv_np, y_cv_np) m.predict(x_test_np) # fit python lists m.fit(x_list, y_list, x_cv_list, y_cv_list) m.predict(x_test_list) # fit files m.fit(x.txt, x_cv=x_cv.txt) m.predict(x_test.txt) Although the demand of working with tabular datasets is not that large, I'll be very happy if carefree-learn could help someone who needs it. I'm also proud that I've written some documents for carefree-learn . What I learned How to build an easy-to-use (Deep Learning?) system :) How to write documents :D How to make videos XD What's next for carefree-learn The next step is to make some benchmark testing and optimize carefree-learn 's performance. I'm pretty sure it can reach a satisfying level with some tuned default settings. And, as always, bug fixing XD <div