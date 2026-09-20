---
slug: "geometry-dance-vfx-mixer"
url: "https://devpost.com/software/geometry-dance-vfx-mixer"
title: "Geometry -- real-time dance vfx"
hackathon: "Facebook Hackathons: AR"
organization: "Facebook"
winner: true
words: 891
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Geometry -- real-time dance vfx

> A tool that allows you to add vfx in your performance in real-time.

[Devpost](https://devpost.com/software/geometry-dance-vfx-mixer) · hackathon [[Facebook Hackathons- AR]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[video_visual]]

**stack** javascript, sparkarstudio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for geometry -- dance vfx mixer

## Body

Inspiration Since this hackathon's topic is for Instagram Reel, the first idea is to create a tool for dancers. Something that can help content creators to do real-time visual effects. But since this project is also a piece of creation of mine, I would like this project to have a style. After doing some research into daning VFXs , I was inspired by Kosuke Iwasaki's Kyoto Girl . Then I decide to make this project geometric. What it does It's a tool that lets you create geometry shapes around you, making dance visual effects in real-time. How I built it Screen to world position with Plane Tracking The most important functionality is to calculate the depth between the camera to the user and convert the gesture's position to world space. This let the user create shapes wherever they wanted. And with the help of the plane tracker, the user can pan the camera and feels the distance between the dancer and the geometries. Which makes the space feels real. Nested Native UI Picker There are a lot of different settings and options for the filter. So I set up a nested UI picker through javascript. And the user can set up their custom shape queue with it! Animated SDF Shapes The basic shape of geometry is simple. So it takes efforts to make it looks nice. There are 8 control channels of each shape: main size, main thickness, outer distance, outer thickness, inner distance, inner thickness, shape edges, and alpha. Spent some time animating these values. Bloom With some help in the Spark AR Community, I add some blur and bloom effect to this project. This does make the project a lot better. Thanks to the great community! Segmentation and Render Pass To put the shapes in front and behind the dancer, it needs segmentation. And with the help of render pass, I added some lighting details. For example, if you create a geometry in front (with the pinch in gesture), the shape will make the segmentation layer brighter, which makes it feels like the shape is really in the space. Persistence Module Use the persistence module to store user's custom shape sequence data. Or it would be too annoying if the sequence resets after every video recording. Challenges I ran into The main challenge of this project is to achieve the need for dancers. (though I didn't really ask any dancers about it) Before I started this project, I've done some research on the topic of VFX dance videos. And I found that it is very important to make the visual feel around the body. For example, there are lots of dancing videos that have drawing strokes passing around their arms and legs. But since Spark AR does not having body tracking yet, this seemed impossible to achieve. But after some tests and digging, I found a way to mimic the surrounding effect using two planes, one behind the user and one in the front, use the animation to make them feels connected. And also the space is important. Spent some time working on the world coordinate system. Since the transform channels are point and scalar signals, the default way to modify their values is through binding instead of setting to a fixed value. This kind of API is kinda awkward for this project, so spent some time testing out the APIs ... but it's all being solved anyway! Accomplishments that I'm proud of All of the challenges listed above are part of the pride. But the proudest thing is the visual result. I put a lot of effort into the lighting. For the shapes in the back, there's an additional ground light. Which makes it feels like the shape is really positioned in the space. And for the shapes in the front, there is an overlay glow on the dancer. (the segmented person layer) Which makes the shape feels like really putting in front of a person. And also the shape animation and the bloom. Since the shape s simple, it has to have some additional effect to achieve the visual goal. And at last, I'm pretty satisfied with the result! What I learned This is a scripting heavy project, and this is my first time scripting ES6 and ES8. So I think my javascript skill might be improved a lot ... What's next for Geometry -- Dance Vfx Mixer Through the working process of this project, it kinda pushes the limit of my imagination of how a filter could be used. I used to treat filters like a piece of work, like a painting, something feeling more "fixed". And this project is like a tool, a brush, which helps users to express themselves, to create their own performance. This project only supports two shapes, but I think is kinda a demonstration, it could be more. For example, let the user customize the color, or even customize the shape's animation, or it could be other kinds of visual. This kind of "creation tool" might be a brand new category of filters. Although this kind of filter might be a little difficult to operate since filters are usually easier to use. But just through some practice, it could be handy. And when users getting used to this kind of filter, there might be more interesting videos to be made! <div