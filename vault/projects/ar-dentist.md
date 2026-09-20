---
slug: "ar-dentist"
url: "https://devpost.com/software/ar-dentist"
title: "AR Dentist"
hackathon: "Junction 2017"
winner: true
words: 305
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
---

# AR Dentist

> augmented reality röntgen vision

[Devpost](https://devpost.com/software/ar-dentist) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]]

**stack** arkit, blender, indesign, ios, iphonex, photoshop, php, rhinoceros, swift, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ar dentist

## Body

Inspiration we wanted to try/learn something new over the weekend What it does Patient can view high resolution scan of his skull, basically simulating "rontgen" vision. What makes this useful is dentist's ability to annotate the scan and explain complex medical issue/treatment to patient in simple manner. How we built it we took 3D face capture from iPhone X's new depth sensors to create map of patients face we optimized high resolution 3D scans of patient's skulls for mobile devices we modified existing WebGL solution to allow doctor to markup and annotate patient's scans in his browser delivered doctor's annotations (via UV mapped textures) to user's device utilized ARKit to merge textures and scans and render them in real time over patient's face optimized numbers 4 & 5 to take less then a second Challenges we ran into sparse documentation of new frameworks and lack of code examples slowed down development our laptops struggled with up to 0.6Gb sized 3D scans, regular freezes of 3D editors Accomplishments that we're proud of immediate delivery of annotations from doctor to patient via textures 60Hz rendering of highly optimized 3D models on mobile devices probably first proof of concept of realistically usable AR in medicine/dentistry What we learned optimizing high resolution 3D data for mobile devices working with ARKit and modern (last September) face recognition APIs manipulation of textures and meshes in real time based on face movement understanding challenges that dentists face with their patients (thanks to discussions with Planmeca) What's next for AR Dentist Next challenge would be cosmetic and reconstructive plastic surgery (burn victims, skin grafts, tissue repair). Recently it started being possible to realistically modify 3D mesh of patients face in realtime and thus preview results of his surgery. This would significantly improve the iteration loop between patient/doctor when planning the future surgery. <div