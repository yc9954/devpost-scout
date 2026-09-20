---
slug: "recycleai-v1dqz5"
url: "https://devpost.com/software/recycleai-v1dqz5"
title: "RecyclAIble"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 1039
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# RecyclAIble

> A computer vision-based, mechanical waste bin that autonomously separates trash and recycling.

[Devpost](https://devpost.com/software/recycleai-v1dqz5) · hackathon [[Funathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** base64, flask, http, logitech, next.js, ngrok, numpy, pandas, python, raspberry-pi, react, sqlite, tailwind.css, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recyclaible

## Body

Front view of RecyclAIble Hardware components Back view of hardware with Raspberry Pi and wiring Items on RecyclAIble lid being analyzed RecyclAIble mechanically disposing of items based on if it is recyclable or not Tensorflow object detection model samples Web-based graphic user interface displaying recycling statistics Web-based graphic user interface displaying recycling statistics (continued) Flask server receiving and processing realtime HTTP requests SQLite database storing collected recycling data Inspiration The EPA estimates that although 75% of American waste is recyclable, only 30% gets recycled. Our team was inspired to create RecyclAIble by the simple fact that although most people are not trying to hurt the environment, many unknowingly throw away recyclable items in the trash. Additionally, the sheer amount of restrictions related to what items can or cannot be recycled might dissuade potential recyclers from making this decision. Ultimately, this is detrimental since it can lead to more trash simply being discarded and ending up in natural lands and landfills rather than being recycled and sustainably treated or converted into new materials. As such, RecyclAIble fulfills the task of identifying recycling objects with a machine learning-based computer vision software, saving recyclers the uncertainty of not knowing whether they can safely dispose of an object or not. Its easy-to-use web interface lets users track their recycling habits and overall statistics like the number of items disposed of, allowing users to see and share a tangible representation of their contributions to sustainability, offering an additional source of motivation to recycle. What it does RecyclAIble is an AI-powered mechanical waste bin that separates trash and recycling. It employs a camera to capture items placed on an oscillating lid and, with the assistance of a motor, tilts the lid in the direction of one compartment or another depending on whether the AI model determines the object as recyclable or not. Once the object slides into the compartment, the lid will re-align itself and prepare for proceeding waste. Ultimately, RecyclAIBle autonomously helps people recycle as much as they can and waste less without them doing anything different. How we built it The RecyclAIble hardware was constructed using cardboard, a Raspberry Pi 3 B+, an ultrasonic sensor, a Servo motor, and a Logitech plug-in USB web camera, and Raspberry PI. Whenever the ultrasonic sensor detects an object placed on the surface of the lid, the camera takes an image of the object, converts it into base64 and sends it to a backend Flask server. The server receives this data, decodes the base64 back into an image file, and inputs it into a Tensorflow convolutional neural network to identify whether the object seen is recyclable or not. This data is then stored in an SQLite database and returned back to the hardware. Based on the AI model's analysis, the Servo motor in the Raspberry Pi flips the lip one way or the other, allowing the waste item to slide into its respective compartment. Additionally, a reactive, mobile-friendly web GUI was designed using Next.js, Tailwind.css, and React. This interface provides the user with insight into their current recycling statistics and how they compare to the nationwide averages of recycling. Challenges we ran into The prototype model had to be assembled, measured, and adjusted very precisely to avoid colliding components, unnecessary friction, and instability. It was difficult to get the lid to be spun by a single Servo motor and getting the Logitech camera to be propped up to get a top view. Additionally, it was very difficult to get the hardware to successfully send the encoded base64 image to the server and for the server to decode it back into an image. We also faced challenges figuring out how to publicly host the server before deciding to use ngrok. Additionally, the dataset for training the AI demanded a significant amount of storage, resources and research. Finally, establishing a connection from the frontend website to the backend server required immense troubleshooting and inspect-element hunting for missing headers. While these challenges were both time-consuming and frustrating, we were able to work together and learn about numerous tools and techniques to overcome these barriers on our way to creating RecyclAIble. Accomplishments that we're proud of We all enjoyed the bittersweet experience of discovering bugs, editing troublesome code, and staying up overnight working to overcome the various challenges we faced. We are proud to have successfully made a working prototype using various tools and technologies new to us. Ultimately, our efforts and determination culminated in a functional, complete product we are all very proud of and excited to present. Lastly, we are proud to have created something that could have a major impact on the world and help clean our environment clean. What we learned First and foremost, we learned just how big of a problem under-recycling was in America and throughout the world, and how important recycling is to Throughout the process of creating RecyclAIble, we had to do a lot of research on the technologies we wanted to use, the hardware we needed to employ and manipulate, and the actual processes, institutions, and statistics related to the process of recycling. The hackathon has motivated us to learn a lot more about our respective technologies - whether it be new errors, or desired functions, new concepts and ideas had to be introduced to make the tech work. Additionally, we educated ourselves on the importance of sustainability and recycling as well to better understand the purpose of the project and our goals. What's next for RecyclAIble RecycleAIble has a lot of potential as far as development goes. RecyclAIble's AI can be improved with further generations of images of more varied items of trash, enabling it to be more accurate and versatile in determining which items to recycle and which to trash. Additionally, new features can be incorporated into the hardware and website to allow for more functionality, like dates, tracking features, trends, and the weights of trash, that expand on the existing information and capabilities offered. And we’re already thinking of ways to make this device better, from a more robust AI to the inclusion of much more sophisticated hardware/sensors. Overall, RecyclAIble has the potential to revolutionize the process of recycling and help sustain our environment for generations to come. <div