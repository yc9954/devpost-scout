---
slug: "thinklogically"
url: "https://devpost.com/software/thinklogically"
title: "#ThinkLogically"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 807
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "user/general_public"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# #ThinkLogically

> Enabling users of news websites and open/closed social networks to request fact-checks directly from their browser or mobile app

[Devpost](https://devpost.com/software/thinklogically) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[civic_government]] [[finance_payments]] [[health_clinical]] [[media_journalism]]
**user** [[general_public]] [[legal_professional]] [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** flask, javascript, keras, mongodb, python, react-native, tf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for #thinklogically

## Body

Overall Approach to Credibility and Veracity Assessment Factchecking Process Flow Successes During Indian Election in 2019 Inspiration The 'infodemic' around the coronavirus, best practices and policy are evident. While social media platforms are trying to combat problematic content, these efforts have been largely overwhelmed by the surge in user generated content and rumours originating from unreliable sources and disinformation campaigns. Furthermore, governments and the public lack transparency on the effectiveness of platform initiatives. What it does Logically's app [production] and browser extension [prototype] How we built it Logically’s fact-checkers are supported by in-house journalists, innovative technology and efficient, streamlined processes designed to safeguard the integrity of our fact-checks whilst maximising their efficiency. While we aspire to a fully automated fact-checking solution, we have developed an hybridised process which supports the development of our fact-checking algorithms, enables the incremental adoption of our automated fact-checking technology as it matures, and enables efficient and high-quality fact-checking in the meantime. Incoming Claim Users can submit suspect claims for fact-checking that they encounter within the Logically app [production], or from third party publishers by sharing the article with Logically natively or pasting the URL into the app; OR directly from facebook, twitter and most news websites via a browser extension [prototype]. Our claim detection technology gets to work extracting the factual claims within, enabling the user to select the one they’d like verified and submit it to our fact-checkers. Users can also enter raw text or paste a message/post from another platform. Claims then appear on the bespoke dashboard developed to help our team progress claims through our process efficiently, maximising our chances of preventing false claims from spreading. Automated Factcheck Incoming claims are first checked against our single source of truth databases through a vectorised analysis of the incoming claim against related claims. This represents an initial processing stage of a larger scalable automated fact-checking solution which will become more effective as our universe of known and inferred ‘facts’ is expanded through human fact-checking and sourcing from single sources of truth databases such as Government Advisory Pages, WHO, CDC, NHS. Additionally, users are able to determine if images are manipulated via the Logically app. The analysis of the image is returned to the user within seconds with colour coded highlights on all areas the models believe likely to be manipulated. Users can forward the same image for fact-checking if they would like the content of the image itself verified. Random Sample Verification Logically conducts random verifications of claims fact-checked through our automation capabilities to ensure that any errors are detected and used to develop the algorithms which conduct the fact-check. Expert Fact-check Process We classify all incoming claims according to our taxonomy of claim types. This helps us quickly identify unverifiable claims which don’t require human attention, and prioritise claims according to their relevance, virality and estimated verification time. A moderator or supervisor will assign an incoming claim to one of the team based on the complexity of the claim and the level of research required for verification. Our fact-checkers are trained to follow carefully constructed processes according to the type of claim they’re verifying, which can be either statistical or text-based. We provide full justifications of our judgement, and links to relevant primary sources used to conduct the fact-check. Research and Conclusion All completed fact-checks must be signed off by a moderator before publication to ensure that the judgement is correct and the justification convincing and substantiated. Fact-checkers can escalate difficult claims to moderators and supervisors as needed, should they be unable to verify its accuracy. Judgement Finally, we publish our verdict, which will be either: True, Partially True, False, Misleading or Unverifiable. Logically’s verdicts have been carefully designed to encourage sharing and maximise virality; the judgement and claim are featured on an eye-catching image designed to look great on social media platforms. Through these viral verdicts, we hope to maximise the impact of each fact-check and help ensure that any false claims are debunked as broadly as possible. Accomplishments that we're proud of Covid-19 Related Selection of our fact-checks (over 500) - https://www.logically.ai/factchecks/covid19 Disinformation investigation - a shallow dive into patient zero for a lot of the current bio-warfare narrative https://www.logically.ai/publicreports/logically-covid-ggi-initial-investigation.pdf . Election Related Identifying Nation State threat actors during elections in India Identifying over 50,000 webpages containing false election related news Factchecking over 10,000 user requests in just 2 months during the election What we learned During the Hackathon: Building a Chrome Extenstion Deploying MLKit on Chrome Extension Distilling Deep Learning Model What's next for #ThinkLogically UX improvement for Browser Extension followed by testing and then a release We propose a public - private sector collaboration to monitor and triage all open communications related to the coronavirus, verifying and removing false and harmful content, and identifying any influence operations and for-profit or nation state disinformation campaigns. https://www.logically.ai/covid/ <div