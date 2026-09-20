---
slug: "submatic-bookings"
url: "https://devpost.com/software/submatic-bookings"
title: "Submatic Bookings with Square"
hackathon: "Square Unboxed Hackathon"
organization: "Square"
winner: true
words: 700
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/web_dom"
---

# Submatic Bookings with Square

> Allowing Square Merchants to sell memberships and packages online for bookable items. Customers can book online using credits that are part of a membership or package.

[Devpost](https://devpost.com/software/submatic-bookings) · hackathon [[Square Unboxed Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[web_dom]]

**stack** bootstrap, codeigniter, javascript, php

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for submatic bookings

## Body

Inspiration I started Submatic to help retailers, restaurants, and service businesses boost customer retention and loyalty. I believe that subscription membership can be very impactful and a powerful influencer of customer behavior. We integrated with Square to give Square merchants the ability to leverage additional subscription and membership tools. What it does For this Hackathon I extended the functionality of Submatic to allow for the purchase of bookable services through a subscription or package. For example if a salon wants to create a membership where members pay monthly and receive 1 cut & dry per month, 1 blow out per month, and 10% off beauty products they can do that using Submatic. With a Submatic subscription, the customer will be billed automatically for these services and then be able to book directly through Submatic without having to submit credit card information or payment at the time of booking. While a merchant might require a credit card or pre-payment to book through their website, we bypass that step for members and track their bookable credits. Any product or discount that is part of a subscription but which is not a bookable item can be redeemed at the POS. How we built it For the booking component we relied heavily on the Square API's booking logic. We limit the amount of data that we're storing to keep things streamlined for merchants. The same logic applies across all categories of our Square integration including Customers, Catalog, and Payments. The code is written on the Codeigniter PHP framework. Challenges we ran into Timezones are fun and one of the many types of options that exist when dealing with a calendar. Square's booking engine is a lot more advanced than I had expected with many different options for sellers with regards to how they manage staff, calendars, and customers. It is challenging to think about all of the possible iterations that exist. For this integration we did have to build our own front-end booking interface. Our UI is not as clean as Square's and it will take some time for us to refine it. It would be nice if we were able to leverage some of the front-end functionality that Square has created for booking which can be embedded on Square merchant websites. One minor thing I noticed that caused some confusion on our side is that in order for the Booking API with writable permissions to work the store must have a credit card added for their Square subscription. It does say in the documentation that the seller must have the "have the Appointments Plus or Premium subscription plan". However requests to a store that is on a free trial of one of these plans but has not yet submitted a credit card will fail. Occasionally when processing payments with Square.js we encounter long wait times. I am not sure if that is happening on the Sandbox only, but that is where we experience the issue. It has not been a big issue for us but I'm just including it here as an FYI. For any other pressing issue we have typically been able to find solutions quickly. I have built integrations with Square, Shopify, BigCommerce, WooCommerce, Stripe, and various other payment platforms. Square is among the best systems to work with from the developer side. The Square developer community, resources, API Explorer and Developer Forum are great resources and I appreciate the investment that Square makes in these areas - thank you! Accomplishments that we're proud of I launched this company this year and already have a number of Square merchants on board as well as others using a separate POS integration. I'm proud to have been able to make that progress and to continue to build out the Square integration to help merchants. What we learned It always takes more time than you think it will. I already knew that but I also sometimes forget it (so thanks for the 24 hour extension). What's next for Submatic Bookings We know that memberships and subscriptions are already somewhat established in the spa/salon space. We hope to be able to work with more Square merchants in this space with the added booking functionality. <div