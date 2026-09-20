---
slug: "enclavemesh"
url: "https://devpost.com/software/enclavemesh"
title: "EnclaveMesh"
hackathon: "OpenD/I: Shaping Data & Infrastructure for the next 10-20 Years"
organization: "Openmesh Network"
winner: true
words: 756
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# EnclaveMesh

> Building Consensus with SGX and libp2p for Verifiable Data Integrity

[Devpost](https://devpost.com/software/enclavemesh) · hackathon [[OpenD-I- Shaping Data - Infrastructure for the next 10-20 Years]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** go, libp2p, mongodb, react, sgx

## How they structured the write-up

- inspiration:
- what it does
- architecture of enclavemesh:
- cryptography in enclavemesh:
- future improvements

## Body

Inspiration: Our inspiration stems from the ever-growing need for secure and decentralized networks. Recognizing the challenges in achieving consensus and maintaining data integrity, we envisioned EnclaveMesh as a pioneering solution that leverages Intel SGX and libp2p to create a robust, verifiable, and decentralized network.] What It Does EnclaveMesh is at the forefront of building consensus within a heterogeneous network, allowing nodes to securely hold both verifiable and regular data. Leveraging Intel SGX enclaves, we ensure the integrity of sensitive information by providing a secure enclave for data processing. EnclaveMesh stands out by delivering data verifiability without redundancy, maintaining the same speed as any centralized network. The utilization of libp2p, an industry-standard protocol, facilitates seamless peer-to-peer communication, enhancing decentralization and scalability. Architecture of EnclaveMesh: Secure Enclave Utilization: EnclaveMesh leverages the security features of Intel SGX enclaves to ensure the integrity and confidentiality of sensitive data processing. A key architectural element is the utilization of SGX's remote attestation, providing a robust mechanism to prove that the program is genuinely running inside an enclave. This attestation process establishes a trust relationship between nodes, enhancing the overall security of the network. Data Verifiability Mechanism: Within the secure enclaves, EnclaveMesh employs algorithms for data verifiability, ensuring that the information processed remains untampered. This mechanism, coupled with SGX's capabilities, allows nodes to trust the authenticity of the data shared within the network without the need for full data redundancy. libp2p DHT for Node Discovery: To facilitate peer-to-peer communication and node discovery, EnclaveMesh integrates libp2p's Distributed Hash Table (DHT). This industry-standard protocol allows nodes to dynamically discover and connect with each other in a decentralized manner. By using libp2p DHT, EnclaveMesh enhances the network's decentralization, scalability, and fault tolerance, creating a robust foundation for secure communication among nodes. Cryptography in EnclaveMesh: BLS Signature for Efficient Data Verification: EnclaveMesh employs BLS (Boneh-Lynn-Shacham) signatures as a cornerstone of its cryptography strategy to enhance the efficiency of data verification. BLS signatures offer a unique advantage by enabling the aggregation of multiple signatures into a single compact signature. This innovative approach significantly reduces computational overhead when verifying numerous signatures concurrently. Signature Aggregation Mechanism: The utilization of BLS signatures allows EnclaveMesh to aggregate signatures related to data from multiple nodes seamlessly. This aggregation not only streamlines the verification process but also conserves computational resources, making it particularly advantageous in a decentralized network where data verification is a frequent operation. Advantages of EnclaveMesh: Seamless Integration with Existing Codebase: EnclaveMesh is written in Go, a language known for its simplicity and efficiency. This design choice ensures seamless integration with xnode's existing codebase. The Go programming language's versatility and ease of use contribute to a smooth adoption process, allowing xnode to leverage EnclaveMesh's capabilities without extensive modifications. Zero Redundancy: EnclaveMesh takes a groundbreaking approach to data storage by eliminating redundancy. The network ensures data integrity without resorting to unnecessary duplication. This optimization not only conserves storage resources but also streamlines data processing, making EnclaveMesh an efficient and resource-conscious solution. Fully Verifiable Data in a Heterogeneous Mesh Network: EnclaveMesh excels in providing fully verifiable data within a heterogeneous mesh network. Leveraging advanced cryptographic techniques, such as BLS signature aggregation within SGX enclaves, the network achieves a level of data integrity that goes beyond traditional consensus mechanisms. This robust verification ensures the reliability of data across diverse nodes in the network. Support for All Types of Ingest: EnclaveMesh is designed to be versatile, accommodating all types of data ingest. Whether it's structured or unstructured, text or multimedia, the network embraces a wide range of data formats. This flexibility allows xnode to handle diverse data sources and types, making EnclaveMesh an ideal solution for comprehensive data processing needs. 100% Guarantee of Source and Timestamp: EnclaveMesh introduces a revolutionary feature by providing an unequivocal guarantee that data originates from a specific source at a precise time. Through the use of SGX enclaves and cryptographic techniques, the network ensures that the integrity of data is not only maintained but also verifiable, offering a level of trust and accountability that is paramount in decentralized ecosystems. Future Improvements Enhanced BLS Signature Mechanism: Optimize efficiency and security of BLS signature aggregation. Improve speed and reliability in verifying multiple signatures. Robust Codebase: Continuously refine the codebase for greater stability. Strengthen error handling and implement industry best practices. Frontend UI Enhancements: Overhaul the frontend user interface (UI) for improved user experience. Create a visually appealing and intuitive interface for seamless interaction. Diversification of Ingestion Methods: Introduce additional methods for data ingestion. Accommodate a broader spectrum of data sources and formats. <div