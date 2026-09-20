---
slug: "oops-i-tapped-it-again"
url: "https://devpost.com/software/oops-i-tapped-it-again"
title: "Oops I Tapped It Again"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 1021
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/legal_professional"
  - "substrate/structured_db"
---

# Oops I Tapped It Again

> Tap the beat. Challenge your friends. Right on Snapchat!

[Devpost](https://devpost.com/software/oops-i-tapped-it-again) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[legal_professional]]
**substrate** [[structured_db]]

**stack** audio, leaderboard-component, lens-studio-5.0+, librosa, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oops i tapped it again

## Body

Tap the beat. Challenge your friends. Right on Snapchat! Devpost Submission Content Inspiration "What if you could compete with friends on a rhythm game, right in Snapchat?" We love rhythm games like Guitar Hero , Beat Saber , and Taiko no Tatsujin . The satisfying feeling of tapping to the beat and building combos is universally fun. When we saw the Play Everywhere: Build with Snap Games Lensathon , we knew this was the perfect opportunity to bring that experience to Snapchat—a platform with millions of users already sharing and competing with friends. Lens Studio caught our attention because of its powerful built-in components. The idea that we could build a complete game with leaderboards, social features, and instant sharing without a custom backend was exciting. What it does Oops I Tapped It Again is a rhythm-based mobile game where players tap falling notes in sync with the music. ♪ ♫ ♪ <- Notes fall from top | | | | | | [L][C][R] <- Tap when notes hit the zone! Key Features Feature Description 3-Lane Gameplay Notes fall in Left, Center, and Right lanes Precision Scoring Perfect, Great, Good, or Miss based on timing Combo System Chain hits for multiplier bonuses Friend Leaderboards Compete with your Snapchat friends Quick Sessions ~60 second songs, perfect for mobile Scoring System The score for each note is calculated based on timing accuracy: $$\text{Score} = \text{BasePoints} \times \text{TimingMultiplier} \times (1 + \text{ComboBonus})$$ Where the timing multiplier depends on how close the tap is to the target time: $$\Delta t = |t_{\text{tap}} - t_{\text{target}}|$$ Rating Timing Window Multiplier Visual Feedback Perfect < 50ms 1.0 Golden burst Great < 100ms 0.75 Blue glow Good < 150ms 0.5 White flash Miss ≥ 150ms 0 Red X How we built it Lens Studio served as our game engine, providing everything from 2D rendering to touch input to social features. We paired it with a Python-based offline tool for audio analysis. Architecture Overview ┌─────────────────────────────────────────────────┐ │ LENS STUDIO (CLIENT) │ ├─────────────────────────────────────────────────┤ │ Conductor → NoteSpawner → HitZoneManager │ │ ↓ ↓ ↓ │ │ SongLibrary.ts (Beatmap Data) │ │ ↓ │ │ Leaderboard Component (Built-in) │ └─────────────────────────────────────────────────┘ ⬇ ┌─────────────────────────────────────────────────┐ │ OFFLINE TOOLS (Python) │ ├─────────────────────────────────────────────────┤ │ generate_beatmap.py │ │ ├── Audio Analysis (librosa) │ │ ├── Beat Detection & Tempo Extraction │ │ └── Lane Assignment (spectral centroid) │ └─────────────────────────────────────────────────┘ Core Components Component Role Key Responsibility Conductor Timekeeper Tracks song position in beats NoteSpawner Spawner Creates notes at the right moment HitZoneManager Judge Detects taps and calculates scores SongLibrary Database Stores pre-generated beatmap data Beatmap Generation Pipeline Our Python tool transforms any audio file into a playable beatmap: Audio File (.mp3) ↓ ┌───────────────┐ │ librosa │ ← Audio analysis library └───────────────┘ ↓ ┌───────────────┐ │ Tempo Detection│ → 95.7 BPM detected └───────────────┘ ↓ ┌───────────────┐ │ Onset Detection│ → Find note positions └───────────────┘ ↓ ┌───────────────┐ │ Lane Assignment│ → Spectral centroid analysis └───────────────┘ ↓ SongLibrary.ts (79 notes generated) Beat Timing Conversion: Given a beat number $b$ and tempo in BPM, we calculate the exact timestamp: $$t = \frac{60 \cdot b}{\text{BPM}} + \text{offset}$$ Example: At 95.7 BPM, beat 10 occurs at $t = \frac{60 \times 10}{95.7} = 6.27$ seconds Lane Assignment via Spectral Centroid: The spectral centroid represents the "center of mass" of the frequency spectrum: $$C = \frac{\sum_{k=0}^{N-1} f_k \cdot |X_k|^2}{\sum_{k=0}^{N-1} |X_k|^2}$$ Centroid Value Lane Assignment Low ($C < 2000$ Hz) Left Medium ($2000 \leq C < 4000$ Hz) Center High ($C \geq 4000$ Hz) Right Challenges we ran into 1. Beat Sync Accuracy Problem: Notes weren't landing exactly on the beat. Solution: Account for travel time from spawn to hit zone: $$t_{\text{spawn}} = t_{\text{hit}} - \frac{d_{\text{travel}}}{v_{\text{note}}}$$ We spawn notes early so they arrive at the hit zone exactly when the beat occurs. 2. Lane Distribution Imbalance Problem: Spectral centroid analysis put ~70% of notes in the center lane. Before tuning: Left: ████ (12%) Center: ████████████████████████████ (72%) Right: ██████ (16%) After tuning: Left: ████████ (20%) Center: ████████████████████ (53%) Right: ██████████ (27%) 3. Note Spacing Problem: Too many notes felt overwhelming; too few felt boring. Solution: Added configurable minimum spacing between notes: if (currentBeat - lastBeat) >= minSpacing: addNote(currentBeat) 4. End-of-Song Timing Problem: Leaderboard appeared before the last note was hit. Solution: Added a 3-second buffer after the final note to ensure all notes clear the screen. Accomplishments that we're proud of "Zero backend, zero problems." Accomplishment Impact Original Art & Music Distinctive visual style and soundtrack created with AI tools Leveraged Lens Studio Built a complete game using the platform's built-in components Zero Backend Required Leaderboard Component handles scores, friends, and rankings Automated Beatmaps Python tool generates beatmaps from any audio in seconds Tight Sync Notes land precisely on beat—feels satisfying Clean Architecture Easy to add new songs (just add to SongLibrary.ts) What we learned Lens Studio Is a Game-Changer This hackathon opened our eyes to how powerful Lens Studio really is. What we thought would require weeks of backend development took just a few lines of code. We expected to build a backend for leaderboards. We didn't need to. What We Thought We Needed What Lens Studio Provided Custom score database Leaderboard Component User authentication Built-in Snapchat login Friend graph management Automatic friend rankings Score submission API submitScoreAsync() Share infrastructure Native Snapchat sharing The entire leaderboard integration: leaderboard.submitScoreAsync(score); leaderboard.show(); leaderboard.hide(); For a hackathon with a tight deadline, this was invaluable. We could focus on making the game fun instead of wrestling with infrastructure. Audio Analysis Key Insight: Pre-generated beatmaps are more reliable than real-time detection. Generating offline ensures perfect sync. What's next for Oops I Tapped It Again We're excited to explore more of what Lens Studio has to offer: Priority Feature Lens Studio Component High More Songs Additional audio assets High PvP Mode Sync Framework for real-time 1v1 battles Medium Custom Beatmaps Remote Assets for user-generated content Medium Visual Polish Particles, screen shake, more juice Low Song Library Remote Service Module for cloud storage The Sync Framework especially excites us—imagine challenging a friend to a head-to-head rhythm battle in real-time, right in Snapchat! Built for the Play Everywhere: Build with Snap Games Lensathon | Lens Studio, TypeScript, Python, librosa <div