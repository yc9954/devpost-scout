---
slug: "vern-kore-botathon"
url: "https://devpost.com/software/vern-kore-botathon"
title: "VERN powered "CARE RN" for Kore Bot-a-thon"
hackathon: "Kore.ai Botathon"
organization: "Kore.ai"
winner: true
words: 1152
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "user/social_worker"
---

# VERN powered "CARE RN" for Kore Bot-a-thon

> VERN AI is emotion recognition technology leveraged into the Kore.ai ecosystem to provide world-class emotional intelligence in real time. CARE RN is a bot to demonstrate capabilities.

[Devpost](https://devpost.com/software/vern-kore-botathon) · hackathon [[Kore.ai Botathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[patient_family]] [[social_worker]]

**stack** vern

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vern kore botathon

## Body

CARE RN. Empathy powered by VERN AI This bot is designed to help empathize when angry customers want to speak to the manager, giving time to assuage upset customers For demo purposes only, we've included VERN analysis that you can see on screen. For demo purposes only, we've included VERN analysis that you can see on screen. Bot in action Bot in action Turn angry conversations Into loyal customers Inspiration Who hasn't experienced an upset customer? What happens if the customer is upset (angry, fearful, or sad) and the bot doesn't recognize it? What happens if the customer doesn't receive empathy? Bad things happen. Customers get upset with automated assistants and lose their cool. Their agency is being challenged and the system makes them feel even more helpless. If they don't receive some empathy, the customer will not only choose a competitor, but may come after you with online reviews that hurt your business. What it does CARE-RN is for customers who are upset and want to speak to the manager! CARE-RN is a lightweight Kore.ai bot link powered by VERN AI emotion recognition; link that recognizes when someone wants to talk to the manager. It then responds to the level of anger appropriately, depending on the level of anger presented...low, medium or high. It is perfect in situations where a live person may be immediately unavailable, or where the operator wants to calm an angry customer down before a human has to deal with them. Low: Acknowledges user's anger. Assures them the situation will be handled soon. Medium: Same as low, but adds camaraderie and team building language. High: Same as medium, but adds an immediate "mirror" of the user's anger, focused on productive outcomes. If the user is expressing fear, it will detect and respond to medium and high levels of fear appropriately as well. Medium: Assuages fear, envisions positive outcome. High: Acknowledgement, reassurance that's why the bot is there, and it won't be much longer. The bot is triggered by someone asking for the manager... no pun intended. For demonstration purposes only, we've included the analysis as we get it from VERN so you can see that it's live, each result is unique, and we detect multiple emotions when present. (For full production models, the analysis will be able to be viewed by either user, or no user depending on the use case specified). CARE RN then recognizes the customer's intent and puts them into a waiting cue while an appropriate person can be found to help them. The user may be impatient, and fearful, so the bot ensures that the customer knows it's there for them and it won't take much longer. Since everyone tends to reveal what their ultimate goals are, it's essential to empathize with them when they tell you what they're here for. The bot responds that it shares the person's goals. This bot is useful for triaging an angry customer, and buying some time to find an appropriate representative who can handle the upset customer. How we built it We built this bot with the Kore.ai chatbot platform and an API call to VERN AI which provided the emotion recognition. VERN AI's emotion recognition is superior to most other forms of analysis and provides us with actionable data points when it came to customer's emotions. We decided to take Anger and Fear signals above & between a specific threshold. We used VERN AI's recommended stratification: 51-65% a low detection; 66-80% a moderate detection; and 81-100% a high detection of the emotion presented. From there, a "low," "medium," and "high" response was triggered when detections met the criteria. Anger and Fear were chosen for this demonstration, and we created responses appropriate for the emotion and level. Since VERN AI intentionally does not label entities, or inherently understand the context, the intents and entities in the Kore.ai system provide the additional context to understand the results. For instance, finding "love" signals in a phrase out of context may seem strange, but in the right context the emotion would be interpreted correctly. VERN AI was designed to be a generalized frame, with applications providing the necessary context and labeling entities specific for their own use case. This worked fantastically with Kore.ai ! Challenges we ran into We didn't experience a steep learning curve. The Kore.ai bot builder was exceptionally well thought out and executed. It was easy to use, and the support documentation and courses made it easy. We do have to give a disclaimer however, it wasn't the first time we've built bots nor been around the science of them. That does help tremendously when understanding concepts and methodologies. The most difficult part of the build was learning how to take action on the VERN AI analysis we got back. That took a little more than a day of fits and starts. But once we were able to port it in, and take action on the analysis, the wheels kept turning. (What else can we do with this??) We've just scratched the surface, having only had a week to build it. We can't wait to work with other teams in bringing this kind of empathy to conversational AI. Accomplishments that we're proud of Full disclosure: We developed VERN AI so seeing it being used as intended and performing well is satisfying. VERN AI's used in VR research, mental health applications, by counselors and therapists in live therapy sessions, to analyze content, and make actionable decisions. This was one of the first chatbots built with this latest VERN AI version. VERN AI was made to help automated systems detect human emotions in interactions. One of it's primary use cases is for chatbots and virtual assistants. It works in real-time and comes out of the box without a need to train it. VERN AI provides a generalized or common understanding of the emotions present in an "utterance," or "phrase," or "sentence" (Lexical). VERN AI being inside Kore.ai's bots, with the power of their "entities," "intents," "dialog tasks," really provides the user with the proper context in which to fully utilize VERN's capabilities. And it's only just the start. This little bot was a week in the making and has a ton of flaws but yet represents a breakthrough in automation. A little empathy can go a long way! What we learned Critical skills such as integrating VERN AI with Kore.ai . Being able to take action on emotions and using the NLU framework to do its thing while VERN AI did its thing too. We learned that Kore.ai is exceptional and we can't wait to learn and do more! We learned that this is just the beginning to what emotionally intelligent chatbots could provide. What's next for VERN Kore Botathon If you'd like to talk to us about VERN AI making your Kore.ai bot more emotionally intelligent, feel free to visit us and drop a line: link <div