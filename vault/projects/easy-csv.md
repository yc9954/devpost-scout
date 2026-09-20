---
slug: "easy-csv"
url: "https://devpost.com/software/easy-csv"
title: "Buzz CSV"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 840
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "user/general_public"
  - "substrate/structured_db"
---

# Buzz CSV

> Save your company time and the headache of trying to get a story from bulky excel files that don’t want to work with you! Ask Buzz what you need and he’ll take care of the rest at hyper speed!

[Devpost](https://devpost.com/software/easy-csv) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[developer]] [[general_public]]
**substrate** [[structured_db]]

**stack** amazon-web-services, api, bedrock, dynamodb, gateway, lambda, rust, s3, sqs, sst, sveltekit5, typescript

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for buzz csv

## Body

Inspiration My name is Damien Pace and I am a solution architect at Acciona in Melbourne, Australia. I was a backend engineer that mainly worked with Lambda for my first 3.5 years of my career. I love Lambdas so I thought this would be a perfect hackathon for me. My career history explains exactly why my frontend code and UX looks like a career backend dev has done it. I currently work in an enterprise environment where people get lots of data from 3rd party sources that is just dumped into an excel spreadsheet and I get approached multiple times a month with conversations go like this. Colleague: "Hey Damien, I am working with an excel spreadsheet..." Damien: "Is there too much data on it and you either can't open it or it's just getting slower by the day?" Colleague: "How'd you know?" Damien: 😀 Sometimes these people need a database or need something in a datalake and with limited resources it can leave them blocked for weeks or months. Some colleagues don't have the technical skills or have some limited Python knowledge and run local scripts that takes days and a lot of LLM calls vibe coding their way into a mess. So I started thinking, surely I could make something to help them out? Then as my 3 year old son came around the corner with his hand on his arm shooting a laser at me screaming "BUZZ LIGHTYEAR!" I thought "what would buzz do?". Then it hit me, buzz would finish the mission. That's how Buzz CSV was born. I wanted to give them something that went above and beyond a CSV. What it does Got a massive CSV file that's crushing Excel and blocking your team for weeks? Buzz CSV swoops in like a space ranger to save the day! This lightning-fast tool transforms your sluggish spreadsheets into turbocharged Parquet files, then lets you chat with your data in plain English . No technical skills required! Minutes feels like hyper speed when you are use to weeks and months to get a story from your data. Perfect for: Enterprise teams drowning in 3rd-party data dumps who need answers NOW, not months later. The mission: Finish what Excel started. Because when you're dealing with millions of rows, you need a space ranger, not a toy. How it was built Buzz CSV uses a serverless-first architecture with AWS Lambda at its core: Frontend: SvelteKit 5 with TypeScript, deployed via CloudFront using SST V3 Backend: Rust for maximum performance and memory efficiency AWS Services: Lambda, API Gateway, S3, SQS, DynamoDB, and Bedrock (Claude 4) The system uses a producer-consumer pattern with two main flows: CSV to Parquet conversion - Multithreaded Rust processes files in 512MB chunks, batching 3.5M rows at a time while utilising 90% of the lambda memory. Natural language querying - Downloads Parquet files in-memory, creates a DuckDB instance, and uses Claude 4 to generate optimised SQL from plain English questions Buzz pushes the limits of it's allocated memory and has a nice mix of efficiency, cost benefit and performance. Challenges I ran into Memory management nightmares - Avoiding the 10GB ephemeral storage trap required careful architecture. Instead of throwing more memory at the problem, I designed a streaming solution that processes files in chunks. SQL dialect differences - Started with Polars but discovered their SQL was different enough to cause prompting issues, leading to DuckDB. DuckDB integration headaches - Getting DuckDB to play nicely with S3 direct querying was hours of binary compatibility issues with Lambda. Accomplishments that I am proud of This is the first time submitting anything into a hackathon and publicly showing my frontend and rust code to the world. I am happy that I was able to get something working end to end that I could take to a company and demo it and get some really good reactions. I am proud that I got an idea into a working product but didn't settle for good enough, I tried to optimise as much as possible and realised there are certain things that I didn't even need to do. I love working with serverless because it becomes an architecture solution instead of a code solution. I made something that my mum would be able to use with minimal effort and in minutes. It use to take her an hour to log into facebook, if I ever add log in that could change the accuracy of the former sentence. What I learned Quite a bit about rust things and processing data in large rows. With some help of the AWS team on Slack I was able to learn more about API gateway timeouts and how they actually work. What's next for Buzz CSV Being able to handle multiple datasets at once, I know there are situations where people at work have to split their excel sheets into multiple datasets because they are just too big. More testing More tweaking Showcasing to people at work and getting some feedback Try and run with it <div