---
slug: "3d-printed-multi-patient-ventilator-manifold"
url: "https://devpost.com/software/3d-printed-multi-patient-ventilator-manifold"
title: "3D printed multi-patient ventilator manifold"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 515
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
---

# 3D printed multi-patient ventilator manifold

> Ventilator shortages around the world are requiring doctors to think about who should live and die. An easily constructed manifold and check valve would multiply ventilator capacity and save lives.

[Devpost](https://devpost.com/software/3d-printed-multi-patient-ventilator-manifold) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]]

**stack** 3dprinting, g-codel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for 3d printed multi-patient ventilator manifold

## Body

Manifold splits fluid flow into 4 separate streams No special equipment needed to make. A full manifold can fit on the average hobbyist 3D printer build plate. In normal flow, the light ping pong ball is lifted. If flow is reversed, the ping bong ball drops and prevents flow. Mechanical test fit Testing on a simulated lung. Inspiration I had just heard my great uncle had contracted Covid-19 and had been placed on a ventilator when a friend who owns a clinic with operating rooms contacted me. My friend was planning to convert his operating rooms into an ICU due to his proximity to 1 of 2 major hospitals in our city. He explained that he had read research that a single ventilator can be split to server multiple patents but it was an extreme option and prone to risks. This method is very controversial for many reasons, but he was concerned about hospitals running out of ventilators to serve a predicted surge of patients. Doctors will soon be forced to decide who gets a ventilator and who dies. Last week my uncle was taken off the ventilator even though he had been showing signs of improving. They needed it for younger, healthier patients. When we tested the concept in his OR, the first two problems that became apparent were cross contamination and pressure transients. If I squeezed one simulated lung, the others would inflate. Since all the exhalation tubes communicate before entering the ventilators exhalation port, a point of cross contamination might occur. A back flow preventor valve would minimize this risk by preventing contaminated air from traveling back up another patient’s exhaust tube. Also, if one patient develops irregular tidal volume, such as coughing or hyper ventilating, the other patients air delivery is perturbed. I.e. when I squeezed one balloon during the test, the other balloons reacted. What it does Ventilator machines use specialized 22mm connections, which are not readily available and prone to supply chain bottle necks leading to no supply. Readily available back flow preventors such as, plumbing check valves, require a lot of pressure to open and are not practical for ventilation assist. We will design in readily available parts found around a typical town such as ping pong balls and specialty shaped, 3D printed chambers to allow flow in a single direction. Each manifold has a back flow preventor to attenuate pressure transients from tachypnea other pressure perturbations. These back flow preventors also minimize cross contamination by only allowing air to flow in a single direction. Stoppers are included to give physicians flexibility to serve 1 to 4 patients. The stoppers also facilitate changing patients without impacting the existing. Dr Trent McKay had the original idea and is testing the designs in his OR on simulated lungs. https://www.providence.org/doctors/profile/202504-robert-trent-mckay How I built it We will design and prototype 3D printed manifolds, test, and report results publicly as well as make the 3D printing models available for all to use. Challenges I ran into Accomplishments that I'm proud of What I learned What's next for 3D printed multi-patient ventilator manifold <div