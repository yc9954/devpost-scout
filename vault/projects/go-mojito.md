---
slug: "go-mojito"
url: "https://devpost.com/software/go-mojito"
title: "Go Mojito"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 1106
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Go Mojito

> Go-Mojito is a fully customizable and modular web framework that allows you to write projects that do not hard-depend on any router, template engine, cache or logger implementation.

[Devpost](https://devpost.com/software/go-mojito) · hackathon [[Go Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** go, golang

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for go mojito

## Body

Go-Mojito helps keep your app maintainable and away from dying dependencies. No matter what router implementation you want to use... ... your app implementation will stay the same. Even if you change it down the line. Render pages with the RendererContext. Of course, the renderer can be swapped out just as easily as the router. One-time handler introspection allows for dependency injection, you can even register custom dependencies. Inspiration Every time we wanted to start a golang web project, it was a hassle to pull all of the dependencies in, and often they were not super easy to use and required helper functions that were copied from project to project, which is not a great thing to do. One of the logging libraries we used a lot eventually announced their discontinuation, which meant that we would have to migrate all the logging to a new library. Not a fun task to do as logging is usually all over the place. Then a better router appeared on the market, but changing to that router would break all our handlers, some of the helper functions, surely all middleware and chances were the interface would not be the same either. We already had our own web frameworks in PHP we created years ago, so we decided to do it all again but in Go. We had a few core goals in mind: It should be easy , it should be modular , it should be clean and of course it should deliver good performance (Varies on the implementations too of course). What it does Go-Mojito decouples your application code from specific dependencies by providing easy-to-use interfaces for routing, logging, caching and template rendering. Together with dynamic handlers that support dependency injection and custom request arguments the app code stays clean and easy to maintain. Examples: Your project is currently built using router "A" and logger "B". Most router and logging libraries differ from each other that makes it hard to just switch an app from one library to another. Had you used Mojito, you would change one import and one line of code in your main file per library. So a total of 4 lines. More on that here. You have dependencies like database connections or similar that you want to use in your handlers. With mojito, you just have to register them once on startup. Once registered, these dependencies are available immediately in all handlers and middleware, regardless of your chosen router. You can also have multiple dependencies of the same type by using named dependencies. See here for more Info! We built a server-side analytics module that works with Plausible to allow for privacy-friendly stats tracking. To allow developers to track custom events in their handlers, a custom request argument was needed. If used, the plausible extension registers a request argument factory for plausible.Context . This means, that handlers can now use plausible plausible.Context as an argument. Since the plausible Context is an extension of mojito.Context , the performance impact is minimal since the object just has to be wrapped. How we built it Go-Mojito is fully functional without any additional dependencies/implementations. It was always the goal to keep the mojito core as close to the standard library implementations that Go provides. So by default Go-Mojito ships with implementations for router, template renderer, logger and cache. The router is based on the http package, the template renderer is using go templates , the logger uses fmt and the cache is an in-memory map -based cache. Currently there are 2 dependencies left in the core that are not maintained by us or are provided by golang, which will be removed in the future. Dependency Injection is achieved by using the Infinytum Injector package, that was also developed by us. All router implementations use the Go-Mojito provided implementation of Handler which contains logic to introspect a given function for request arguments and dependencies. The router does not have to worry about that at all, it just has to call the handler when a request comes in. This is why dependency injection, custom request args and middleware is always consistent across implementations. The shortcut function like mojito.GET also use the dependency injector to resolve the default router implementation to register the route on. The idea is that no function really has to know which implementation is currently present, as long as one is present. Challenges we ran into We had a hard time separating the interfaces and helper functions that reside in the main mojito package and the default implementations, as they relied on each other (Import cycle). We really did not want the default implementation or other specific code in the main package, as its not necessary 99% of the time (You only need some things when making your own router implementation for example). Ultimately we found a good solution by having the public interfaces extend the implementation-critical interfaces in the sub packages. That allowed us to remove any dependency from the sub packages to the main package. Accomplishments that we're proud of We are really proud of the overall modularity and decoupling of the application code to the implementation. During development we moved around a lot of files, even re-did the whole thing at one point. Yet the app barely noticed any of that, thanks to the stable interfaces they use. The biggest change we had to make in one app was to switch from mojito.Request / mojito.Response to mojito.Context , and even that was not strictly necessary as a compatibility file ensured old handlers would still work the same as before. This showed us that the core idea and concept of this project are very sound and resilient to changes, even if these changes are done on the core repository. What we learned During this project we explored Go Generics for the first time. For example the introspector and injector both use generics. We also made great use of generics in Infinytum Structures which made it easy to create custom lists and tables that were easy and type-safe to use. We also learned how to split up code in a better way to prevent import cycles in the main package, while keeping it clean. What's next for Go Mojito We want to extend the core with interfaces for metrics (Think prometheus, influx) and improve the test situation of the project. While we have some tests in place, its not enough yet. We also want to expand our documentation on the project, so its even easier for other people to use. Also we definitely want to tag a stable version for core and our recommended stack soon. <div