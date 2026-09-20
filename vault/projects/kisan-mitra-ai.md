---
slug: "kisan-mitra-ai"
url: "https://devpost.com/software/kisan-mitra-ai"
title: "Kisan-Mitra AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 2979
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Kisan-Mitra AI

> Built on AWS and powered by Amazon Nova Pro, the platform eliminates the literacy barrier with a voice-first interface supporting 15+ regional dialects. By leveraging Amazon Bedrock.

[Devpost](https://devpost.com/software/kisan-mitra-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[privacy_tech]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[agriculture_food]] [[civic_government]] [[climate_energy]] [[developer_tools]] [[education]] [[finance_payments]] [[supply_logistics]] [[transportation]]
**user** [[developer]] [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** ai, amazon-cloudfront-cdn, amazon-cloudwatch, amazon-dynamodb, amazon-nova, api-gateway, aws-lambda, awscognito, bedrock, dotnet, dotnet-api, nova, polly, s3

## How they structured the write-up

- 🌟 inspiration
- 💡 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for kisan-mitra ai
- 🎯 impact metrics
- 🛠️ technical specifications
- 📹 demo & resources
- 👥 team
- 🙏 acknowledgments
- 📄 license

## Body

Login Page Login Mobile View Page Register Page Kisan Mitra - AI Dashboard Page Mobile View Dashboard Page Soil Analysis Page Soil Analysis History Page Soil Analysis Saved Report Page Soil Analysis Recommendation Page Soil Analysis 12 Months Regenerative Plan Page Quality Grading Page Quality Grading History Results Page Voice Query Page Voice Query with Result Page Voice Query Mobile ViewPage Planting Advisory Page Planting Advisory History Result Page Kisan Mitra - AI About Page Kisan-Mitra AI - Amazon Nova AI Hackathon Submission 🌟 Inspiration Agriculture is the backbone of India's economy, supporting over 58% of the rural population. Yet, farmers face numerous challenges daily: Language Barriers : Most agricultural information is available only in English, creating a massive accessibility gap for regional language speakers Information Asymmetry : Farmers struggle to access real-time market prices, leading to exploitation by middlemen Limited Expert Access : Agricultural experts are scarce in rural areas, leaving farmers without timely guidance Soil Health Ignorance : Expensive soil testing and complex reports prevent farmers from understanding their land's needs Quality Assessment Challenges : Farmers lack tools to objectively grade their produce, resulting in unfair pricing We were inspired to bridge this digital divide by creating an AI-powered companion that speaks the farmer's language, understands their challenges, and provides actionable insights at their fingertips. Kisan-Mitra AI (Farmer's Friend AI) was born from the vision of democratizing agricultural knowledge through cutting-edge AI technology. 💡 What it does Kisan-Mitra AI is a comprehensive, voice-first agricultural intelligence platform that empowers farmers throughout the entire farming lifecycle. It combines Amazon Bedrock's Nova Pro model with AWS AI services to deliver: 1. 🎤 Krishi-Vani (Voice Intelligence) Natural Language Conversations : Farmers can speak naturally in Hindi, English, or regional dialects Real-time Advisory : Ask about market prices, weather forecasts, crop diseases, or farming techniques Voice Responses : Get answers in their preferred language through text-to-speech Example Queries : "Aaj ke aloo ke bhav kya hain Delhi mein?" (What are today's potato prices in Delhi?) "Mere khet mein gehun ki patti peeli ho rahi hai, kya karun?" (My wheat leaves are turning yellow, what should I do?) 2. 📸 Quality Grader (Vision AI) Instant Produce Grading : Take a photo of fruits or vegetables to get quality assessment AI-Powered Analysis : Detects defects, analyzes size, color uniformity, and freshness Market Price Estimation : Provides grade (A, B, C) with estimated market value Supported Crops : Potatoes, tomatoes, onions, apples, and more 3. 🌱 Dhara-Analyzer (Soil Intelligence) Digital Soil Health Cards : Upload a photo of soil test reports for instant digitization Automated Data Extraction : AI extracts all nutrient values (N, P, K, pH, organic carbon, micronutrients) Personalized Recommendations : Get fertilizer plans and regenerative farming strategies Soil-Specific Crop Suggestions : Recommendations tailored to your soil's unique characteristics 4. 🌾 Sowing Oracle (Planting Advisor) Smart Crop Recommendations : AI suggests what to plant based on location, season, and soil conditions Optimal Planting Windows : Know exactly when to sow for maximum yield Seed Variety Selection : Get recommendations for specific seed varieties with yield potential Market Demand Forecasts : Understand which crops will be profitable 5. 💰 Mandi Price Intelligence Real-time Market Prices : Access live wholesale prices from major mandis across India Historical Trends : Analyze price patterns to make informed selling decisions Location-based Pricing : Get prices specific to your region 🛠️ How we built it Architecture Overview We built Kisan-Mitra AI using a modern, serverless architecture on AWS, with Amazon Bedrock's Nova Pro model as the core intelligence engine. ┌─────────────┐ │ Farmer │ (Voice/Photo/Text Input) └──────┬──────┘ │ ▼ ┌─────────────────────────────────────┐ │ React Frontend (PWA) │ │ - Voice Recording (Web Audio API) │ │ - Image Upload & Preview │ │ - Real-time Chat Interface │ └──────────────┬──────────────────────┘ │ ▼ ┌─────────────────────────────────────┐ │ API Gateway + AWS Lambda │ │ - ASP.NET Core 8 API │ │ - JWT Authentication (Cognito) │ │ - Request Routing & Validation │ └──────────────┬──────────────────────┘ │ ┌───────┴───────┐ ▼ ▼ ┌─────────────┐ ┌─────────────┐ │ AWS AI │ │ Data Layer │ │ Services │ │ │ │ │ │ - DynamoDB │ │ - Bedrock │ │ - S3 │ │ Nova Pro │ │ - Timestream│ │ - Transcribe│ │ │ │ - Rekognition│ │ │ │ - Textract │ │ │ │ - Polly │ │ │ └─────────────┘ └─────────────┘ Technology Stack Backend (.NET 8 / C#) Framework : ASP.NET Core 8 Web API Architecture : Clean Architecture (Core, Infrastructure, API layers) Deployment : AWS Lambda with Function URLs Authentication : Amazon Cognito with JWT tokens Testing : xUnit with property-based testing (FsCheck) AI & Cloud Services (AWS) Amazon Bedrock Nova Pro : Core AI reasoning engine for all intelligent features Voice query understanding and response generation Seed variety recommendations with soil-specific reasoning Planting advisory with context-aware suggestions Soil analysis interpretation and regenerative farming plans Amazon Transcribe : Multi-language speech-to-text (Hindi, English, Punjabi, Bengali) Amazon Polly : Natural-sounding text-to-speech responses Amazon Rekognition : Image analysis for quality grading and defect detection Amazon Textract : OCR for soil health card digitization Amazon S3 : Scalable object storage for images and audio files Amazon DynamoDB : NoSQL database for user profiles and mandi prices Amazon Timestream : Time-series data for price trends and weather AWS Lambda : Serverless compute for cost-effective scaling Amazon Cognito : Secure user authentication and authorization Amazon CloudFront : Global CDN for low-latency content delivery Frontend (React + TypeScript) Framework : React 18 with TypeScript State Management : Redux Toolkit UI Components : Material-UI with custom theming Audio Recording : Web Audio API for voice capture Image Handling : Canvas API for client-side optimization PWA : Progressive Web App for mobile-first experience Key Implementation Details 1. Direct Bedrock Nova Pro Integration We implemented direct API calls to Amazon Bedrock's Nova Pro model for maximum flexibility and cost efficiency: // DirectBedrockSeedVarietyRecommender.cs public async Task<List<SeedVariety>> RecommendVarietiesAsync( PlantingWindow window, string location, SoilAnalysisResult soilData) { // Build context-rich prompt with soil data var prompt = BuildPrompt(window, location, soilData); // Direct Bedrock API call var request = new InvokeModelRequest { ModelId = "us.amazon.nova-pro-v1:0", Body = JsonSerializer.SerializeToUtf8Bytes(new { messages = new[] { new { role = "user", content = prompt } }, inferenceConfig = new { temperature = 0.7, maxTokens = 2000 } }) }; var response = await _bedrockRuntime.InvokeModelAsync(request); // Parse AI-generated recommendations return ParseVarieties(response); } 2. Voice Query Pipeline // VoiceQueryService.cs public async Task<VoiceQueryResponse> ProcessVoiceQueryAsync( Stream audioStream, string language) { // Step 1: Speech-to-Text var transcription = await _transcribeService .TranscribeAudioAsync(audioStream, language); // Step 2: AI Understanding & Response (Nova Pro) var aiResponse = await _bedrockService .GenerateResponseAsync(transcription, userContext); // Step 3: Text-to-Speech var audioResponse = await _pollyService .SynthesizeSpeechAsync(aiResponse, language); return new VoiceQueryResponse { Transcription = transcription, TextResponse = aiResponse, AudioResponse = audioResponse }; } 3. Soil Analysis with AI Interpretation // SoilAnalysisService.cs public async Task<SoilAnalysisResult> AnalyzeSoilHealthCardAsync( Stream imageStream) { // Step 1: Extract text from image var extractedData = await _textractService .ExtractTextAsync(imageStream); // Step 2: Parse soil parameters var soilParams = ParseSoilParameters(extractedData); // Step 3: AI-powered interpretation (Nova Pro) var analysis = await _bedrockService .InterpretSoilDataAsync(soilParams); // Step 4: Generate regenerative farming plan var plan = await _bedrockService .GenerateRegenerativePlanAsync(soilParams, analysis); return new SoilAnalysisResult { Parameters = soilParams, Analysis = analysis, RegenerativePlan = plan }; } 4. Quality Grading with Vision AI // QualityGradingService.cs public async Task<QualityGrade> GradeProduceAsync( Stream imageStream, string cropType) { // Step 1: Image analysis var imageAnalysis = await _rekognitionService .DetectImagePropertiesAsync(imageStream); // Step 2: Defect detection var defects = await _rekognitionService .DetectDefectsAsync(imageStream); // Step 3: Calculate quality score var score = CalculateQualityScore(imageAnalysis, defects); // Step 4: AI-powered grading explanation (Nova Pro) var explanation = await _bedrockService .ExplainGradingAsync(score, imageAnalysis, defects); return new QualityGrade { Grade = DetermineGrade(score), Score = score, Explanation = explanation, EstimatedPrice = GetPriceRange(cropType, score) }; } Development Process Requirements Gathering : Interviewed farmers to understand pain points Architecture Design : Designed serverless, cost-optimized architecture Backend Development : Built .NET 8 API with clean architecture principles AI Integration : Integrated Amazon Bedrock Nova Pro with custom prompting strategies Frontend Development : Created responsive React PWA with voice and image capabilities Testing : Comprehensive unit and integration testing Deployment : Automated deployment to AWS Lambda with CI/CD Optimization : Iterative performance and cost optimization 🚧 Challenges we ran into 1. Cost Optimization Challenge Problem : Initial architecture used Amazon OpenSearch Serverless for RAG (Retrieval-Augmented Generation), costing $197/month (~$7,114/year) for a prototype. Solution : Pivoted to direct Amazon Bedrock Nova Pro API calls with intelligent prompting, reducing costs to ~$2/month while maintaining high-quality recommendations. This 98.5% cost reduction made the solution viable for scale. 2. Multi-language Voice Recognition Problem : Indian farmers speak various dialects with regional accents, making accurate transcription difficult. Solution : Leveraged Amazon Transcribe's multi-language support with custom vocabulary for agricultural terms. Implemented fallback mechanisms and confidence scoring to handle unclear audio. 3. Soil Health Card Variability Problem : Soil test reports come in different formats from various labs, making consistent data extraction challenging. Solution : Used Amazon Textract with custom post-processing logic to handle format variations. Implemented fuzzy matching for parameter names and unit conversion for standardization. 4. Real-time Performance on Lambda Problem : Cold starts on AWS Lambda caused delays in voice query responses (3-5 seconds). Solution : Implemented Lambda provisioned concurrency for critical functions Optimized .NET 8 startup time with ReadyToRun compilation Used Lambda function URLs for direct invocation (bypassing API Gateway overhead) 5. Image Quality Grading Accuracy Problem : Produce images taken in varying lighting conditions and angles affected grading accuracy. Solution : Implemented client-side image preprocessing (brightness normalization, rotation correction) Used Amazon Rekognition's ImageProperties API for lighting analysis Combined multiple detection features (color, texture, shape) for robust scoring 6. Context Preservation in Voice Conversations Problem : Farmers often ask follow-up questions that require context from previous queries. Solution : Implemented conversation history tracking in DynamoDB with sliding window context. Nova Pro's large context