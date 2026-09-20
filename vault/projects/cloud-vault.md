---
slug: "cloud-vault"
url: "https://devpost.com/software/cloud-vault"
title: "Cloud Vault"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 739
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/security_privacy"
  - "user/developer"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Cloud Vault

> Cloud Vault is a containerized file uploader using Chainguard Images for secure environments. It secures data with HTTPS, SSL certs, and persistent storage, ensuring safer file management with Docker.

[Devpost](https://devpost.com/software/cloud-vault) · hackathon [[ShellHacks 2024]]

## Facets

**domain** [[education]] [[security_privacy]]
**user** [[developer]] [[educator_student]] [[small_business]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** chainguard, css3, docker, flask, html5, javascript, pip, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cloud vault

## Body

A secluded serenity above the skies. Inspiration As a student who is interested software development and cybersecurity, Cloud Vault was inspired by the increasing need for secure file storage solutions in an era of rising cyber threats. With data breaches becoming more frequent, I realized that many individuals and even small businesses lack convenient and accessible options for securely storing and sharing files. This project aims to fill that gap, providing a user-friendly program that prioritizes security through Docker. What it does Cloud Vault is a secure web app where users can upload files through a Flask-based web interface. These files are stored in a secure Docker container, using Chainguard's Wolfi OS and SSL certificates with HTTPS to minimize vulnerabilities and increase security during file transmission and storage. The application setup is portable, isolated, and secure, making it easier to run anywhere while being shielded from security risks. How we built it The development of Cloud Vault was a collaborative effort that involved several technologies Frontend: We built the user interface using vanilla HTML, CSS, and JavaScript, focusing on sleek simplicity with cutting-edge responsiveness. Backend: We used Flask, a Python web framework, to create the server-side logic and handle user requests regarding validating SSL certificates and file uploads. Deployment: We used Docker to create a consistent development environment for our Cloud Vault project. By containerizing the application, we ensured that all team members had the same dependencies, versions, and configurations. This minimized setup time and potential conflicts, allowing us to focus on quick, minimalistic, and secure development. Security: We utilized Chainguard Wolfi OS images to enhance the security posture of our application by providing a minimal and trusted environment for our containers. Coupled with the implementation of HTTPS and SSL certificates, we ensure that all data is securely transmitted and that user trust is maintained. Together, these security measures create a robust framework for protecting sensitive information and enhancing user confidence in our application. Development Tools: Our team utilized Git for version control, enabling us to track changes and collaborate effectively. Working on Fedora Workstation 40 and Windows 11 allowed us to leverage a customizable and versatile development environment. Challenges we ran into Configuring Docker for our project proved to be more difficult than anticipated. We encountered several technical issues related to networking configurations and service connections within our Docker containers. Two of our teammates were new to front-end development, which presented additional challenges. They needed time to familiarize themselves with HTML, and CSS. This occasionally slowed down progress on implementing user interface features and required more guidance and support from the rest of the team to help them get up to speed. Overall, the experience ultimately helped us grow as programmers and improve our problem-solving skills. Accomplishments that we're proud of We are proud to have successfully implemented key features of ChainGuard's WOLFI for the containerized security of sensitive documents. These features are functioning well and provide a solid foundation for the application. As first-time hackathon participants, we are thrilled to have taken on this challenge and successfully developed a functional application within a limited timeframe. This experience has boosted our confidence and inspired us to continue pursuing projects in the tech field. What we learned We gained a deeper understanding of how containerization enhances the development and deployment processes. Docker allowed us to create isolated environments for our application, ensuring each team member could work within the same setup. Through using Chainguard Wolfi OS, we learned the importance of selecting a minimalist operating system tailored for container environments. The reduced attack surface and focus on security provided by Wolfi OS align well with our goal of building a secure file storage solution. Overall, our experiences with Docker, Chainguard Wolfi OS, and web security have equipped us with valuable knowledge and skills that we will carry into future projects. The lessons learned emphasize the importance of security in application development and the need for collaboration and efficient workflows in a team environment. What's next for Cloud Vault Expand file uploads to include a broader range of file types. Strengthen security with advanced scanning encryption for files during transmission as well as file integrity checks to ensure that submitted files have not been tampered with. Improve UI with additional responsive design elements, drag-and-drop functionality, and progress indicators. Implement file compression for larger file uploads. These upgrades will enhance functionality, security, and user experience, making Cloud Vault more robust. <div