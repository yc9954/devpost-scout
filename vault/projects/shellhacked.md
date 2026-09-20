---
slug: "shellhacked"
url: "https://devpost.com/software/shellhacked"
title: "ShellHacked"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 715
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/structured_db"
---

# ShellHacked

> Refresh on digital security with hands-on challenges and tips, all from your command line. Stay safe, stay smart, and learn to protect your online world effortlessly.

[Devpost](https://devpost.com/software/shellhacked) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[education]] [[security_privacy]]
**user** [[general_public]]
**substrate** [[structured_db]]

**stack** charm.sh, go, ngrok, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shellhacked

## Body

Inspiration We were inspired to create ShellHacked after witnessing the increasing complexity of online threats and the lack of accessible resources for everyday users to defend themselves. With cyberattacks becoming more sophisticated, we wanted to empower individuals to take control of their digital security through interactive and engaging lessons. By simplifying cybersecurity education, we aim to make it approachable for everyone—from beginners to tech-savvy users—so they can navigate the online world confidently, and what better way to present it than through a CLI. Our mission is to bridge the knowledge gap and foster a safer, more secure digital community. What it does ShellHacked is a command-line tool designed to boost your digital security literacy through interactive lessons and real-world challenges. It covers essential topics like phishing detection, password management, and safe browsing practices. Users can engage in hands-on exercises that simulate real-life cyber threats, helping them build critical security skills. With personalized feedback and practical tips, ShellHacked equips you with the knowledge to protect your personal data and devices, ensuring you're prepared to navigate the digital landscape safely and confidently. How we built it We built ShellHacked using Go, leveraging its efficiency and simplicity for developing a lightweight and powerful command-line tool. For the interactive user interface, we integrated Charm.sh's Bubble Tea framework, which allowed us to create a dynamic and intuitive experience right in the terminal. We also utilized the Huh framework to manage input focus and streamline user interactions. To record users' progress and answers, we chose SQLite, a reliable and lightweight database, ensuring that the tool runs smoothly even on low-resource devices. Together, these technologies enabled us to create an engaging and responsive platform for learning cybersecurity, while ensuring a seamless and secure experience for users. Challenges we ran into One of the biggest challenges we faced while building ShellHacked was working with the Bubble Tea framework. Although Bubble Tea is incredibly powerful for creating interactive CLI applications, it presented some hurdles in terms of customizing the UI and styling within a terminal environment. Managing focus transitions between input fields and maintaining smooth interactions required careful tuning, especially when handling multiple inputs simultaneously. Additionally, achieving a clean and intuitive layout was difficult due to the limited styling options available in terminal-based interfaces. These challenges pushed us to find creative solutions, optimize our code, and ensure the tool remained user-friendly without compromising functionality. Accomplishments that we're proud of We're proud to say that ShellHacked actually works! After many late nights, countless cups of coffee, and a few 'Why isn't this working?!' moments, we managed to create a fully functional, interactive CLI tool. Getting the Bubble Tea framework to behave was no small feat, and figuring out how to make everything look good in a terminal was like trying to paint a masterpiece with only 16 colors. But in the end, we pulled it off! We're thrilled to have built a tool that not only educates users on digital security but also doesn't crash every five minutes (most of the time). What we learned From completing ShellHacked, we learned that building an intuitive and interactive command-line tool is both an art and a science. We discovered the intricacies of working with Go, how to bend Bubble Tea to our will (with a bit of patience and trial-and-error). We also gained a deeper appreciation for simplicity—sometimes the smallest features take the most effort. Most importantly, we learned that perseverance (and a little humor) goes a long way when facing seemingly impossible bugs and design challenges. In the end, we came out with a solid tool and an even stronger understanding of how to create smooth, user-friendly CLI applications. What's next for ShellHacked Next for ShellHacked is expanding its capabilities to cover even more cybersecurity topics, such as social engineering, ransomware prevention, and secure coding practices. We also plan to introduce new interactive challenges and quizzes to keep users engaged and sharpen their skills. Additionally, we're working on improving the user experience by adding more customization options for styling and enhancing accessibility for different terminal environments. We're also exploring the possibility of integrating cloud-based progress tracking, so users can pick up where they left off across devices. Ultimately, we want ShellHacked to become the go-to tool for mastering digital security, one command at a time. <div