---
slug: "postit-share-with-your-group"
url: "https://devpost.com/software/postit-share-with-your-group"
title: "PostIT: Share with your group"
hackathon: "Zero to One Hackathon by Convex"
organization: "Convex"
winner: true
words: 1131
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/media_journalism"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PostIT: Share with your group

> PostIT is an application where users can create groups that can either be public or private. In addition to group creation, the application also supports direct messaging between users.

[Devpost](https://devpost.com/software/postit-share-with-your-group) · hackathon [[Zero to One Hackathon by Convex]]

## Facets

**domain** [[civic_government]] [[media_journalism]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** convex, nextjs, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- tech stack:
- how is convex being used?
- challenges i ran into
- accomplishments that we're proud of
- what have i learned?
- what's next for postit: share with your group

## Body

Home Page when user is logged in. PostId page User profile page Screenshot of a conversation Settings route of a group Request route of a private group Inspiration I was inspired to create this application so that I can have a better understanding of how to work with Convex and something out of my comfort zone so that it helps me to explore errors that I have not encountered before. I also believe that the code base will be of great help to someone who wants to explore more about Convex. What it does It is a forum-style web application where a user can create a group and then post inside the group. A group can be public (default) or private. All the posts made in a public group are visible to anyone, but posts made in private groups are only visible to group members. To post in a public group, a user does not need to join that group. I have added functionality to upvote, downvote, bookmark, and comment on a post. Apart from that, users can send direct messages to other users and reply to other comments too. Once a user is logged in, a personalized feed is shown. In a personalized feed-only post made on groups, the user who has joined is shown. Also, there is the user profile page, where the user's activity (posts and comments) is shown. For a private group, a user needs to send a request to join it. Then the admin or owner needs to accept it. Overview of the schema User Management: The users, sessions, and accounts tables handle user registration, authentication, and session management. Groups: The group, group_join_request, and group_members tables manage the creation of groups, requests to join groups, and the members within each group. Groups can be public or private, and users can have different roles within a group. Posts: The posts table handles the creation of posts within a group. Posts can be public or private, and they can be archived. They can also have tags and files (like images) associated with them, as managed by the tags and files tables. Interactions: Users can interact with posts in several ways. They can vote on posts (votes table), comment on posts (comments table), and vote on comments (comment_vote table). They can also bookmark posts (bookmarked_posts table). Messaging: The messages and conversation tables handle direct messaging between users. Tech stack: Convex for database and storage Next.js for the frontend framework next-auth for authentication Tailwind CSS for styling Anyscale AI endpoint for generating summaries Zod for client-side validation TipTap as WYSIWYG editor to write the post. shadcn/ui for ui components How is convex being used? In this application, Convex has been used for database and storage. All the API calls are done using convex queries and mutations. I have also implemented the use of the withSearchIndex functionality to search for posts and groups. In some queries, I have implemented pagination and for AI summary I have used actions with internal functions. The technicality of joining a group: In my database, I have a table for groups and group_members. So when someone joins a public group, a row is created with the user information, and thus the user is a member. But for a private group, my approach is on a request basis. So the user needs to send a request, and then the admin or owner of the group needs to accept it. So when the request is sent, a row gets created on a table called group_join_request and when it is accepted, a row gets created for that user to be a member in the group_members table. After sending a request, the user has the option to cancel the request, and if the user cancels his/her/their request, then the row in group_join_request gets deleted. View for a user after sending the join request View of private group request page when someone sends a request Challenges I ran into While creating this application, I did face some problems, but at the end of the day, I was able to fix them. The majority of the problems occurred due to my lack of planning. But it has been a good learning experience and a great lesson for my future self. In the initial design of the application, I had a route named "/submit" which was intended to serve as the destination for users to compose their posts. Upon completion of their writing, users would interact with a button labeled "Publish", triggering the insertion of their post into the post table within the database. However, the introduction of image-adding functionality to the posts presented a complex challenge. The crux of the issue revolved around establishing a connection between the images and their corresponding post, given that the creation of a post was contingent upon the user’s interaction with the "Publish" button. To resolve this predicament, I had to reassess the situation and explore the various alternatives at my disposal. A novel approach emerged from this contemplation, leading to a significant alteration in the post-creation process. Under the new system, the creation of a new post by a user no longer directs them to the "/submit" route. Instead, a new post is instantaneously generated in the database as a draft (marked by !isPublic) and the user is redirected to the "/postId/edit/" route. The existence of a postId at this stage facilitates the attachment of images to the post. Furthermore, I incorporated a checkbox on the edit page to regulate the visibility of public posts, ensuring that they are only accessible to others when explicitly permitted by the user. This refined process not only addressed the initial issue but also enhanced the overall user experience by providing greater flexibility and control over the post-creation and editing processes. Accomplishments that we're proud of In the end, I am proud of the final application, as creating it has provided me with in-depth knowledge about Convex, and I am confident that I will be using Convex for future projects too. What have I learned? Throughout creating this application, I have learned a lot about convex in-depth and how I can structure the code in a way to take the most benefit from it and query efficiently. Before taking part in the hackathon, I never used convex actions, but now I am confident in my skills to use them. What's next for PostIT: Share with your group I want to make the repository public so that others can learn from it. This application has a lot of individual elements that can be used or learned from to use in other projects. Also, I would be very grateful if I got any feedback, since that way, I would learn if I made any mistakes and help improve this application. <div