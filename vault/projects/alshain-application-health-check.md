---
slug: "alshain-application-health-check"
url: "https://devpost.com/software/alshain-application-health-check"
title: "Alshain: Application Health Check"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 644
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Alshain: Application Health Check

> The aim is to create a system which allows user to define multiple IPs/addresses which will be pinged to check their availability.

[Devpost](https://devpost.com/software/alshain-application-health-check) · hackathon [[AWS Graviton Hackathon]]

## Facets

**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** amazon-ec2, amazon-web-services, couchbase, golang, postgresql, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for alshain: application health check

## Body

Inspiration The idea was to get an application which can check whenever a website goes down specifically, it was to make sure that this check is based on regions. eg. one website can be down in singapore, but working perfectly fine in europe. What it does This application can check if a site is accessible from across the world The user specifies an application and the interval in which it checks its health. A task is run on different regions in the world checking if that application is available User can also check the history of these checks from different regions How we built it This is designed to make it work in an environment where there are multiple regions involved (much like aws). Several things were kept in mind when making the architecture Making sure that the scalability (both in same regions and different regions) is straight forward Making sure that the write to the database after execution results were as fast as possible Mainly there are four components of this application: Executor Webui PostgreSQL Couchbase Executor and webui are services written in golang, while postgreSQL and couchbase are popular databases Postgres is used to store information about the application Couchbase is used to store results of the exection For any region where we want to make it work, we need at least one couchbase instance. Couchbase instance across different regions should be in an xdcr replication An executor simply writes its results to couchbase within it's region Webui reads the results(along with replicated data) from couchbase instance in it's own region Challenges we ran into Biggest challenge i ran into was finding a database which fits this requirement. I wanted a database which can do following: Do distributed writes (Write can be done on any instance in a cluster) Give good performance in replication even on different regions Handle time series database Due to above points, i chose couchbase Another major challenge was making sure that the setup I was doing for databases and the application itself were easy to scale I used terraform to help with that Accomplishments that we're proud of The performance of the application Though there are no metrics for this yet, in my observation, the performance of the application is better than other products like this. It is due to several factors, one major one being that the executor is very lightweight and only does this one specific thing of doing very simple network request Written in golang, executor performs really well and on top of that, I feel more performance can be extracted from it with simple optimizations This simple designed coupled with golang's optimization for arm64 architecture, gives really good performance on graviton CPUs I am able to check health for 100 applications using one tg4.micro instance running this executor What we learned One big thing, which i learnt is that making softwares which can scale well is significantly different from making one instance solutions. I had to reiterate the architecture itself a several times before i was sure that this would work Another big thing i realized is that most database support replication which is read only(you can write on master node, and read from any other node) this architecture of database would not fit my design, and getting a good database which can do distributed write was difficult. in the end, I settled for couchbase, and after working with it, it is not perfect and has a learning curve, but gets the job done What's next for Alshain: Application Health Check Performance optimization It is clear that more performance can be extracted out of executor, which i look forward to doing Better database Couchbase has some performance issues when it comes to aggregation queries, I look forward to solving them with couchbase itself or replace the database layer with something else entirely <div