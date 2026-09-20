---
slug: "voluntree-ml"
url: "https://devpost.com/software/voluntree-ml"
title: "voluntree.ml"
hackathon: "Amazon Raise-up Buildathon"
organization: "Amazon"
winner: true
words: 1148
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# voluntree.ml

> Machine Learning based solution to automate volunteer recruiting from social media

[Devpost](https://devpost.com/software/voluntree-ml) · hackathon [[Amazon Raise-up Buildathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, celery, django, django-channels, drf, react, redis, tensorflow

## How they structured the write-up

- inspiration
- what it does
- main features
- how we built it
- what's next for voluntree.ml

## Body

[Admin App] Dashboard [Admin App] Organization Settings [Admin App] Connected Pages [Admin App] 3rd Party Integrations [Admin App] Create Signup [Admin App] Create Facebook Post [Admin App] Volunteer List [Admin App] Volunteer Profile and Activities [For Volunteer] Email verification [For Volunteer] Easily add event to calendar [For Volunteer] Share activity with your network and motivate others [For Volunteer] Share participation certificate in social media Inspiration Nonprofits can reach more potential volunteers where they are already spending their time – on social media. Many nonprofits around the world are already using social media as an effective way to expand their volunteer base, engage with community members and grow fundraising opportunities. To learn more about effective use of social media for volunteer program support: However, recruiting volunteers from social media can lead to a lot of manual work like keeping track of volunteers on spreadsheets. Imagine having to collect emails from individual chat inbox and create an account in a volunteer management system. Or, going through the spreadsheet for sending an important update to enlisted volunteers. Data in temporary spreadsheets eventually gets lost eventually and volunteers have to fill up a form every time they come back. There remains no way to recognize returning volunteers and pay tribute to their excellent work. On top of that, the manual bookkeeping process doesn’t scale, especially if the nonprofit has a large number of followers on social media. During this challenging time of the COVID-19 pandemic, we have seen how nonprofits from our local community are struggling due to the lack of automation tools for recruiting and managing volunteer pool from social media. And it was a great motivation to automate this process with software. What it does Voluntree provides automation to the volunteer recruitment workflow from social media. Once connected to a Facebook page, VolunTree will listen to the feed and page inbox. It will automatically recognize interests to sign up as a volunteer (from comments and messages). It will initiate any data collection, onboard volunteers and even create accounts in third party volunteer management software that your nonprofit already use. It will also be able to answer factoid questions by learning from the knowledge base that you provide- so that you don’t have to deal with repetitive questions over and over again. Main Features For Nonprofits Outreach Tool 📝 Detailed “Sign Up” creation with specific dates, times and slots 🚀 Spread the words with multiple pages and posts within the app 👀 See response in real-time, who is signing up for which slots 🚥 Take actions on sign up: Disable response collection, ban volunteers, rate volunteers, broadcast updates Sign Up Management 📄 Automated data collection, email verification and onboarding 🗂 Account linking with 3rd party integrations like NationBuild, Kindful etc 📊 Volunteer profile, past activities & ratings Communications 🤖 Automated onboarding from comments on page feed and messages from page inbox 🔮 Automated response about sign-up details, facts, volunteer info and payment info 📥 Broadcast updates about in messenger For Volunteers Convenience 📲 Review and respond on the go 💬Comment on the post to show interest 📥Concerned about privacy? Send a direct message to the page inbox 📌 Easy to use slot picker for booking slots according to availability 🔗 Links up with existing volunteer management account using the email address 📆 Convenient "Add to Calendar" button for adding events to personal calendar Motivate your friends 👥 Share sign-up activity with their friends and motivate others to sign up 🥇 Share participation certificates in social media How We built it This will help you write a similar app from scratch. Tech Stack For the main web app, we used ReactJS to build a Single Page Application. Get started here: https://reactjs.org/docs/getting-started.html This client application communicates with Django based server via REST API. We used Django Rest Framework for this: https://www.django-rest-framework.org/tutorial/quickstart/ For storing data we used Relational database, PostgreSQL can be a good choice: https://www.postgresql.org/download/ To maintain real-time communication via WebSockets we used Django Channels in the server. We used Celery as our distributed task queue and Redis as a cache come message broker. WebSocket API: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket Django Channels: https://channels.readthedocs.io/en/latest/ Celery: https://docs.celeryproject.org/en/latest/index.html Redis: https://redis.io/download Integration with Social Media For managing Facebook pages on users' behalf we implemented OAuth2. This will need to be implemented for all social platforms that we might add in future (for example, LinkedIn). Build Oauth flow: https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/ Post as a Page: https://developers.facebook.com/docs/pages/publishing/ We added webhook callbacks to be informed about comments on their feed or messages in page inbox. Webhook API: https://developers.facebook.com/docs/graph-api/webhooks/ Webhook for Messenger: https://developers.facebook.com/docs/messenger-platform/webhook/ Building conversational interface When such an event occurs (i.e. comment on a post or a message in page's inbox), we parsed what user intended to say by the means of Natural Language Processing. Initially we did so by building a Machine Learning solution from scratch using Tensorflow. But later we switched to 3rd parties. Wit.ai can be a good choice since it is free of cost and it can be built into Facebook's messenger experience. Though it lacks dialog management capabilities. To get started visit: https://wit.ai/docs/quickstart For a full blown conversational experience, ASW Lex can be a better choice (but not free of cost): https://aws.amazon.com/lex/ Sync data with 3rd party volunteer management tools We implemented OAuth2 for 3rd party integrations as well, mainly to get authorization to create volunteer accounts and sync data across two platforms. For example, NationBuilder OAuth: https://nationbuilder.com/api_quickstart Deployment It is hosted on AWS EC2 while the database is managed on AWS RDS and user media files are stored on AWS S3 . It also uses AWS SES for sending emails and Redis Enterprise Cloud hosted on AWS as cache and in-memory database for features like real-time updates. Source Code Please reach out to us, if you are a nonprofit who is looking to get started with your own copy of Volunntree. Clone the repository git clone https://github.com/mehamasum/voluntree cd voluntree Setup python virtual environment for project virtualenv -p python3.6 .venv Activate virtual environment source .venv/bin/activate # for linux .venv/Scripts/activate # for windowns Set required environment variables cp sample.env .env Install backend dependencies pip install -r requirements.txt Run redis docker run -p 6379:6379 redis Install ML dependencies while read line; do python -m nltk.downloader $line; done < nltk.txt Migrate the database python manage.py migrate Open up server using ngrok (HTTPS required for Facebook webhooks) ngrok -p 8000 Add the ngrok https url as APP_URL in .env APP_URL='https://foo.ngrok.io' Run backend server python manage.py runserver 0.0.0.0:8000 Create an admin account python manage.py createsuperuser Create an org and associate admin with the org => visit http://localhost:8000/api/admin/ Setup webhook callbacks for our FB app (admin login required from above step) => visit http://localhost:8000/facebook/setup/ Run celery celery -A config worker -B -l debug Install frontend dependencies npm i Run dev server npm start Now visit http://localhost:3000 and voluntree is up! What's next for voluntree.ml Recruit from LinkedIn, Twitter and Instagram Add more 3rd party integrations <div