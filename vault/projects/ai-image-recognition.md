---
slug: "ai-image-recognition"
url: "https://devpost.com/software/ai-image-recognition"
title: "AI Image Recognition"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 430
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# AI Image Recognition

> Our AI Image Recognition gamifies image analysis by using a CNN. This experience showcases the potential of AI while emphasizing security, as it is built on the Chainguard PyTorch-dev base image.

[Devpost](https://devpost.com/software/ai-image-recognition) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[supply_logistics]]
**substrate** [[video_visual]]

**stack** docker, github, numpy, pillow, python, streamlit, streamlit-drawable-canvas, torch, torchvision

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai image recognition

## Body

Inspiration Our team attended the Chainguard workshop. After listening to Chainguard representatives, we got inspired by their dedication to provide a safe software supply chain by using their images; free of CVEs. What it does The AI Image Recognition project is an interactive project that enables user-bot communication, where the user provides a drawing, which the AI will then analyze and decide what the user has drawn. How we built it We built the project based on the pytorch-dev image from chainguard to develop a secure application free of CVEs. This image includes crucial libraries for AI integration such as torch, torchvision, and pillow. Likewise, the streamlit and streamlit_drawable_canvas libraries were employed to develop a friendly and interactive GUI application. Finally, we created an image via Dockerfile, which is used to run the application, allowing easy deployment. Challenges we ran into Although the pytorch-dev chainguard image includes all of the essential libraries; streamlit and streamlit_drawable_canvas were not installed. Therefore, those libraries had to be installed in the existing image by adding those dependencies in the Dockerfile. This process was tedious because we had to integrate the dependencies into the path variable so these can be imported in our application. Likewise, we ran into issues using pre-trained models as they were very inaccurate. Also, we ran into issues with excessive loading times during execution. Lastly, we had a problem with multithreading in Python3 on Windows since it needed to be wrapped in a main function. Accomplishments that we're proud of We are proud of implementing these emerging technologies which include training an AI model, containerization, and using streamlit to produce content for entertainment purposes in an scientific programming language. That being said, we are proud to have been able to develop a cutting edge technology under such a tight deadline. Finally, we are proud of the communication and collaboration our team demonstrated during this project. What we learned We have learned how to build applications based on an initial image. Moreover, we learned how to use multithreading to improve efficiency when training AI models. Likewise, we learned how to develop GUI applications with the streamlit framework in Python. Lastly, we learned how to quickly and effectively develop an application in a short time. What's next for AI Image Recognition The next steps are increasing the efficiency and accuracy during the training process and finding new ways to implement the usage of AI and machine learning into more and more use cases. Also lowering the hardware requirements for complex AI models are crucial for the integration of AI into everyday life. <div