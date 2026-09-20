---
slug: "maskcam"
url: "https://devpost.com/software/maskcam"
title: "HealthCam"
hackathon: "AWS Marketplace Developer Challenge: ML Powered Solutions"
organization: "Amazon"
winner: true
words: 1263
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# HealthCam

> Camera-enabled IoT device powered by AWS SageMaker to detect if people are wearing masks when accessing restricted areas in hospitals in an effort to flatten the curve of COVID-19.

[Devpost](https://devpost.com/software/maskcam) · hackathon [[AWS Marketplace Developer Challenge- ML Powered Solutions]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[health_clinical]] [[scientific_research]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, graphql, greengrass, lambdas, python, rds, s3, sagemaker, typescript, vue

## How they structured the write-up

- aws services used
- website
- raspberry pi
- setup
- challenges we ran into
- what we learnt
- whats next
- thanks

## Body

HealthCam IoT Device with Door Lock Admin Dashboard System Setup powered by AWS Door Access Activity/Protocol Violations IoT Device Try HealthCam's Admin Interface online! (healthcam.silentbyte.com) Check out and fork our Github Repo! Watch the presentation on YouTube View the slides from the presentation HealthCam In an effort to help with the currently ongoing COVID-19 health crisis, we have developed HealthCam (healthcam.silentbyte.com) , a system based on the Raspberry Pi Camera and utilizing the PPE Detector for Laboratory Safety model provided by VITech Lab, which provides predictions for whether a person is wearing a mask or not. With this information, the system is able to automatically restrict door-access to sterile areas for people not wearing a mask in order to prevent the spread of infections. Our submission contains two major components: the actual Raspberry Pi Camera with a door lock and the accompanying website to give administrators access to manually flag detections as incorrect, and to view history of compliance, violation and manual override events. AWS Services Used Service Usage Greengrass Remote code deployment onto Raspberry Pi API Gateway Framework to publish and manage API Lambda Serverless functions to perform API actions Amplify Framework to build web applications S3 Object storage RDS Hosting of a PostgresSQL database IAM Management of AWS Permissions Sagemaker Models Marketplace Model for Mask detection Website The website is powered by AWS Amplify and Vue/Vuetify, with all API calls made to AWS API Gateway. This website gives administrators the ability to manually flag detections as incorrect and view a history of compliance, violation and manual override events. When the Rasbperry Pi detects movement in the frame, it sends an image along with some metadata to an API gateway endpoint. A lambda function then picks this up, and first queries a Sagemaker endpoint created with the PPE Detector for Laboratory Safety . The endpoint then returns information about the number of people in frame, the probability that each item is a person, and the probability that they're wearing a mask. If there are people in the frame, then we take the lowest mask detected probability, compare it to a user defined minimum probability to determine whether it's compliant or not and upload image to a S3 bucket, a reference to where that image is along with the probability and number of people in frame to an RDS instance. Finally the Lambda sends a response back for whether the door should be opened or not. We have implemented a manual override button to open the door for emergency situations and in case of a false detection to guarantee that health works can continue to operate effectively and efficiently. Raspberry Pi The Raspberry Pi system runs AWS Greengrass core. This allows the remote pushing of code and configurations through the AWS Greengrass Docker connector. The main "Program" is installed as a python package and continually monitors for a percentage of pixels that have changed by some user defined percentage. If this threshold has exceded then it will send the image it has captured through to an AWS API Gateway endpoint, which will then do analysis on the image using the PPE Detector for Laboratory Safety model, to determine whether everyone in frame is wearing a mask. If they are wearing a mask, then the Raspberry Pi Turns a GPIO pin connected to a relay to HIGH, which will actuate the locking mechanism. In the event of an emergency or false detection, there is a manual override button which will trigger an interrupt, immediately opening the door, recording a picture and tagging the event as "override". Bill of Materials Item Description USB-C 5V 3A Power Supply Power for the Raspberry Pi 12V 1A Power Supply Power for the Lock Mechanism Electronic Latch Lock Lock Mechanism for Door 5V relay Relay to isolate the lock power from the Pi Pi Camera V2 Camera Dupont Line Wiring Button Press button for manual override of system 10KΩ Resistor Pull down resistor for button Setup We've written extensive documentation on how to setup the aws resources and raspberry pi requirements to run this. Create Sagemaker Endpoint Setup Frontend Setup Pi Challenges we ran into GreenGrass Setup We wanted to drive our development and infrastructure without having to click through into the AWS UI to try to learn how to better use the CLI and AWS SDKs. Because we hadn't used much Greengrass in the past it took us a while to properly setup a Greengrass core and drive deployments without using the AWS UI. We'd recommend checking out this article if you're attempting greengrass and Raspberry Pi. Unfortunately due to time constraints and last minute changes, one of the dependencies we introduced didn't work well with our docker container, so we had to deploy via Pip instead. IAM We don't work with AWS a lot and we wanted to avoid our bad behaviours of the past with allow *, so learning how to properly apply the required AWS policies to roles specific to their task was an interesting experience. We've identified a lot of cases where we could have done a lot better, so hopefully we'll fix those up. OpenCV and Raspberry Pi Some changes to OpenCV (used for detecting image differences) in November broke a few packages. Thankfully Adrian Rosebrock has updated his blog with steps around this. In retrospect given the problems we had, it would probably have been worth doing the pixel change detection in numpy instead of using such a heavy library to do it for us. Models Limitations Currently, the SageMaker model seems to have a limitation in that it doesn't properly detect non-white/blue masks. What We Learnt This hackathon gave us the chance to once again dive into Amazon Web Services. New services for us this time were AWS IoT Greengrass and AWS Amplify, which are now part of our toolbox. Whats next Authentication Currently there is no Authentication on the API gateway or website. This is something that's probably required if anyone is going to use this, so it would be well worth us putting in the effort to get this in. We would probably want to use AWS Cognitio with Federated Identities to do manage credentials. Cloudformation Deployments Because we used two different frameworks (Serverless Framework and AWS Amplify) we didn't really have a single deployment pipeline. Ideally we'd fully embrace Infrastructure as a Service and use Cloudformation to manage all of our cloud resources. Proper Deployment Pipleine (CICD) One of the things that slowed us down a bit was the lack of a proper deployment pipeline which occasionally slowed us down: We would probably want to implement proper Continuous Integration/Continuous Deployment to avoid us having to push code manually and to make sure that we have some automated tests running against our code once deployed to AWS. Proper Bootstrap Script for Raspberry Pi Currently the setup of the Raspberry Pi and Greengrass is a bit more complicated than it needs to be. Based on the steps, it should be easy enough to set up a proper bootstrap script to setup the pi ready for greengrass deployments. Thanks There were a few resources that we found invaluable while we were making this Setting up Greengrass on a Raspberry Pi was a great into to Greengrass. Accessing the Raspberry Pi Camera had some useful tips on how to poll the Pi Camera a lot faster than I was previously polling it. Install OpenCV4 on Raspberry Pi Launch RDS with AWS CLI raspi-config noint commands very useful for enabling things via cli AWS Docker Connector information on the Greengrass docker connector <div