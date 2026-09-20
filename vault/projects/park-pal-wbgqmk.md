---
slug: "park-pal-wbgqmk"
url: "https://devpost.com/software/park-pal-wbgqmk"
title: "Park Pal"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 605
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Park Pal

> The Airbnb for Parking

[Devpost](https://devpost.com/software/park-pal-wbgqmk) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**domain** [[finance_payments]] [[legal_justice]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** claude, code, css, mapbox, next.js, novus, postgresql, react, shadcn/ui, stripe, supabase, tailwind, typescript, v0

## How they structured the write-up

- what we built
- who it's for
- what makes it distinctly ours
- tools we used
- what we learned shipping it

## Body

What we built ParkPal is a peer-to-peer parking marketplace, think of it as the Airbnb for driveways. Homeowners with an unused driveway, carport, or garage list it; drivers who need parking near a stadium, a campus, or a packed neighborhood find it on a map and book it by the hour. The space already exists and ParkPal just makes it findable, bookable, and safe for both sides. It's a real, deployed, two-sided marketplace. It includes core functionality such as being able to search spots on a live map, filter by type, price, covered, or EV charging, open a listing with photos and a verified host, request a booking, get approved, pay, and have the exact address unlocked. Hosts can list a spot, review who's requesting it, and approve or decline before anyone parks on their property. Who it's for Two sides of one problem in dense cities like Seattle. Drivers heading to Seahawks and Mariners games, concerts, UW, or any event that is in high demand. A quick note we want to add is that though we are starting in Seattle, we are building the product to be used in other cities in the future. As referenced by our sub stack article, there is a lot of regulations to map out. Homeowners have driveways that go empty for most of the day and would happily earn from them, we believe that if they trusted the people pulling in, they would be willing to list them up. We validated this with 260+ surveys of drivers and homeowners, and the central finding shaped the whole product: homeowners didn't ask "who needs parking?", they asked "what happens if something goes wrong?" What makes it distinctly ours Two things. First, we didn't guess where demand is, we mapped it, building a companion GIS demand tool that overlays parking-ticket and event data to pinpoint the blocks with the most parking pain. Second, because the real barrier was trust, we built a trust framework before we built anything flashy: ID and license-plate verification, host approval on every booking (letting a stranger onto your property is not a one-tap action, the host sees who's coming first), timestamped check-in/check-out photos, and exact addresses kept private until a booking is confirmed. The less exciting the feature sounded, the more it mattered. We've also begun the harder, non-technical work of making a residential parking network legal, securing a letter of intent from PMI Arka, a property management firm, as a path to onboarding supply at scale. Tools we used Built with v0 for UI design, Claude Code as the primary builder, on a stack of Next.js, Supabase (Postgres, auth, storage), Stripe (payments), and Mapbox for the map. Deployed on Vercel. Novus is installed for product analytics so we can see how real users move through the app. What we learned shipping it A month ago, "deploy a two-sided marketplace with auth, a database, maps, and payments" sounded like a year of work and a team. However, after completing this challenge and exposing ourselves to the revolutionary power of AI tools. We were able to get beyond the technical work and into the product development. What AI exposed is that the hard part was never the code. It was the product judgment: what to build first, what to cut, when "good enough to ship" was actually good enough. Deciding that host-approval mattered more than a slick instant-book. Deciding a flawless booking flow was worth more than a beautiful but empty inbox. When anyone can build, the thing that separates a demo from a product is knowing what's worth building. That part is still on us. <div