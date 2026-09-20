---
slug: "medisystem"
url: "https://devpost.com/software/medisystem"
title: "medisystem"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 505
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# medisystem

> making the communication for patient with the hospital a lot easier

[Devpost](https://devpost.com/software/medisystem) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** css, gemini, python, react, supabase, talwind, vercel

## How they structured the write-up

- 📱 android app
- 🧪 testing & setup guide
- 🧬 gemini-powered 3d anatomy
- 📡 connectivity & tunnels
- 🛠 tech stack

## Body

the android app or the patient portal MedicationSystem (MediHealth Global) Built: January 2025 Status: v0.1 - Active Development (UX Refinement in Progress) MedicationSystem is a next-generation clinical coordination platform designed to unify the workflows of Patients, Coordinators, Nurses, Doctors, and Hospital Administrators . It bridges the gap between patient reporting and clinical action using Gemini AI and high-fidelity 3D Bio-Anatomy . 📱 Android App The ecosystem includes a dedicated Android App for Patients/Users, allowing them to: Submit requests (Text/Voice/PDF) on the go. Track their medical journey and 3D diagnostics. Access their secure Pharmacy Wallet for QR-based medication pickup. 🧪 Testing & Setup Guide To test the full system, follow this end-to-end flow: 1. Hospital Creation & Staff Onboarding Create Hospital : Log in and register a new Hospital Node. Invite Staff : From the Hospital Admin dashboard, generate invite links for: Coordinator (Secretary) Nurse Doctor Connect : Once these users register via the invite, they are automatically linked to your hospital's private ecosystem. 2. The Clinical Journey (Example: ACL Injury) User Request : A user logs into the app/portal, selects your hospital, and submits a request: "I think I have an ACL injury." They can also attach a PDF medical report. Coordinator Triage : The Coordinator receives the request first. They review the AI urgency score and assign a Nurse and Doctor to the case. Nurse Intake : The Nurse opens the case, registers the patient's Vitals and Triage Notes , then passes the case to the assigned Doctor. Doctor Consultation : The Doctor reviews the clinical synthesis. 3D AI Analysis : If a PDF or text was provided and a Gemini API Key is in the .env , the system performs a deep analysis. Anatomical Mapping : The problem area (e.g., the Knee) is highlighted on the 3D Humanoid . Red areas indicate damaged tissue/bone as identified by the AI. 3. Pharmacy QR Flow After the consultation, the Doctor prescribes medication. The user receives a QR Code in their digital wallet. Dispensing : The pharmacist scans this QR code. Verification : Upon scanning, the pharmacist sees the Hospital Name , Doctor Name , and Exact Medication (Patient diagnosis remains private). 🧬 Gemini-Powered 3D Anatomy Automated Analysis : Gemini 1.5 Flash/Pro converts complex medical jargon into 3D mesh coordinates. Visual Diagnostics : Highlights specific parts (e.g., LegL: ACL , Vertebrae: L4 ) in red to represent pathology. Workflow Integration : Accessible by both the patient (for understanding) and the clinical staff (for precision). 📡 Connectivity & Tunnels [!IMPORTANT] For the real-time link between Users/Patients and Hospital Staff to function (especially when using the Android App or Vercel), the Backend Tunnel must be running . Run the tunnel in your terminal: lt --port 8001 --subdomain medical-hub-brain 🛠 Tech Stack Frontend : React + Vite (Vercel). Backend Logic : FastAPI (Python) + Gemini AI. Database : Supabase (PostgreSQL + RLS). Communication : Real-time subscriptions via Supabase. Note: Some UI components are currently being redesigned for enhanced clinical efficiency. We are still working on the final polish. <div