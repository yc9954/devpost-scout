---
slug: "one-click-photo-repair-with-diffusion"
url: "https://devpost.com/software/one-click-photo-repair-with-diffusion"
title: "One-Click Photo Repair with Diffusion"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 1010
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# One-Click Photo Repair with Diffusion

> diffusion, inpainting, computer graphics

[Devpost](https://devpost.com/software/one-click-photo-repair-with-diffusion) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[geospatial]] [[video_visual]]

**stack** diffusion, fastapi, mobilesam, node.js, opencv, python, react, sam, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for one-click photo repair with diffusion

## Body

Inspiration In daily photography, images are often imperfect. Unwanted elements such as random pedestrians, electrical wires, or distracting objects frequently appear in photos. Although professional editing software can remove these objects, it usually requires technical skills and significant learning time. For casual users, the editing process can be complicated and time-consuming. Recent advances in diffusion models have enabled high-quality image generation and completion. However, many existing AI tools lack fine-grained control over which specific region should be modified. Therefore, we aim to build a controllable image inpainting system that allows users to directly select unwanted regions and remove them without requiring professional knowledge. What it does One-click object removal : Users upload an image and simply paint over unwanted regions (e.g. pedestrians, wires, distracting objects). The system automatically restores a reasonable background. SAM-assisted masking : In Pro mode, users can first draw a bounding box around the target object. The backend sends the selected region to SAM, which generates a segmentation mask automatically. Users can then refine it with a brush or eraser before inpainting. Manual mask editing : Users can still directly paint over unwanted regions, which is useful when automatic segmentation is not enough. Multiple candidate outputs : For the same mask and prompt, users can generate multiple variations using different seeds and choose the best result. Real-time progress tracking : The backend creates a job and the frontend polls /progress/{job_id} to display step-by-step progress, improving user experience during generation. Cartoon / illustration support : Includes a "Fill" mode (traditional OpenCV inpainting) to handle flat-color or stylized images more reliably. How we built it Frontend (React + Vite) Workflow: Upload -> Mask Editor -> Prompt Picker -> Generate -> Result The Mask Editor uses a fixed canvas (640 x 420) for drarwing masks. manual brush painting eraser-based refinement In Pro mode, box selection for SAM-based automatic masking After the user selects a box, the frontend sends the original image and bounding box coordinates to the backend /sam-mask endpoint. The returned mask is overlaid on the editor, allowing the user to further refine the segmentation before continuing. The Generate page: Sends a POST /inpaint request to api to create a job includes job_id. Polls Get /progress/{job_id} to update generation progress. Fetches results from GET /result/{job_id} once completed. Supports multiple outputs and clean UI transitions. Backend (FastAPI) POST /inpaint : Accepts image, mask, prompt, negative prompt, steps, guidance, number of outputs, the generating mode, etc. Creates a background job and returns a job_id. GET /progress/{job_id} : Returns global step (the current step for total steps), total steps, percentage and job status (running, in queue, done). GET /result/{job_id} : Returns generated images in Base64 and seeds once finished. POST /sam-mask : Accepts the original image together with a bounding box (x, y, w, h) Uses MobileSAM on the backend to segment the selected object and return a binary mask. The mask is slightly expanded around the object boundary to provide a safer editing buffer, which improves inpainting quality near edges. Model & Inference Pipeline Based on Stable Diffusion Inpainting (runwayml/stable-diffusion-inpainting) via Hugging Face Diffusers and OpenCV inpainting. For automatic object selection, we integrated MobileSAM, so users do not need to manually paint the initial mask from scratch. We also apply mask post-processing after SAM inference to slightly expand the segmented region beyond the object boundary. This helps cover edge pixels and reduces visible artifacts when blending the repaired result back into the image. ROI-based inpainting: Computes a bounding box around the mask. Only runs model on that region. Uses feather blending to seamlessly merge results back into the original image. Uses negative prompts (e.g. "people, person, text, watermark, logo") to reduce unwanted artifacts. Cartoon / Illustration Handling We introduced multiple modes: Fill Mode: Pure OpenCV inpainting (Telea/Navier-Stokes). Gen Mode: OpenCV first fills the region, then diffusion generates with prompts. Normal Mode: Pure diffusion with prompts. This significantly improves performance on flat-color and stylized images. Challenges we ran into Mask alignment issues : Since the frontend uses a fixed-size canvas, mask resizing had to be carefully aligned with the original image to avoid distortion. Boundary quality after segmentation : Even when SAM correctly detects an object, the returned mask can be too tight around the edges. This can leave visible artifacts during inpainting, so we added post-processing to slightly expand the mask boundary. Unstable Generations (e.g. people reappearing): Even with negative prompts, diffusion can hallucinate unwanted elements. Prompt engineering alone is not always sufficient. Cartoon images performing poorly : Stable Diffusion struggles with flat-color and line-art styles. This led us to integrate OpenCV-based fallback strategies. Performance & memory limits : Lower-end GPUs can run out of memory. We had to limit resolution and inference steps for stability. Accomplishments that we're proud of Built a fully working end-to-end system: upload -> mask -> prompt -> generate -> multi-result selection. Integrated SAM-assisted object selection into the workflow, making mask creation much faster and more user-friendly. Added manual refinement tools such as brush and eraser so users can correct segmentation results before generation. Implemented real-time progress tracking for long-running diffusion jobs. Added multi-seed generation to increase success rate. Designed an ROI + feather blending pipeline to improve quality and reduce computation. Integrated traditional computer vision methods with diffusion models for greater robustness. What we learned User experience in AI tools depends heavily on system, not just model quality. Automatic segmentation is powerful, but users still need refinement tools for practical editing. Diffusion models are powerful but unpredictable, fallback strategies are essential. Long-running AI tasks require asynchronous job systems for a smooth user experience. What's next for One-Click Photo Repair with Diffusion More interactive SAM guidance : Support click-based point prompts in addition to box prompts for finer object selection. Improved unwanted-object suppression : Integrate detection models (e.g. human detection) to automatically reinforce negative prompts. Better cartoon pipeline : Explore LoRA or specialized checkpoints for illustration-style images. Performance optimization : Improve batching, memory efficiency and inference speed. More control options : Adjustable denoise strength, feather control, background-only mode, controlled object insertion (e.g. "add a penguin") <div