---
slug: "effiscienc-y"
url: "https://devpost.com/software/effiscienc-y"
title: "EffiScienc-y"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 828
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# EffiScienc-y

> Leverage mass testing in a context of limited resources

[Devpost](https://devpost.com/software/effiscienc-y) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**user** [[researcher]]
**substrate** [[structured_db]] [[web_dom]]

**stack** .net, azure, c#, excel, html, javascript, python, web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- post hackathon

## Body

Inspiration The unprecedented world health situation we're going through and like everyone else we're longing for a return to normality. We're inspired by the methods proposed by R. Dorfman during World War II and the use of batch testing techniques as a response to the lack of available tests for mass testing. Until a vaccine is widely available to the general public or herd immunity is achieved, mass testing the population of each country is key to come out of the current situation and slowly progress to easing lockdown and social distancing measures. As reported by news outlets, current testing capacities are insufficient in most countries around the world and no mass testing strategy seems viable with existing human and material resources. Without such generalised testing strategies in place, recurrent waves and lockdown measures are likely to become a new normal in society. Project EffiScienc-y is laid out after and inspired by multiple research articles voicing the support for a generalised use of batch testing as the quickest, easiest way to allow people back to work and return to a functional society. Batch or group testing is a proven method to simultaneously test groups of people by combining a given number of samples and mixing these together for joint analysis. In practice, the result of this single test will come out negative if all individuals in that group have not been infected (or the other way around for anti-body testing). This is key to enable programs such as the Immunity Passport for such people who have been tested and cleared. Arguably, this technique could be used to ramp up mass testing capacity four-fold, thus saving up precious testing kits and reducing lead time between sample collection and results for a wider group of people. What it does To promote efficient use of resources we developed a mathematical model and implemented this in Excel as a proof of concept before designing a web-based working prototype. As a social project, we aim at providing a free, open-access web application that enables authorities, labs and other health agents to make the most efficient use of limited testing resources. Main features of our web application: Compute infection probability given the latest daily testing data (number of tests made and number of positive results); Estimate region-specific ideal batch size given the local input data (population and infection probability); Display and compare the number of tests required for traditional testing and batch testing. How we built it We started by building an Excel file that would allow us to prove our concept and develop our initial outputs. Afterwards, a fully working website prototype was built to provide a free and open access batch optimiser. For this, we used: Backend: .NET and C# to program the back logic with ASP.NET Web Forms Frontend: HTML and JavaScript were used to properly display the website Hosted: MS Azure cloud services were used to deploy the website. Challenges we ran into To create our model we needed to mathematically validate our hypothesis which we did by using our Excel tool. After trying using the tool with different values for the variables, we concluded that the results made sense from a reality point of view. When building the website and since none of us had much experience doing it so, we bumped into some issues as we went along. With a great deal of trial and error, we overcame most of our technical difficulties and successfully build our very first iteration of the optimiser. What we learned We learned more about medical testing techniques and mathematical models. Also, by building the website we leveraged our knowledge on the used tools. As with most challenges, it was also a personal learning experience and a growth journey achieved by being subject to the pressure of delivering results under such time constraints. Accomplishments that we're proud of We are proud of being able to successfully develop in a short weekend, a functional tool that it's easy to use, reliable, and most important: free to use! We are also really excited about being one of the 117 select projects invited to the Matchathon and we are looking forward to the challenges ahead for our project. Post Hackathon Underway Working on a scientific article comparing alternative methods for batch size determination, to strengthen the scientific background for our tool; Partnering with Portuguese academic and research entities alongside health authorities to further develop the existing prototype and gather local data; Next steps Work towards the application of batch testing to a pilot-site (in Portugal) and develop a case study from there; Improve our tool and release better iterations feature-wise (during this pandemic); Develop tools to assist in infection probability estimation and integrate with local databases from healthcare systems (during this pandemic); Promote EU-wide visibility and raise awareness for the use of batch testing and of our support tool; Apply the same principles to other disease testing and promote efficiency in the health sector (post-pandemic). <div