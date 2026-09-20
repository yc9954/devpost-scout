---
slug: "musicbucket"
url: "https://devpost.com/software/musicbucket"
title: "MusicBucket"
hackathon: "AWS Marketplace Developer Challenge: ML Powered Solutions"
organization: "Amazon"
winner: true
words: 351
team_size: 0
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MusicBucket

> Challenge friends to a music battle and get access to cameras at event venues

[Devpost](https://devpost.com/software/musicbucket) · hackathon [[AWS Marketplace Developer Challenge- ML Powered Solutions]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[video_visual]] [[web_dom]]

**stack** android, api-gateway, api-gateway-websockets, aws-cognito, aws-lambda, aws-rds, aws-transcribe, inkscape, java, node.js, postgresql, s3, sagemaker, twilio

## How they structured the write-up

- what it does
- how i built it
- what's next for musicbucket

## Body

What it does Invite your friends, family, or strangers to a karaoke room, upload a song that will use a machine learning model to extract voice from background music that you can choose to sing to. Practice to see if you're in tune with only the artists voice or do a solo with only background music of the song. Access a event's camera streams to see different angles of the performance from your phone. How I built it It's a completely Serverless App AWS Machine Learning Models Utilized: Quantiphi - Source Separation Quantiphi - Barcode/QR-code Scanner Sample input: https://musicbucket-audio-uploads.s3.us-east-2.amazonaws.com/testfaint.mp3 Audio Output: A .out file that needs to be unzipped https://musicbucket-audio-uploads.s3.us-east-2.amazonaws.com/audio_file_1586905867.0400276.mp3_accompaniment.wav https://musicbucket-audio-uploads.s3.us-east-2.amazonaws.com/audio_file_1586905867.0400276.mp3_vocals.wav Scan Sample Input: A image/jpeg https://musicbucket-ticket-uploads.s3.us-east-2.amazonaws.com/7Yr7YI-1-of-1.jpeg Ticket Scan Output: JSON "{"09161b30-bdcb-4f03-afac-4e35ac9aba6e": "QRCODE"}" How I called the Sagemaker Models AWS Cognito credentials used to generate presignedurls. Audio file is uploaded to s3 bucket. Once the Audio File is uploaded it triggers an s3 bucket function. Trigger function invokes Sagemaker endpoint, stores s3 bucket urls/metadata into RDS. Function then grabs websocket connection IDs from DynamoDB and returns JSON through API Gateway websocket connection back to user. Music Room Built with Twilio WebRTC integrated with Lambda function for generating tokens. User first invites friends by making a request through API Gateway(RestAPI) to a lambda function to generate tokens, and those tokens are sent to the invited users in json by going through their respective API Gateway(Websockets) connections which generates a notification which they can click on, and it joins the music room. The Chat is built with API Gateway Websockets and connections managed with DynamoDB. Lyrics created by placing the vocal track returned by source seperation model into AWS Transcribe. What's next for MusicBucket There are a couple of things I want to do: -Build video rooms to support more than 4 -Have option to create streams so other users outside of room can watch and chat. Song - Faint Artist - Linkin Park Album - Faint/Street Team Sampler Writers - Mike Shinoda, Chester Bennington, Rob Bourdon, Brad Delson, Joseph “Joe” Hahn, Dave Farrell Released: 2003 Meteora Copyright: Warner Music Group (WMG) <div