---
slug: "paracrates"
url: "https://devpost.com/software/paracrates"
title: "Paracrates"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 1372
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Paracrates

> Slingshot live applications instantly between computers. Enhance developers workflows, easily share demos in a classroom, and live migrate services between servers.

[Devpost](https://devpost.com/software/paracrates) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[transportation]]
**user** [[developer]] [[educator_student]] [[frontline_worker]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** bash, cockroachdb, criu, docker, electron, go, linux, node.js, react

## How they structured the write-up

- 💡 inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for paracrates

## Body

our great logo for now Home Screen Login Screen Push Screen 💡 Inspiration As a developer, you of course spend many hours developing code. However, we noticed that significant time is spent on the interactions between developers in a team. That is, the time you spend committing work-in-progress code to branches and attempting to bring up services and configs on your fellow developers' workstations. As a business, ensuring maximum uptime is of the highest priority. Most back-end services inherently have state while they are running, and so server migration is always a challenge (reboot). What if we could literally dump the running memory of the application, and restore it on the other machine instantly, without missing a hitch? We envisioned a solution that is like screen sharing on steroids for users. Could we just send live , running applications without complications? In fact, wouldn't this be useful in a wide variety of situations? Like when a teacher needs to share a fully set up application, at a particular screen, with a classroom full of computers? What it does Paracrates is a service that allows its users to instantly share live, running applications between computers. This is not a simple container deployment! Paracrates dumps the memory of a running process to migrate the application and its state live over the network. Once transferred to the destination computer, we can instantly restore the application's state from the dumped memory! In our demo, we used a Minecraft server as the application slingshotted. We start the server on one computer, joined it, and then transferred it to another computer in real time, without disconnecting the users! Seemingly a simple demo, there are many moving parts in order to accomplish live, seamless, instant transfer of an entire running program (skipping the boot up sequence, restoring directly to the state of the previous machine). How we built it There are several significant moving parts that come together to bring the flow of Paracrates. Electron + React (Client Application) CRIU (Checkpoint/Restore In Userspace) Docker Go (Transparent TCP Failover Proxy) NodeJS (Backend Microservice, running as a Websocket gateway) CockroachDB (database and microservice sync streaming server) The user interface is a desktop application written using React and Electron. This client app is responsible both for the user-facing interface (login/register, selecting processes, destination users, etc), and also for orchestrating the application transfer and receive process behind the scenes (NodeJS side of Electron). The heart of the transfer process is CRIU (Checkpoint/Restore In Userspace). CRIU works by freezing the target process (similar to how a debugger works), dumping its memory, file descriptors, TCP socket states, and more. Any process can be dumped into a handful of files describing its current running state. The application environments are inside Docker containers, allowing a consistent file system layout and OS environment for the target process. CRIU saves the running memory state of the application, while Docker saves the files. We created a quick transparent TCP failover proxy in Go, used in our demo, to redirect network traffic as soon as the Minecraft server transfer completes, without any disconnects noticed by Minecraft clients. The backend side of Paracrates was designed as a scaleable microservice, written in NodeJS. It is a websocket gateway that the clients connect to, and are able to send and receive messages (authentication requests, "Crate" push requests, etc). Why not REST? The real-time nature of Paracrates means Websockets are much more of an efficient choice. CockroachDB was our database of choice here for data storage, and its scaleable nature lends perfectly to our backend design. But we didn't just leverage its standard SQL capabilities, we were able to use it for much more... Because the backend is designed to be deployed as a swarm and cluster, we needed a mechanism to synchronize the state between instances of the backend (because clients maintain a single stateful connection to a given backend server). This is where we made use of CockroachDB Changefeeds . Changefeeds allow clients to subscribe to a JSON stream of table changes. This means we can efficiently communicate state changes across the entire backend swarm/cluster through CockroachDB. Specifically, we insert a row into a "changes" table every time a client does an action through the backend. This means we both have logs of actions (for data analysis, very useful!), and so that every node in the cluster will be given an event to keep track of users across the entire network. Challenges we ran into The documentation of CRIU is quite scarce, as it is quite obscure and has a small userbase. We spent much of the time debugging various limitations of CRIU, especially with restoring live TCP sockets and their source IPs. We ended up having to get around this by using failover proxies on each machine, that would emulate remote connections as local ones. We also ran into issues with the environment between the source and destination, as they had to maintain the same file structure (for restoring the address space) and package dependencies. We ended up using Docker in order to maintain the system environment, along with its experimental integration with CRIU for checkpointing and restoring containers. We had issues with getting the demo working with the live Minecraft server migration in particular. This was due to inherent limitations of the Minecraft client that caused it to time out during the dump and restore process. We used our failover proxy to provide a single "server" for clients which routed traffic as soon as the migration was complete. We decided to self-host our backend and CockroachDB on a Raspberry Pi (for a number of reasons, mostly to demonstrate that the backend can fit on small edge nodes and scale up). However, this did prove challenging for CockroachDB, since there aren't any ARM64 builds available from Cockroach themselves. Short of having to compile the DB from scratch, we luckily found a Docker image with compiled binaries of ARM64 CockroachDB. This did have some disadvantages, namely we weren't able to use Enterprise changefeeds, and instead had to use the core changefeeds (which mean we could only stream using the sql cli, not a sink like Kafka), though this wasn't a huge issue for our design. Fun fact: One of our team members forgot their laptop. Luckily, they didn't forget to bring a 2006 Dell Optiplex 755, with a whopping 2 cores and 6GB of RAM!! Our first few hours of the hackathon was trying to debug defective memory sticks and graphics drivers (as our team member forgot to add a graphics card and had to find one). Accomplishments that we're proud of We are pretty proud that we were able to pull together so many pieces to accomplish the vision we set out. In particular, getting CRIU to work properly probably took most of our time, and was really the single most important component to the entire project. The most exciting moment would be when we got the entire live migration demo working late Saturday night, after so many setbacks and debugging mind-meltingly obscure issues. We are also proud of the backend architecture. The websockets gateway proved fast and reliable, and our use of CockroachDB (incl. changefeeds) made it surprisingly scaleable (especially given the speed of development, usually it would be quite difficult). Oh, and the entire backend stack is running on (and fit on) this tiny little happy Pi :) What we learned We learned a lot about the details of how processes run on Linux when dealing with CRIU, from how files are accessed, networking, user permissions, and the address space. We also learned more about networking in general, as we had to figure out how to proxy Minecraft clients to different remotes without interruption. On the microservice side, we used CockroachDB for the first time and learned how to incorporate it. Exploring some of the features unique to CockroachDB like Changefeeds and its scaleable architecture (compared to a traditional DB like PostgreSQL). What's next for Paracrates CRIU does currently have some limitations with regards to transferring graphical applications, especially when dealing with X11. Our next order of business would be to tackle that, with the goal of being able to live transfer programs like browsers, video editors and etc. <div