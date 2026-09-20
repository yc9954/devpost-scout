---
slug: "ramadda-asdi"
url: "https://devpost.com/software/ramadda-asdi"
title: "RAMADDA ASDI"
hackathon: "Amazon Sustainability Data Initiative (ASDI) Global Hackathon"
organization: "Amazon"
winner: true
words: 701
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# RAMADDA ASDI

> Build rich interactive interfaces to ASDI S3 data

[Devpost](https://devpost.com/software/ramadda-asdi) · hackathon [[Amazon Sustainability Data Initiative -ASDI- Global Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[disaster_emergency]]
  <sub>weak: climate_energy</sub>
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-ec2, java, javascript, ramadda, s3-sdk

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ramadda asdi

## Body

RAMADDA ASDI Site Flood Risk Africa Soil Information Service NOAA ISD Crowdsourced Bathymetry Data NOAA Climate Forecase System Diversity, Inclusion and Equity - Access to Food NEXRAD on AWS NARA Census Data Inspiration I love building interactive tools centered around data, mapping and visualization. I was like a kid in a candy store exploring the ASDI data collection. What it does Easily integrate S3 data into RAMADDA enabling RAMADDA's rich suite of services to be applied to the data - browse, search, mapping, charting, data & metadata access, etc. How I built it Using Amazon's S3 Java SDK I added support to RAMADDA for accessing S3 data via the S3 API. Specifically, this consisted of brand new development in support of the challenge: A new AWS/S3 RAMADDA plugin composed of 1100 lines of new Java code as well as an entry types definition file for the new S3 Root, S3 Bucket and S3 File RAMADDA entry types. A new ASDI plugin composed of 2 new Java classes (200 LOC) and an entry type definition file for 3 new entry types to support the NOAA/ASDI Global Surface Summary of the Day (GSOD) dataset, the ASDI SondeHub data set and the NOAA ASDI Integrated Surface Database (ISD) dataset. Two new utility classes for accessing the S3 API - FileWrapper.java and S3File.java totaling 1600 lines of code In addition to the development of new RAMADDA plugins there was also - Substantial modification of RAMADDA's StorageManager.java class to provide transparent support for accessing both local files as well as S3-based files. This includes a new long-term caching mechanism that dynamically copies over and stores S3 files as needed. Substantial modification of RAMADDA's Harvesters to support harvesting external S3 file stores. Development of a new geo-tiling facility in RAMADDA's SeeSV package in support of the Community Bathymetry data set Development of a command line OCR-text corpus extraction mechanism and ingest in support of the NARA Census data set. Beyond the code changes I also added 16 different ASDI (and other) datasets and developed interactive visual interfaces for them. This includes: Ingesting the NEXRAD on AWS radar dataset and adding in alias, data type, spatial metadata and display template specification files in order to produce a more effective browse interface. Ingesting the First Street Flood Risk Summary Statistics data set from ASDI-S3. I then created interactive map interfaces for the State, Congressional and County level datasets. Ingested the African Soil Information Service Soil Chemistry dataset. I created a color-coded and searchable map interface based on the georeferences.csv file that they provided. This map interface allows users to browse and search the data sampling sites and then provides a link into the S3 Search API that RAMADDA provides. Ingested the Global Fisheries Data from ASDI-S3, cleaning up the dataset, defining a database schema for the data and creating a searchable database into this data. Copied a large subset of the ASDI Crowd-Sourced Bathymetry dataset. Ran a newly created geo-tiling service to create a new data set of tiled bathymetry dataset This dataset was then ingested in RAMADDA providing a browsable map interface into the dataset. Ingested a number of other datasets to demonstrate various aspects of this work. Challenges I ran into RAMADDA is a large code base with numerous services. Many of these services require the data files on disk to operate on and needed to be retrofitted to deal with the dynamic caching of the files Accomplishments that I'm proud of I am proud of both the interfaces into ASDI datasets that I created as well as being able to enable other data engineers to build similar interfaces using RAMADDA-S3. What I learned I had not had much experience with S3 or the S3 SDK prior to this effort but I learned alot about that space. What's next for RAMADDA ASDI Currently Unidata is in the process of updating their RAMADDA to make use of the new NEXRAD on AWS capabilities. Likewise, my colleagues at NOAA will be integrating these services. I also plan on encouraging other members of the RAMADDA community to make use of these new services. One thing I will be exploring is supporting writing data into an S3 bucket via RAMADDA. <div