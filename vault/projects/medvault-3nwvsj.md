---
slug: "medvault-3nwvsj"
url: "https://devpost.com/software/medvault-3nwvsj"
title: "MedVault"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1480
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/genomic_bio"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MedVault

> Encrypted health records in your pocket. Share with any doctor in 10 seconds, in any language. Works even when you can't speak.

[Devpost](https://devpost.com/software/medvault-3nwvsj) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[structural_withholding]]
**domain** [[finance_payments]] [[health_clinical]] [[labor_employment]] [[supply_logistics]] [[transportation]]
**user** [[clinician]] [[frontline_worker]] [[patient_family]]
**substrate** [[document_pdf]] [[genomic_bio]] [[medical_record]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** react, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- tech stack
- what's next

## Body

Landing Page Emergency Share Profile MedVault Wallet Card Inspiration It started with a question I couldn't stop thinking about. A close family member was rushed to the emergency room while travelling abroad. Unconscious. Phone locked. No medical history on them. The ER doctors didn't know about the blood pressure medication they were on, or that combining it with the sedative they were about to administer could cause a dangerous drop in blood pressure. We got lucky. Someone remembered and called ahead in time. But I kept thinking — what if nobody had called? What if they were travelling alone? What if the hospital was in a country that spoke a different language? What if there was nobody to call? The more I looked into it, the more I realised this wasn't a rare edge case. It is the default state of emergency medicine. Medical errors are the third leading cause of death in the United States — responsible for over 251,000 deaths annually . Poor communication and incomplete patient information are contributing factors in over 60% of all hospital adverse events (The Joint Commission). The information exists. Lab results, prescriptions, allergy records — patients have them somewhere. The problem is that there is no reliable way to get that information to a doctor who has never seen the patient before, in the first 60 seconds of an emergency, without requiring the patient to be conscious and cooperative. That is the problem MedVault is built to solve. What It Does MedVault is a zero-knowledge, end-to-end encrypted health record platform. Patients store their medical documents in an encrypted vault, and can share them with any doctor in the world — in seconds, in any language — even when unconscious. The core flow: Patient uploads lab results, prescriptions, and vaccine records. Everything is encrypted with AES-256-GCM in the browser before it touches our servers — we store only ciphertext. Patient prints a wallet card — credit-card sized, kept behind their driver's licence. Front: name and a QR code. Nothing else. In an emergency, a paramedic or ER doctor scans the QR. It opens instantly in any browser — no app, no account, no login . The doctor selects their language. AI generates a structured clinical summary — blood type, allergies, medications, conditions, emergency contacts — in under 10 seconds. For full document access, the patient (or a bystander) generates a time-limited QR from the Emergency Share screen. The doctor's browser decrypts the original files , not summaries or screenshots. Access expires automatically. Every scan is permanently logged in an immutable audit trail — who accessed, when, and in which language. What a Doctor Sees After Scanning the Wallet Card PATIENT: Sarah Chen, 34 BLOOD TYPE: A+ ⚠ CRITICAL ALERTS • Severe sulfa drug allergy — do NOT administer sulfonamides • Currently on warfarin — elevated bleeding risk ACTIVE CONDITIONS • Atrial fibrillation (diagnosed 2023) CURRENT MEDICATIONS • Warfarin 5mg daily · Metoprolol 25mg twice daily EMERGENCY CONTACT • James Chen (Husband) · +1 (212) 555-0147 No app. No account. No phone unlock. No language barrier. No guesswork. How We Built It Frontend Built with React 18 + TypeScript + Vite . TailwindCSS for styling with CSS variables for automatic dark/light mode. Every cryptographic operation happens client-side — the server is never involved in any key material. Encryption Architecture All encryption uses the Web Crypto API — browser-native, hardware-accelerated, no third-party crypto libraries, no supply chain risk. $$\text{MasterKey} = \text{PBKDF2-SHA256}(\text{password}, \text{salt}=\text{userId}, \text{iterations}=100{,}000)$$ Each document gets its own AES-256-GCM key, which is then wrapped (encrypted) with the master key and stored in the database. The master key itself never leaves the browser. For emergency shares, an ephemeral share key is generated per session and embedded in the URL fragment ( #key=... ). URL fragments are never transmitted in HTTP requests by specification — the server literally cannot see the key. $$\text{ShareKey} \rightarrow \text{base64} \rightarrow \text{/doctor/:token#key=}$$ The ciphertext goes to the server. The key never does. Backend Supabase — PostgreSQL with Row Level Security on every table, Storage for encrypted blobs, and Auth with JWT. RLS enforces data isolation at the database layer, not in application code. AI Features Google Gemini 3 Pro powers three distinct features: 1. Multilingual Clinical Summary (DoctorView) The doctor's browser decrypts the documents, then sends the decrypted base64 content directly to Gemini with a prompt specifying the target language. The AI reads the actual original documents — not summaries — and produces a structured clinical brief in 15 languages. 2. Lab Biomarker Extraction (Health Metrics) When a patient uploads a lab result, Gemini extracts all numeric biomarkers (HbA1c, cholesterol, haemoglobin, eGFR, and 20+ others) along with values, units, reference ranges, and status. Results are cached in the health_metrics table — Gemini runs exactly once per document , never again. $$\text{Biomarkers} = f_{\text{Gemini}}(\text{decrypt}(\text{doc})) \rightarrow {(\text{name} i, v_i, \text{unit}_i, \text{status}_i)} {i=1}^{n}$$ 3. Permanent Card AI Summary (MedicalIDCard) The permanent wallet card page generates a clinical summary purely from the patient's profile data — no document decryption needed. This is what appears when a paramedic scans the wallet card without a full emergency share active. Permanent Wallet Card The card is exported as a print-ready PNG using the browser's native Canvas 2D API — no html2canvas, no server, no external dependencies. Front: patient name and QR code only. Back: instructions for medical professionals. Rendered at 1011×638px (ISO credit card dimensions at 300dpi). Access Audit Trail Every scan of every QR token writes an immutable row to scan_logs with timestamp and language used. The Emergency page groups these by token, detects first vs. repeated access, and shows whether each token is still active or has expired. Patients see exactly who has viewed their records. Challenges We Faced 1. The Supabase Client Deadlock The most subtle bug of the entire project. When making Supabase database calls inside onAuthStateChange , the client deadlocks — the auth listener blocks the same connection pool the DB query is waiting on. The symptom was a loading screen that hung forever after login with no error in the console. The fix was a setTimeout(0) to push the DB call outside the listener's execution context — letting the event loop clear the auth callback before the query runs. One line. Four hours to find. 2. Stale Closure in the Language Switcher The generateDoctorSummary function is async and closes over selectedLang at creation time. When a doctor changed the language and re-ran the summary, the old closure still held the previous language code — so the AI summary silently came back in the wrong language with no error. The fix was pairing useState with a useRef that is updated synchronously before state is set. The async function reads from the ref (a mutable object outside the closure) rather than the state variable. // State for UI rendering const [selectedLang, setSelectedLang] = useState<LangCode>("en"); // Ref for async functions — always current, never stale const selectedLangRef = useRef<LangCode>("en"); // In the picker onClick: selectedLangRef.current = lang.code; // synchronous — happens immediately setSelectedLang(lang.code); // triggers re-render What We Learned Zero-knowledge architecture is a design constraint, not a feature. Every product decision had to be evaluated against it. Can the server see this? If yes, why? Is there an alternative where it can't? This discipline produced a cleaner, more honest product. The real problem in healthcare technology is not AI or encryption — it is trust. Doctors don't trust patient-provided summaries because patients control what they share. MedVault's most important property is that the doctor decrypts the original file — the patient had no opportunity to modify it after upload. That chain of custody is what makes the system trustworthy, not the feature set. Gemini is remarkably capable across African languages. The quality of clinical summaries in Yoruba, Hausa, and Igbo was comparable to English. This was genuinely surprising and matters enormously — the language gap between patients and doctors in West Africa is one of the largest barriers to quality emergency care, and it turns out AI can close it. Browser cryptography has matured enough to build production systems. The Web Crypto API handles everything MedVault needs — AES-GCM encryption, PBKDF2 key derivation, key wrapping — without any third-party libraries. No npm packages means no supply chain risk for the most security-critical part of the application. Tech Stack Frontend React 18, TypeScript, Vite, TailwindCSS Backend Supabase (PostgreSQL, Storage, Auth, RLS) Encryption Web Crypto API — AES-256-GCM, PBKDF2-SHA256 AI Google Gemini 2.5 Flash Preview Charts Recharts QR qrcode (npm) PDF jsPDF Deploy Vercel What's Next FHIR R4 import — pull records directly from hospital EHR systems NFC wristband — write permanent card URL to a £1 NFC sticker, tap to open on any phone Offline vault — service worker caches encrypted documents for areas with no connectivity Next-of-kin delegation — trusted person can generate emergency QR on the patient's behalf Built solo for FrostByte Hackathon 2026. <div