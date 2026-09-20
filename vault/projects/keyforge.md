---
slug: "keyforge"
url: "https://devpost.com/software/keyforge"
title: "KeyVault"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 932
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# KeyVault

> A self-hosted key management platform that keeps your secrets on your infrastructure while providing enterprise-grade monitoring, automation, and control through a centralized dashboard.

[Devpost](https://devpost.com/software/keyforge) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[provenance_signing]] [[structural_withholding]]
**domain** [[developer_tools]] [[disaster_emergency]] [[transportation]]
**user** [[developer]]
**substrate** [[sensor_telemetry]]

**stack** docker, gin, go, kubernetes, postgresql, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for keyvault

## Body

Inspiration The inspiration for KeyVault came from the growing need for developers to maintain control over their secrets while still benefiting from centralized management capabilities. Traditional cloud-based key management services require trusting third parties with sensitive data, which creates compliance challenges and security concerns. We wanted to build a solution that gives developers the best of both worlds: the security of self-hosted infrastructure with the convenience of centralized monitoring and automation. What it does KeyVault is a decentralized key management platform that enables developers to securely store and manage secrets on their own infrastructure while providing centralized monitoring and automation. The platform consists of a self-hosted Vault Agent that stores encrypted secrets locally using AES-256-GCM encryption, a centralized Control Plane service that provides monitoring and analytics without ever accessing actual secret values, an intuitive Web Dashboard for managing vault agents and viewing usage analytics, and comprehensive CLI Tools for automation and CI/CD integration. The system provides automated secret rotation with customizable policies, comprehensive audit logging for compliance requirements, role-based access control with fine-grained permissions, and offline-first operation that maintains full functionality even when disconnected from the control plane. KeyVault integrates seamlessly with popular development tools and CI/CD pipelines through extensive APIs and SDKs. How we built it We built KeyVault using a specification-driven development approach with Kiro, which allowed us to systematically implement a complex distributed system. The architecture follows zero-trust principles with Go-based vault agents featuring pluggable storage backends supporting SQLite, PostgreSQL, and MySQL. Security is implemented through mTLS communication, client certificate authentication, and customer-managed encryption keys that ensure secrets never leave customer infrastructure. The system includes a comprehensive web dashboard for management and monitoring, RESTful APIs with complete OpenAPI specifications, and SDKs for multiple programming languages. We designed the infrastructure to support Docker containers, Kubernetes operators, and native binaries for easy deployment across different environments. The architecture supports horizontal scaling with multiple vault agent instances and implements comprehensive monitoring through Prometheus metrics. Challenges we ran into The biggest challenge was designing a secure communication protocol that ensures secrets never leave customer infrastructure while still providing centralized management capabilities. We had to implement a zero-trust architecture where the control plane only receives encrypted metadata, never actual secret values, while maintaining the user experience of centralized management. Creating an offline-first operation model proved complex, as vault agents must maintain full functionality even when disconnected from the control plane. Performance optimization was another significant challenge, requiring us to support over 1000 requests per second per vault agent instance while maintaining strict security requirements. We also had to build a sophisticated policy engine that supports fine-grained access control with conditional policies based on user identity, time, network location, and request context. Implementing proper cryptographic security throughout the system required careful attention to key management, secure random number generation, and encryption both at rest and in transit. Balancing these security requirements with performance and usability demands required extensive testing and optimization. Accomplishments that we're proud of We successfully implemented a complete zero-trust architecture where secrets never leave customer infrastructure, giving organizations full data sovereignty while maintaining enterprise-grade management capabilities. The comprehensive security model includes AES-256-GCM encryption, mTLS communication with certificate-based authentication, and robust audit logging that meets compliance requirements. Our performance achievements include supporting over 1000 requests per second with sub-100ms latency while maintaining strict security standards. We created a developer-friendly ecosystem with intuitive APIs, comprehensive SDKs, and seamless integrations that make security tools easy to adopt. The enterprise-ready features include a sophisticated policy engine, comprehensive audit logging, and compliance-focused capabilities that meet regulatory requirements. The scalable architecture we designed supports horizontal scaling with multiple vault agent instances and provides high availability through leader election and failover mechanisms. We're particularly proud of the offline-first design that ensures vault agents remain fully functional even during network outages or control plane maintenance. What we learned Building a distributed security system taught us valuable lessons about the importance of designing security into the architecture from the ground up rather than retrofitting it later. The specification-driven development approach with Kiro proved invaluable for systematically implementing such a complex system, allowing us to maintain consistency and completeness across all components. We gained deep insights into zero-trust principles and the challenges of never trusting any component in a distributed system. The experience highlighted the delicate balance between cryptographic security and high-performance requirements, teaching us optimization techniques that maintain security while achieving performance goals. Perhaps most importantly, we learned that developer experience is critical for security tool adoption. No matter how secure a system is, it won't be effective if developers find it difficult to use or integrate into their workflows. This insight drove many of our design decisions around APIs, documentation, and integration patterns. What's next for KeyVault We plan to expand the integration ecosystem by adding support for more CI/CD platforms, cloud providers, and development tools to make adoption even easier. Advanced analytics capabilities powered by machine learning will provide anomaly detection and security insights to help organizations identify potential threats and optimize their secret management practices. Mobile support through native apps will enable on-the-go secret management and monitoring for DevOps teams. We're pursuing compliance certifications including SOC 2 and ISO 27001 to meet enterprise security requirements. Integration with hardware security modules will provide enhanced key protection for organizations with the highest security requirements. Future development includes support for multi-region deployment with geographically distributed vault agent clusters, enhanced backup and disaster recovery capabilities, and advanced policy templates for common compliance frameworks. We're also exploring integration with emerging technologies like confidential computing and zero-knowledge proofs to further enhance security capabilities. <div