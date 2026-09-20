---
slug: "apwide-booking"
url: "https://devpost.com/software/apwide-booking"
title: "Apwide Booking"
hackathon: "Codegeist 2024"
organization: "Atlassian"
winner: true
words: 430
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
---

# Apwide Booking

> Book anything in Jira: meeting rooms, devices, or vehicles. Our Booking App ensures conflict-free scheduling with smart Rovo Agent assistance. Simplify asset bookings for your team!

[Devpost](https://devpost.com/software/apwide-booking) · hackathon [[Codegeist 2024]]

## Facets

**domain** [[transportation]]

**stack** forge, rovo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for apwide booking

## Body

Inspiration Our journey began with our customers' resourcefulness. We discovered teams were repurposing our Golive tool for mobile device bookings, while others created booking systems using ScriptRunner or Jira Automation. When the Jira Admins who built these systems left, no one could maintain them. At Team24 in Barcelona, experiencing Atlassian's System of Work philosophy sparked our solution - a sustainable, script-free booking system built right into Jira. What it does Apwide Booking transforms Jira into a powerful resource management system. It provides automated conflict detection, eight pre-built templates for common booking scenarios (from meeting rooms to mobile device booking), and AI-powered assistance through the Booking Rovo Agent. Users can quickly set up booking flows, manage resources, and handle scheduling - all through familiar Jira workflows. How we built it We developed pre-built templates that configure Jira automatically, allowing teams to start booking immediately. The Rovo Agent integration provides AI-powered booking assistance, checking availability and creating Jira booking requests instantly. Challenges we ran into Our biggest challenge was balancing simplicity with flexibility. Organizations needed an app that was easy to set up yet powerful enough for complex booking scenarios. We used the UI kit framework, as we wanted to spend less time on the UI, however we’ll explore custom UI in the future, to make it more spicy for our users. We also had to implement conflict detection without impacting Jira's speed. Accomplishments that we're proud of We successfully transformed complex booking processes into a sustainable, admin-independent solution. Our template-first approach provides immediate value while allowing customization. The integration of Rovo AI assistance improves the booking process, and our conflict detection system maintains high performance even under load. What we learned The best solutions often come from observing how customers work around limitations. We learned that sustainable solutions need to balance immediate usability with long-term maintainability. The importance of building for both current and future needs became clear as we developed our template system. What's next for Apwide Booking Here's a sneak peek at what's coming next: 1- On the Booking Flow screen, we will introduce a timeline (or another view, TBC) to help you visualize resource usage and easily identify suitable time slots for your bookings. 2- When creating a new booking request, we’ll provide guidance to help you find the most appropriate resource and time slot. This will be similar to the assistance offered by the Rovo Agent, but presented visually in a banner. 3- For the resource pool, we’ll enhance flexibility by allowing you to source your resources from Jira issues (via JQL) or from Jira Assets. <div