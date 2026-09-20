---
slug: "robo-jab"
url: "https://devpost.com/software/robo-jab"
title: "Robo Jab"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1214
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Robo Jab

> Phone video in, fighting humanoid robot out. We made a markerless mocap, sim-trained balance, deployed straight to a real 29-DoF Unitree G1.

[Devpost](https://devpost.com/software/robo-jab) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**domain** [[finance_payments]] [[housing_homeless]] [[transportation]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** bash, cuda, ffmpeg, gmr, gvhmr, hmr2, hugging-face, isaac-lab, mujoco, numpy, onnx, python, pytorch, runpod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what is next

## Body

GIF From phone video to gray-man capture to G1 robot, the full jab pipeline in one strip. GIF Trained policy tracking the jab in sim. Solid robot is the policy, ghost is the target. GIF Wrist velocity over one jab clip Inspiration We wanted to teach a Unitree G1 humanoid to throw a boxing jab without writing a single keyframe by hand. Motion capture suits are expensive and most reference motions for humanoids come from clean lab data, which does not look like how a real person actually moves. Our bet was simple: a phone camera and one sweaty person in leopard tights should be enough to drive a 29 degree of freedom robot. If we could go from a normal video to a trained policy, anyone could turn human movement into robot behavior. What it does The project is a full pipeline that takes ordinary monocular phone videos of a person jabbing and produces robot reference motions plus a trained control policy for the Unitree G1. The flow is: Record short clips of a jab on a phone. Run markerless motion capture to recover the 3D human body per frame. Retarget that human motion onto the G1 skeleton (29 joints). Export each clip as a reference CSV (root position, root rotation, joint angles). Validate every CSV, then render the robot and an overlay so we can eyeball quality. Train a multilayer perceptron (MLP) tracking policy on the reference motions and export it as an ONNX policy. The output is a batch of clean, validated jab references and a policy that makes the robot reproduce the motion. How we built it The core chain is GVHMR for markerless capture, GMR for retargeting, and an Isaac style tracking trainer for the policy. GVHMR turns each video into world grounded SMPL-X parameters. It runs YOLO for person detection, ViTPose for 2D keypoints, HMR2 for body shape, and the GVHMR network for world grounded recovery. GMR takes the SMPL-X motion and solves inverse kinematics to fit the G1, giving us joint angles per frame. A small exporter converts the retargeted pickle into the headerless CSV format the trainer expects, and a validator checks units, NaNs, foot contact, and frame count. We wrote a headless MuJoCo renderer that draws the robot only, with a camera that re-centers every frame, so the output video shows the motion clearly instead of the robot drifting off screen. Everything is wrapped in an idempotent batch script that processes around 122 clips, skips work that is already done, and stages every artifact (CSV, pickle, overlay video, robot video, side by side) into one output folder. Training ran on rented GPUs, producing checkpoints, a policy ONNX, and verification videos. All of this ran on a Windows laptop through WSL2 with a 8 GB RTX 4060, which forced us to be careful about memory the whole way through. Challenges we ran into 8 GB of VRAM broke the obvious plan.** The naive approach was to load GVHMR, YOLO, ViTPose, and HMR2 and run a clip straight through. Four models plus SMPL-X parameters does not fit on a 4060. We rewrote the flow to load one model at a time, run it to completion, dump its output to disk, free the GPU, and only then load the next stage. That turned a single function call into a staged pipeline with intermediate files between every step. It doubled the disk traffic, but it was the only way the clips ran at all. Numbers passed validation and the motion was still wrong. Our validator checks units, NaNs, foot contact, and frame count, and a clip can clear all four while the robot does something that looks nothing like a jab. A retarget that puts the wrist in the right place with the elbow folded backward is valid by every metric we wrote and useless on the robot. We only caught these by watching the render, so we stopped trusting the CSV and started trusting the video. The MuJoCo render itself fought us. The robot's root translates across the floor during a jab, so a fixed camera lets it walk out of frame within a second and the clip is unwatchable. We wrote a camera that recomputes its target from the robot's root every frame so the body stays centered while the motion still reads. Getting that re-centering to track the body without also cancelling the motion we wanted to see took more iterations than the capture code did. The overlay never lined up on the first try. GVHMR recovers a generic SMPL-X body, and that body is not the specific person in leopard tights, so projecting the recovered mesh back onto the original footage drifts at the shoulders and hips. The capture is correct in 3D and still looks wrong composited on 2D video, which sent us chasing a bug that was not a bug before we added an explicit alignment step for the overlay. Running the batch dozens of times surfaced its own problem. With around 122 clips and a laptop that needed sleep, any crash on clip 80 used to mean restarting from clip 1. We made the batch idempotent so it skips any clip whose artifacts already exist and stages every output, the CSV, pickle, overlay, robot render, and side by side, into one folder per clip. That script was not clever, and it saved us more time than anything clever did. Training had to leave the laptop, and finding a GPU to rent took some hunting. Nebius set us up with free credits, which was a real help going in. The catch was timing: the whole hackathon was reaching for GPUs at once, so the instances with enough VRAM to hold the policy and the reference batch kept coming back as unavailable whenever we tried to grab one. Rather than wait it out against the deadline, we moved the training setup over to RunPod and got a machine there. By the time checkpoints, the ONNX policy, and the verification videos came back, lining up the compute had been as much work as writing the code that ran on it. What we learned Validation catches format errors, not semantic ones. We added visual checks (overlay, global view, robot render side by side) because numbers alone lied to us. Off the shelf monocular capture is good but not perfect. The 3D body shape never fits one specific person exactly, so the overlay needs an alignment step if you want it to look right on top of the original footage. Small hardware changes the engineering. Most of our design decisions, from static camera mode to one model at a time scheduling, came from living inside 8 GB of VRAM. A boring, idempotent batch pipeline that puts everything in one folder is worth more than any single clever script, especially when you are re running it dozens of times under a deadline. What is next More motion types beyond the jab, better automatic quality scoring so bad clips get filtered without a human looking, and pushing the trained policy onto real hardware. The longer-term goal is medical: adapting the pipeline for surgery by focusing on precise wrist sensing and signaling, so a surgeon's fine hand motion can be captured from video and faithfully mimicked by a robot. <div