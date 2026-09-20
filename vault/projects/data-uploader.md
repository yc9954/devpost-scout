---
slug: "data-uploader"
url: "https://devpost.com/software/data-uploader"
title: "Data Uploader"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 426
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/structured_db"
---

# Data Uploader

> This application allows you to update an existing Monday board with your local Excel file.It could be useful to manipulate data locally and submit the result on your Monday Board.

[Devpost](https://devpost.com/software/data-uploader) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[structured_db]]

**stack** mondayapi, react

## How they structured the write-up

- please look at my github account how to make configuration board.
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for data uploader

## Body

Data Uoloader Brief How to Configuration Board Target board before running Data Uploadetr Local Data for uploading Feed Excel/CSV on Data Uploader Target board after running Data Uploader Please look at my GitHub account how to make Configuration board. Inspiration We use an ERP to manage our daily jobs, but the ERP is very poor to present job flows. Monday.com can visualize job flows clearly and let users share information easiliy. In addition, Monday has awesome integration and automation functions to make daily routine jobs easier and more efficient. Monday.com allows users to upload Excel file to initiate Board. However, users have to upload new data on their existing board manually. In our use case, it is a serious bottleneck. Sometimes, we have to upload a few dozens jobs in a day. The intense manual data entry task is not only to waste our colleagues' productive time but also cause data integrity problem which might induce serious problems. This application can take Excel file and update items via Monday GraphQL API. User can specify id on Monday board data and local Excel data, so this app choose new data from Excel file and upload them. This app let our colleagues release from their tedious data entry tasks and provides error free data entry services. What it does Data Uploader takes local Excel file and update Monday board. This application compares the local data and the data on the Monday board, and if the program detects difference, add new items or update the existing in the Monday board. This application can update the following columns: name, text, number, date, long-text, and label. How I built it I build it by React.js Challenges I ran into Generate GraphQL query according to the data type. Transform Excel/CSV Data format into JavaScript Data format. Come up with the data structure to compare two data set. Asynchronous function calls Accomplishments that I'm proud of Generate configuration data from Configuration variables. What I learned JavaScript, mainly how to use Promise Object and functional programming paradigm React.js What's next for Data Uploader Prevent the users from making the wrong configuration file. Almost all errors are generated because of the incorrect configuration file or the wrong data in the local data set, such as number column having text and label column having non-existing label. Add GUI configuration file generator to prevent typo. Add more user friendly error handling method, such as before generating query, scan each local column data and warning the potential problem to users. Add history mode: reverse the uploading event. <div