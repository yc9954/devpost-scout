---
slug: "dr-store"
url: "https://devpost.com/software/dr-store"
title: "Descope & RavenDB Store"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 629
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Descope & RavenDB Store

> An interactive Online Store that Connects Products Buyers and Sellers around the world Powered by Descope, RavenDB, Paypal Payment Gateways, Google Maps etc.

[Devpost](https://devpost.com/software/dr-store) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** ajax-jquery, descope, google-maps, paypal, php, ravendb

## How they structured the write-up

- inspiration: combining force of descope & ravendb in building highly secured web applications
- what it does
- how to use the application
- how we built it
- what i need to see improved on ravendb api
- what we learned

## Body

Application Dashboard Descope Login Flow Products Ordering and Payment System Product Gelocation Mapping Product Gelocation Mapping2 Product Rating and Comenting System Published Products Sample Products Search Engine System Application Landing Page Inspiration: Combining Force of Descope & RavenDB in Building Highly Secured Web Applications While Descope is the Leader in the World of Web Application Authentication and Security & RavenDB is the leader in the World of NoSQL Database Management System. By combining this 2 Giant Tech, it becomes easier for Developers to easily build highly Secured and Database Scaleable application for Small, Medium, Large and Extremely Large Enterprise Applications..... No Need to worry about your Application Database Performance and Security Issues as Descope and RavenDB Gets you Covered In Summary, Great will be achieved when building RavenDB Scalable Application on top of Descope Highly Secured Authentication and Security management System.. What it does An interactive Online Store that Connects Products Buyers and Sellers around the world Powered by Descope, RavenDB, Paypal Payment Gateways, Google Maps etc. How to Use the Application 1.) Users Signup and Login with information are Stores and Queries to and from Descope 2.) Products Sellers can Publish their Products on the Platform with Data managed by RavenDB 3.) Users can access and be connected with various Nearby Products on Google Map with Data managed by RavenDB . 4.) Users can Like, Unlike, Rates, Comments and Review each of the products Published with Data managed by RavenDB . 5.) Search Engine System allow Users to Search Products by Categories, Location/Country etc.. with Data managed by RavenDB 6.) Products Buyers can Order items and make Payments to Sellers via PayPal with Data managed by RavenDB 7.) Each Products Sellers can easily build their Stores Fonts/Selling Pages with Data managed by RavenDB 8.) Users can Share Published Sellers Products on Facebook, Twitter,Linkeldn, Telegram, Whatsapp etc... with Data managed by RavenDB 9.) Load More Button Triggers Data Paginations thus allowing Users to Load More Content via RavenDB How we built it This Application was built with Descope, RavenDB, Curl, PHP, GoogleMap, yseditor, Bootstrap, Jquery-Ajax and much more. Descope I Integrated, 2 options for Signing Up and Login into the application via Descope 1.) Signup & Login by Descope Flow via SDK. FrontEnd Flow Integration: https://docs.descope.com/build/guides/gettingstarted/ This is handle by just 2 files descope_signup_login_flow.php & descope_html_auth_ajax.php 2.) Signup & Login via One Time Password OTP: Here is the list of API Used Users Signup: https://docs.descope.com/api/openapi/otp/operation/UserSignupOtpEmail/ Users Login: https://docs.descope.com/api/openapi/otp/operation/UserSigninOtpEmail/ Users Signup/Login Email OTP Verification: https://docs.descope.com/api/openapi/otp/operation/VerifyOtpEmail/ Users Session Validation: to ensure this session validation, I ensured that descope_session_validate.php file is dynamicaly called on every page accessed by Users.. https://docs.descope.com/api/openapi/session/operation/ValidateSession/ Users Signout: https://docs.descope.com/api/openapi/session/operation/Logout/ RavenDB RavenDB Database is used to create and manage all data on the platform: items table/Collection : used to store and query Products Data likes table/Collection : used to store and query like data on each published products unlikes table/Collection : used to store and query unlike data on each published products ratings table/Collection : used to store and query ratings data on each published products comments table/Collection : used to store and query comments/Reviews data on each published products orders table/Collection : used to store and query orders and payments data placed on each published products I leverage RavenDB Restful Client API Below. https://ravendb.net/docs/article-page/6.0/csharp/client-api/rest-api/document-commands https://ravendb.net/docs/article-page/6.0/csharp/client-api/rest-api/queries HTML5 Rich-Text Editor Used: https://github.com/yusufsefasezer/ysEditor.js Google Map Integration This help Users to easily locate all the nearby products shippable to users country/geolocations on Google Map Paypal Payments Integration This help Users to easily order and make payments to products Sellers via Paypal Payments Gateways What I need to see Improved on RavenDB API rest-api/queries does not currently supports Inserts and Update Statements . We will like those features in future.. What we learned RavenDB Restful Client API is very easy to integrate... <div