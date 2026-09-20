---
slug: "juno-a2f8j0"
url: "https://devpost.com/software/juno-a2f8j0"
title: "Juno"
hackathon: "hack:now"
winner: true
words: 541
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "user/researcher"
---

# Juno

> Juno is serverless deployment for data scientists and researchers. We make it trivial to turn data science prototypes into deployed public APIs.

[Devpost](https://devpost.com/software/juno-a2f8j0) · hackathon [[hack-now]]

## Facets

**mechanism** [[on_device_local]]
**user** [[researcher]]

**stack** ast, firebase, flask, google-cloud-compute-engine, google-cloud-functions, javascript, postman, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for juno

## Body

Inspiration All sorts of scientific secrets are locked away in Jupyter notebooks right now, with no easy way to reproduce the science or build off of it. We want to change that. What it does Juno allows users to upload a Jupyter notebook, and in one click, deploy API's that expose specified functions in their notebook . Juno first scans the notebook to find functions the user wants to make public. Note that these functions can’t be deployed on their own -- they depend on context from the notebook, like imports declared previously, and global variables, typically trained models. Juno performs static analysis on these functions and creates custom runtime environments, which are automatically deployed with Google Cloud Functions . This runtime environment allows functions to access variables across the notebook, not just those in its scope. How we built it We wrote Juno's frontend in React. The frontend allows users to upload notebooks, and view and test their API's. Juno's backend is written in Python. A Flask server processes notebooks by extracting public functions, figuring out function dependencies, and global variables. It calculates values for global variables at the appropriate part in the program, and stores these values on Firebase. The Flask server is hosted Google Compute Engine. Juno modifies the functions to accept HTTP requests, and pull any necessary global variables from Firebase. It then exposes these modified public functions as public APIs by automating deployment to Google Cloud Functions. Challenges we ran into We found it challenging to preserve the state of the notebook from when the user ran it locally. Jupyter users typically use global variables to carry state throughout their notebook. We ended up solving this by performing static analysis on the uploaded notebook to find global variables, then serializing these values and storing them on Firebase. When a function is invoked that uses global state, it is brought down from firebase and deserialized. We also ran into deployment issues getting our scripts to run. Accomplishments that we're proud of We're proud of the overall solution we came up with. It doesn't require fiddling to deploy an API, and is the kind of thing we would use ourselves. What we learned We learned about using Firebase, Google Cloud Functions, and Python static analysis and code transformations using the AST module. What's next for Juno We'd to iterate on our frontend design as most of the hackathon was spent creating a comprehensive solution for the conversion process. We believe there are more features to add to the dashboard that could further enable researchers and data scientists. In 2011, NASA launched the Juno spacecraft from Cape Canaveral, Florida. Since 2016, the Juno spacecraft has orbited Jupiter, giving scientists a glimpse into a previously locked away world. What the spacecraft did for the planet, we want to do for the notebook. Again, all sorts of scientific secrets are locked away in Jupyter notebooks right now, with no easy way to reproduce the science or build off of them. We believe that Juno provides a glimpse into the future of how researchers and companies can bootstrap and deploy their models and research. With public APIs available, data scientists can easily publish, improve, and build off of each other’s works. <div