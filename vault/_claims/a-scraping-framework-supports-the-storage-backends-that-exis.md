---
tags:
  - "claim"
confidence: 0.7
evidence: "concrete-instance"
---

# a scraping framework supports the storage backends that existed when it was written, so newer storage is unreachable from the tool most scraping runs through

Asserted by [[scrapy-ipfs-filecoin]] — *scrapy-ipfs-filecoin*  
<sub>Chainlink Fall 2022 Hackathon</sub>

**Problem** a widely used scraping framework supports filesystem, FTP and cloud storage and not decentralised storage

**Mechanism** pipelines and feed exports writing scraped items to decentralised storage services  
**Beneficiary** researchers and archivists preserving scraped data

**Recurs in** [[logging backends]] [[backup targets]] [[data pipelines]]