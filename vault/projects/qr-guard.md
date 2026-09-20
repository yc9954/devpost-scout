---
slug: "qr-guard"
url: "https://devpost.com/software/qr-guard"
title: "QR-Guard"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 630
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# QR-Guard

> QR-Guard is a specialized security application designed to mitigate the risks associated with Quick Response (QR) code interactions on mobile devices

[Devpost](https://devpost.com/software/qr-guard) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[accessibility]] [[agriculture_food]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[security_privacy]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** expo.io, nativewind, react-native, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for qr-guard

## Body

Inspiration The rapid adoption of Quick Response (QR) codes for everything from restaurant menus to payment portals has created a dangerous blind spot in mobile security. We observed a growing trend of "Quishing" (QR Phishing), where attackers exploit the inherent opacity of QR codes to direct users to malicious sites. A human cannot visually distinguish between a legitimate URL and a credential harvester, especially when link shorteners are involved. We wanted to build a tool that restores transparency and agency to the user, effectively acting as digital "protective eyewear" for the physical world. What it does QR-Guard acts as a security interceptor between the physical QR code and the mobile browser. Instead of immediately opening a scanned link, the application: Decodes the Matrix: Instantly translates the QR pattern into a readable string. Performs "X-Ray" Expansion: If the link uses a shortening service (e.g., bit.ly), QR-Guard autonomously traces the redirect path to reveal the final destination URL without downloading potentially malicious content. Analyzes Risk: It applies heuristic algorithms to detect homograph attacks (spoofing), suspicious top-level domains, and known phishing patterns. Enforces a Decision Point: The user is presented with the full, unmasked URL and a clear "Safe" (Green) or "High Risk" (Red) status, requiring an explicit confirmation before the link can be opened. How we built it We engineered QR-Guard using a modern, high-performance mobile stack: Expo (React Native): Chosen to ensure a native, buttery-smooth 60fps experience on both Android and iOS with a single codebase. NativeWind (Tailwind CSS): Leveraged for rapid UI development, allowing us to create a high-contrast, "cyberpunk-inspired" aesthetic that communicates security status through clear visual cues. Custom Network Logic: We implemented a custom URL resolution engine using HTTP HEAD requests. This allows the app to follow redirect chains to discover the final URL headers while explicitly avoiding the download of the response body, preventing the execution of drive-by scripts or malware. Heuristic Engine: We developed a local analysis module capable of real-time string parsing to detect common obfuscation techniques used by attackers. Challenges we ran into One of the primary technical hurdles was implementing the URL expansion safely. Simply fetching the URL to see where it leads would expose the user's device to the very malware we aimed to prevent. We realized that performing a standard GET request was too risky. We overcame this by implementing a strict HEAD -only request strategy, which retrieves the metadata (including the final destination URL) without accepting the payload. Additionally, handling the asynchronous nature of network states while maintaining a responsive UI required careful management of React state and side effects. Accomplishments that we're proud of We are particularly proud of the "Safe Tracing" architecture. Successfully implementing a mechanism that can unmask a shortened link without "visiting" the site was a significant win for user safety. Furthermore, achieving a UI that feels both professional and futuristic—effectively communicating "security" without being dry or clinical—was a major design milestone. The seamless integration of complex string analysis within the React Native runtime works instantaneously, providing immediate feedback to the user. What we learned This project deepened our understanding of mobile security vectors and the mechanics of HTTP-based attacks. We learned extensively about the intricacies of URL redirection codes (301 vs 302) and how they can be weaponized to hide final destinations. On the development side, we gained valuable experience in optimizing NativeWind for production-grade mobile applications and managing camera hardware permissions within the modern Expo ecosystem. What's next for QR-Guard Our roadmap for QR-Guard includes integrating third-party threat intelligence APIs (such as Google Safe Browsing) to augment our local heuristic analysis. We also plan to implement a secure history log, allowing users to review scanned codes later, and a "Report" feature to enable community-driven flagging of malicious QR codes found in public spaces. <div