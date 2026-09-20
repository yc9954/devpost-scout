---
slug: "simple-mapper"
url: "https://devpost.com/software/simple-mapper"
title: "Simple Mapper"
hackathon: "PennApps XII"
winner: true
words: 117
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Simple Mapper

> Floorplan mapping using a single camera

[Devpost](https://devpost.com/software/simple-mapper) · hackathon [[PennApps XII]]

## Facets

  <sub>weak: sensor_fusion</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** matlab

## Body

An extremely simple range finder using video from a single camera intended to produce data akin to a LIDAR. This hack demonstrates range-finding to walls in a structured environment under several simplifying assumptions. To demonstrate the efficacy of this measurement technique, the resulting range data are used in a previously developed SLAM algorithm to map a hallway and display its floorplan. By constraining the camera to remain horizontally aligned a fixed height above the floor, the distance to walls can be estimated by finding the boundary between the floor and wall using edge detection and pinhole camera geometry. This simplified distance measurement makes several assumptions including nearly uniform floor color, smooth camera motion, and sparse furnishings. <div