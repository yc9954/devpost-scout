---
slug: "cluster-api-civo"
url: "https://devpost.com/software/cluster-api-civo"
title: "cluster api provider civo"
hackathon: "Civo Hackathon 2021"
organization: "Civo"
winner: true
words: 784
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# cluster api provider civo

> A kubernetes sig cluster api provider for civo. This lets you manage your civo clusters decoratively along side your other kubernetes clusters simply using `kubectl apply -f myCluster.yaml`

[Devpost](https://devpost.com/software/cluster-api-civo) · hackathon [[Civo Hackathon 2021]]

## Facets


**stack** civo, cluster-api, git, github, go, kubebuilder, kubernetes, vim, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for cluster api - civo provider

## Body

Inspiration We wanted to learn more about how kubernetes cluster api providers worked, all while bringing something useful to the civo community and learning about the civo api while we where at it! And thus was birthed the idea of not only extending the civo community to support one of the leading opensource kubernetes cluster and infrastructure projects. What it does If you follow the read me, it lets you run cluster api with the civo provider. This lets you create, manage and delete civo clusters using cluster api. Its as easy as kubectl apply -f civoCluster.yaml. This enables a wide range of ability not limited letting you declare your civo clusters as kubernetes yaml files and check these files into git empowering your gitops. How we built it Blood sweat and tears mostly We used quite a few technologies: go, the software language made popular with kubernetes. kubebuilder, the leading upstream kubernetes operator framework. cluster-api, the base project we created a provider for. Our project itself is written in go, using a collection of tools. From Goland, Vim and VScode to write the project (it seems like everyone in the team used something different and I don't know what OS each of them used.) Challenges we ran into There where a few, this might not be an all encompassing list, though we would love to chat more on them. First, We set out to make the "fully managed" cluster api (capi) provider for civo. Making a kubeadm based one on machines/vm's in Civo was out of scope, BUT capi is designed in such a way that it wants to manage and know about the kubernetes control plane. even down to what machines it runs on. This means we had to do some crazy things to fool it into thinking it had a control plane to manage. Second. Time zones, one of the cool things about this and my position on youtube is that I was able to bring together a diverse group of people. But along with that we got diverse timezone! This made a short time hackathon a little more challenging when it comes to working together. Third. So much to do in so little time! We had a few hickups with the civo kubernetes api, it did not always function like we might have expected it! For example we would have expected the CivoClient.UpdateKubernetesCluster function call that returns a "cluster" object to return the current cluster as it is in civo, but it seemed to be returning incorrect values, at least of it's current cluster ready state. but learning about a new API is all part of the fun and we mostly found it quite simple to use! After figuring that out we ran into IP address shadow quota issues. If you use the api to get quota's it exists but it is not on the dashboard. We are also unaware of how to free IP addresses if there are no clusters connected to them as it is not a resource we control. Further more, when selecting a firewall or network for your clusters the API is not always able to find the network/firewall by name, but it is never able to find it by ID. Accomplishments that we're proud of The project, it works and there are 3 people that learned quite a bit. We brought something that with a little more polish could be useful that people might find useful. we learned a LOT. Not all of us where as experiences as the rest and i'm really proud of how the team pulled together to share knowledge and grow. I respect the two people that joined me quite a bit more now and am really glad if nothing else to have the chance to know them a little bit better. That being said. for 3 people that knew very little about each other and some who knew very little about civo and kubernetes operators, we pulled together and wrote some code that does something cool. What's next for cluster api - civo provider Well, better support for one! it's just an initial release of a bunch of code! We will have to continue to add more support. One thing we need to add is support for running clusters with different cluster providers, like the kubeadm. This would bring different ways of running kubernetes in civo to the provider and let us leverage the bare machines. Another thing that would be useful is to get it accepted by the upstream community, it will need more work before that but having getting it to a point where you can install it with clusterctl init --infrastructure civo would be really awesome. <div