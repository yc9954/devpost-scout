---
slug: "one-database-manager-1dbm"
url: "https://devpost.com/software/one-database-manager-1dbm"
title: "One Database Manager (1DBM)"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 361
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/structured_db"
---

# One Database Manager (1DBM)

> Secure credential storage and access to popular SQL and NoSQL cloud databases from a single source, via REST APIs.

[Devpost](https://devpost.com/software/one-database-manager-1dbm) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[education]] [[finance_payments]] [[transportation]]
**user** [[developer]] [[educator_student]] [[frontline_worker]]
**substrate** [[structured_db]]

**stack** azure, cassandra, cosmosdb, elasticsearch, express.js, gcp, heroku, ibm-cloud, mongodb, mysql, node.js, postgresql, redis, sql-server

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for one database manager (1dbm)

## Body

Inspiration Developers often find themselves in a situation where they are away from their workstations, and require access to their database, but do not have all the credentials at the moment, or access to a machine with the essential drivers installed for connecting to a database. The services available for this problem in the market are either paid and/or require a lot of time to setup. These services are also not meant for students or young developers, with relatively new or small projects. That's where 1DBM comes into picture. What it does One Database Manager is a key-store for database credentials, and a common platform for querying databases, rolled into one. With 1DBM, you can: Store all of your database credentials in one place Access credentials using a single password, just like a password manager. Get the uniquely assigned database id, and query any of these databases using REST APIs and eliminate the need of database drivers. Supported Platforms: [x] MongoDB [x] PostgreSQL [x] MySQL [x] MSSQL/Azure SQL server [x] Redis [x] Cassandra (Astra Datastax not supported) [x] IBM Db2 [x] Elasticsearch Not available for on-premise database solutions that are not exposed for remote usage. Credential storage is optional. Credentials can also be provided during queries. How we built it The server is written in Node.js, and makes use of JavaScript drivers provided by the platforms listed above. All drivers have been re-implemented to generalize the querying process. This allows users to utilize almost every feature provided by the driver in a 1:1 manner. Challenges we ran into Lack of free-tier services in the market. (MongoDB, Redis, Db2 and PostgreSQL were tested using free-tier services) Setting up IAM for limited database access to testers. Accomplishments that we're proud of Secure and encrypted credential storage, which is completely optional (for users that have security concerns) 1:1 database driver re-implementation for RESTful access What we learned Various database query languages Advanced language syntax Various cloud database technologies available in the market What's next for One Database Manager (1DBM) Adding a web interface for accessing this service Adding more functionality to already implemented services Adding support for Oracle MariaDB Neo4j Couchbase and more... <div