---
slug: "smart-graahak"
url: "https://devpost.com/software/smart-graahak"
title: "Smart Graahak"
hackathon: "Google Cloud Vertex AI Agent Builder Hackathon"
organization: "Google"
winner: true
words: 1227
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/media_journalism"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/regulation_legal_text"
  - "substrate/web_dom"
---

# Smart Graahak

> Smart Graahak allows users to search for products effortlessly, understand their benefits, and make informed choices about sustainability and safety. Smarter, hand more responsible shopping decisions.

[Devpost](https://devpost.com/software/smart-graahak) · hackathon [[Google Cloud Vertex AI Agent Builder Hackathon]]

## Facets

**domain** [[agriculture_food]] [[civic_government]] [[media_journalism]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[regulation_legal_text]] [[web_dom]]

**stack** gcp, openapi, python, vertex, vertexai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart graahak

## Body

Label Padhega India OpenAPI Schema Inspiration The recent "Label Padhega India" movement (Indians will read labels) inspired us to create Smart Graahak (Smart Consumer). In India, the complexity and unfamiliarity with label reading have led to a lack of regulation and awareness regarding FMCG products. Issues such as non-compliance with rules, language barriers, misinformation, misleading claims, inconsistent labelling standards, illegible labels, and inadequate enforcement have plagued the industry. The "Label Padhega India" campaign highlights these issues and aims to boost consumer activism and awareness, much like the government's "Jaago Grahak Jaago" campaign. Despite challenges, the campaign arrives at a crucial moment, with increasing scrutiny on product labelling and a call for greater transparency, particularly regarding added sugars in food products. What it does Smart Graahak is a chatbot designed to empower Indian consumers by providing detailed product information. Users can search for any product and learn about its benefits, brand, sustainability practices, and safety. The bot educates users on harmful ingredients such as parabens, sulfates, microplastics, and SLAs, especially in products from major brands. By making this information easily accessible, Smart Graahak helps consumers make informed and healthier choices. How we built it We built Smart Graahak using Google Vertex AI Agent and integrated various tools to gather and provide product information: Smart Label Product Search: To search and retrieve product details. Consumer Brands List: To find product brand and company information. Consumer Query: To check for detailed information on potentially harmful ingredients. Graahak Agent Instructions - Warm greeting in user's preferred language "Namaste! I'm an AI assistant here to help you understand products and labels better. How can I assist you today?" - "Did you have a specific product in mind you wanted information on? Or would you prefer I start with some general education about reading labels and finding sustainable, safe options?" - If the user names a product: - "Okay, let me confirm - you're asking about [product name]?" - Use ${TOOL:Smart Label Product Search} to find matching products - "Here are the top 5 matching results I found:" - List product name, brand, UPC code, link for each. - Display selected product details: "Based on your search, it seems this is the product:" - Show product link, brand, UPC - "Does this look like the right product you were asking about? If not, no worries - I can try searching again." - If not correct, use ${TOOL:Consumer Brands List} to get brand details - "Okay, I couldn't find an exact match, but here are some details on the [brand] brand and their parent company:" - Once product is confirmed: - "Great, let me share some key information about this [product category] product:" - List primary ingredients - Highlight using ${TOOL:Consumer Query}: "However, this product contains [concerning ingredient] which can be problematic because [explain issue]." - Note claims: "This product is marketed as [natural/organic claim], and the ingredients [do/do not] fully support that." - If food: Summarize nutrition facts - If non-food: "It [does/does not] have certifications like [EWG Verified, USDA Organic] that indicate safer ingredients." - "Given the [concerning ingredients], I would suggest considering these alternative [safer product/ingredient] options instead:" - If user prefers general label education: - "Reading product labels is so important for your health and the environment. Here are some key things to look out for:" - Discuss ingredients to avoid, backed by examples/visuals - Explain certifications that indicate safer products - Tips for interpreting nutrition labels - "Did you have a particular product category you wanted me to focus on - like food, personal care, household cleaners?" - Throughout: - Check "Does this make sense so far?" - Use simple language, examples, visuals - "I'm happy to discuss this more, or let me know if you had any other questions!" - "Thank you for your interest in this important topic! I hope I've helped increase your confidence in reading labels. Let me know if you need anything else before we wrap up." We utilized Vertex AI Tools for OpenAPI-based third-party API calling (Smart Label: https://smartlabel.org/ ) What is Smart Label? SmartLabel is a nimble, adaptable digital platform launched in 2015 by national brands and retailers in major grocery categories to give consumers access to more detailed product information than could ever fit on a package. It is fast and easy to use, with a consistent display across participating brands in these product categories: food, beverage, household cleaning, pet care, personal care, dietary supplements, and over-the-counter medications. What can you find on SmartLabel that you can’t find on the package? SmartLabel enables brands to provide information on ingredients, nutrition, and allergens and goes beyond the package label to include things like how to use or prepare the product, how to recycle the packaging, safety and handling instructions and even tasty recipes. You can be confident that the information in SmartLabel is accurate and up-to-date because it comes straight from brands. The chatbot leverages natural language processing to understand user queries and provide relevant information in an easy-to-understand format, catering to the diverse needs and technological awareness of Indian consumers. OpenAPI Schema: openapi: 3.0.0 info: title: SmartLabel API version: 1.0.0 servers: - url: 'https://api.smartlabel.org/api' paths: /search: get: summary: Search for products by query operationId: searchProducts parameters: - in: query name: product required: true description: Product name to search for schema: type: string - in: query name: perPage required: false description: Number of results per page schema: type: integer example: 1 - in: query name: page required: false description: Page number to retrieve schema: type: integer example: 1 responses: '200': description: A list of products matching the search criteria content: application/json: ...... We also downloaded product safety and ingredient guides for different FMCG companies to index and search on them using our AI Agent, since Web Search with Vertex Agent Data tool needs domain ownership verification . Challenges we ran into Data Availability: Accessing reliable and comprehensive data on product ingredients and their effects was challenging. Public URL web search is not allowed in Vertex AI without ownership verification. Language Barriers: Ensuring that the chatbot could understand and respond accurately in multiple Indian languages. Google Vertex Agents don't support all Indian regional languages User Education: Educating users who are unfamiliar with label reading and product safety simply and engagingly. Accomplishments that we're proud of Successfully integrating various data sources to provide comprehensive product information. Developing a user-friendly interface that caters to a diverse audience. Contributing to the "Label Padhega India" movement by empowering consumers with knowledge and helping them make healthier choices. What we learned The importance of clear and accurate product labelling and its impact on consumer health and safety. The challenges and opportunities in educating a diverse population about product safety and sustainability. The potential of AI and chatbots to drive consumer awareness and activism. What's next for Smart Graahak Expansion of Data Sources: Incorporate more data sources to provide even more detailed and comprehensive product information. Multilingual Support: Enhance the chatbot's capabilities to support more Indian languages and dialects. User Feedback Integration: Continuously improve the chatbot based on user feedback to ensure it meets the evolving needs of Indian consumers. Partnerships: Collaborate with FMCG companies, health organizations, and consumer rights groups to further promote product transparency and consumer awareness. Smart Graahak aims to become an indispensable tool for Indian consumers, fostering a culture of informed and responsible shopping. <div