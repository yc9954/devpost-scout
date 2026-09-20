---
slug: "campus-dining-management-system-using-face-recognition"
url: "https://devpost.com/software/campus-dining-management-system-using-face-recognition"
title: "Campus Dining Management System using Face Recognition"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 1153
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Campus Dining Management System using Face Recognition

> Creating a face recognition system that detects people with food allergies or specific dietory restrictions to prevent them from consuming certain ingredients

[Devpost](https://devpost.com/software/campus-dining-management-system-using-face-recognition) · hackathon [[Boost Hacks II]]

## Facets

**domain** [[education]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** face-recognition, open-cv, python, rasberry-pi, socket-communication, tkinter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what we learned
- what's next for campus dining management system using face recognition

## Body

Display Screen Campus Dining Management System using Face Recognition Inspiration I was reading the news and I came across an article which made me concerned. It was about students encountering allergens in the school dining hall. This article made me question myself - what if the same incident happens to my peer classmates? I thought that this was not the only case, but as a person who is studying in an international school with various cultures, I noticed that some of them are not allowed to eat certain ingredients due to religious dietary restrictions. With further research, I found out that more than 40 percent of children with food allergies have experienced a severe reaction. Not only is this the problem, but as mentioned above, religion comes across as well. Therefore, I was thinking of a way to prevent this from happening, and I was given a perfect opportunity to make this come true. What it does My program is designed to prevent students and teachers from consuming allergic food and restricted ingredients due to religious reasons. The program is divided into 3 main parts : 1. Initialisation and Detection of students, 2. Network Communication, 3. User Interface Display. 1. Initialisation and Detection of Students First, I initialised the students by entering their student IDs and recording their face samples. Not only that, but also the allergic or restricted ingredients. These ingredients are recorded as integers, each number representing an ingredient. For example, 1 means eggs, 2 means milk, etc. I have included the list in the third Python file. Detecting faces is done by open CV. It uses a pre-trained algorithm called "Haar Cascade Frontal Face Default" which is specifically designed for human faces. This is called a classifier and it analyses the human facial features pattern and when a face is detected, it draws a rectangular boundary around it. 2. Network Communication I have decided to use socket network communication which is a Python library. It establishes a network connection between two devices: a client and a server. The client is the raspberry-pi and the server is the main desktop. The Raspberry Pi and the server desktop had to have the same IP address and port number. Sometimes, the port crashes unexpectedly and has to figure out the ideal value of the port. 3. User Interface Display The program uses Tkinter, a Python library for creating a graphical user interface (GUI). It is to display the information in a clear and user-friendly format. It creates a temporary window for each person who is detected. The information being displayed on the screen includes the student ID and image of the student. This is to recognise who the server should not give the certain food. It contains today's menu and whether or not to serve the food right next to the menu. How I built it I had to go through lots of thinking processes and answer some questions to dive deeper into the project and proceed with the project Answering these questions helped me to develop my project: How am I going to detect people with food allergies? How am I going to communicate all the information with the dining hall staff? What other areas do I need to take into consideration? Why face recognition? (hygienic, efficient, quick) Thus, I thought that creating a system to diagnose food allergy might be out of budget and too much of an effort as this is not the main part of the project. Therefore, I have decided to initialise people with food allergies as they join the school or a form will be sent to students’ parents to confirm their children’s allergy status. This is the best idea so far because it does not cost any money, and will be more accurate than diagnosing on the spot. Moreover, by answering the first two questions above, I came up with a plan to provide information about students’ allergies to the people serving the food. it had to be a form of either a web socket or HTTP communication protocol. After a bit of research, I concluded that a web socket is more suitable for my project as we do not require any responses from the staff’s computer. The reason why I chose to use the face recognition system instead of any other system was due to several reasons. First of all, hygiene. The dining hall is a place where hygiene is key. If I were to use a system like a fingerprint, every single student have to touch the machine which is considered unhygienic. Second of all, efficiency. As all of us know, the school dining hall during lunchtime is extremely crowded and we are short on time. Therefore, I was thinking of a time-efficient detection system but accurate at the same time. I realised that facial detection is the fastest and reasonably accurate system. Challenges we ran into I had to make a lot of compromises and go through try and error to figure out the most ideal value of each. For example, while initialising people's faces, I had to decide on an optimum number of face samples so that the accuracy remains high, but it does not take up too much storage space. Having lots of face samples would elevate the accuracy level of detection, but too much of it will cause a problem with storage space. With a bunch of try and error, I figured out that 1000 samples are the ideal number. To support the storage issue, I decided to take the photo samples in black and white as well. Accomplishments that I am proud of I believe that nothing else can be the accomplishment that I am proud of, but the fact that I successfully made the program work. It was a long journey with lots of ups and downs, making this project the accomplishment that I am most proud of. What we learned The whole process of creating this program was a priceless experience for me. I had to conduct multiple research to overcome a bunch of unexpected errors. I was on the verge of giving up in the middle, but if I did not have those moments and given up at that point, I could not be who I am today. All those moments gave me chance to grow patience, perseverance and determination . I am pleased that I was given the perfect opportunity to open a broader perspective on the IT world. What's next for Campus Dining Management System using Face Recognition It is time for me to make the dream come true. I am currently working with the school IT department on my project and considering installing the machine in our school dining hall. Although making it practical will be a completely different story compared to just writing lines of code, I will try my best to prevent any similar incidents like the article from happening. <div