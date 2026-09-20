---
slug: "graph-learning-for-drug-drug-interaction-predction"
url: "https://devpost.com/software/graph-learning-for-drug-drug-interaction-predction"
title: "TigerLily Finding drug interactions in silico with the Graph"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 672
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# TigerLily Finding drug interactions in silico with the Graph

> Drug-drug side-effects are rarely tested directly in the pharmaceutical development process. Our system can generate in silico indications of drug-drug interactions using graph machine learning.

[Devpost](https://devpost.com/software/graph-learning-for-drug-drug-interaction-predction) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[finance_payments]] [[scientific_research]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[structured_db]]
  <sub>weak: code_repository, video_visual, web_dom</sub>

**stack** light-gbm, python, pytigergraph, scikit-learn, tigergraph

## Body

TigerLily Workflow Drug Interaction Prediction with Tigerlily Documentation | Example Notebook | Youtube Video | Project Report Tigerlily is a TigerGraph based system designed to solve the drug interaction prediction task . In this machine learning task, we want to predict whether two drugs have an adverse interaction. Our framework allows us to solve this highly relevant real-world problem using graph mining techniques in these steps: (a) Using PyTigergraph we create a heterogeneous biological graph of drugs and proteins. (b) We calculate the personalized PageRank scores of drug nodes in the TigerGraph Cloud . (c) We embed the nodes using sparse non-negative matrix factorization of the personalized PageRank matrix. (d) Using the node embeddings we train a gradient boosting based drug interaction predictor. (A) Creating and populating a Graph As a first step, the basic TigerLily tools are imported, and we load the example dataset that integrated DrugBankDDI and the BioSNAP datasets. We create a PersonalizedPageRankMachine and connect to the host with the Graph . The settings of this machine should be the appropriate user credentials and details; a secret is obtained in the TigerGraph Graph Studio . We install the default Personalized PageRank query and upload the edges of the example dataset used in our demonstrations. This graph has drug and protein nodes, drug-protein and protein-protein interactions. Our goal is to predict the drug-drug interactions. from tigerlily.dataset import ExampleDataset from tigerlily.embedding import EmbeddingMachine from tigerlily.operator import hadamard_operator from tigerlily.pagerank import PersonalizedPageRankMachine dataset = ExampleDataset() edges = dataset.read_edges() target = dataset.read_target() machine = PersonalizedPageRankMachine(host="host_name", graphname="graph_name", username="username_value", secret="secret_value", password="password_value") machine.connect() machine.install_query() machine.upload_graph(new_graph=True, edges=edges) (B) Computing the Approximate Personalized PageRank vectors We are only interested in describing the neighbourhood of drug nodes in the biological graph. Because of this, we only retrieve the neighbourhood of the drugs - for each drug we retrieve those nodes (top-k closest neighbors) which are the closest based on the Personalized PageRank scores. We are going to learn the drug embeddings based on these scores. drug_node_ids = machine.connection.getVertices("drug") pagerank_scores = machine.get_personalized_pagerank(drug_node_ids) (C) Learning the Drug Embeddings and Drug Pair Feature Generation We create an embedding machine that creates drug node representations. The embedding machine instance has a random seed, a dimensions hyperparameter (this sets the number of factors), and a maximal iteration count for the factorization. An embedding is learned from the Personalized PageRank scores and using the drug features we create drug pair features with the operator function. embedding_machine = EmbeddingMachine(seed=42, dimensions=32, max_iter=100) embedding = embedding_machine.fit(pagerank_scores) drug_pair_features = embedding_machine.create_features(target, hadamard_operator) (D) Predicting Drug Interactions and Inference We load a gradient boosting-based classifier, an evaluation metric for binary classification, and a function to create train-test splits. We create a train and test portion of the drug pairs using 80% of the pairs for training. A gradient boosted tree model is trained, score the model on the test set. We compute an AUROC score on the test portion of the dataset and print it out. from lightgbm import LGBMClassifier from sklearn.metrics import roc_auc_score from sklearn.model_selection import train_test_split X_train, X_test, y_train, y_test = train_test_split(drug_pair_features, target, train_size=0.8, random_state=42) model = LGBMClassifier(learning_rate=0.01, n_estimators=100) model.fit(X_train,y_train["label"]) predicted_label = model.predict_proba(X_test) auroc_score_value = roc_auc_score(y_test["label"], predicted_label[:,1]) print(f'AUROC score: {auroc_score_value :.4f}') Head over to the documentation to find out more about installation and a full API reference. For a quick start, check out the example notebook . If you notice anything unexpected, please open an issue . Citing If you find Tigerlily useful in your research, please consider adding the following citation: @misc{tigerlily2022, author = {Benedek Rozemberczki}, title = {TigerLily: Finding drug interactions in silico with the Graph}, year = {2022}, publisher = {GitHub}, journal = {GitHub repository}, howpublished = {\url{https://github.com/benedekrozemberczki/tigerlily}}, } Installation To install tigerlily, simply run: pip install tigerlily Running tests Running tests requires that you run: $ tox -e py License Apache 2.0 License Credit The TigerLily logo and the high level machine learning workflow image are based on: Kubos Origami Font Noun Project Icons Benedek Rozemberczki has a yearly subscription to the Noun Project that allows the customization and commercial use of the icons. <div