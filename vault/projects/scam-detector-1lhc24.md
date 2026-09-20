---
slug: "scam-detector-1lhc24"
url: "https://devpost.com/software/scam-detector-1lhc24"
title: "VoxShield"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 1359
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# VoxShield

> "Unmasking AI voice scams through sound." VoxShield flags AI-generated voices from a single audio clip and, for verified human speech, profiles the speaker's English accent, all in one report.

[Devpost](https://devpost.com/software/scam-detector-1lhc24) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[structural_withholding]]
**domain** [[finance_payments]] [[health_clinical]] [[media_journalism]] [[security_privacy]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[transcript_audio]]
  <sub>weak: financial_record</sub>

**stack** cloud-run, cloud-storage, deep-learning, docker, firebase, google-cloud, google-colab, huggingface, librosa, machine-learning, numpy, python, pytorch, torchaudio

## How they structured the write-up

- problem statement
- solution overview
- key features
- technologies used
- target users
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voxshield

## Body

Test with renamed file test-1 from Australian Human Voice Example-1 Correct result: Australian Human Voice (renamed to test-1) Test using with synthetic file-1 Correct result: Synthetic Sound (synthetic sound-1) Test with US human Voice Correct Result: Human sound with US accent Test with Indian Voice Correct Result: Human sound (Indian test) Correct Result: Indian accent English Test using with Synthetic file-2 Correct Result: Synthetic sound (synthetic sound-2) Test with Australian Voice file (without renamed) Correct Result: Australian Human voice-2 Test with Chinese-accented English voice Correct Result: Chinese-accented Human English Voice Problem Statement As AI voice synthesis and voice cloning improve, it has become genuinely hard to tell whether a voice on a phone call belongs to a real person or to a machine. Voice phishing, impersonation, and financial fraud actively exploit that gap, and victims act on the assumption that they are speaking to someone real. Investigators who receive a suspicious recording face the same problem, and existing tools force them to choose. Deepfake detectors answer the authenticity question but say nothing about the speaker. Accent analysis tools describe the speaker but assume the input is already a genuine human voice. Nothing brings the two answers together in one confidence-scored report. That gap is what inspired VoxShield. We wanted to build more than a demo classifier, and from the start we committed to treating accent responsibly, as a pronunciation pattern for security triage and never as a claim about someone's nationality. Solution Overview VoxShield analyzes an English voice recording using a single WavLM-base backbone carrying two lightweight classification heads that run in parallel . The detection head returns a binary judgment of whether the clip is human or AI-generated, with a confidence score. The accent head returns a probability distribution over six English accent groups (U.S., U.K., India, Canada, China, Australia). Because both heads share one backbone, the heavy feature extraction runs only once, which keeps inference fast and the model compact. The two outputs are merged into a single investigation-support report . Accent results appear only when the clip is verified as human , because accent estimates carry no meaning for AI-generated speech. A synthetic clip is simply flagged as high risk. Crucially, the accent output represents pronunciation similarity, not nationality or identity . Try it yourself: live demo · demo video · source code Key Features Synthetic speech detection. Determines whether a recording is a real human voice or AI-generated, and returns a confidence score rather than a bare label. Accent profiling. For verified human speech, produces a probability distribution across six English accent groups. One backbone, two heads. Both tasks reuse a single WavLM representation, so one forward pass yields both answers. Human-only gating. Accent output is withheld for synthetic audio, preventing a meaningless result from being read as evidence. Integrated report. Authenticity verdict, accent profile, and confidence scores are delivered together in one output. Web demo. Upload a clip in the browser and see the full report, no setup required. Technologies Used Language and ML framework Python 3.12 PyTorch Hugging Face Transformers Model WavLM-base, fine-tuned end to end Two linear classification heads (binary and six-class) Audio processing librosa torchaudio NumPy Cloud infrastructure (Google Cloud Platform) Vertex AI Custom Training for model training Vertex AI Model Registry for version management Cloud Storage for datasets and model artifacts Cloud Run for model serving Web interface Firebase Development environment Google Colab, Visual Studio Code, Docker Datasets ASVspoof 2019 LA GLOBE Speech Accent Archive (SAA) Target Users VoxShield is built for fraud and security teams triaging suspicious call recordings, for call-center agents who need a quick synthetic-voice flag before acting on a caller's request, and for investigators who need a confidence-scored, explainable report rather than a single opaque verdict. More broadly, anyone who receives a suspicious call benefits from a way to check whether the voice on the other end is real. How we built it Data. For synthetic detection we assembled a balanced 70,000-clip set (35,000 real and 35,000 fake), drawing synthetic speech from ASVspoof 2019 LA. For accent profiling we curated 30,000 clips from GLOBE and the Speech Accent Archive, covering six accent groups at 5,000 clips per class and spanning 3,756 unique speakers. Everything was unified to 16 kHz mono , with speaker-independent, stratified 70/15/15 splits to prevent speaker leakage and preserve class balance. Model. A single WavLM-base self-supervised speech model is fine-tuned end to end. It takes the raw waveform and aggregates frame-level features through mean pooling into an utterance-level representation. Two linear heads sit on top, one binary for human versus synthetic and one six-class for accent, trained jointly. Outputs. The detection head yields the synthetic probability, and the accent head yields the six-class distribution. The report merges both and suppresses the accent profile whenever a clip is flagged synthetic. Deployment. We trained on Google Cloud Vertex AI, stored datasets and model artifacts in Cloud Storage, registered versions in the Vertex AI Model Registry, served the model through Cloud Run, and built a Firebase web interface for audio upload and result delivery. Challenges we ran into The first challenge was making the project more meaningful than an accent classifier , so we unified synthetic detection and accent profiling onto one shared backbone, producing both signals from a single pass. A deeper challenge was data composition . Our human speech came largely from accent corpora while the synthetic examples came from ASVspoof, so we had to ask whether the model was learning genuine spoofing cues or merely recording-domain differences. We unified preprocessing through resampling and silence trimming to narrow that gap, and we treat it as an open risk rather than a solved problem. We also faced an ethical challenge. We did not want the system to infer nationality from a voice, so the accent output is framed strictly as pronunciation similarity for security purposes, and it is withheld entirely for synthetic audio. Finally, choosing the representation mattered . We moved from hand-crafted spectrogram features toward self-supervised WavLM representations for stronger generalization. Accomplishments that we're proud of We're proud that VoxShield turns a simple accent-classification idea into a practical voice-security system built on one efficient model. On our held-out test set: Synthetic detection : EER 4.10% , F1-score 95.9% , balanced accuracy 95.9% Accent profiling : Macro F1 70.3% across six classes, where chance level is 16.7%, with India highest at 80.5% and U.S. lowest at 65.4% Integrated system : accuracy 84.18% , Macro F1 84.08% Most of all, we're proud of building an explainable and responsible system. Instead of a single opaque verdict, VoxShield surfaces the synthetic probability, the accent distribution, and the confidence behind each result, while deliberately avoiding any claim about a speaker's identity or nationality. What we learned We learned how to process and model audio with self-supervised speech models such as WavLM, how a shared backbone with task-specific heads lets two related problems reuse one representation, and why threshold-independent metrics like EER matter for security tasks. We learned the importance of data rigor . Early on, a random split let the same speaker appear in both training and evaluation data. The resulting scores looked excellent but meant nothing, because the model had memorized speakers rather than learning speech characteristics. Moving to a speaker-disjoint split lowered our numbers and made them trustworthy. And we learned that AI projects should optimize not only for accuracy but for real-world impact, fairness, and responsible use . Because voice and accent are sensitive human characteristics, the system had to be designed carefully so that it helps users without making unfair assumptions. What's next for VoxShield Next, we plan to train VoxShield on larger and more diverse deepfake voice datasets and newer TTS and cloning attacks, and to add more real-speech domains so the model learns genuine spoofing cues rather than recording conditions. We want to broaden accent and language coverage , close the per-class gap where U.S. accent is currently our weakest class, tune the decision threshold and audio-segment lengths, and keep evaluating with EER, Accuracy, and Macro F1. Longer term, VoxShield could become a real-time, streaming call-warning system , piloted with fraud and investigation teams and continuously retrained as new spoofing methods emerge. <div