---
slug: "descriptor-encrypt"
url: "https://devpost.com/software/descriptor-encrypt"
title: "descriptor-encrypt"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 1126
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
---

# descriptor-encrypt

> Efficiently encrypt any Bitcoin wallet descriptor with an identical access control policy

[Devpost](https://devpost.com/software/descriptor-encrypt) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]

**stack** rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for descriptor-encrypt

## Body

Inspiration Bitcoin wallet descriptors are a notorious pain point for users. Contrary to expectations, seed phrases are not always enough to recover one's funds. If a multisig or a more complex wallet is used, users must also back up the wallet descriptor in order to access their funds. The most common way to do so is to either store the descriptor in the cloud or print it out and store it alongside each seed phrase. The former is ill-advised, because cloud data can be deleted, and it can be difficult for heirs to find and access. The latter is also not ideal, because the descriptor is stored in plaintext, giving anyone with access to it (ex: an intruder) knowledge of the wallet's balance and activity. We can solve the privacy problem by encrypting the descriptor such that it can only be decrypted by a set of keys that can spend the funds. The encrypted data could then be privately stored alongside each seed phrase. Alternatively, it could be stored in public (on social media, on Bitcoin, etc.), so that users only have to back up their seed phrases and heirs can easily find it later. Earlier this year, I released a proof-of-concept ( multisigbackup.com ) that helps users encrypt and recover multisig descriptors by inscribing them on Bitcoin. It only supports legacy and segwit multisigs, however, and it lacks support for Taproot and miniscript. It also lacks a rust library that wallets can easily integrate. This project aims to generalize and standardize descriptor encryption, providing support for all descriptor types and miniscript. The library can be easily integrated into wallets, and it has a built-in command line tool. Users can encrypt and store their descriptor wherever they like (in the cloud, offline, on Bitcoin, etc.), with the assurance that the descriptor cannot be decrypted without access to a threshold number of public keys. What it does descriptor-encrypt is a rust library and command line tool that encrypts Bitcoin wallet descriptors such that only those who can spend the funds can recover the descriptor. Overview Security Mirroring : The descriptor's spending policy is analyzed and transformed into an equivalent encryption policy Recursive Secret Sharing : Shamir's Secret Sharing is applied recursively to split encryption keys following the script's threshold requirements Per-Key Encryption : Each share is encrypted with the corresponding public key from the descriptor, ensuring only key holders can access them Compact Encoding : Tag-based and LEB128 variable-length encoding is used to minimize the size of the encrypted data. Payload Extraction : Sensitive data, including the master fingerprints, public keys and xpubs, hashes, and timelocks, are extracted from the descriptor and encrypted. Template Extraction : The descriptor template and derivation paths remain visible in plaintext, allowing key holders to derive the necessary public keys and recover the full descriptor. Details Threshold-Based Security Model Threshold Authentication : The descriptor's access control policy (e.g., m-of-n multisig) automatically determines the decryption threshold Policy Mirroring : Encryption security policy directly mirrors the descriptor's spending policy - if a wallet requires 2-of-3 keys to spend, it will also require 2-of-3 keys to decrypt Cryptographic Implementation Deterministic Key Derivation : Master encryption keys are derived deterministically from the descriptor's structure and content Shamir Secret Sharing : Implements recursive Shamir's Secret Sharing to split the master encryption key according to the descriptor's threshold requirements Public Key-Based Access Control : Each share is encrypted with the corresponding public key from the descriptor ChaCha20-Poly1305 Encryption : Uses modern, efficient encryption for both the payload (ChaCha20) and the key shares (ChaCha20Poly1305) Complex Descriptor Support Full Descriptor Coverage : Supports all Bitcoin descriptor types including: Single sig (wpkh, pkh) Multisig (sorted, unsorted) Complex scripts (Miniscript expressions) Taproot descriptors with internal keys and script paths Nested Threshold Handling : Properly handles nested threshold conditions (e.g., an OR with AND conditions inside it) Time and Hash Lock Support : Maintains time locks and hash locks in the template while encrypting the specific values Template and Path Extraction Origin Path Extraction : Can extract derivation paths from encrypted descriptors without full decryption Template Generation : Can reveal the structure of an encrypted descriptor (with dummy values) without revealing the actual keys Compact Encoding Tag-Based Encoding : Uses tag-based encoding to minimize the size of the descriptor template Variable-Length Encoding : Uses LEB128 variable-length integers to minimize the size of the encrypted data This ensures that a descriptor can only be decrypted by the same keys needed to spend from it, creating a direct correspondence between fund access and descriptor recovery. How we built it This project is built as a rust crate with extensive testing. It has two sub-modules, one for encoding and decoding a descriptor into a template and payload, and one for encrypting and decrypting that payload from a descriptor and set of public keys. The master encryption key is derived deterministically from the descriptor data using Sha256. The project uses the rust-bitcoin and rust-miniscript libraries to parse, analyze, and encode Bitcoin descriptors. It uses chacha20 and chacha20poly1305 to perform encryption and decryption and implements recursive Shamir secret sharing to shard the master encryption key into shares that correspond to keys in the descriptor. Encryption starts by first decomposing a descriptor into a tree of nodes, where each node is either keyless, a key, or a child node. Satisfiable keyless nodes are then pruned, updating each threshold as if they were satisfied. The resulting tree consists of only keys, which is then used to recursively shard a master encryption key into shares. The library returns the encrypted data as raw bytes, which can be encoded to ASCII or stored directly. The command line interface returns the data encoded as Base64. Challenges we ran into This project requires extensive testing of the full range of possible descriptors, including miniscript. This proved somewhat challenging, as the range of descriptors and miniscript is incredible large. I solved this problem by decomposing encoding / decoding into the encoding / encoding of every class in rust-miniscript that composes a descriptor. Each class is then comprehensively tested, ensuring the full range of descriptors is covered. Accomplishments that we're proud of I'm proud of this project's ability to cover the full range of descriptors, and I'm particularly proud of how extensively it is tested. What we learned I learned how to use the rust-miniscript library and how to write a rust library from scratch. What's next for descriptor-encrypt I plan to share this library with the broader Bitcoin community, and I hope it can form the basis for a standard that can be integrated into wallets. Future development plans include a web app to encrypt and decrypt and an indexer or a nostr / twitter bot to make it easy to store and recover. <div