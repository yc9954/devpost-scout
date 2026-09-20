---
slug: "snacs-x-hypersdk"
url: "https://devpost.com/software/snacs-x-hypersdk"
title: "SNACS x HYPERSDK"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 793
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SNACS x HYPERSDK

> Snark accounts on hypersdk.

[Devpost](https://devpost.com/software/snacs-x-hypersdk) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** avalanche, gnark, groth16, hypersdk, snarks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- demo
- challenges we ran into

## Body

Inspiration There is a wide discussion on implementing Snark accounts on Celestia (a cosmos SDK chain) for interoperability of TIA between Celestia and rollups using Celestia for data availability. This made me research implementing Snark-based accounts, where proofs would be used as equivalent to signatures, proving key as the private key, and verifying key as the public key. What it does This project shows a way and makes the first implementation of Snark Accounts using Hypersdk for hyperchains. How we built it We have implemented a new auth type called SNACS in hypersdk. Hypersdk address is derived from verifying key. SNACS currently supports verifying the pre-image of the mimic hash circuit, but with some loosened assumptions, verification can be made independent of the circuit used to generate proofs. This auth type is used by users for generating and verifying proofs. type SNACS struct { VKey groth16.VerifyingKey `json:"vkey,omitempty"` Proof groth16.Proof `json:"proof"` addr codec.Address } This circuit defined in SNACS module. This circuit checks if the mimic hash of PreImage equals Hash in BN254 curve. type Circuit struct { PreImage frontend.Variable Hash frontend.Variable `gnark:",public"` } func (circuit *Circuit) Define(api frontend.API) error { mimc, _ := mimc.NewMiMC(api) mimc.Write(circuit.PreImage) api.AssertIsEqual(circuit.Hash, mimc.Sum()) return nil } While signing a transaction, the sha224 hash of the msg is mimic hashed. msg is the transaction digest (obtained with tx.Digest() ) sent while signing. As this auth module uses the BN254 curve for proof generation, msg should be its field element, but msg may be larger than 254 bits, so to keep it under 254 bits, we sha224 hash msg . func (s *SNACSFactory) Sign(msg []byte) (chain.Auth, error) { msgHash := sha256.Sum224(msg) hash := MimcHash(msgHash[:]) assignment := &Circuit{ PreImage: frontend.Variable(msgHash[:]), Hash: frontend.Variable(hash), } witness, err := frontend.NewWitness(assignment, ecc.BN254.ScalarField()) if err != nil { return nil, fmt.Errorf("error creating new witness: %s", err) } proof, err := groth16.Prove(s.CS, s.PKey, witness) if err != nil { return nil, fmt.Errorf("error generating proof: %s", err) } return &SNACS{Proof: proof, VKey: s.VKey}, nil } The Verification function logic defines the circuit-dependent or circuit-specific verification but holds the security guarantee. i.e the proof is somehow related to the msg. Our implementation of the verification function is circuit-specific, but this can be made circuit-independent if we avoid deriving public witness from msg (this is an extra check to verify if the proof corresponds to the public witness derived from the msg ). func (s *SNACS) Verify(_ context.Context, msg []byte) error { msgHash := sha256.Sum224(msg) hash := MimcHash(msgHash[:]) assignement := &Circuit{ PreImage: frontend.Variable(msgHash[:]), // preImage can be anything, as PreImage is not public input. But filling the field is necessary for the witness to be created Hash: frontend.Variable(hash), } witness, err := frontend.NewWitness(assignement, ecc.BN254.ScalarField()) if err != nil { return err } pubWit, err := witness.Public() if err != nil { return err } return groth16.Verify(s.Proof, s.VKey, pubWit) } Demo Launch Subnet The first step to running this demo is to launch your own morpheusvm Subnet. You can do so by running the following command from this location (it may take a few minutes): ./scripts/run.sh; When the Subnet is running, you'll see the following logs emitted: cluster is ready! avalanche-network-runner is running in the background... use the following command to terminate: ./scripts/stop.sh; By default, this allocates all funds on the network to morpheus1qrzvk4zlwj9zsacqgtufx7zvapd3quufqpxk5rsdd4633m4wz2fdjk97rwu . The private key for this address is 0x323b1d8f4eed5f0da9da93071b034f2dce9d2d22692c172f3cb252a64ddfafd01b057de320297c29ad0c1f589ea216869cf1938d88c9fbd70d6748323dbf2fa7 . For convenience, this key is also stored at demo.pk . Build morpheus-cli To make interacting with the morpheusvm easy, we implemented the morpheus-cli . Next, you'll need to build this tool. You can use the following command: ./scripts/build.sh This command will put the compiled CLI in ./build/morpheus-cli . Configure morpheus-cli Next, you'll need to add the chains you created and the default key to the morpheus-cli . You can use the following commands from this location to do so: ./build/morpheus-cli key import ed25519 demo.pk Next, you'll need to store the URLs of the nodes running on your Subnet: ./build/morpheus-cli chain import-anr ./build/morpheus-cli chain import-anr connects to the Avalanche Network Runner server running in the background and pulls the URIs of all nodes tracking each chain you created. Setup SNAC factory: for using an SNAC account, we need the factory to be initialised, The factory contains the proving key, verifying key and circuit constraints. ./build/morpheus-cli key generate-snacs copy the snac address. Send Tokens to the SNAC account Lastly, we trigger the transfer: ./build/morpheus-cli action transfer Send funds to the Snac Account Address copied previously. Make transactions from the SNAC account: transfer funds to morpheus1qqds2l0ryq5hc2ddps04384zz6rfeuvn3kyvn77hp4n5sv3ahuh6wgkt57y, using snac account ./build/morpheus-cli action transfer-snac Challenges we ran into It could have been better if there existed access to the state while verifying; this would have simplified circuit-independent verification. But, with the knowledge of recent advancements on hypersdk, removing state access makes sense. <div