---
slug: "volume-vengeance"
url: "https://devpost.com/software/volume-vengeance"
title: "Volume Vengeance"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 577
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
---

# Volume Vengeance

> Volume Vengeance is a fast, solo-or-co-op horde shooter for Horizon Worlds where googly-eyed cubes, spheres, and other low-poly primitives swarm vibrant arenas.

[Devpost](https://devpost.com/software/volume-vengeance) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[multi_agent]]

**stack** typescript

## Body

Inspiration I wanted a remix-first horde shooter that feels great out of the box and invites other creators to put their own spin on it. The hook was charming, low-poly “googly-eyed” primitives—cubes, spheres, capsules—set against bright arenas so readability stays high even when chaos erupts. From the start I optimized for clarity, snappiness, and moddability: clean HUD, pooled FX, and a simple event contract so anyone can swap weapons, enemies, and waves without surgery. What I Built Dynamic spawn-ring director that orbits the active play area (centroid/leader modes) and continuously places spawn points with jitter to avoid clumps. Enemy framework with pooled lifecycle, knockback-aware movement, and “far-distance catch-up” so combat recenters quickly. Weapons stack (WeaponBase → melee/gun/utility) handling cross-device inputs, two-hand support, holstering, and networked damage. Readable UI/HUD (wave timer, health, ammo) with conditional visibility—nothing extra on screen before a match starts. Pooled FX & curved damage numbers for feedback that stays smooth under heavy load. Creator-friendly events (damage, spawns, FX, game state) to treat the project as a template for remixes. How I Built It Architecture. I separated systems (spawning, pooling, weapons, UI) and made them talk via events rather than tight coupling. This keeps the “remix surface” large. Pooling everywhere. Enemies, particles, audio, floating text—prewarmed and reused to avoid spikes. Device-aware inputs. One path for VR/Desktop/Mobile so creators don’t wrestle with controls. Data-driven tuning. Most difficulty knobs live in props/params, not code: wave pacing, ring radius, enemy mixes, SFX/FX options. A tiny taste of the math that guides pacing Spawn ring growth over time: 𝑅 ( 𝑡 ) 𝑅 0 + 𝛽 𝑡 R(t)=R 0 ​ +β t ​ which gently widens the arena pressure without sudden difficulty cliffs. Enemy budget by player count 𝑁 N and elapsed time 𝑡 t: 𝐵 𝐵 0 + 𝑘 𝑁 + 𝛼 𝑡 B=B 0 ​ +kN+αt balancing co-op scaling with minute-to-minute intensity. Catch-up velocity when an enemy is punted too far: 𝑣 desired 𝑣 0 ⋅ ( 1 + 𝑠 ⋅ clamp01 𝑑 − 𝑑 0 𝑑 max ⁡ − 𝑑 0 ) v desired ​ =v 0 ​ ⋅(1+s⋅clamp01 d max ​ −d 0 ​ d−d 0 ​ ​ ) so extreme knockbacks don’t turn into downtime. What I Learned Readability beats raw effects. Big shapes + consistent silhouettes let me push enemy counts without losing clarity. Events are the remix API. A small, reliable set of broadcasts (damage, state, FX) empowers creators more than monolithic managers. Holstering/attachables matter. Correct avatar-attach flags and slot poses solved a surprising number of “why did my weapon drop?” issues. Guard rails prevent heisenbugs. Clamping velocities, validating UI children, and isolating pooled gizmos eliminated NaN explosions and phantom UINodes. Challenges I Faced (and how I solved them) UI initialization errors (View children not UINodes): added strict guards and early returns during HUD boot. Physics NaNs after big knockbacks: added out-of-bounds clamps and a zero-velocity or ramped catch-up path beyond a distance threshold. Script/version conflicts: standardized component names and ensured only one active version loads to avoid “different version already loaded.” Holster/pose weirdness: enforced Avatar Attachable settings and per-slot default offsets; simplified the holster rules to three clear slots. Why it’s Remix-Ready Swap the art, keep the contract. Replace shapes, SFX, and materials—events stay the same. Tune without recompiling. Wave mixes, ring size, pacing, and weapon feel live in props. Extend by subclassing. Add a new enemy or weapon with a few overrides; everything else (HUD, FX, pooling) just works. <div