---
slug: "jet-setter"
url: "https://devpost.com/software/jet-setter"
title: "Jet Setter"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 429
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/web_dom"
---

# Jet Setter

> Recording purchased and remaining seats is imperative for any profitable airline company. With our website, Jet Setter, you can select your desired seats and we save that information!

[Devpost](https://devpost.com/software/jet-setter) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[web_dom]]

**stack** amazon-web-services, java, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jet setter

## Body

Inspiration Our team was inspired by a workshop we attended at this year's ShellHacks where we learned the basics of Terraform and wanted to build a project around an open-source tool. From there we brainstormed ideas of what to focus on and settled on creating a seating registry for airplane companies. What it does Jet Setter traverses through a 2D array to access the different rows of seats and their section letter to reserve the users' desired seat(s). As the user chooses their seat, Jet Setter saves this information so that if the user tries to select the same seat(s) they will be met with an error message that states the seats are already taken. How we built it Jet Setter was built by utilizing Java for the back-end portion of the project. We used methods, 2D arrays, scanner class, while loops, and booleans. Then, to build the infrastructure of the program we used Terraform for the front-end portion. Challenges we ran into Since the back-end portion of the code was fairly basic and in a familiar language we didn't struggle with Java. However, Terraform was proving to be slightly difficult to manage due to certain errors that we kept getting such as command not found or file doesn't exist . Debugging these errors took some time but solidified the understanding of how Terraform functions. Accomplishments that we're proud of Our group is proud of being able to implement a new skill in a way that isn't local like a JPanel window command. Being able to integrate rudimentary Java skills with a newly acquired tool was a first-time experience for us and certainly broadened our knowledge of programming in general. What we learned We learned that Terraform can be used to link a Java file with a domain page to display its contents. One specific fact we learned is the importance of naming conventions which can be seen in the case for nano.main tf. This would create a file with the core infrastructure definitions. What's next for Jet Setter In the future, we will incorporate graphics followed by a color key that will depict the availability of the seats on the aircraft. User experience is an integral part of building an application as it affects their viewpoint of a company's interest in maintaining customer convenience and satisfaction. Ensuring a smooth checkout process is part of this mindset. We would also like to add a feature that includes static pricing so that Jet Setter develops into something closer to what real airline companies are utilizing in their system today. <div