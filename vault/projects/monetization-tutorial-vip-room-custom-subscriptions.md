---
slug: "monetization-tutorial-vip-room-custom-subscriptions"
url: "https://devpost.com/software/monetization-tutorial-vip-room-custom-subscriptions"
title: "VIP Room & Custom Subscriptions - Monetization Tutorial"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 683
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
---

# VIP Room & Custom Subscriptions - Monetization Tutorial

> Tutorial on setting locked areas/rooms only accessible through either one-time purchases OR our custom monthly subscription system.

[Devpost](https://devpost.com/software/monetization-tutorial-vip-room-custom-subscriptions) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
  <sub>weak: video_visual</sub>

**stack** github, horizons, typescript, vim

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for monetization tutorial - vip room & custom subscriptions

## Body

Header Image Example of "Key" Subscription Item Gated Room Setting up "Key" Item Editor View Top of Tutorial Page Inspiration One of the most popular ways to monetize social experiences in other Metaverse platforms (like VRChat) is to create gated rooms/areas in worlds specifically for financial supporters as a reward. Because Horizon Worlds has built-in monetization already, we decided to create this tutorial to showcase how to create those sorts of "VIP Rooms" for in-world purchasers. The systems don't just apply to VIP Rooms either. They could be remixed for a variety of other creative purposes! The core inspiration is creating an easy-to-follow explanation for creating any type of gated content. What it does This tutorial has two different variations of creating monetization gating that a creator could choose to follow. 1. One-time Purchases In this model, players purchase an item that works as the unlock "key." When approaching the gated area, the door does a check for the item in their inventory. If the check passes, players may open the door. 2. Monthly Subscription Model This model works the same as the one-time purchase variation but marks the "key" item as consumable. The consumable item expires automatically after a set period of time, meaning after the expiration players would no longer pass the inventory check. Although we center the tutorial around the idea of VIP Rooms with locked doors, these methods can be customized to work in other scenarios as well. The "key" item could be any item creators choose. Same with the object containing the unlockable interaction. Our scripts are easy to copy and paste custom values into but are formatted for immediate plug-and-play on any gated content! How we built it We used the existing monetization system in Horizon Worlds and built our implementation around that. We started by creating two prop items. One got assigned "requiresKey" and the other as "keyItemSKU." From there we added the interaction callback and created the player "entitlement" system to see if they own the item. After that, we added the subscription-based model through auto-use consumables and persistent variables. We used the IWPSeller gizmo script for this as it provides a method to retrieve how long it's been since an item has been purchased. This works with variable groups to create the timed gated content system. Challenges we ran into Because there's no native subscription model available in Horizon Worlds' monetization features already, we had to get creative on ways to make this possible for players who want to purchase multiple months. There's no way to prevent players from buying multiple single-month subscriptions at a time, which initially seemed a massive problem that could potentially lead to players acidentally wasting money. To make sure buyers get their full money's worth, we found a way to make it so each subscription purchase stacks onto the total expiration time rather than just restarting a new 30-day period. Meaning with our model, buying 3 subscription items at once would give the item owner 90 days of access before expiration. Accomplishments that we're proud of Our tutorial is condensed, concise, and straight to the point for easy and quick creator implementation. We focus on guiding readers through the reasoning behind each step so they know exactly why they're using each script and what it's actually doing. It's super easy to follow, even for a complete monetization beginner with little to no programming knowledge. For slightly more proficient creators, our scripts are written to be clean and readable when it comes to easily implementing their own creative use case ideas! What we learned When it comes to money, you always have to value the customer experience first. Making sure the monetization process is completely seamless for purchasers is vital when asking for financial contributions. While creating this monetization tutorial, we learned how important it really is to deeply consider user experience in addition to the developer's setup experience as well. What's next for Monetization Tutorial - VIP Room & Custom Subscriptions If this tutorial does well, we'd love to continue making more just like it for other topics! <div