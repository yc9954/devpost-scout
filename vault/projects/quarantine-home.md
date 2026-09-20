---
slug: "quarantine-home"
url: "https://devpost.com/software/quarantine-home"
title: "Quarantine@Home"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 928
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
---

# Quarantine@Home

> Donate your spare computer cycles to find drugs for COVID19 ! This platform performs small-molecule docking against key virus proteins by using volunteer computers.

[Devpost](https://devpost.com/software/quarantine-home) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[scientific_research]]
**user** [[researcher]]
**substrate** [[code_repository]] [[genomic_bio]] [[structured_db]]

**stack** autodock, cuda, docker, flask, javascript, mysql, nglviewer, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quarantine@home

## Body

Targeting the binding interface between virus spike protein (blue) and the human ACE2 receptor (green) Our current prototype is also targeting the viruses "Mpro-1" protease, needed for replication. More proteins coming soon! The current homepage - better leaderboards are coming soon! This is version 1 of the result viewer : better seen live here : https://quarantine.infino.me/view/11168/ Inspiration When I was a teenager, my parents gave me a telescope for christmas and I fell in love with astronomy. Shortly after this, I discovered the SETI@Home project, and before long had managed to fill my bedroom with ~15 pentium computers chugging along. This was my first exposure to both science and computing. Many years later, during my PhD work in computational biology, I learned how to use the Autodock suite of tools to perform small-molecule "docking" to large proteins and estimate binding energies. When the pandemic hit, I wanted to find a way to find drugs to save lives, so I turned to the framework I was familiar with and realized that I needed a LOT more computing power to test everything. What it does This project consists of a master server that dispatches jobs to volunteer computers, and allows results to be collected. The top-scoring virtual drug hits for various coronavirus proteins are displayed in a "leaderboard", along with links to the drug and a display widget that shows how well the drug fit against the protein. See the leaderboard in action here, and click and of the "results" links on the right column : https://quarantine.infino.me/ How we built it The web server is a standard flask/mysql stack, similar to that I built for my obesity genomics nonprofit that has been running for many years : www.infino.me The client software is a set of python wrappers that receive instructions, prepare files, and coordinate work performed by the core Autodock4 "kernel", created by The Scripps Research Insitute. This academic docking software is a gold standard in the computational biology community, and comes in opensource flavors for both linux and windows, including an extremely fast GPU version. We are currently leveraging all of these builds to best fit what donors can provide. The windows port is nearing completion, and is built with pyInstaller, allowing python programs to be delivered as built exe's. Parallel to this effort, a client-side GUI interface is the last remaining thing we are throwing together before the windows launch. Challenges we ran into The biggest challenge for me has been learning how to make a windows port of the client. While the linux docker version of this project was available early on, I discovered quickly that there were few friends of mine on Facebook who could run it and contribute to the cause. Donors need to be able to contribute without having to build Dockerfiles. Accomplishments that we're proud of Up until now, I have amassed a handful of volunteers with GPUs to run the linux (Docker) client, and we have completed the screening of 40,000 small molecule drugs against just two virus proteins. About halfway into the implementation of this platform, scientists at Oak Ridge National Lab published a nearly-identical docking study as the basis for this project. This publication proved the concept that the spike protein can be targeted with drugs, proving that our amateur approach wasn't so "crazy" after all! https://www.fox17online.com/scientists-using-supercomputer-to-fight-coronavirus However, the Oak Ridge team only screened ~4,000 drugs from the "SWEETLEAD" database of compounds. Even though they had the fastest supercomputer, they only tested a tiny portion of the total available chemical compounds available in the largest database of drugs. Their top binding drug had a binding energy of -7.4 kcal/mol. With our platform, using traditional Autodock (not vina) and pulling from a much larger pool of molecules, we have performed >40k jobs and found drugs that bind with energies better than -12 kcal/mol. This corresponds to drugs that bind very tightly at extremely low concentrations! There is a downside to our approach. We are testing EVERYTHING we can, even if it's never been approved to be used in humans. We think with enough volunteers around the world running our client, we can test everything quickly! What we learned As I write this, the earliest git commit for this project is March 8th. I am astonished that this came together so quickly! Many of these technologies (specifically the web stack) were learned slowly over 7 years of building www.infino.me , a nonprofit research project to study obesity. This project has become mostly defunct over the last two years and is extraordinarily complex and difficult to maintain. Tearing into this project however gave me a clean slate, as well as a globally-important life-or-death motivation to work efficiently without fear of doing things perfectly. It is a very different pace than I am used to, but I am extremely grateful that my friends and family have supported me as I tackle this important work. What's next for Quarantine@Home The biggest challenges we face is channeling this prototype into a stable-enough implementation to release the windows version, which I suspect will bring about many orders of magnitude more users. There are more than a million virtual drug compounds we wish to screen, and likely upwards of 50 possible proteins we can target that are important for the workings of this virus. Scaling the userbase with a stable platform is our current focus. After this, we have many collaboration opportunities to push the science much further, including more sophisticated free energy calculations that other computational biologists wish to perform with our dataset (which is open). <div