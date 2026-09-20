---
slug: "my-custom-ryu-sdn-rest-api-set"
url: "https://devpost.com/software/my-custom-ryu-sdn-rest-api-set"
title: "My custom Ryu SDN REST API set"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 1266
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/video_visual"
---

# My custom Ryu SDN REST API set

> Ryu is a software defined network controller made in Python. I find it very cool and I want to use it to manage OpenFlow switches using APIs.

[Devpost](https://devpost.com/software/my-custom-ryu-sdn-rest-api-set) · hackathon [[The Postman API Hack]]

## Facets

**user** [[developer]]
**substrate** [[video_visual]]
  <sub>weak: document_pdf</sub>

**stack** apis, flask, linux, mininet, python, ryu, virtualbox, vm

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for my custom ryu sdn rest api set

## Body

This is a Python script that automates building the virtual network topology in Mininet for testing purposes. This is a screenshot of the endpoints document text file. This is a screenshot of my project in action. Inspiration I was inspired to make this SDN project when I started learning how software defined networking can help manage network infrastructure. Instead of having to manually configure devices through the command line, it would be better to manage the same network devices through using APIs instead. The infrastructure of a software defined network is pretty intriguing because it separates the control plane from the data/forwarding plane. The network controller is on the control plane where it controls how data is transferred through the network while the switches reside in the data plane where it simply forwards the data. In addition, I really like how the open source network controller called Ryu was set up. Even though Ryu is not being widely used, I wanted to learn more about it simply out of curiosity. After taking some time to learn about software defined networking and the Ryu, I realized that this controller has a lot of potential of being widely used in more network environments to control the infrastructure. Thus, I really wanted to tap into its potential by expanding on the network controller's features, integrate my custom code into its existing architecture and explore how it can be used by network or infrastructure engineers to help them manage networks more efficiently. What it does This project uses the power of Flask and the software defined network controller Ryu, which was written in Python, to programmatically manage flows. Flows is a set of instructions that is used by the network switches to forward data on a software defined network, as well as to programmatically manage the switches that are connected to the controller. All of this is done through the network protocol known as OpenFlow, which is used by the switches and the controller to communicate with one another to keep the network infrastructure together. However, the intention is that only the Flask application server would communicate with the Ryu controller through APIs since the controller manages the network and it would be more secure to limit which devices have access to the controller. Thus, the clients would send their API requests to the Flask server, and then the Flask server sends an API request to the controller to process the request. Then, after the controller processes the request, it runs any configurations that was given in the request body and responds back to the Flask server, which then returns the response back to the end user. How I built it I built this virtual architecture design by using Python as well as using the ofctl_rest REST API application that comes by default with the Ryu. I used it as a template to help create my custom version of Ryu's REST API feature because I did that because I did not like how the default REST API application was set up. Thus, I made my own custom version with custom endpoints and set up the code in a way that I felt was easier to understand. However, I ensured that I understood how the original REST API application worked to retrieve data as well as make network configurations through the API calls as well as made sure that my application is using the correct OpenFlow and Ryu functions to work properly. Then, I also made the corresponding API endpoints in a Flask server application, so that the client would use the Flask API endpoints to talk to the Flask server instead of directly to the Ryu controller for security purposes. Furthermore, I used Mininet, a software defined networking emulator program, to emulate a software defined network environment where I would control it using the APIs that I have made. Challenges I ran into Some challenges that I ran into was the limited documentation that Ryu had about its REST API feature and about the controller in general. Therefore, I had to take an extensive amount of time to understand how the Ryu controller and the default REST API application work to ensure that my custom version would function properly. In addition, I had to do some research on the OpenFlow network protocol to see how flows are added, changed, deleted, as well as the type of OpenFlow messages that are sent between the OpenFlow switches and the network controller. Plus, I had to take some time to understand how OpenFlow messages are structured and processed by the Ryu network controller by running various tests and occasionally using Wireshark to analyze packets. I also needed a network environment to test with, so I made a small-scale virtualized version of the network design that I had in mind by using Mininet to make a virtual network topology for the controller to control. In addition, I used Open vSwitch, a Linux virtual switch that runs the OpenFlow network protocol because I needed to use a network switch that can use the OpenFlow network protocol. I had to make a virtual machine that would have Ryu, Flask, Mininet and Open vSwitch installed so that the user has an environment to use the APIs without needing to manually provision the environment on their own local machine. Furthermore, Mininet has the ability to make Python scripts that automate the process of setting up a virtual software defined network topology, so I had to figure out how to make one so that users do not have to manually build a virtual topology in the virtual machine to test my project. I also had to ensure that I was using OpenFlow version 1.3 as it is the most compatible OpenFlow version of the virtual switch. Accomplishments that I am proud of I am very proud of being able to get a better understanding of software defined networking, Ryu and APIs on my own. The passion and willingness to learn about a topic that is not yet well documented and has a bit of a learning curve felt like a big milestone to me. I was learning something that even IT professional with years of experience are starting to learn about during my free time. I feel like this is something that can be brought up to scale in more data centres around the world to manage their networks through APIs. Plus, it was really awesome to be able to write and proofread my own documentation about setting up the project and what the API endpoints do so that a user can test this project effectively. What I learned I learned how revolutionary software defined networking is with helping networks become more agile and keep up with the network demand that newer cloud applications and services will be needing. I learned how OpenFlow is used to forward data through the network using flows in flow tables and I learned about group tables and meter tables that are also part of an OpenFlow switch. I learned how to make API calls from a Flask server to the network controller using custom endpoints that I have made to expand more on Ryu's REST API feature. Lastly, I also learned how the Ryu network controller works and how it can be integrated with Python or web applications to control a network environment. What's next for My custom Ryu SDN REST API set What is next is to continue working and gaining experience with software defined networking to help make network infrastructure more programmatically efficient to configure and manage in the future. <div