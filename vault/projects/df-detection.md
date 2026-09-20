---
slug: "df-detection"
url: "https://devpost.com/software/df-detection"
title: "Deepfake Detection"
hackathon: "InnovateHacks 2.0"
organization: "Dublin Hack Club"
winner: true
words: 823
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/media_journalism"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Deepfake Detection

> Beneath the Mask: Revealing the Hidden Danger of Deepfakes

[Devpost](https://devpost.com/software/df-detection) · hackathon [[InnovateHacks 2.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[finance_payments]] [[media_journalism]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** cnn, css, lstm, machine-learning, numpy, opencv, pandas, python, resnet, scikit-learn, streamlit, tensorflow

## How they structured the write-up

- inspiration💡
- deepfake-detection
- key features and technologies
- technological workflow :
- impact and benefits :
- how we built it?
- results:

## Body

Interface Features Upload and detect Inspiration💡 The project was inspired by the rise of deepfakes and the risks they pose, from spreading misinformation to damaging personal reputations. With fake videos becoming harder to detect, the goal is to build a reliable AI tool that can spot these manipulations, helping protect the truth and maintain trust in digital content. Deepfake-Detection The emergence of deep fakes, or synthetic media, has created new difficulties for media verification. DeepFakes are artificial intelligence (AI)-based manipulations or creations of Video and audio information that seem real but are actually completely fake or altered. This technology has the power to erode confidence, spread false information, and result in serious harm, including fraud and defamation. The complexity of detecting these kinds of fakes has increased as artificial intelligence and machine learning have progressed. Proposed Solution In order to address these issues, VerifEye offers an AI/ML-based solution that can identify face-swapped DeepFakes in video and audio files. The tool offers precise identification, real-time analysis, and intuitive verification features by combining a number of cutting-edge technologies. Key Features and Technologies Video Face Swap Detection : ResNet: By concentrating on residual differences, ResNet (Residual Networks) improves detection capabilities and makes it easier to identify minute abnormalities in facial patterns. Long Short-Term Memory (LSTM) Networks: These networks are used to identify manipulation over time by detecting temporal inconsistencies in video frame sequences. Detailed Report with Graph Generation : Extensive Reports: VerifEye produces extensive reports that contain graphical depictions of anomalies found in FaceSwap Videos and in-depth details regarding the content's authenticity. Visual Results: VerifEye provides viewers with a visual depiction of the DeepFakes that have been identified, clearly illustrating the location of the face swap in the video. Audio DeepFake Detection : By comparing audio with expected genuine audio characteristics, models identify manipulated audio content by looking for anomalies in frequency and temporal patterns. Anti-Spoofing Protection : Detection of Subtle Inconsistencies: Anti-spoofing features are implemented to identify subtle anomalies in facial features and voices, adding an additional layer of security against spoofing attempts. 4.1 Real-Time Analysis and Feedback : ◾ WebRTC Integration : WebRTC allows quick access to the user's camera, making it easy to capture live video and audio. This helps in analyzing content instantly as it is being recorded. ◾ dlib for Face Landmark Detection : dlib improves the accuracy of face analysis and manipulation detection by using real-time facial landmark detection. Integration with Communication Tools : ◾WhatsApp and Telegram Bot Integration : Users can send media for analysis using a WhatsApp and Telegram bot, which will process the media and return detailed reports and real/fake analyses via WhatsApp or Telegram Video. ◾ Video Authenticity Chrome Extension : Chrome Add-on with the use of a Chrome extension, consumers can quickly and easily verify the legitimacy of media material right from their browser. Technological Workflow : Neural networks (ResNet, LSTM) : Applied for pattern recognition and anomaly detection in video and audio content. Python and Libraries : Utilizes Python with Scikit-Learn for data processing, Pandas for data management, NumPy for numerical operations, OpenCV for video frame processing, and TensorFlow for deep learning models. Detection Workflow : Users can simply visit VerifEye and login to the platform. Then navigate to the upload and detect tab. Browse and Upload the suspicious media and Detect whether the video/audio is fake/real, along with graphical results and reports. Also users can forward suspected media to a whatsapp/telegram bot or use an extension during web-surfing to check authenticity of video/audio they encounter. The media is processed, analyzed for anomalies, and results are delivered through detailed reports document. Impact and Benefits : a) Prevents misinformation : VerifEye helps stop the spread of false information and reduces the harm it can cause by identifying fake content/media. b) Enhances Media Integrity : VerifEye helps to preserve the integrity of digital media by providing dependable detection and verification capabilities. c) User-Friendly Tools : By making it simple for users to validate media content, the browser extension and bot encourage widespread adoption and efficient use. Conclusion : VerifEye is a trustworthy solution for detecting deepfakes. It uses advanced AI to provide accurate, real-time checks and simple tools to verify media. With its unique approach, VerifEye helps fight the spread of fake content, giving users confidence in what they see online. How we built it? Dataset Collection 📂 Collected FaceForensics++ and DFDC datasets. Data Preprocessing 🛠️ Extracted frames and performed data normalization. Model Development 🧠 Started with CNN; switched to ResNet with LSTM for enhanced accuracy.(92%) Training the Model 🚀 Aimed for accuracy above 85% using early stopping and learning rate adjustments. Evaluation and Tuning ⚙️ Fine-tuned model parameters based on validation results. User Interface Development 💻 Created a user-friendly interface with Streamlit. Feature Integration 🔗 Added audio analysis, biometric detection, and WhatsApp bot functionality. Testing and Validation ✅ Conducted comprehensive testing for reliability. data used - https://drive.google.com/open?id=10NGF38RgF8FZneKOuCOdRIsPzpC7_WDd Results: ◾Training Accuracy= 92% ◾Validation Accuracy= 86% <div