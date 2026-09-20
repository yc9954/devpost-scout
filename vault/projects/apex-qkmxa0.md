---
slug: "apex-qkmxa0"
url: "https://devpost.com/software/apex-qkmxa0"
title: "Apex"
hackathon: "United Hacks V7"
organization: "Hack United"
winner: true
words: 2409
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/media_journalism"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Apex

> A reimagined way to enjoy motorsports

[Devpost](https://devpost.com/software/apex-qkmxa0) · hackathon [[United Hacks V7]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[media_journalism]] [[transportation]]
**user** [[developer]] [[educator_student]] [[frontline_worker]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** css, html, javascript, three.js, webgl

## How they structured the write-up

- race data processing
- converting data into 3d movement
- building the 3d circuit
- creating the replay engine
- designing the interface
- making apex offline-first
- synchronizing imperfect race data
- preventing jitter and teleportation
- reconstructing a real circuit
- keeping everything synchronized
- browser performance
- turning data into a story
- managing hackathon scope
- data visualization starts with data engineering
- smooth animation requires more than frequent data
- coordinate systems matter
- performance is part of the user experience
- motorsports are ideal for spatial storytelling
- accessibility can shape technical architecture
- more races and circuits

## Body

Inspiration Formula 1 generates an incredible amount of data during every race, including driver positions, lap times, sector performance, tire information, gaps, overtakes, and retirements. However, most fans experience this information through timing tables, simplified 2D maps, or platforms that require expensive and specialized hardware. We were inspired by immersive motorsport experiences that allow viewers to watch races spatially, but many of these experiences are limited to devices such as the Apple Vision Pro. That led us to ask: What if anyone with a laptop could explore a real Formula 1 race as an interactive 3D world? That question became Apex . Apex transforms historical Formula 1 race data into an interactive 3D replay that runs directly in a web browser. Instead of only showing dots moving around a flat map, Apex reconstructs the story of the race: where every driver was, when battles developed, when positions changed, and how the field evolved from the start to the checkered flag. Our goal was to make immersive motorsport visualization accessible without requiring a VR headset, gaming computer, paid application, or complicated installation process. What it does Apex converts real Formula 1 race data into an interactive, GPU-accelerated 3D replay. Users can: Watch the entire field move around a three-dimensional circuit Play, pause, and scrub through the race timeline Jump to any moment in the race Track every driver's position View a live-style timing tower Inspect race and driver information See position changes, battles, and retirements Follow close racing through a dedicated Battle Cam Explore circuit information through the Map Info interface View track elevation instead of a completely flat circuit See surrounding buildings and recognizable trackside structures Switch between supported races and circuits Run the replay locally in a browser Our primary showcase recreates a Formula 1 race around the Las Vegas Grand Prix circuit. Instead of displaying only a racing line, Apex turns the circuit and its surrounding environment into an explorable 3D race experience. How we built it Apex was built as a browser-based 3D application using: HTML CSS JavaScript Three.js WebGL Public Formula 1 datasets JSON-based race data The application is divided into several major systems. Race data processing We used publicly accessible Formula 1 data from sources including OpenF1 and MultiViewer-compatible datasets. The raw data contains timestamped information about each driver, but it does not arrive as a finished animation. Different drivers may have samples recorded at different times, and some parts of the data may be incomplete or irregular. We processed this information into a synchronized race timeline that the replay engine could query. For any replay time (t), Apex determines the data points immediately before and after that moment. The normalized progress between two samples is calculated using: $$ \alpha = \frac{t-t_i}{t_{i+1}-t_i} $$ Where: (t_i) is the timestamp of the previous sample (t_{i+1}) is the timestamp of the next sample (\alpha) represents the car's progress between the two samples This allows Apex to estimate where each driver should appear at any moment, including when the user jumps to a different point in the race. Converting data into 3D movement Raw race coordinates cannot be placed directly into a Three.js scene. The coordinates first need to be translated into a consistent local coordinate system, scaled correctly, rotated, and aligned with the rendered track. Moving cars directly between recorded telemetry points caused several visual problems: Cars appeared to jump between positions Vehicles rotated too suddenly Movement looked jittery Cars occasionally appeared to cut through corners Missing data created unnatural gaps To improve the animation, we used interpolation and Catmull-Rom spline-based movement. Instead of teleporting between recorded points, each car follows a smoother path between samples. The application also calculates the direction of movement so that each car faces the correct way while traveling around the circuit. Building the 3D circuit We did not want Apex to look like a flat line placed on an empty surface. We worked on incorporating: Accurate circuit proportions Track width Elevation changes Curbs and barriers Pit-lane positioning Buildings Trackside structures Recognizable surroundings This was especially important for Las Vegas because the city is a major part of the circuit's identity. The race takes place through an urban environment, so the surrounding buildings and streets help users understand where the cars are and make the replay feel more immersive. We also designed the track system so that additional circuits can eventually be added without rebuilding the entire application. Creating the replay engine The replay engine is the core of Apex. A single master race clock controls: Driver positions Vehicle rotation Lap progress Timing information Race order Position changes Retirements Driver information Battle detection Camera movement Timeline playback When the user pauses or scrubs through the timeline, every system must update to the same race timestamp. This was important because Apex is not a pre-rendered video. The race is reconstructed interactively. A user can jump from the opening lap to a late-race battle, and the application must immediately rebuild the correct position and state of every driver. Designing the interface We wanted Apex to feel like a combination of a Formula 1 broadcast, a telemetry dashboard, and a 3D simulation. The interface includes: A live-style timing tower Playback controls A full-race progress bar Driver information Race status information Map and circuit details Battle indicators Retirement indicators Camera controls Race selection controls One of our main features is Battle Cam . A full-circuit view is useful for understanding the entire field, but it can make close battles difficult to see. Battle Cam focuses the camera on cars that are racing closely together, making overtakes and defensive driving easier to follow. This helps Apex tell the story of the race rather than simply displaying data. Making Apex offline-first One of our main goals was to reduce setup and make the experience portable. Once the race data and assets are packaged, Apex can run without continuously communicating with a backend server. The application can be distributed as a browser-based experience containing: Replay data Rendering logic Interface components Track geometry Required visual assets This makes Apex useful for: Hackathon demonstrations Classrooms Presentations Motorsport exhibits Archived race collections Locations with unreliable internet access Challenges we faced Synchronizing imperfect race data Public motorsport datasets are not designed as finished 3D animations. Different drivers can have: Missing records Irregular update intervals Incomplete telemetry Unsynchronized timestamps Sudden gaps in position data We needed to create logic that could reconstruct a believable race despite those inconsistencies. Preventing jitter and teleportation Displaying every raw telemetry point directly caused unnatural movement. Cars could jump, rotate suddenly, vibrate, or appear to move through parts of the circuit incorrectly. We improved this using: Position interpolation Catmull-Rom splines Direction calculations Rotation smoothing Time normalization Track alignment Reconstructing a real circuit Creating a recognizable Formula 1 track was much more difficult than drawing a line. The circuit needed: Correct proportions Track width Elevation Pit-lane placement Barriers Nearby roads Buildings Environmental details Las Vegas was particularly challenging because the circuit passes through a dense city instead of a traditional permanent racetrack. Keeping everything synchronized Scrubbing through the race affects more than the cars. The following systems all need to display information from the same moment: Timing tower Lap counter Driver positions Race order Battles Retirements Driver cards Cameras Progress bar Even a small synchronization issue could result in a driver appearing in one position on the track while being shown in a different position on the leaderboard. Browser performance Apex may need to animate approximately 20 cars while simultaneously: Rendering a detailed 3D environment Updating race data Calculating vehicle direction Managing camera movement Updating interface components Responding instantly to timeline controls We had to balance visual quality with performance so that Apex could run on ordinary laptops rather than only high-end gaming computers. Turning data into a story Placing cars on a map is relatively straightforward. Explaining why a moment matters is much harder. We had to decide: When the camera should focus on a battle How overtakes should be highlighted How retirements should be displayed What information belongs in the timing tower How much telemetry should be shown How to avoid overwhelming casual viewers The goal was to make the experience understandable to new fans while still providing useful information to experienced motorsport viewers. Managing hackathon scope Our complete vision for Apex includes: Live race support Team radio Onboard cameras AI race analysis Multiple racing series Highly detailed digital twins of every circuit Building every feature during a hackathon was not realistic. We focused on creating a strong foundation: A functional historical race replay A reusable 3D rendering system Smooth vehicle movement Synchronized race controls A detailed circuit environment A timing interface Battle-focused camera logic A clear path for future expansion Accomplishments that we're proud of We are proud that Apex is not just a concept, static mockup, or pre-rendered video. It is an interactive race reconstruction engine. Our biggest accomplishments include: Reconstructing a real Formula 1 race using timestamped data Animating the complete field instead of only one driver Creating smooth movement from irregular telemetry samples Building a real-time 3D experience inside a web browser Supporting playback, pausing, and timeline scrubbing Synchronizing the 3D environment with the timing interface Displaying battles, position changes, and retirements Creating a Battle Cam for close on-track action Including track elevation and surrounding structures Designing the architecture to support multiple circuits Making the experience portable and offline-capable Most importantly, we demonstrated that immersive motorsport visualization does not need to be restricted to expensive headsets or specialized applications. What we learned Data visualization starts with data engineering The most visible part of Apex is the 3D race, but a large amount of work happens before anything is rendered. Cleaning timestamps, handling missing samples, synchronizing drivers, transforming coordinates, and reconstructing race state are what make the visual experience possible. Smooth animation requires more than frequent data We initially assumed that displaying every telemetry point would create smooth movement. In practice, even frequently recorded data can appear rough when it is used to animate vehicles. Interpolation, splines, orientation smoothing, and normalized timing dramatically improved the replay. Coordinate systems matter Geographic coordinates, telemetry coordinates, track-model coordinates, world coordinates, and screen coordinates all represent the same race differently. A small error in scale, rotation, origin, or elevation can cause cars to appear beside the circuit instead of on it. Building Apex gave us a deeper understanding of coordinate transformation and geospatial alignment. Performance is part of the user experience A visually impressive replay is not useful if it only runs smoothly on the developer's computer. We learned to carefully manage: Geometry complexity Scene de