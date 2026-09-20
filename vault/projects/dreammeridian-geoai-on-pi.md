---
slug: "dreammeridian-geoai-on-pi"
url: "https://devpost.com/software/dreammeridian-geoai-on-pi"
title: "DreamMeridian: GeoAI on Pi"
hackathon: "Arm AI Developer Challenge "
organization: "arm"
winner: true
words: 3092
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DreamMeridian: GeoAI on Pi

> When disasters strike, networks fail first. DreamMeridian runs LLM-powered spatial queries entirely offline on a Raspberry Pi 5: 5-8 watts, real data, 10-second response times, no cloud needed.

[Devpost](https://devpost.com/software/dreammeridian-geoai-on-pi) · hackathon [[Arm AI Developer Challenge]]

## Facets

**mechanism** [[benchmark_measured]] [[graph_reasoning]] [[on_device_local]] [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]] [[education]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[immigration_refugee]] [[labor_employment]]
**user** [[developer]] [[educator_student]] [[frontline_worker]] [[general_public]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** duckdb, folium, llama.cpp, networkit, osmnx, streamlit, uv, xlam

## How they structured the write-up

- inspiration
- what it does
- why dreammeridian
- pre-built datasets
- arm optimization
- how i built it
- benchmark results
- hardware
- challenges
- what i learned
- what's next
- step-by-step instructions
- example queries
- works cited

## Body

Full web UI with live Pi 5 system stats, location selector, and clinic search results. Map markers show MSF health posts near Camp 8W. 15-minute isochrone generation from Condado, San Juan. 636 reachable street nodes calculated via NetworKit graph routing in 7.72s. Hardware verification: Raspberry Pi 5 Model B Rev 1.1 with ARM Cortex-A76 architecture (aarch64). Pi 5 query: "Find fuel near Miramar" → 3 gas stations with walking times in 7s. Cortex-A76 @ 64°C, 9.6 tok/s. Pharmacy search revealing limited access - nearest pharmacies are 8+ hours walk from Camp 8W, highlighting healthcare gaps in the camp. San Juan isochrone from Condado neighborhood. Denser urban grid yields different walkability patterns than Cox's Bazar camps. Hospital density query finding 15 facilities within 2km of Condado, demonstrating the system's utility for urban disaster preparedness. Turn-by-turn walking route between refugee camps. 1.8 km path calculated from the precomputed road network graph. Walking directions from Cipulir to Lebak Bulus—route computed entirely on-device in 11 seconds via NetworKit graph routing. 15-minute walkable coverage from Serdang visualized as an isochrone polygon. Full spatial query processed offline on Raspberry Pi 5. CLI query finding 19 clinics near Camp 8W in Cox's Bazar refugee camp, including MSF health posts. 7.71s response time on Raspberry Pi 5. Walking route calculation between refugee camps in Cox's Bazar. Geocode layer resolves both "Camp 6" and "Camp 9" from local OSM data. Natural language fuel station query in San Juan, Puerto Rico. Returns walking times to three gas stations. 💠 DreamMeridian: GeoAI on Pi Author: Adam Munawar Rahman, December 2025 DreamMeridian answers natural language spatial queries entirely on-device on a Raspberry Pi 5. Ask "Find hospitals within 2km of Camp 8W" in Cox's Bazar, "How do I walk from Condado to Santurce?" in San Juan, or "Is there a pharmacy near Gelora?" in Jakarta, and get real answers with walking routes and distances in under 11 seconds. No internet, no cloud, no GPU. Just a $120 ARM board running at under 10 watts. Overview video (also attached to DevPost reel): https://www.youtube.com/watch?v=80KqDcOSRPc Inspiration At UNICEF Innovation, I built algorithms to calculate distances between schools and health facilities across programme countries. It worked, but required connectivity, cloud compute, and coding expertise that field workers don't have. Hurricane Maria showed what happens when that infrastructure fails. Within two days, 95.6% of Puerto Rico's cell sites went down (FCC, 2017). The island lost power for months; excess mortality reached 2,975 in the six months following (Santos-Burgoa et al., 2018). This pattern repeats. After the 2023 Turkey-Syria earthquake, connectivity failed across affected regions during the critical 72-hour rescue window. The 2022 Tonga eruption severed the undersea cable for five weeks. When networks fail, cloud-based tools fail with them. And 2.6 billion people remain offline globally even without disasters (ITU, 2024). Millions of humanitarian workers, including over 16 million volunteers in the Red Cross/Red Crescent network (IFRC, 2025), deploy regularly to connectivity-constrained environments. "There is a gap in getting information and data to local-level responders, humanitarians or governments at the smallest geographic level." — MapAction Operations Director The gap : Offline data collection has mature solutions. KoBoToolbox serves 32,000+ organizations with 300+ million submissions. Offline map viewing is well-addressed. QField brings substantial QGIS capability to mobile. Offline POI search and routing exist in consumer apps like OsmAnd. But natural language spatial queries on low-power edge hardware remain unavailable. A field worker can collect a GPS point, view a map, and search for nearby POIs, but cannot ask "How many people live within walking distance of this clinic?" without exporting to desktop GIS software or reaching headquarters. Free tools like QGIS with PostGIS and the QNEAT3 plugin provide powerful offline analysis including isochrones, but require technical expertise to deploy and operate. DreamMeridian fills this gap: natural language spatial queries on an ARM-based single-board computer, entirely offline. No GIS training required to run queries. What It Does DreamMeridian is an on-device spatial query engine. You ask questions in natural language; it returns walking routes, distances, and POI locations from a local OpenStreetMap database and precomputed road network graph. Why Spatial Queries Matter for Humanitarian Operations UNHCR mandates that 80% of refugees must be within one hour's walk of a health facility. Sphere standards require households within 500 meters of water points. These standards can be verified with existing GIS tools like QGIS, but not easily in the field without specialized training. DreamMeridian enables queries like: "Find the nearest hospital to Bambu Apus" "What can I reach in 15 minutes from Camp 12? "What are the nearest shelters to Condado?" Interfaces CLI ( dream-meridian.py ): Query from the command line Web Dashboard ( app.py ): Streamlit interface with Folium maps and live system stats Spatial Tools 6 functions the LLM can call: Tool Purpose Example Query list_pois POIs by type within radius "List clinics within 2km of Camp 6" find_nearest_poi_with_route Nearest POI with walking directions "Find nearest hospital to Condado" calculate_route Walking route between two points "How do I walk from Camp 3 to Camp 8W" find_along_route POIs along a path "Pharmacies between Ocean Park and Puerta de Tierra" generate_isochrone Walkable area from a point "15 minute walking radius from Camp 5" geocode_place Place name → coordinates "Where is Gelora" Why DreamMeridian Offline data collection tools (KoBoToolbox, ODK) dominate humanitarian operations but cannot perform spatial analysis. Offline GIS tools (QField, QGIS) provide spatial queries but require GIS expertise. Consumer navigation apps (OsmAnd) offer routing and POI search but lack compound spatial reasoning like isochrones from natural language. You can navigate to a point and search for nearby hospitals, but you can't ask "Which communities are more than one hour from a health facility?" DreamMeridian brings together natural language spatial queries , offline graph routing , and accessible interfaces on ARM edge hardware. This combination is unavailable in existing open-source tools. The current implementation demonstrates handling of: Multiple phrasings ("find me," "I need," "show me," "where is") 10 POI types Routes from 0.66km to 33km Isochrone analysis up to 20 minutes Multiple geographic contexts (24K to 208K nodes) All with 95% accuracy on hardware costing ~$150. The code is designed for extension: swap the datasets via build_location.py , adjust POI types, deploy to other ARM devices. The benchmark methodology and failure analysis provide a clear path for improvement. Pre-Built Datasets Three disaster response scenarios with offline data: Location Context Graph Nodes POIs Place Names Cox's Bazar, Bangladesh Rohingya refugee camps 27,551 6,509 464 San Juan, Puerto Rico Hurricane response 24,602 11,351 405 Jakarta, Indonesia Urban flood response 208,281 41,028 331 Data sourced from OpenStreetMap via OSMnx (Boeing, 2025). POI types: hospitals, clinics, pharmacies, schools, shelters, banks, markets, fuel stations, police, places of worship. ARM Optimization Why Raspberry Pi 5 The Cortex-A76 was chosen over Pi 4's Cortex-A72 for its dot product extensions. The A76 supports SDOT/UDOT instructions that accelerate INT8 multiply-accumulate operations, which are critical for quantized LLM inference (ARM Cortex-A76 Technical Reference Manual). The A72 lacks these entirely, falling back to slower scalar operations. Published benchmarks show the Pi 5 delivers 2 to 3x the CPU performance of Pi 4 (Raspberry Pi, 2023), with the Cortex-A76 at 2.4GHz compared to the Cortex-A72 at 1.5GHz. This architectural advantage, combined with higher clock speed and improved memory bandwidth, yields substantially faster inference for quantized LLM workloads. Additional advantages: native FP16 arithmetic (vs conversion-only on A72), 2MB shared L3 cache, and improved LPDDR4X memory bandwidth (Raspberry Pi Product Specifications). Raspberry Pi in Humanitarian Contexts Raspberry Pi hardware is already deployed in humanitarian contexts: RACHEL-Pi : According to World Possible, their user surveys indicate RACHEL has reached an estimated 500,000+ learners across refugee camps and remote schools in countries including Guatemala, Kenya, and Tanzania UNICEF Pi4L : Deployed to support Syrian refugee education in Lebanon (2014-2016) Jangala Big Box : Pi-based connectivity for Calais camp and Kakuma (Kenya); won 2019 Tech4Good Africa award DreamMeridian adds spatial intelligence to this proven hardware platform, with its current implementation on Raspberry Pi serving as a powerful proof-of-concept that can scale up to ARM Edge devices with more available compute or via clustered Pi devices. Full-Stack ARM Efficiency Every layer optimized for ARM edge deployment: llama.cpp : The llama.cpp developers implemented hand-written NEON intrinsics with DotProd acceleration for quantized inference. Built with -mcpu=cortex-a76 to enable ARMv8.2-A optimizations. DuckDB : Official ARM64 binaries with columnar-vectorized execution. Processes 2048-tuple batches that benefit from compiler auto-vectorization targeting NEON. NetworKit : OpenMP parallelization scales across all 4 Cortex-A76 cores. Graph algorithms are memory-bound, benefiting from Pi 5's improved LPDDR4X bandwidth. DietPi : Minimal Linux distribution with ~400MB base footprint. No GUI overhead, services trimmed to essentials. The result: a full GIS + LLM stack in under 4GB RAM. Why xLAM-2-1B Small LLMs typically struggle with structured tool-calling, which is why specialized models like xLAM exist. Salesforce's xLAM-2-1b-fc-r was trained specifically for function calling on 60,000 examples across 3,673 executable APIs (Liu et al., 2024). The xLAM model family achieved top-tier rankings on the Berkeley Function-Calling Leaderboard, with xLAM-7B(fc) outperforming GPT-4 on tool-use benchmarks (Salesforce AI Research, 2024). Q5_K_M quantization compresses the model to ~1.1GB while preserving accuracy, fitting comfortably in Pi 5's RAM with headroom for the spatial database and graph routing. How I Built It Data Preparation build_location.py : For any location string (e.g., "Cox's Bazar, Bangladesh"), this one-time online process: Resolves the string to geographic coordinates via OSM's Nominatim Downloads the street network within a bounding box via OSMnx Converts the NetworkX graph to NetworKit's binary format for fast routing Queries OSM for humanitarian-relevant POIs Extracts neighborhood and locality names for the geocoding layer Loads everything into a DuckDB database with spatial indexes This can run on the Pi itself or on a separate machine. The resulting .duckdb and .nkb files are portable and compact enough for FTP transfer and version control: coxs_bazar/ 5.5MB .duckdb + 1.5MB .nkb = ~7MB san_juan/ 6.3MB .duckdb + 1.3MB .nkb = ~8MB jakarta/ 21MB .duckdb + 11MB .nkb = ~32MB Runtime Pipeline Fully on-device, fully offline: User Query → Geocode Layer → LLM (xLAM) → Tool Selection → Spatial Tools → Result + Map ↓ ↓ "Camp 6" → coords DuckDB queries + NetworKit routing All inference and spatial computation happens locally. No network calls at runtime. I simulated field conditions by disconnecting the Pi from the network and running the full query suite successfully. Map Visualization The web dashboard uses online map tiles (Carto Dark Matter) as a background layer. When offline, the UI remains fully functional: routes, POI markers, and coordinates render correctly, just without the map background. Offline tile caching is supported via build_location.py --tiles , b