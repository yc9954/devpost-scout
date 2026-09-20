---
slug: "affectlink"
url: "https://devpost.com/software/affectlink"
title: "AffectLink"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 1099
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# AffectLink

> AffectLink provides real-time multimodal emotion insights for tele-health with HP AI Studio. Uncovers hidden cues via facial, audio, & text analysis, boosting clinician understanding & patient care.

[Devpost](https://devpost.com/software/affectlink) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[sensor_telemetry]] [[transcript_audio]]

**stack** deepface, hp-ai-studio, hugging-face-transformers, librosa, mlflow, numpy, openai-whisper, opencv, python, pytorch, scipy, sounddevice, soundfile, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for affectlink

## Body

Affectlink's dashboard provides real-time multimodal emotion insights. It reveals hidden emotional cues via facial, audio, & text analysis. AffectLink's architecture: Real-time, local multimodal emotion AI. HP AI Studio deploys audio/text models; facial processing is local. MLFlow is used to log experiments and register models that can then be deployed to swagger. Models that are deployed using HP AI Studio can be easily accessed and interrogated using a Swagger API. HP AI Studio Project Story (Reworked) AffectLink: Bridging the Empathy Gap in Tele-Healthcare with Multimodal AI Inspiration The rapid shift to tele-health has brought convenience but also a significant challenge: how do clinicians truly understand a patient's emotional state when nuanced non-verbal cues are often lost through a screen? Traditional tele-health lacks the rich emotional context present in in-person interactions. This inspired AffectLink , a project aimed at empowering mental health professionals with deeper, data-driven insights into patient emotions during virtual sessions, ultimately improving care. What it does AffectLink is a real-time, local-first AI application designed to provide comprehensive emotional analysis by processing three key modalities: facial expressions, speech tone (audio emotion), and spoken content (text emotion) . Our core innovation, the Emotional Consistency Index (ECI) , synthesizes these independent emotional streams, highlighting when a patient's verbal message might diverge from their non-verbal cues. For example, a patient might say "I'm fine," but their facial expression or tone suggests underlying distress. AffectLink surfaces these critical discrepancies, acting as a powerful tool for clinicians to identify unexpressed emotions and guide their therapeutic approach. All processing occurs securely and locally on the HP workstation, ensuring patient privacy and HIPAA compliance. How we built it AffectLink was built from the ground up to showcase the power and security of HP AI Studio for real-time, on-device AI inference. Our technical workflow is as follows: Data Capture: Live video and audio streams are captured from the user's webcam and microphone. Orchestration ( main_processor.py ): This central component manages the overall pipeline, distributing data to specialized AI modules and aggregating their results. Facial Emotion Analysis: Video frames are sent to a Video Emotion Processor which utilizes DeepFace (running locally). While we aimed for full AI Studio integration, due to specific complexities encountered during the hackathon timeframe, DeepFace is currently executed directly via its Python library to detect and classify facial expressions in real-time on the local machine. Audio Processing: Audio chunks are sent to an Audio Pre-processor . This module prepares the audio for the deployed AI models. HP AI Studio Integration (Swagger API): This is a core highlight. Our Whisper (ASR) model for speech-to-text transcription, our Speech Emotion Recognition (SER) model for vocal tone analysis, and our Text Emotion model (for analyzing transcribed text) are all successfully registered and deployed locally via HP AI Studio's Swagger API . This ensures secure, high-performance, and on-device inference without cloud dependency for these critical AI components. Multimodal Fusion: The main_processor.py receives results from all modalities (facial, audio emotion, text emotion, and transcription). It then calculates the Emotional Consistency Index , providing a unified view of the patient's emotional state. Data Visualization (Streamlit): All processed data, including live video frames and emotion metrics, are written to local temporary files ( affectlink_emotion.json , affectlink_frame.jpg ). This method of inter-process communication was chosen for efficient real-time updates. The AffectLink Streamlit UI dashboard then reads these files, providing an intuitive, interactive display for clinicians. MLflow Tracking: Throughout the development process, MLflow was leveraged within HP AI Studio to track experiments, manage model versions, and log metrics, ensuring full reproducibility and control over our AI models. Challenges we ran into Real-time Performance: Balancing complex multimodal AI models with real-time performance on local hardware was a significant challenge. We optimized frame processing rates and experimented with different model sizes (e.g., Whisper 'tiny' or 'base'). Synchronization: Ensuring accurate synchronization between video frames, audio chunks, and their corresponding emotional analyses was crucial for the ECI. We implemented robust timestamping and buffering mechanisms. DeepFace Integration with AI Studio Deployment: We encountered integration complexities with the DeepFace library within the hackathon's compressed timeline. This led us to handle facial emotion analysis locally via direct Python library calls rather than deploying it via AI Studio's Swagger API like our other models. HP AI Studio Deployment: Configuring and deploying other models (ASR, SER, Text Emotion) to the local Swagger API within HP AI Studio required careful attention to environment dependencies and API endpoint definitions. Accomplishments that we're proud of Successful Local-First AI Deployment with HP AI Studio: We successfully registered and deployed our Whisper (ASR), Speech Emotion Recognition (SER), and Text Emotion models locally via HP AI Studio's Swagger API, demonstrating secure, high-performance, and on-device inference without cloud dependency. Novel Emotional Consistency Index (ECI): Developed and implemented the ECI to synthesize multimodal emotional streams, providing unique insights into discrepancies between verbal and non-verbal cues. Robust Real-time Multimodal Pipeline: Built a functioning real-time pipeline integrating facial expressions, speech tone, and spoken content analysis on local hardware. Effective Inter-process Communication: Implemented efficient local file-based communication for seamless data flow between AI processing modules and the Streamlit UI, achieving real-time visualization. Strong Privacy and HIPAA Focus: Delivered a "local-first" design directly addressing ethical concerns in healthcare AI by ensuring no sensitive patient data leaves the device. MLflow Integration: Leveraged MLflow within HP AI Studio for comprehensive experiment tracking, model versioning, and metric logging, ensuring reproducibility. What we learned Diverse Model Packaging Requirements: The DeepFace integration challenge reinforced our understanding of diverse model packaging requirements and the importance of a clear, iterative development process within HP AI Studio to overcome such hurdles. HP AI Studio Deployment Best Practices: We learned best practices for packaging models and managing their lifecycle within the platform, including the efficiency gains from consolidating audio-related models into a single environment. Optimization for Local Performance: Gained insights into optimizing frame processing rates and model sizes for real-time performance on local hardware. Ethical AI Design: Reinforced the importance of a "local-first" design as a key strategy for ensuring patient privacy and HIPAA compliance in sensitive AI applications like healthcare. What's next for AffectLink AffectLink has the potential to significantly impact the healthcare industry by providing clinicians with a vital "sixth sense" in tele-health. Beyond mental health, the multimodal analysis framework could be adapted for sales training, customer service, or even remote education, providing real-time feedback on emotional engagement and comprehension. Its secure, local deployment model makes it highly attractive for sensitive enterprise applications. Future enhancements could include exploring more advanced fusion techniques for the ECI, integrating more deeply with Electronic Health Records (EHR) systems, and potentially expanding to other biometric signals. <div