---
slug: "id-hub-oi719w"
url: "https://devpost.com/software/id-hub-oi719w"
title: "ID Hub"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 842
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/web_dom"
---

# ID Hub

> Helping developers adopting modern identity practices like SSO and JWTs via Postman.

[Devpost](https://devpost.com/software/id-hub-oi719w) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** angular.js, java, oauth, openid, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for id hub

## Body

Inspiration As developers, we usually inspire to create APIs or consume an external one. Most innovative ideas those days are usually based on top of pre-existing services. The challenge we experienced was double: how to consume easily an API in Postman that has a highly secured API ? How can we expose our API the same way? Using pre-script, you can workaround the first one. Although it seems usually a bit complex to use a JWT external library inside postman and has limitations, like not exposing your public keys externally. This is the case with for example Open Banking APIs, highly protected with OAuth2 and JWT and it seems that this kind of protection will become the norm. ID Hub JWT comes from that experience. We wanted to offer a more Postman experience by simply externalising the basic usage of JWT to an API. This way, we could leverage Postman functionalities to simply manipulate JWTs, without extensively use pre-scripts. Maybe not everyone is confortable to use IDHub JWT online API, for security reason maybe, we made this service open source and dockerised. This way you can run it locally and still use Postman the same way to manipulate JWT The second APIs we wanted to offer was around Single Sign-on, things we experienced every day with google login. One of the most basic needs of an application, is to provide a way to authenticate users, the classic login page. Too many times, as developer, we developed such login page and instead, we should all use SSO. In the spirit of helping developers building great application and focusing on their ideas, and not a login page, we created ID Hub SSO: a simple way to offer SSO using OpenID connect, with many providers in one go. We wanted to make SSO easy to use, accessible and fast to put in place. We also had two APIs from a previous project, ID Hub checker and ID Hub wallet. Following the same ideas of making identity easy to use, those two APIs helps you leveraging identity for use-cases from the real world. Even though we usually design software for digital use, the reality is that we live in a physical world too where we also need to identify ourself. For those developers who wanted to offer services that could help you in our daily basis in the real world, we wanted to offer them to identify their users in a secured and easy way too. We got a nice presentation about this APIs and what you could build from it in https://idhub.io What it does For web use-cases: SSO and JWT are now becoming essential parts to any web applications. Those collections will help you designing secured application in respect to GDPR. SSO: how to adopt Single Sign On in your website with multiple identity providers like Google, Github, Meetup, without any boiler plat integration JWT: manipulate JSON Web Token directly in Postman. Skipping the challenge of using Javascript pre-script in postman and instead use REST calls For physical use-cases: Not everything is online, you may need to interact with your users via another interface than web or even in person. Those collections will help you making the bridge in managing identities between the digital and physical world. Wallet: Private API from IDHub to help your users generate identity on their phone and scannable. Perfect for use-cases where you got a physical interaction How we built it We developed them in Java and deployed them in CI/CD to GKE Challenges we ran into Making simple, something that is technically complex. We wanted our postman to be ready to use without having to read much our documentations. We had some challenged to setup the Postman authorization in such a way anyone can use the postman collection and not having to worry about the authorization. At the end, you just setup 2 environments variables with your client id, client secret and you are all set. Accomplishments that we're proud of Implementing something that we find useful as developers. It solves challenge that we met as developers when we build applications and been able to share this experience and make the journey of others developers easier was important for us. On top of that, we somehow help developers adopting more secured APIs and helping them protecting their own applications. With all the privacy debates we hear those days, re-enforce with GDPR, services like IDHub JWT and SSO will really help everyone building great applications without compromising security or privacy. What we learned An occasion to re-enforce our knowledge around Postman and their new public workspace features. Seems we dont need to build developer portals now, which is great for exposing APIs fast and usuable. What's next for ID Hub We want to keep continue contribute in the open source space. We will promote our APIs now and write articles on how to implement secured APIs and SSO. We created ID Hub in the occasion of hackathon, to help developers and we will keep going in that spirit. <div