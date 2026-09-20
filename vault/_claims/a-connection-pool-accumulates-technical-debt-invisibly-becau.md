---
tags:
  - "claim"
confidence: 0.7
evidence: "concrete-instance"
---

# a connection pool accumulates technical debt invisibly because it works, so the component under every request is the one least likely to be revisited

Asserted by [[improvements-to-reva-s-grpc-client-pool]] — *Improvements to Reva's gRPC client `pool`*  
<sub>Go Hack</sub>

**Problem** a client pool carried technical debt and lacked security configuration

**Mechanism** restructuring the pool with design patterns and configurable security  
**Beneficiary** everyone depending on the service's reliability

**Recurs in** [[database drivers]] [[message brokers]] [[HTTP clients]]