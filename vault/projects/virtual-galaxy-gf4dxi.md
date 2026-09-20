---
slug: "virtual-galaxy-gf4dxi"
url: "https://devpost.com/software/virtual-galaxy-gf4dxi"
title: "Virtual Galaxy"
hackathon: "2019 Developer Circles from Facebook Community Challenge"
organization: "Facebook"
winner: true
words: 1246
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Virtual Galaxy

> Watch movies real time with friends and like minded people with group peer to peer voice calls, synced video playbacks and voice assistance to control movie player

[Devpost](https://devpost.com/software/virtual-galaxy-gf4dxi) · hackathon [[2019 Developer Circles from Facebook Community Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** firebase, flask, node.js, python, react360, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for virtual galaxy
- limitation

## Body

Movie Collection Movie Screen Joining a watch party Rating Exit Custom built virtual keyboard Sending friend request Login Inspiration Everyone loves a good movie. Watching it with your friends, just makes the experience memorable! We wanted to create a platform where one can watch movies with friends , likeminded people and talk to them in real-time. Watching movies with like minded people across the globe opens up a whole new socialising experience to connect and meet. It also has voice commands for pause, play and seek the video player,this is to enable users who use VRHeadsets like cardboard i.e without a controller to control the player using voice. All of this is built in browser ,so Zero plugins or Skype or a mandatory VR setup required, making it an immersive cinematic experience. Our idea is also aimed at connecting people who are physically challenged or paralysed. Bringing a virtual cinema-like experience to them. The platform thus helps in uniting people together and provide comfort even to the differently-abled. In order to ensure privacy, we decided to make the communications private (browser to browser P2P). We chose webRTC to establish a mesh network between all the peers. Then the movies as to be in sync with others in order to be at the same pace and position as the other users watching the movie together. We were also excited to work with new software and concepts like React360, peerjs and speech recognition APIs as there are limited controls in a Virtual Reality environment(especially in React360). The people to be joined have to be connected in a way that the people enjoy the movie watching together, which makes the experience fun. This is where recommendation systems comes in play, to bring in people with the same taste into the room. What it does It helps you enter an environment where you can watch movies either with friends or with other like-minded people, people who are suggested to you by the recommendation system. On entering the theatre/room you can pause/play/seek the video as you like. These changes are in sync and get reflected in all the peers' screen. At the same time, you are connected to all peers in the room through a call thus ensuring that you feel like your in the same room. Other features include React360 keyboard, watch party feature and suggest party features. you can use these features to connect to people and make the movie-watching experience worth the time. How we built it The whole system was built with React360, Webrtc and signaling servers,p5js speech recognition, Real-time web sockets and firebase realtime database. Once the users click join, they automatically join a socket room and mesh peer to peer connection is established with calls. Each control changes in the video player are broadcasted to all the peers in the socket room. Once a peer leaves each peer is alerted about it and graciously removing the dead peer. The Site is fully functional with firebase realtime database connections, once a watch party is created the notification is sent to all of his friends. The suggest watch party sends a suggestion of joining the party to online people who might like to watch the movie with that particular person. The suggestion is based on similarity correlation of the requesting person with other people online. For example, consider this scenario where out of 4 people 3 love superhero action movies and one prefers romantic movies. When one of the action movie lovers triggers the suggest movie option, only the other two action movie lovers will get the recommendation of joining the movie. And the person liking action movies is indirectly deduced from the ratings the person made when he watched other movies. Alongside p5js speech recognition to control the video player through voice. Watch the call feature in action https://youtu.be/B9B-Koyg45g Challenges we ran into The following were the challenges that we faced in React 360: The system React360 is running on parallel service workers and which doesn't obtain the normal window components like navigator.mediaDevices.getUserMedia was not available. These variables were available only in the client.js module. Due to input restrictions and the input type of only VrButton, we have developed a virtual keyboard for the system to get username, movie input. The callbacks from the client.js that have to be called multiple times which was not possible. This could be solved by invoking recursive callbacks. This was the solution to listen to real-time socket connection database (firebase). Integrating speech to text APIs with p5 was possible only by using recursive callback after the callback sent to the speech API as it could be invoked only once. The Video module with controls was edited to handle the controls from broadcasted peers in the room. This handles the controls on all the client people's video page. Challenges in WebRTC: The webRTC connections for multiple users to transmit all the controls to all the users and the communication stream. The webRTC is implemented by peer.js module with stun servers. Finding out peer.js requires a host and set up a host server for the same. Handling the call audio and video setting separately and ensuring that the videos are always in sync. Ensuring all the calls are in sync by maintaining a connectPeer[] array. Solving the edges cases of entering and exiting the room without disconnecting from the socket. Found that socket.removeListner() can be used to solve duplicate peer id generation on entering and exiting the room. Challenges in Speech and recommendation: To maximize the results for the speech recognition we came up with a solution where we post-process the results from the speech API with homophones. This makes the speech to text API more efficient and reliable. The recommendation required here is the user-user based collaborative filtering system which has to be light and fast in order to create results as fast as possible. So we decided on using cosine similarity between the user-user matrix. And to handle the cold-start problem we would collect information about the categories that the user likes the most. By this, the user can be suggested with peers right from the start and would also continue to rate the movies and improve the recommendation model's accuracy. Accomplishments that we're proud of The React360 callback recursion when the last once ends is possibly the one that made the app to be in real-time sockets. Recommendation System using user-user collaborative filter using a flask server and proxying it with a node JS server to collect the data from the firebase database. Connecting calls without any latency across the browser for all the peers in the room. Reducing the latency to about 0.2s for each video player in the room so that people can watch the movies in real-time. What's next for Virtual Galaxy Study on the ratings that the users make and try out other higher-level models such as autoencoders/Boltzmann machines to improve the efficiency of the recommendations. The project is planned on scaling as a combined study platform where students of like interests can come together, form classrooms or study groups and learn concepts faster. Peer connection in webRTC is done using mesh network. In order to improve the connection speed and peer generation, we would like to introduce a new network using DHTs and better routing techniques. Limitation The voice assistance works only in chrome browser. Group peer to peer calls supported only in Firefox and Chrome browser. Safari does not support Webrtc yet. <div