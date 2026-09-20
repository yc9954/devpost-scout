---
slug: "hyper-wasm"
url: "https://devpost.com/software/hyper-wasm"
title: "Hyper-wasm"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 703
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Hyper-wasm

> Stateful wasm runtime supported by hyper-sdk

[Devpost](https://devpost.com/software/hyper-wasm) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** avalanche, golang, hyper-sdk, rust, wasm, wazero

## How they structured the write-up

- inspiration
- what it does
- how we built it
- more info
- demos
- what's next for hyper-wasm

## Body

Inspiration The Ethereum virtual machine or evm is fine and is the first ever blockchain virtual machine. But evm, stack-based architecture has its own set of problems and restrictions. It does not support floats yet and is prone to multiple attack vectors because of its design. So, there is a necessity for altVMs to enable execution in any alt language like C, C++, Rust, Python, Java, PHP, Ruby, Javascript or any better language like MOVE. What it does Hyper-wasm is a stateful wasm runtime for executing wasm code. Programmes written in Rust, C, C++, C#, Java, Python, Go and so on can be compiled to wasm/web assembly. Hyper-wasm SDK is a rust SDK for writing hyper-wasm contracts. How we built it We used wazero, a zero dependency go runtime from tetrate labs, to write actions for our hypersdk. Merkle DB is interesting to work with, theoretically infinite storage at any node. We leveraged it to store our contracts. More Info Thread: Introducing Hyper-Wasm Rules Declare public functions as extern with C layout, e.g., pub extern "C" fn simplefunction() Use #[no_mangle] macro for external functions Ensure structs follow C layout, i.e., #[repr(C)] Public functions should use u/i/f/32/64 for input. Hyper-WASM communicates with Rust contracts using pointers due to WASM's limited support for data types (limited to u/i/f/32/64) memoryHex Usage in Hyper-WASM memoryHex is supported and writes to the zero pointer before transaction execution. Use cases for this behaviour should be explored. Hyper-WASM State Storage Hyper-WASM provides 32 slots for state storage, numbered 0 to 31. Hyper Wasm Sdk Hyperwasm SDK provides the necessary modules required for writing a contract. SDK |-- allocator |-- state |-- tx |-- utils Necessary declarations for contract use hyper_wasm_sdk::allocator::*; For state interactions use hyper_wasm_sdk::state::*; state |-- fn store_uint(slot: u32, x:u64); |-- fn store_int(slot: u32, x:i64); |-- fn store_float(slot: u32, x:f64); |-- fn store_string(slot:u32, ptr: u32, size: u32); |-- fn store_bytes(slot:u32, ptr: u32, size: u32); |-- fn store_append_array(slot:u32, ptr: u32, size: u32); |-- fn pop_array(slot:u32, position: u32, size: u32); |-- fn insert_array(slot:u32, ptr: u32, size: u32, position: u32); |-- fn replace_array(slot:u32, ptr: u32, size: u32, position: u32); |-- fn delete_array(slot: u32); |-- fn get_uint(slot: u32) -> u64; |-- fn get_int(slot: u32) -> i64; |-- fn get_float(slot: u32) -> f64; |-- fn get_string(slot: u32) -> u64; |-- fn get_bytes(slot: u32) -> u64; |-- fn get_array_at_index(slot: u32, size: u32, position: u32) -> u64; |-- fn CALL(); // ⚠️ not supported yet |-- fn DELEGATECALL(); // ⚠️ not supported yet During Output Output must always be u64. Left 32 bits represent the pointer, while the rest represent the size Example for Output // Get a pointer to MyStruct: let struct_ptr: *const MyStruct = &my_struct; // Extract the u32 value from the pointer: let u32_value: u32 = struct_ptr as *const _ as u32; // Calculate the size of the struct: let size_of_struct = mem::size_of_val(&my_struct); // Output Packing std::mem::forget(msg_sender); return ((ptr as u64) << 32) | len as u64; Function Inputs 0 inputs: Implies tx::info is not passed during the function call. 1 input: Implies tx::info is passed during the function call. 2 inputs: Implies tx::info is passed along with an input struct during the function call. During input For non-supported data types, provide inputHex Hyper-WASM writes it to contract memory and returns the pointer Use the pointer to access the desired data type Example for mutable and non-mutable structs sent during input // Immutable Struct: #[no_mangle] pub extern "C" fn immutable_struct_function(tx_info_ptr: *const tx::Info){ let tx_info = unsafe { &*tx_info_ptr }; } // Mutable Struct: #[no_mangle] pub extern "C" fn mutable_struct_function(tx_info_ptr: u32){ // Safety: Ensure that the input is not null if input.is_null() { //take necessary action or return an appropriate error code } // Safety: Dereference the pointer to access the struct let tx_info = unsafe { &mut *(tx_info_ptr as *mut tx::Info }; } Demos Build ./scripts/run.sh; ./scripts/build.sh; #build cli ./build/token-cli key import demo.pk ./build/token-cli chain import-anr Deploy Contract ./build/token-cli action deploy-contract Transact ./build/token-cli action transact What's next for Hyper-wasm We don't want to stop this as a hackathon project and wish to take it further. Todo: Separate Hyper-Wasm VM from tokenVM. Hyper-Wasm-Sdk standardisation and abstraction. Write reusable go components. Sample Smart contracts. Add support for crypto libraries. Functional MsgValue and contract balance. <div