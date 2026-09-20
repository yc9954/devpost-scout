---
slug: "encrypted-file-transfer-program"
url: "https://devpost.com/software/encrypted-file-transfer-program"
title: "Encrypted File transfer program"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 642
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Encrypted File transfer program

> The program to use if you want to send secure files discretely

[Devpost](https://devpost.com/software/encrypted-file-transfer-program) · hackathon [[Funathon]]

## Facets

**substrate** [[document_pdf]] [[structured_db]]

**stack** java

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for encrypted file transfer program

## Body

This is the GUI of the main window This is a demonstration of the core idea of the program Inspiration I find cryptography incredibly interesting as it show the extreme lengths we as humans go for great secrecy, I love secrets and privacy and I want to be able to send files to my friends with no stress of the files being intercepted, so I designed a file encryption transfer service to fulfill that need. What it does When a user attempts to login the program sends the user info to a database server on an external computer. This external computer then tells the program whether the client has the correct authority, if the client has the correct authority, the program gives them the option to select whether to send or receive files, if the client wishes to send files, then the program will require a file and a client destination. When both are confirmed the client’s document will be encrypted with a shared hash key. This hash key is created by combining the username, PROCESSOR_IDENTIFIER and the PROCESSOR_LEVEL to create a hash key, this hash key is unique per client, when a connection has been established the client and destination client’s hash keys are combined to encrypt the file with their shared key. The encrypted file then gets transferred to the client where it is decrypted and stored. The shared hash key will be stored on each computer within the transfer for future use as well as a PCID to help distinguish different computers. How we built it I started by researching into cryptography techniques, mainly being sha-256 to generate hashes and the AES for encryption, since I wanted to write my own AES I opted to use some of its fundamental ideas, mainly being column and row shifting of 4x4 string matrices and XOR'ing these data points, when I started I had no clue what any of this meant. I then researched into ServerSockets for the sharing over a network and later on port forwarding to bring my program to the internet, so I could share it between friends. Challenges we ran into Writing an AES clone is hard as one small mistake and the whole output is corrupted, one missing char and the whole output is corrupted, one packet loss and the whole output is corrupted. A large challenge I ran into was avoiding corruption of data and ensuring consistent outputs, this was done through many hours of fine tuning my algorithm and network adapter. One of the largest challenges I encountered was sending large files across a ServerSocket as ServerSockets can only send and receive a certain amount of data before the are full, the way around this I found initially was to set up a queue, so the server waits for multiple packets to be sent by the client until the server got a confirmation the full encrypted file had been sent, so the server could get to work reconstructing the message, the main problem with this approach was the speed, the file transfer rate was ridiculously slow and dividing files up in to certain size packets just led to more errors, so I opted to use Channels, which can transfer more data at a time. Accomplishments that we're proud of The GUI of the main window is well designed and easy to use, and the program sends files without fail. What we learned I learned a lot about networking, encryption, GUI, ergonomics, data storage, hashing and so much more. Another large addition to my knowledge was how to multithread, I use multithreading frequently now as it is an amazing feature What's next for Encrypted File transfer program I plan to better the encryption algorithm as at the moment it is rather slow and I really believe I can speed it up by rewriting some sections. <div