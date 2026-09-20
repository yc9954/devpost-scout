---
slug: "watchdog-onxyge"
url: "https://devpost.com/software/watchdog-onxyge"
title: "Bino-SoRAs"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1108
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/media_journalism"
  - "user/general_public"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Bino-SoRAs

> AI-generated video detection using interpolated next-frame-prediction and Fréchet inception distance to generate 92% accurate zero-shot classification. Novel Binocular method applied to OpenAI's SORA.

[Devpost](https://devpost.com/software/watchdog-onxyge) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[media_journalism]]
**user** [[general_public]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** github, intel, numpy, opencv, pytorch, scikit-learn, tensorflow

## How they structured the write-up

- the gist
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for binosoras

## Body

The Gist We combine state-of-the-art LLM/GPT detection methods with image diffusion models to accurately detect AI-generated video with 92% accuracy. Inspiration As image and video generation models become more powerful, they pose a strong threat to traditional media norms of trust and truth. OpenAI's SORA model released in the last week produces extremely realistic video to fit any prompt, and opens up pathways for malicious actors to spread unprecedented misinformation regarding elections, war, etc. What it does BinoSoRAs is a novel system designed to authenticate the origin of videos through advanced frame interpolation and deep learning techniques. This methodology is an extension of the state-of-the-art Binoculars framework by Hans et al. (January 2024), which employs dual LLMs to differentiate human-generated text from machine-generated counterparts based on the concept of textual "surprise". BinoSoRAs extends on this idea in the video domain by utilizing Fréchet Inception Distance (FID) to compare the original input video against a model-generated video. FID is a common metric which measures the quality and diversity of images using an Inception v3 convolutional neural network. We create model-generated video by feeding the suspect input video into a Fast Frame Interpolation (FLAVR) model, which interpolates every 8 frames given start and end reference frames. We show that this interpolated video is more similar (i.e. "less surprising") to authentic video than artificial content when compared using FID. The resulting FID + FLAVR two-model combination is an effective framework for detecting video generation such as that from OpenAI's SoRA. This innovative application enables a root-level analysis of video content, offering a robust mechanism for distinguishing between human-generated and machine-generated videos. Specifically, by using the Inception v3 and FLAVR models, we are able to look deeper into shared training data commonalities present in generated video. How we built it Rather than simply analyzing the outputs of generative models, a common approach for detecting AI content, our methodology leverages patterns and weaknesses that are inherent to the common training data necessary to make these models in the first place. Our approach builds on the Binoculars framework developed by Hans et al. (Jan 2024), which is a highly accurate method of detecting LLM-generated tokens. Their state-of-the-art LLM text detector makes use of two assumptions: simply "looking" at text of unknown origin is not enough to classify it as human- or machine-generated, because a generator aims to make differences undetectable. Additionally, models are more similar to each other than they are to any human , in part because they are trained on extremely similar massive datasets. The natural conclusion is that an observer model will find human text to be very perplex and surprising, while an observer model will find generated text to be exactly what it expects. We used Fréchet Inception Distance between the unknown video and interpolated generated video as a metric to determine if video is generated or real. FID uses the Inception score, which calculates how well the top-performing classifier Inception v3 classifies an image as one of 1,000 objects. After calculating the Inception score for every frame in the unknown video and the interpolated video, FID calculates the Fréchet distance between these Gaussian distributions, which is a high-dimensional measure of similarity between two curves. FID has been previously shown to correlate extremely well with human recognition of images as well as increase as expected with visual degradation of images. We also used the open-source model FLAVR (Flow-Agnostic Video Representations for Fast Frame Interpolation), which is capable of single shot multi-frame prediction and reasoning about non-linear motion trajectories. With fine-tuning, this effectively served as our generator model, which created the comparison video necessary to the final FID metric. With a FID-threshold-distance of 52.87, the true negative rate (Real videos correctly identified as real) was found to be 78.5%, and the false positive rate (Real videos incorrectly identified as fake) was found to be 21.4%. This computes to an accuracy of 91.67%. Challenges we ran into One significant challenge was developing a framework for translating the Binoculars metric (Hans et al.), designed for detecting tokens generated by large-language models, into a practical score for judging AI-generated video content. Ultimately, we settled on our current framework of utilizing an observer and generator model to get an FID-based score; this method allows us to effectively determine the quality of movement between consecutive video frames through leveraging the distance between image feature vectors to classify suspect images. Accomplishments that we're proud of We're extremely proud of our final product: BinoSoRAs is a framework that is not only effective, but also highly adaptive to the difficult challenge of detecting AI-generated videos. This type of content will only continue to proliferate the internet as text-to-video models such as OpenAI's SoRA get released to the public: in a time when anyone can fake videos effectively with minimal effort, these kinds of detection solutions and tools are more important than ever, especially in an election year . BinoSoRAs represents a significant advancement in video authenticity analysis, combining the strengths of FLAVR's flow-free frame interpolation with the analytical precision of FID. By adapting the Binoculars framework's methodology to the visual domain, it sets a new standard for detecting machine-generated content, offering valuable insights for content verification and digital forensics. The system's efficiency, scalability, and effectiveness underscore its potential to address the evolving challenges of digital content authentication in an increasingly automated world. What we learned This was the first-ever hackathon for all of us, and we all learned many valuable lessons about generative AI models and detection metrics such as Binoculars and Fréchet Inception Distance. Some team members also got new exposure to data mining and analysis (through data-handling libraries like NumPy, PyTorch, and Tensorflow), in addition to general knowledge about processing video data via OpenCV. Arguably more importantly, we got to experience what it's like working in a team and iterating quickly on new research ideas. The process of vectoring and understanding how to de-risk our most uncertain research questions was invaluable, and we are proud of our teamwork and determination that ultimately culminated in a successful project. What's next for BinoSoRAs BinoSoRAs is an exciting framework that has obvious and immediate real-world applications, in addition to more potential research avenues to explore. The aim is to create a highly-accurate model that can eventually be integrated into web applications and news articles to give immediate and accurate warnings/feedback of AI-generated content. This can mitigate the risk of misinformation in a time where anyone with basic computer skills can spread malicious content, and our hope is that we can build on this idea to prove our belief that despite its misuse, AI is a fundamental force for good. <div