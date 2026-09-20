---
slug: "covid-19-prognosis"
url: "https://devpost.com/software/covid-19-prognosis"
title: "COVID-19 PROGNOSIS"
hackathon: "Civo Hackathon 2021"
organization: "Civo"
winner: true
words: 1363
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# COVID-19 PROGNOSIS

> COVID-19 Prediction Powered by AI

[Devpost](https://devpost.com/software/covid-19-prognosis) · hackathon [[Civo Hackathon 2021]]

## Facets

**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]] [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** actions, argo, civo, docker, dockerhub, flask, github, keras, kubernetes, kustomize, mongodb, numpy, opencv, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covid-19 prognosis

## Body

Home Page X-Ray Prediction Argo CD Dashboard CIVO Dashboard Github Actions Inspiration In the year 2020-21, the most demanded medical test, was the test of the COVID-19 virus . The traditional methods involved collecting samples for RT-PCR tests. But this process often gave false negatives and also took a long time to predict the result. Various research works by foreign scientists and researchers had proved that X-Ray/CT images could be efficiently used for the detection of the COVID-19 virus. It is seen that patients suffering from COVID-19, developed some particular type of lesions in their lungs, which is medically termed as Ground-Glass Opacities (GGOs) . These lesions can be easily be seen through Chest X-Ray or CT images. Several researchers had developed various Deep Learning models to automatically classify the Radiological images of patients. There are various journal as well as conference papers in this context. But these researches were not implemented in applications to reach the common people. This project aims to integrate the Deep Learning Models into Web Applications, to provide an intuitive UI through which people can interact with the model to get proper predictions. What it does The project is a Computer-Aided Diagnostic System which is used to predict whether a person has been infected with COVID-19 . The prediction is possible through the integration of the COVID-19 X-Ray Classifier into a Web Application. By uploading Frontal Chest X-Rays, the model can perform classification between COVID and non-COVID X-Rays using Modified DenseNet architectures. The users are given the option to save the results to the Database to receive further advice from doctors. The data is stored securely in MongoDB. Apart from this, REST API has been provided for Developers to access the Deep Learning Model and get prediction data in their applications. How we built it The project kickstarted with the Development of the Web Application. The UI was finalized and then the application was developed. Several open-source styles, libraries and toolkits were used during the development of the Frontend with HTML, CSS and JavaScript . After completion, the backend of the application was developed with Python & Flask framework. The routes were created and mapped to the Frontend. The Deep Learning Model was integrated with the backend REST APIs. Various libraries such as Numpy, Pillow and Tensorflow was used to manage the model. Finally, MongoDB was integrated with the backend to save the Form data. This completed the Web Application Development. The next stage involved deploying the application on CIVO K3s Cluster by developing an automated DevOps CI/CD Pipeline. First, the entire application code was pushed to a GitHub repository. Through this step, a code version control is ensured and any change in the code would automatically trigger the entire pipeline. To deploy applications on K8s, the application needed to be containerized. The building of the Docker container should automatically take place once any code gets changed. After building the container, it needs to be pushed to a Docker Repository, here Dockerhub. Also, the old Docker Image Tag mentioned in the code would need to be replaced by the new Docker Image Tag. For automating all these, a Continuous Integration Pipeline was created with the help of Github Actions as the CI tool. A workflow file was written to sequence the jobs that needed to be performed, once the code get changed in the repository. The jobs involved building and pushing the Docker container to Dockerhub . After pushing, the new container tag replaced the older one mentioned in the customization file automatically, with the help of Kustomize.io . The Deployment, Service and Ingress YAML files were pushed to the repository as K8s needed these files during deployment. This completed the Continuous Integration process. The final stage was to deploy the Docker Image pushed in DockerHub, into a CIVO k3s Cluster . For this, a K3s cluster was created on CIVO. Due to CPU intensive nature of the application, the Largest Node configuration was selected. Then through the CIVO CLI, the KubeConfig file was connected with the local KubeCTL tool. Through KubeCTL, a namespace was created and ArgoCD was installed in it. Inside ArgoCD, the configuration was provided to continuously track the GitHub Repository for changes in the Kustomization file. Since previously through CI, we had managed to update the Kustomization file after a new code change took place, this update in the Kustomization file triggered the ArgoCD to re-deploy the application based on the newer Docker Image Tag provided. Thus after an initial manual Sync, ArgoCD managed to complete the Continuous Deployment process. Finally, the CI/CD Pipeline was successfully created which helped to automatically deploy code changes to production. Challenges we ran into From finding the right model to be integrated with the application to the actual deployment of the application in the CIVO K3s Cluster, a lot of challenges were faced. Some of them were: Pushing the model weights file to GitHub was a challenge because it was larger than the permissible single file size limit of GitHub. Since the model needed to be frequently downloaded, LFS was not an ideal option due to its bandwidth cap. Thus after brainstorming, came up with the idea of splitting the large file into smaller chunks and pushing it into Github. During the Building of the container, all the pieces were merged and then pushed into the container as a single file. All these steps were mentioned in the Dockerfile. It was a challenging task, integrate the Model Weights file with the Flask Application because the input image uploaded in the Frontend form, needed to first be converted into Base64 to get transferred to the backend. At the backend, it was again decoded back and passed into the model after some manipulations with Numpy and PIL libraries to make it suitable for the model, to ensure high accuracy. It was a challenging task of selecting the combination of CI/CD tools being used in the application. Since there are numerous tools available for these purposes, it becomes challenging to select the one which can be set up quickly and can support the workflow properly. In this project, although I had experience with Github Actions, there was a need to involve ArgoCD in the picture as it is more suitable for the project. Accomplishments that we're proud of Completing the Project without much deviation from the original idea is an accomplishment. The fact that the entire project was made single-handedly, takes it to a higher level. This is the first project, I deployed on Kubernetes, all thanks to CIVO for the wonderful sessions and guides. It is the first time, I had worked on ArgoCD, which I had heard a lot about in GitOps. Apart from that, the fact that I had developed an application, which can surely help in medical science in the not-so-distant future, is an achievement for me. What we learned Throughout the development of the project, I learnt a lot about Kubernetes . Although I had an idea of its functions, I was able to get deeper into the work and have hands-on experience with the CIVO K3s Cluster . I learnt about deployments, services, ingress and many other features of K8s and its difference with K3s. Apart from that, I learnt about the ArgoCD platform which is a great tool focussed on GitOps development. I also learnt a lot about the various libraries of python to perform image manipulations. What's next for COVID-19 PROGNOSIS Due to lack of time, I was not able to integrate the Monitoring services like Prometheus and Grafana with the application. Through this, we can get various insights about the metrics of the cluster. I would surely integrate the monitoring and logging tools with the application inside the cluster. The model which has been deployed can currently perform classification only. But recently, in some researches, it has been proved that through Instance Segmentation on the X-Rays, we can actually measure the severity of the spread of the virus by precisely identifying the locations of the GGOs. In the future, I want to integrate such a model with the application, so that users can also measure the severity of the virus instantly. <div