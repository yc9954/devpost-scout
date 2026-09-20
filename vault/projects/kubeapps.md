---
slug: "kubeapps"
url: "https://devpost.com/software/kubeapps"
title: "kubeapps"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 473
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# kubeapps

> Super-charge your Kubernetes cluster https://github.com/ervin210/kubeapps.git

[Devpost](https://devpost.com/software/kubeapps) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[code_repository]] [[web_dom]]

**stack** go, makefile, shell

## How they structured the write-up

- quickstart
- installation
- build from source
- next steps
- useful resources

## Body

Kubeapps Kubeapps is a set of tools written by Bitnami to super-charge your Kubernetes cluster with: Your own application dashboard , allowing you to deploy Kubernetes-ready applications into your cluster with a single click. Kubeless , a Kubernetes-native Serverless Framework, compatible with serverless.com . SealedSecrets , a way to encrypt a Secret into a SealedSecret, which is safe to store...even for a public repository. Quickstart Kubeapps assumes a working Kubernetes (v1.7+) with RBAC enabled and kubectl installed and configured to talk to your Kubernetes cluster. Kubeapps binaries are available for both Linux and OS X, and Kubeapps has been tested with both minikube and Google Kubernetes Engine (GKE). On GKE, you must either be an "Owner" or have the "Container Engine Admin" role in order to install Kubeapps. The simplest way to try Kubeapps is to deploy it with the Kubeapps Installer on minikube . Assuming you are deploying a binary installer on Linux, here are the commands to run: curl -s https://api.github.com/repos/kubeapps/kubeapps/releases/latest | grep linux | grep browser_download_url | cut -d '"' -f 4 | wget -i - sudo mv kubeapps-linux-amd64 /usr/local/bin/kubeapps sudo chmod +x /usr/local/bin/kubeapps kubeapps up kubeapps dashboard These commands will deploy Kubeapps in your cluster and launch a browser with the Kubeapps dashboard. To remove Kubeapps from your cluster, simply run: kubeapps down Installation Get the latest release of Kubeapps Installer on the Github releases page. Alternatively, when you have configured a proper Go environment (refer to the first two steps of Build from Source section), the latest Kubeapps Installer can be get-able from source: go get github.com/kubeapps/kubeapps Build from Source The Kubeapps Installer is a CLI tool written in Go that will deploy the Kubeapps components into your cluster. You can build the latest Kubeapps Installer from source by following the steps below: Visit the Go website , download the most recent binary distribution of Go and install it following the official instructions . The remainder of this section assumes that Go is installed in /usr/local/go . Update the paths in subsequent commands if you used a different location. Set the Go environment variables: export GOROOT=/usr/local/go export GOPATH=/usr/local/go export PATH=$GOPATH/bin:$PATH Create a working directory for the project: working_dir=$GOPATH/src/github.com/kubeapps/ mkdir -p $working_dir Clone the Kubeapps source repository: cd $working_dir git clone https://github.com/kubeapps/kubeapps Build the Kubeapps binary and move it to a location in your path: cd kubeapps make binary cp kubeapps /usr/local Next Steps Use the Kubeapps Dashboard to easily manage the deployments created by Helm in your cluster and to manage your Kubeless functions, or look under the hood to see what's included in Kubeapps . In case of difficulties installing Kubeapps, find more detailed installation instructions . For a more detailed and step-by-step introduction to Kubeapps, read our introductory walkthrough . Useful Resources Walkthrough for first-time users Detailed installation instructions Kubeapps Dashboard documentation Kubeapps components https://github.com/ervin210/kubeapps.git <div