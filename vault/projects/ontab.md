---
slug: "ontab"
url: "https://devpost.com/software/ontab"
title: "OnTab"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1330
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# OnTab

> Cursor Tab for Everything

[Devpost](https://devpost.com/software/ontab) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[human_in_the_loop]] [[on_device_local]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** anthropic, fastapi, huggingface, javascript, modal, onnx, openai, plasmo, python, pytorch, react, stagehand, webgpu, webllm

## How they structured the write-up

- introduction
- inspiration
- the product
- how we built it
- challenges
- what we learned

## Body

Introduction We built OnTab: Cursor Tab for everything. It's a Chrome extension that watches how you work, predicts your next browser action (clicking a button, filling a form, navigating to a page), and executes it when you press Tab. Today's computer-operating agents are where coding agents were in 2024: not yet trusted to run autonomously end-to-end, but powerful with a human in the loop. Just like Cursor's thesis for code, we believe users want the speed of automation without giving up control over their device. OnTab gives you both, one tap at a time. Inspiration We noticed that knowledge workers spend hours on the same mechanical browser sequences. Recruiters cycle between LinkedIn profiles and spreadsheets. Medical office staff copy patient details across portals to fill out prior authorization forms. Accountants tab between bank statements, tax software, and client records. These are patterns a model should be able to learn and predict. Crucially, these are also high-trust environments. A wrong autofill on a prior auth can delay a patient's care, a misplaced number in a tax filing has real consequences. Full autonomy isn't appropriate here. But a system that suggests the next step and lets a human confirm it? That's the right level of AI for these workflows today. The insight was that browser actions are a lot like code completions. They're sequential, context-dependent, and repetitive. If Cursor can predict your next line of code, we should be able to predict your next browser action. But the key constraint is trust. People are protective of their browser, especially when handling sensitive data. Tab-to-accept felt like the natural interaction: show the prediction, let the user verify, then execute. The Product Background agent that passively observes your browsing and suggests actions when confident One-step-at-a-time execution : press Tab to advance, Esc to dismiss: full user control Custom per-user LLM that adapts to your individual workflows via reinforcement learning Cross-tab continuity : workflows that span multiple tabs (e.g., LinkedIn → Google Sheets → Gmail) work seamlessly How We Built It See image attached! Two-Layer Prediction Pipeline Our core architectural decision was splitting prediction into two layers: understanding what the user is doing vs. figuring out how to do the next step. Layer 1 — Task Description (fast). When a user acts on a page, we call Claude Haiku 4.5 to generate a short natural-language summary of the user's current task and recent steps. This runs in ~200ms and gives us a semantic understanding of intent based on a sequence of raw DOM events. Layer 2 — Action Planning (precise). We pass that task description along with a snapshot of the current page's interactive elements to Claude Sonnet 4.5 / ChatGPT 5-mini, which generates a concrete sequence of browser actions (clicks, inputs, navigations, keypresses) as structured JSON. This is the step that actually knows where to click and what to type. This separation matters. The task describer generalizes across pages (it doesn't care about specific button IDs), while the action planner is grounded in the actual DOM. Splitting them made each layer simpler and more reliable than a single monolithic model trying to do both. We also maintain an on-device fallback using WebLLM (Qwen2.5-1.5B via WebGPU), which can replace Layer 1 for fully offline, private inference. We pivoted to cloud-first as the default after measuring that Haiku is faster than on-device inference for most users. Action Execution Actions are executed directly via DOM manipulation in the content script ( querySelector , click() , dispatchEvent() , setting input values), no external runtime dependencies. The content script captures a snapshot of visible interactive elements (buttons, inputs, links, up to 40 per page) and resolves targets using a layered selector strategy: element ID, className, XPath, text content, and ARIA roles. A queue controller manages multi-step execution with up to 3 retries per step to handle flaky selectors and dynamic pages. Chrome Extension Architecture The extension runs as a Manifest V3 Chrome extension with three main components: A content script that records user actions and executes predicted steps A service worker that routes messages and manages queue state across tabs An offscreen document that runs the inference pipeline in an isolated context, keeping the main browsing experience snappy Post-Training & Reinforcement Learning To fully personalize suggestions, we fine-tune a per-user model. Every time a user accepts or rejects a prediction, we log it: the predicted action, whether it was accepted, and what the user did instead if they rejected it. Once we accumulate 50+ examples, we trigger an async training job on Modal (A10G GPU). The training uses KTO (Kahneman-Tversky Optimization) , a reinforcement learning method that learns from both acceptances and rejections. Unlike standard supervised fine-tuning which only learns from correct examples, KTO explicitly downweights rejected predictions, so the model learns what not to suggest just as much as what to suggest. We fine-tune Qwen2.5-1.5B with LoRA adapters (10-50MB), keeping the base model frozen. The trained adapter gets compiled into an MLC-compatible WebAssembly library and uploaded to HuggingFace. On the client side, a model lifecycle manager polls for new adapters and hot-swaps them into the on-device predictor: no restart, no user intervention. Since RL is computationally expensive and can contain 20,000+ rows of evals, we containerize the function in Modal. We leverage Modal Volumes to store the LoRA adapter files, and fetch them during runtime when users log-in. This allows concurrency and scaling. After post-training our Qwen model with 1,000+ data points, tab acceptance rate doubled from 26% to 52%. [see image attached] For cold-start, we synthetically generated 1,000+ browser action entries using Browserbase's Stagehand. We scripted diverse browser tasks (navigating pages, filling forms, clicking through flows), executed them in parallel cloud browsers via the Stagehand API, and parsed the event logs into our RL training schema. This gave us a solid base dataset with minimal compute, generated in ~20 minutes. Challenges Latency vs. accuracy tradeoff. Our first approach used two on-device WebLLM instances: one for task description, one for action generation. Inference was private but slow (300-500ms per layer). We found that users notice anything over ~1 second total. Moving Layer 1 to Haiku and Layer 2 to Sonnet cut perceived latency dramatically while improving prediction quality, at the cost of requiring an API key. DOM fragility. Browser pages are messy. Elements load asynchronously, IDs change between sessions, and class names are often auto-generated. We went through multiple selector strategies before landing on a layered approach that tries ID, className, XPath, text content, and ARIA roles in sequence. Learning from rejections. Standard fine-tuning only learns from positive examples. Early on, our model would keep suggesting the same wrong action because it never learned not to. Switching to KTO was valuable because it treats rejected predictions as explicit negative signals, which made the model noticeably better at avoiding repeated mistakes. Cross-tab state. Browser workflows naturally span tabs (LinkedIn → Sheets → Gmail), but Chrome extensions have limited cross-tab communication. We had to build a shared state layer in the service worker that tracks queue progress across tab boundaries, so a workflow that starts on one page can continue seamlessly when the user switches tabs. What We Learned The biggest lesson was that the right level of AI autonomy depends on the domain. For browser automation, one-step-at-a-time with Tab-to-accept is the sweet spot right now. It builds trust incrementally. Users who start by carefully reviewing every suggestion eventually just Tab through entire workflows without looking. The trust has to be earned, not assumed. We also learned that splitting inference into semantic layers (understanding vs. planning) is a powerful pattern. It made each component independently testable, swappable, and debuggable. When Haiku gives a bad task description, we can see it immediately without digging through action-level logs. Finally: reinforcement learning from real user feedback, even small amounts of it, beats large amounts of synthetic data. Our 50-example personalized models outperform the base model trained on 1,000+ synthetic examples, because real rejection signals encode exactly what matters to that specific user. <div