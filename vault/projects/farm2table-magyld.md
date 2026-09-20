---
slug: "farm2table-magyld"
url: "https://devpost.com/software/farm2table-magyld"
title: "Farm2Table."
hackathon: "GNEC Hackathon 2025 Fall - Compete For UN-Affiliated/NGO Internships & Prizes"
organization: "Global NGO Executive Committee"
winner: true
words: 850
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/structured_db"
---

# Farm2Table.

> Connecting farmers to customers in seconds via farm2table web application

[Devpost](https://devpost.com/software/farm2table-magyld) · hackathon [[GNEC Hackathon 2025 Fall - Compete For UN-Affiliated-NGO Internships - Prizes]]

## Facets

  <sub>weak: realtime_stream</sub>
**domain** [[agriculture_food]] [[finance_payments]] [[supply_logistics]]
**user** [[frontline_worker]] [[general_public]]
  <sub>weak: legal_professional</sub>
**substrate** [[structured_db]]
  <sub>weak: financial_record, geospatial, web_dom</sub>

**stack** flask, html5, paystack

## Body

landing page web app Inspiration The inspiration for Farm2Table came from a stark contrast I observed in my own community: local farmers struggling to find buyers for their fresh, high-quality produce, often leading to significant waste, while at the same time, many families and consumers struggled to access that same fresh food. Globally, this disconnect results in an astonishing 1.3 billion tons of food being wasted every year . This isn't just a logistical problem; it's a direct barrier to achieving UN SDG 1 (No Poverty) for small-scale farmers and SDG 2 (Zero Hunger) for communities. I was inspired to use technology to build a bridge across this gap—to create a simpler, smarter, and more direct path from the farm to the table. What it does Farm2Table is a web platform that directly connects local food producers (sellers) with consumers (buyers), creating an efficient and transparent marketplace. For Sellers (Farmers): It provides a simple, easy-to-use dashboard where they can create a profile, list their products, set prices, and manage their inventory in real-time. This gives them direct access to a market they might otherwise be unable to reach. For Buyers (Consumers): It offers a clean, searchable interface to discover local producers, browse available fresh produce, and purchase goods directly through a secure payment gateway (integrated with Paystack). Key Innovation - The "Future Harvest" Marketplace: Our most unique feature allows farmers to pre-sell their crops and produce before they are even harvested. This guarantees income for the farmer, dramatically reduces the risk of waste, and allows consumers to reserve the freshest possible food at a fair, locked-in price. How we built it We built Farm2Table as a functional Minimum Viable Product (MVP) within the one-week hackathon sprint, using a rapid and reliable technology stack to ensure feasibility and speed. Backend: The application is powered by Python using the Flask micro-framework. This allowed us to quickly build a robust backend with user authentication, session management, and CRUD (Create, Read, Update, Delete) functionalities for producers and products. Database: For the prototype, we used SQLite with SQLAlchemy as the ORM. This choice enabled a zero-configuration setup for rapid development, while the SQLAlchemy abstraction layer ensures the application can be seamlessly migrated to a production-grade database like PostgreSQL with a single line of code change. Frontend: The user interface was built with clean, semantic HTML, CSS, and vanilla JavaScript . The focus was on creating a simple, intuitive, and responsive design that is accessible to users of all technical skill levels. Payments: We integrated the Paystack API to handle transactions, providing a secure and reliable payment experience for consumers. Challenges we ran into The primary challenge was time. Building a two-sided marketplace (for both buyers and sellers) with a full authentication system and product management in under a week was a significant undertaking. We had to be extremely disciplined with our scope, focusing only on the most critical features that would prove the core concept. Another challenge was designing the database schema in a way that was simple enough for a prototype but robust enough to support our future plans, such as the "Future Harvest" pre-selling feature. Accomplishments that we're proud of We are incredibly proud that we were able to build a fully functional, end-to-end prototype —not just a collection of mockups. We successfully implemented: A complete user registration and login system with distinct roles for Buyers and Sellers. A functional dashboard for sellers to manage their own products. A live product browsing and discovery page for all users. A successful integration with a real-world payment API (Paystack). Most of all, we are proud that this working demo proves the technical feasibility of our idea and serves as a solid foundation for a platform with the potential for real-world impact. What we learned This hackathon was a powerful lesson in scoping and execution . We learned how to prioritize features ruthlessly, focusing on the "Minimum Viable" part of the MVP to deliver a working product on a tight deadline. We also gained valuable hands-on experience in integrating a third-party payment API and designing a multi-user authentication system from scratch. Most importantly, this project reinforced our belief that even a small, focused application can be designed to tackle massive global challenges like poverty and food waste. What's next for Farm2Table This hackathon project is just the beginning. Our vision is to grow Farm2Table into a global network of local food ecosystems. Our post-hackathon roadmap is clear: Phase 1: Refine & Beta Test (4 Weeks): We will incorporate the judges' feedback, polish the user interface, and onboard our first 100 users (50 farmers, 50 consumers) for a closed beta test to gather real-world data. Phase 2: Public Launch & Marketing (4 Weeks): We will deploy the application publicly, migrate to a production database, and begin targeted digital marketing campaigns to build our initial user base in our first launch city. Phase 3: Scale & Feature Expansion (Ongoing): We will begin implementing our "Future Harvest" feature and integrate AI-driven tools for supply chain optimization (e.g., delivery route planning) as we expand to new regions and countries. <div