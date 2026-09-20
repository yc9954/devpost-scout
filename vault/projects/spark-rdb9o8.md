---
slug: "spark-rdb9o8"
url: "https://devpost.com/software/spark-rdb9o8"
title: "Spark"
hackathon: "Square's Local Community Hackathon"
organization: "Square"
winner: true
words: 624
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/structured_db"
---

# Spark

> Marketplace for square merchants to find collaborators and sponsors for their events seamlessly.

[Devpost](https://devpost.com/software/spark-rdb9o8) · hackathon [[Square-s Local Community Hackathon]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[structured_db]]

**stack** nextjs, prisma, react, square-checkout, squareapi, supabase, tailwind, trpc, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what square apis did we use to build it?
- challenges we ran into
- accomplishments that we're proud of

## Body

Browse merchants Home page - your events Collaborate on an event Event page Future events Sponsor an event Inspiration The inspiration for Spark came from recognizing the challenges small business owners face in networking and establishing partnerships for events. This insight was gained through conversations with 4 small business owners, like Cheyenne from Little Oat Collective in North Carolina. Cheyenne highlighted the difficulties in finding and collaborating with new partners using existing platforms, which are not specifically tailored for local business collaborations. These challenges include the repetitive nature of partnering with the same businesses and the significant time investment required to build new business relationships. Spark was designed to address these issues by providing a dedicated platform that facilitates easy connections between local businesses for sponsoring and collaborating on events. What it does Spark is a marketplace that allows small businesses to sponsor and collaborate on each other's events easily. It offers a user-friendly platform where businesses can create events, specify their needs for sponsors and collaborators, and browse potential partners by category, business type, and location. Spark provides detailed profiles of businesses, including their past event participation and other relevant stats, which helps users make informed decisions when choosing collaborators or sponsors. The platform is designed to enhance visibility for local businesses at events, providing them new revenue opportunities and ways to engage with the community. Additionally, Spark supports a responsive interface that works seamlessly on both web and mobile devices, enabling users to manage their event needs on the go. How we built it We started by doing user research by talking to local businesses. From the pains they faced we pattern matched and tackled the issue we thought were going to have the largest impact. Sophie and Landon decided on the MVP roadmap which Landon then designed. Sophie then worked on the schemas and the backend while Landon hooked up most of the frontend. What Square APIs did we use to build it? Square auth Was required to get an access token that had permissions to use all the other APIs Square merchant API To get information about a merchant and sync the information onto our marketplace, this information would then be displayed in various places to give context to other businesses on our marketplace Square locations API All the location information about a business was information for the browse merchant page. This would help businesses find collaborators who were in their city for example or if they needed a vendor that sold food at their event they could be able to filter by the MCC code on Spark's browse merchant page. Square checkout - Payment links, webhooks If a business wants to be a sponsor at an event they have to pay through our platform which opens up the square checkout. Square payments We then grab the orderId from the webhook and then fetch the payment link id we created from Square to update the correct payment link in our database. Challenges we ran into Webhooks were quite difficult to test and took us some time to configure. We wished that Square also allowed Payment links to be reused like they can be in the merchant dashboard, we thought this was the case and would have made things a lot easier. Accomplishments that we're proud of We were super happy with the focus we had in solving the problem described above. With the focus we had, we were able to build a really good solution to this one big problem small businesses were facing. This meant using the exact APIs needed and not using APIs unnecessarily. We were also very happy with the design and it's responsiveness. Our product works even better on the go which was by design. <div