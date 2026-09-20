---
slug: "elk-finance"
url: "https://devpost.com/software/elk-finance"
title: "Elk Finance"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 1011
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
---

# Elk Finance

> Developing cross-chain infrastracture for investors & businesses to move between blockchains. Our technology creates increased access to the DeFi landscape for investors, institutions, & developers.

[Devpost](https://devpost.com/software/elk-finance) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
  <sub>weak: web_dom</sub>

**stack** apis, cloudfare, go, html, javascript, python, rust, shell, solidity, typescript, vue, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for elk finance

## Body

Any chain, any where, any time™️ Inspiration The inspiration for Elk Finance arose after the team bore witness to the first scalability problems in 2016–2017. We realized that the situation would inevitably get worse in the future. Today, between the vast amount of blockchains being launched, we are starting to see significant fragmentation across chains, most of them are unable to communicate with each other. With this comes a very large interoperability problem. This is a problem we aim to solve, and that is why we founded Elk Finance in March 2021. What it does Elk Finance develops cross-chain infrastructure for investors and businesses alike to efficiently move between blockchains. Our technology stack results in an increase in accessibility in the decentralized finance landscape for investors, institutions, and developers. The ElkNet v2 cross-chain bridge allows you to move value and information between 20 blockchains (at the time of writing) at record speeds in a secure and decentralized manner. With the next iteration of ElkNet, v3, we aim to create a first-of-its-kind decentralized bridging and cross-chain communication protocol. Elk Finance aims to connect all EVM and non-EVM chains. Elk’s Bridge-as-a-Service (BaaS) SDK allows anyone to take their new token, existing token, or NFT cross-chain without having to worry about the various technicalities that different blockchains present. BaaS will also allow anyone to do cross-chain contract calls, mint cross-chain NFTs, or create a custom bridge that is robust and highly scalable. How we built it Baal and our talented team of developers have combined a multitude of products in our ecosystem. Products such as our Farming-as-a-Service, Cross-Chain Swaps, Bridging-as-a-Service SDK, ElkNet and its node infrastructure, ElkDEX, and ELK token are written in a variety of languages. For example, our smart contracts are written in Solidity, and will be written in other languages on non-EVM chains, and our node infrastructure will be written with a combination of Python and Go. Here is an example in Solidity of one potential implementation of our BaaS SDK for the creation of a token that is transferred and locked on the origin chain and is released on the destination chain. // SPDX-License-Identifier: BUSL-1.1 pragma solidity >=0.8.0; import "@openzeppelin/contracts@4.5.0/access/AccessControlEnumerable.sol"; import "@openzeppelin/contracts@4.5.0/access/Ownable.sol"; import "@openzeppelin/contracts@4.5.0/utils/math/Math.sol"; import "@openzeppelin/contracts@4.5.0/utils/math/SafeMath.sol"; import "@openzeppelin/contracts@4.5.0/token/ERC20/utils/SafeERC20.sol"; import "@openzeppelin/contracts@4.5.0/security/ReentrancyGuard.sol"; import "IReservoir.sol"; contract ReservoirLockExample is Context, AccessControlEnumerable, ReentrancyGuard, IReservoir { using SafeMath for uint256; using SafeERC20 for IERC20; /* ========== STATE VARIABLES ========== */ address override public tokenAddress; IERC20 public token; uint256 public txLimit; uint256 public constant REALM_ID = 0; bytes32 public constant OPERATOR_ROLE = keccak256("OPERATOR_ROLE"); /* ========== CONSTRUCTOR ========== */ constructor(address _tokenAddress, uint256 _txLimit) { tokenAddress = _tokenAddress; token = IERC20(_tokenAddress); txLimit = _txLimit; _setupRole(DEFAULT_ADMIN_ROLE, _msgSender()); } function available() override external view returns (uint256) { return token.balanceOf(address(this)); } function deposited(bytes32) override external pure returns (address, uint256) { revert(); } function withdrawn(bytes32) override external pure returns (address, uint256) { revert(); } function validateRealm(uint256 _realmId) override external pure returns (bool) { return _realmId == REALM_ID; } /* ========== RESTRICTED FUNCTIONS ========== */ function deposit(address _from, uint256 _amount, bytes32 _id) override external nonReentrant onlyRole(OPERATOR_ROLE) { require(_amount <= txLimit, "Reservoir::deposit: Cannot deposit amount larger than limit!"); require(_amount <= token.balanceOf(_from), "Reservoir::deposit: Not enough balance to deposit!"); token.safeTransferFrom(_from, address(this), _amount); emit Deposited(_from, _amount, _id); } function withdraw(address _to, uint256 _amount, bytes32 _id) override external nonReentrant onlyRole(OPERATOR_ROLE) { require(_amount <= txLimit, "Reservoir::withdraw: Cannot withdraw amount larger than limit!"); require(_amount <= token.balanceOf(address(this)), "Reservoir::withdraw: Not enough balance to withdraw!"); token.safeTransfer(_to, _amount); emit Withdrawn(_to, _amount, _id); } /* ========== EVENTS ========== */ event Deposited(address indexed from, uint256 amount, bytes32 id); event Withdrawn(address indexed to, uint256 amount, bytes32 id); } Challenges we ran into If cross-chain interoperability were easy, everyone would have been able to do it, and bridge exploits/hacks would be a thing of the past. The ElkNet, for example, needs to adapt to the needs of each specific blockchain. Some blockchains have many issues with RPC reliability, and each has its own gas mechanisms to which the ElkNet needs to adapt. This led to a large degree of testing with ElkNet v1, and addressing cross-chain concerns on-the-fly from users. This troubleshooting was very helpful, but required an immense amount of agility from our developers, community managers, and marketing teams. In the end, because we have security top-of-mind, we have not faced issues related to hacks or exploits. Not a single ELK token has been lost in a cross-chain transfer! Accomplishments that we're proud of We are proud of making the security of our cross-chain infrastructure the number one priority since inception. It is highly secure against exploits due to the various failsafe and security mechanisms built into our tech stack. More than 55 000 users have trusted Elk for their value transfer needs with over 352 000 cross-chain transfers to date. There has never been any downtime and no funds have ever been lost, and we intend to keep it that way. What we learned A lot of blockchains that have got extensive media attention (and audiences) have poor technology behind them and can not even deal with simple technological bottlenecks like building efficient RPCs. We have also learned that we made the right decision by not trying to rush unfinished products to the market just to be “early” and get our “hype share” of the bull run. We put a high emphasis on security and this can not be stated by the majority of our competition as 2022 has been an exceptionally bad year for most bridges due to exploits and hacks. What's next for Elk Finance Our inspiration comes from seeing the first blockchain scalability problems and realizing that this situation would likely get worse in the future. Today, the "race to scale" (among other races, e.g. to provide other features) for blockchains has led to significant fragmentation across chains. There are now hundreds of chains, most of them incompatible. We want to address that and, with it, make it easier for new users to adopt blockchain technology. Ultimately, our vision is to make it so that users don't have to think so hard about which chain they are on when interacting with blockchain applications. <div