---
slug: "subspace"
url: "https://devpost.com/software/subspace"
title: "Subspace"
hackathon: "Hack the North 2020++"
winner: true
words: 675
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Subspace

> Work side-by-side again during COVID? Subspace gives you cloud-based desktops for remote collaboration, allowing you to instantaneously share your computing environment with others.

[Devpost](https://devpost.com/software/subspace) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[scientific_research]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]

**stack** cockroachdb, javascript, node.js, vm, vue.js, vuetify

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for subspace

## Body

Dashboard VM Session Home Page Logo Inspiration We noticed that traditional remote working technologies like Slack/Zoom, or even normal RDP couldn't replicate what it was like to work physically next to someone. Sometimes all we need is friend's pair of eyes to see that obvious typo or bug. What we also missed was having someone take the "driver's seat" for a few minutes on your physical computer, but obviously COVID-19 makes that hard. Enter Subspace. Building off of virtualization software, we developed Subspace to fix those two pain points of remote working. Subspace allows you to work in a virtualized, configurable remote environment in teams to allow easy collaboration. What it does Virtualized and easily reproducible VM images with friendly web UI Work on a desktop environment simultaneously, similar to Google Docs Copy a link to your VM desktop to share with anyone instantaneously Easily pause work to pick up on a different device, or share to your friend to allow them to debug or work right where you left off We want you to be able to work fully in the cloud, so that your computing environment is available wherever you go. The benefit of this is that we can now "share" your desktop to friends, coworkers, are more! Compared to traditional RDP hosted on your own computer, this does not require you to be online (server always is) or for anyone to install any additional software, reducing friction. It also allows you to send over your work to anyone for them to continue working or to give you a quick debug session that wouldn't justify spending 15-30 minutes downloading and configuring a work environment. As you can see from our demo, this works great for quick programming sessions and even visual work in GIMP! How we built it We built a Node.js API server that interfaces with the Nuxt.js front-end and a Flask server that integrated with our virtualization system. Users can interact with the service and deployment will be done programmatically through cloud-init to automatically assign a internal IP address and start the VNC websocket rebroadcast. Users are able to request any package to be installed during the VM creation process through the menus. To enable different users on a VNC session to see each other, we built a separate WebSocket server to receive all cursor positions for each session and rebroadcast to all clients. Finally, we layered a separate canvas on top of the VNC canvas to draw in the cursor position of the other users. For strorage, we used CockroachDB as our database with sequelize as the ORM, and we especially appreciate the compatibility with PostgreSQL. It allowed us to switch easily when there was some downtime with CockroachDB Cloud. Challenges we ran into Configuring the virtualization environment and setting up the networking and configuration our VMs needed Working with a new database (CockroachDB) "Scheduled maintenance" at the Vultr datacenter hosting our dedicated server Putting together all these moving parts in 36 (sleep deprived!) hours was a definite challenge, and we honestly can't believe we made it through. Interfacing with the OS and extending upon opensource browser VNC libraries was difficult as well. Accomplishments that we're proud of Finishing it Learning more about websockets, new databases, networking, and deployment tools such as cloud-init Extending upon VNC to provide better multi-cursor support through a secondary WebSocket server What's next for Subspace Given more time and resources, we'd like to improve the performance of the VMs through GPU hardware acceleration We'd also like to improve and polish the collaboration layer to include things such as drag-and-drop between VMs Finishing our Vonage integration. As of right now, we haven't integrated it with the UI yet. Making the deployment configuration more full-featured and potentially enabling Windows VMs To Run: https://subspace.tech is our main link, but we were having trouble with WebSocket SSL and Netlify won't let us disable HTTPS. If that doesn't work, please try http://subspace.jamesxu.ca . Trying the second link is probably your best shot if you are viewing this right now. <div