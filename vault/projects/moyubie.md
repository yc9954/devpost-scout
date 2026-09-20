---
slug: "moyubie"
url: "https://devpost.com/software/moyubie"
title: "Moyubie"
hackathon: "TiDB Future App Hackathon 2023"
organization: "PingCAP"
winner: true
words: 1048
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Moyubie

> Talk to AI and your friends in private, and get ads free news feeds!

[Devpost](https://devpost.com/software/moyubie) · hackathon [[TiDB Future App Hackathon 2023]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** dart, flutter, openai, tidbserverless

## How they structured the write-up

- inspiration
- what it does
- how we built it
- is tidb serverless necessary?
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moyubie
- try it out

## Body

Share a room and invite others to join Get your news Browse news on your tablet AI generated news that you may interested Set open AI access key & TiDB Serverless connection token The architecture of Moyubie Moyubie Project link: https://github.com/flowbehappy/moyubie Inspiration For this hackathon, we really want to build something we will use daily. And the apps we are currently daily using include messaging apps and news app. And some facts we don't like: Although we already have many IM apps (Whatsapp, Snapchat, Instagram, Wechat, etc), they are all controlled by companies or third parties. And our own messages data is controlled by them. News feeds are great, like Quora and TikTok, but the problem is that our data and the recommendation algorithms are totally controlled by big companies. We are in information cocoon, surrounded by bias information and ads. We think the only way to avoid that is to build a communication and news feed app which all parts of it are completely owned by individual. Among the features of TiDB Serverless, we favor scalability and global accessibility the most. So TiDB Serverless has the potential of being a connector between everybody. And with AI, we can make the connection much more interesting and motivative. What it does Moyubie is a cross-platform AI powered IM (Instant Messaging) App. Users can chat to anyone in a chat room in a private environment. It is a convenient AI chat client. Chat messages are stored in TiDB Serverless and synchronized between different devices. There is no server side required. Chat messages are secure and completely owned by users. All chat messages are stored in users' TiDB Serverless clusters, which only accessible by users themselves. A news list powered by AI, no ads. Supported platforms: iOS, Android, MacOS, Windows, Linux How we built it Cross-platform We use flutter to build the app, so that it can be cross-platform naturally and run on any device. Remote communication The chat messages are stored in TiDB Serverless, so other users from anywhere can access them instantly. Is TiDB Serverless necessary for each user? TiDB Serverless is not strictly required but strongly recommended. Only the users with own TiDB Serverless cluster can (1) Create their own chat room. The users without TiDB Serverless cluster can only join other users' chat room; (2) Store chat messages remote and then synchronize between different devices. How to do instant messaging? Messages are written into chat room table, and other users in the same room periodically (1s) select the chat room table in TiDB Serverless to fetch new messages. Create chat room Only the users with their own TiDB Serverless cluster can create new chat rooms. For each chat room, Moyubie create one particular table in the TiDB Serverless cluster to store the messages. To control the accessibility, Moyubie create one particular user with only SELECT and INSERT accesses on the table. With the host, port, user and password, other users can write and read messages on the chat room table. Share chat room Moyubie create a unique token for each chat room. The token is base64 encoded string, which contains host, port, user and password, roomId, roomName. Performance Moyubie cache all messages on local devices with sqlite. So TiDB Serverless only have to return the latest messages. How AI do recommendation? Each time a user ask AI anything, AI will analyze the question and generate some tags for the user. Moyubie stores the tags and use them to do news recommendation next time. The more user ask, the more accurate. It is very simple but affective. We will further investigate more useful algorithm later. App activity analytics We integrated Google Analytics to have full insights of our app. It could be very useful after we published it to app stores. Is TiDB Serverless necessary? Yes. Here are the criterions for the remote database of Moyubie: Global accessibility and full accessibility control policy. Strong consistency. Otherwise it will be too challenging to implement a reliable app. Secure serverless database, with unlimited scalability. Moyubie has no server side so there is no way to maintenance the database. A HTAP database. We would like to provide high-end paid features which require some analytic jobs. And there is no way to set up complex workloads for Moyubie, we totally count on the remote database services. Challenges we ran into It is very challenging to finish an IM app in a short time. The four of us are all backend developers and has less experience on frontend programing. We only started the project about 3 weeks before the deadline and can only take advantage of your spare time after work. There are several aspects that make this task difficult: Unpredictable user operation and network environment. For example, since we connect directly to the AI service and TiDB Serverless, the connection could be break down in any steps. And users could kill the app in any seconds. We pay much attention to make sure not breaking the data's consistency. It is complex to do messages synchronization between local devices and remote TiDB Serverless. Thankfully, with TiDB Serverless, there are not backend setup tasks. And the project can immediately get ready for production after we finished the app. Accomplishments that we're proud of We publish the app just in time. It is the power of team work. We proved that TiDB Serverless can be a successful ToC product. It has the potential of being a popular infrastructure to anybody, not just developers or companies. If Moyubie succeeded, lots of people will need a TiDB Serverless cluster. We built an app which we self are going to use every day. It will be published in App Store and Google Play. What we learned How to build a real life app. TiDB Serverless can dramactically reduce the effort of building an app. What's next for moyubie More chatting features. E.g. quotes, links, and pictures Share to twitter, more news sources [Advanced Feature] More powerful news recommendation algorithm [Advanced Feature] Connect to third party tools [Advanced Feature] Powerful messages control, message searching and analytics based on TiDB's HTAP ability. Try it out You can download the app here: https://github.com/flowbehappy/moyubie#downloads Here is a public room which can join in: bXlzcWwgLXUgJzRQbjhxSlAyNXU5Nmh0ZS5NWUJfUDdFUWhlS05teicgLWggJ2dhdGV3YXkwMS5ldS1jZW50cmFsLTEucHJvZC5hd3MudGlkYmNsb3VkLmNvbScgLVAgNDAwMCAtcHVhdVMyZG1QY0VoQ0J3OUg0Uk9YIC0tcm9vbSAnOTcwNTc3MDAtMmM4ZS0xMWVlLTg4ZGYtMTViOWI1MGExMTJhJyAtLXJvb21fbmFtZSAnUHVibGljIFJvb20g8J+RqOKAjfCfkanigI3wn5Gn4oCN8J+Rpic= Copy and paste the token into here: <div