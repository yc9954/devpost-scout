---
slug: "medocr-vision-medical-document-ocr-with-paddleocr-vl"
url: "https://devpost.com/software/medocr-vision-medical-document-ocr-with-paddleocr-vl"
title: "MedOCR-Vision: Medical Document OCR with PaddleOCR-VL"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 693
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MedOCR-Vision: Medical Document OCR with PaddleOCR-VL

> Fine-tuned PaddleOCR-VL for medical documents - achieving superior text extraction from prescriptions, lab reports, and medical forms while maintaining general OCR capabilities.

[Devpost](https://devpost.com/software/medocr-vision-medical-document-ocr-with-paddleocr-vl) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[graph_reasoning]] [[vision_ocr]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[medical_record]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** datasets, ernie, huggingface, lora, modal, novita, paddleocr-vl, pandas, peft, python, pytorch, transformers, unsloth

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges i faced
- impact & future work

## Body

Inspiration The healthcare industry generates millions of medical documents daily—prescriptions, lab reports, and medical forms—most of which remain locked in paper or image formats. Healthcare professionals waste countless hours manually transcribing these documents, leading to delays in patient care and potential errors. I was inspired to tackle this challenge after witnessing the inefficiencies in medical document digitization and recognizing the potential of vision-language models to transform this process. What I Learned This project was a deep dive into domain-specific fine-tuning and production-ready ML engineering : Domain Adaptation : I learned that successful medical OCR requires more than just accuracy—it needs to understand document structure and maintain context. The continuous text output format proved superior to line-by-line extraction for downstream medical NLP tasks. Data Quality Over Quantity : Curating a balanced dataset of 2,462 high-quality samples (59.4% medical, 40.6% general) proved more effective than using larger, unbalanced datasets. This balance prevented catastrophic forgetting while specializing the model for medical documents. Parallel Processing at Scale : Implementing multi-provider parallel processing with Nebius and Novita APIs reduced dataset preparation time, demonstrating the importance of infrastructure optimization in ML workflows. Evaluation Methodology : Building comprehensive evaluation metrics revealed that my fine-tuned model achieved significant improvements in information extraction, header capture, and medical terminology recognition compared to the base model. How I Built It Phase 1: Dataset Curation I assembled a domain-balanced dataset from four sources: Medical Prescriptions (1,000 samples): Direct extraction from existing annotations Medical Lab Reports (426 samples): Parallel LLM-based text extraction using multiple API providers OMR Scanned Documents (36 samples): LLM-based processing for complex forms Invoices & Receipts (1,000 samples): General domain data to prevent overfitting The dataset was split 80/10/10 for training, validation, and testing, ensuring representative coverage across document types. Phase 2: Model Fine-tuning Using LoRA (Low-Rank Adaptation) , I fine-tuned the PaddleOCR-VL (1B parameters) model with carefully optimized hyperparameters: $$\text{Effective Batch Size} = \text{per_device_batch_size} \times \text{gradient_accumulation_steps} = 4 \times 2 = 8$$ Training Configuration Learning Rate : 5e-5 with linear warmup LoRA Parameters : Rank (r): 64 Alpha (α): 64 Dropout: 0 Training Duration : 3 epochs (~738 steps) on NVIDIA L4 GPU Optimization : AdamW (8-bit) with mixed precision (BF16/FP16) Phase 3: Evaluation & Validation I developed a comprehensive evaluation framework comparing the fine-tuned model against the base model across multiple dimensions: Information extraction completeness Medical terminology accuracy Document structure understanding Content coverage metrics The results demonstrated clear, measurable improvements across text output quality, test value extraction, and reference range capture. Challenges I Faced 1. Data Annotation Bottleneck Challenge : Medical lab reports lacked ground truth annotations. Solution : Implemented parallel LLM-based text extraction using multiple API providers (Novita, Nebius), reducing processing time by 3x through concurrent API calls. 2. Domain Balance vs. Specialization Challenge : Balancing medical specialization without losing general OCR capabilities. Solution : Carefully curated a 60/40 medical-to-general ratio, validated through iterative testing to ensure the model maintained versatility while excelling at medical documents. 3. Output Format Design Challenge : Deciding between line-by-line extraction vs. continuous text output. Solution : After analysis, I chose continuous text format as it better preserves semantic context and proves more useful for downstream medical NLP tasks like summarization and entity extraction. 4. Training Efficiency Challenge : Limited GPU resources and training time constraints. Solution : Leveraged LoRA for parameter-efficient fine-tuning, reducing memory requirements from 24GB to ~12-16GB while maintaining model quality. Implemented checkpointing every 100 steps to enable recovery and best model selection. 5. Production Readiness Challenge : Ensuring the model is deployment-ready, not just a proof-of-concept. Solution : Merged LoRA adapters into the base model, creating a single float16 model that requires no adapter loading at inference time, simplifying deployment and reducing latency. Impact & Future Work MedOCR-Vision highlights how domain-specific fine-tuning can translate research advances into robust, real-world healthcare solutions. By focusing on medical documents and workflows, the approach showcases strong potential for supporting: Hospital document digitization systems Electronic Health Record (EHR) integration Medical data extraction pipelines Healthcare document management platforms Looking ahead, future enhancements could explore multi-language support, advanced table and layout understanding, and deeper integration with medical knowledge graphs to further enrich entity recognition and contextual understanding. <div