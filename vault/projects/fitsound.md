---
slug: "fitsound"
url: "https://devpost.com/software/fitsound"
title: "FitSound"
hackathon: "Junction 2017"
winner: true
words: 868
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# FitSound

> Fit sounds, fit people, fit city

[Devpost](https://devpost.com/software/fitsound) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[civic_government]] [[developer_tools]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** c-programming, gesture-recognition, motion-tracking, movesense, qt, sensors, spotify-android-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitsound

## Body

Gestore detection and recognition. Visualisation by QtPy. Motion sensor Inspiration Running is a popular and healty hobby of the urban population. Many runnersare listening to the music while jogging trough the streets of their neigh bourhoods. We saw ways to improve this music listening experience and incentivize the runners to contribute to the fitness of their jogging routes. What it does A motion sensor on the wrist of the runner detects the rhythm of the running. This information is used by an app that currates the playlist of the runner. The app finds a song with BPM (Beats Per Minute) that is similar to the runner's tempo. As casual joggers and careful listeners, we know that a sudden song with a dissonant tempo may break the The same motion sensor is used to control the playback of the songs. A simple but well distinguishable gesture of a hand will pause the music or a podcast that the runner is listening on the Spotify. This is convinient when crossing noisy highways or trying to hear something in your environment. No need to fishing your phone out of the pockets and no need to taking off your gloves in winter in order to push the miniature bottons on the headphones. The same gesture returns the music the ears. Another gesture skips the current song for the next one, which we already know, will have a pleasantly suitable pace. By adding more recognizible gestures, we open a way for the runner to control additional things. These gestures migh also be usedx to mark different observations on the runners route. Wiht enabled gps and a simple gesture, runner can indicate, that a concrete street has a lot of litter, or that the grass there needs more watering. Garbage cans on several streets are too full too often, and a concrete bus station is overcrouded each Friday at noon. People usually want to see their neigbourhoods nice and clean. We propose easy and game-like way for them to give the city managment wide and timely data that can be used for quick and efficient improvements. The volume and credibility of each runner can be measured and used by city management to incentivize their population to exercise and contribute even more. How we built it The system was built using Movesense sensors for activity intensity detection and gesture detection. We implemented gesture detection algorithms on Move sense sensor by implementing custom services, that allows to save battery life (no need for raw sensor data transmission via bluetooth) The program was created Movesense SDK. The Music selection was developed using Spotify platform SDK for android platform. Challenges we ran into The proposed idea is ambitious and canno't be implemented in few days. So what we managed during the Junction event was the practical implementation of detection of human's rhythm of running using motion sensors, automatic finding of the appropriete song in a playlist, detection of different hand gestures by the motion sensor, and the control of the music's playback using the Spotify's API. Challenge to learn the Movesense architecture to learn how to use built in sensor data services and more importantly to build custom service implementing data processing on the sensor device. The abstraction of the whole development artchitecture is quite high an has very steep learning curve. Challenge to learn spotify android SDK, to integrate spotify platfom in our appliation. A lot of problems unpredicted development related problems where faced but luckily where overcome. The WiFy is scarce. Accomplishments that we're proud of That we solved alot of development problems. Didn't give up and managed to finished almost everything we wanted. What we learned We learned really cool system architecture for Movesense sensors. It uses high level of abstraction making it easy to use in production (But a bit provided a little bit of steap learning curve to begin development). Learned the usage of spotify android of sdk and Movesense android sdk. What's next for FitSound Rhythm of running is only one of parameters that are detectable by motion sensors. Whith a more advanced processing of sensor data, other parameters of the runner or the chosen workout mode can be used lead to even better currated playlists. For example, songs with slightly lower or higher tempos than that of the runner may help one to warm up or increase the intensity of the workout at recommended times periods. The even greater work awaits the FitSound in the field of fit cities. The ambition is to create a game-like platform where joggers compete for who is making their own city more organised and more cared of. The gesture based approach makes it effortless to give many important datapoints on your usual running route. Dynamic point-based incentives may also force the players/runners to oversee the routs that are currently less monitored. The reliability of the results might be maintened by a voting system, where similar observations by different runners means a more reliable datapoint. City governments may reward the best data gatherers with honors and prises. Also the private companies might be interested in such incentivizing, since most of us want to be fit ourselves and live in cities that are healthy as well. <div