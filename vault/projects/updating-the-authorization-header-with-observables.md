---
slug: "updating-the-authorization-header-with-observables"
url: "https://devpost.com/software/updating-the-authorization-header-with-observables"
title: "Updating the Authorization header with Observables"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 346
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
---

# Updating the Authorization header with Observables

> Learn how to subscribe to changes of a value from any React component using the Observer pattern, Dependency Injection and the React useContext hook.

[Devpost](https://devpost.com/software/updating-the-authorization-header-with-observables) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]

**stack** inversify, react, rxjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for updating the authorization header with observables

## Body

Inspiration Modern applications that send authenticated requests to a server will likely do it with a JSON Web Token string value in the Authorization header of the request. The problem is that the token is not always directly available in the component were we instantiate the client. What it does This simple React application exemplifies how to subscribe to changes of a certain value across the entire components chain. How I built it The application uses inversifyJS to create a DependencyContext that can be used with the React useContext hook from any component. With the DependencyContext you can get the AuthTokenModel dependency and subscribe to the changes of an authToken value that may be returned from the server. The authToken value is later passed to a GraphQL client component and the Authorization header will be set with the value if it exists. Challenges I ran into By developing React Native applications, I came across the challenge of updating the client's Authorization header whenever the server returned a valid JWT token upon a request. The problem is that a complex React application will have a large components' chain under a certain navigation stack. So how to keep the client aware of a JWT token that's been returned from a call in another component in the chain and update the headers accordingly? Accomplishments that I'm proud of Understanding the Observer pattern and Dependency Injection pattern gave my projects' architecture a boost of simplicity and reliability. What I learned With this tutorial I expect other developers to feel empowered (as I do) by the use of the DependencyContext and the Observable subscriptions inside their React and React Native applications. What's next for Updating the Authorization header with Observables Go ahead and extract the parts of the code of this tutorial to inject your own dependencies in your components. Simplify your authentication flows by using the Observable subscriptions as exemplified here. Your company and your users will experience smooth screen transitions and you as a developer will be more confident about what is happening in each of your components! <div