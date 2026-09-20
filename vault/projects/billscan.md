---
slug: "billscan"
url: "https://devpost.com/software/billscan"
title: "BillScan"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 132
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
---

# BillScan

> Never be late to pay a bill again

[Devpost](https://devpost.com/software/billscan) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]]

**stack** python, tesseract

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for billscan

## Body

Inspiration What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for BillScan Scanning Bills: Implemented OCR using Python's pytesseract library for text extraction from the scanned bills. Processed the extracted text to extract key information like the bill amount, due date, and vendor name. Parsing Information: Used regular expressions to extract structured data, such as dates and payment amounts, from the raw OCR output. Integration with Google Calendar: Utilized the Google Calendar API to create events for each due date of a bill. Automated adding reminders to alert users before the due date. User Interface: Developed a basic command-line interface (CLI) for initial interaction. Enhanced the interface to be desktop or mobile-friendly, which will be implemented in future versions. <div