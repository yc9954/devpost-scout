---
tags:
  - "claim"
confidence: 0.85
evidence: "benchmark"
---

# an OCR model that is also a vision-language model can be fine-tuned as a VLM rather than as an OCR system, which is a different set of methods entirely

Asserted by [[paddleocr_vl_receipt-a-sft-model-extract-info-from-receipt]] — *PaddleOCR_VL_Receipt - A SFT Model Extract Info From Receipt*  
<sub>ERNIE AI Developer Challenge</sub>

**Problem** a model's capabilities are bounded by the training paradigm applied to it rather than by the model

**Mechanism** apply VLM fine-tuning to an OCR model for prompt-defined structured extraction  
**Beneficiary** anyone extracting structured data from documents

**Recurs in** [[invoices]] [[medical forms]] [[historical records]]