---
slug: "hashnode-blog-cards"
url: "https://devpost.com/software/hashnode-blog-cards"
title: "Hashnode Blog Cards"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 763
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Hashnode Blog Cards

> ⚡ The Project presents a set of APIs that will fetch the Blogs from Hashnode and can be put anywhere in Github .md file, Devpost Description, Postman Documentation 😉, or any website as image

[Devpost](https://devpost.com/software/hashnode-blog-cards) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[finance_payments]] [[health_clinical]]
**substrate** [[video_visual]] [[web_dom]]

**stack** cloud, graphql, html5, javascript, node.js, postman, svg

## How they structured the write-up

- hashnode blog with url
- hashnode blog with sequence
- set of latest hashnode blogs
- what's next for hashnode blog cards

## Body

Hashnode Blog Cards ⚡ The below APIs will fetch the Blogs from Hashnode and can be put anywhere in Github .md file, Devpost Description, Postman Documentation 😉, or any markdown editor. It can also be added to any website with HTML syntax. Hashnode Blog with URL GET /getHashnodeBlog About the API The below syntax when copied to a markdown editor will give an SVG in image displaying the blog in response like this will be generated. [![Hashnode Blog with URL](https://github-cards-external-blogs.souravdey777.vercel.app/getHashnodeBlog?url=https://blog.larsbehrenberg.com/use-javascripts-fetch-api-with-asyncawait-to-fetch-your-instagram-feed-in-react&large=true)](https://blog.larsbehrenberg.com/use-javascripts-fetch-api-with-asyncawait-to-fetch-your-instagram-feed-in-react) This can also be taken as src value in img tag of HTML. ` width attribute can also be defined to resize the SVG image in HTML. <a href="https://blog.larsbehrenberg.com/use-javascripts-fetch-api-with-asyncawait-to-fetch-your-instagram-feed-in-react"> <image src="https://github-cards-external-blogs.souravdey777.vercel.app/getHashnodeBlog?url=https://blog.larsbehrenberg.com/use-javascripts-fetch-api-with-asyncawait-to-fetch-your-instagram-feed-in-react&large=true" alt="Sourav Dey's Blog Cards" </a> This API can fetch Blogs from Hashnode when given the URL of the blog as query parameters url The other parameter is large which is not a required field and the default value is false when given true It shows a larger SVG image in response. Thus Query Params are: url = URL of the blog large = large size of SVG. Default value is false Eg. large = false Eg. large = true some example URLs for testing simply copy them to the value of url : url = https://blog.larsbehrenberg.com/top-50-gatsby-plugins-youre-going-to-love url = https://h.daily-dev-tips.com/creating-a-newsletter-layout-with-tailwind url = https://aditya01.hashnode.dev/an-simple-guide-to-recyclerlistview OR, go to Hashnode Click on any Blog Open it take the URL, and paste it. as the url query parameter. Hashnode Blog with Sequence GET /getHashnodeBlogBySequence ⚡ The Above API will fetch the Blogs from Hashnode and can be put anywhere in Github .md file, Devpost Description, Postman Documentation 😉, or any markdown editor. It can also be added to any website with HTML syntax. About the API The below syntax when copied to a markdown editor will give an SVG in the image displaying the blog in response like this will be generated. This API will always give the latest blogs of the user. It can be added to Github Readme or a personal website showing the latest blogs. Something like the last 5 blogs can be shown which will be always the latest whenever you open. [![Hashnode Blog with Sequence](https://github-cards-external-blogs.souravdey777.vercel.app/getHashnodeBlogBySequence?sequence=2&username=sandeep&large=true)](https://sandeep.dev/how-to-check-javascript-errors-in-console-on-mobile-chrome) This can also be taken as src value in img tag of HTML. ` width attribute can also be defined to resize the SVG image in HTML <a href="https://sandeep.dev/how-to-check-javascript-errors-in-console-on-mobile-chrome"> <image src="https://github-cards-external-blogs.souravdey777.vercel.app/getHashnodeBlogBySequence?sequence=2&username=sandeep&large=true" alt="Sourav Dey' s Blog Cards" </a> This API can fetch Blogs from Hashnode when given the username of the blogger as query parameters username and sequence as the no of Blog starting from 1 being the Latest and sequentially rest will come. The other parameter is large which is not a required field and the default value is false when given true It shows a larger SVG image in response. Thus, Query Params are: username = username of the blogger sequence = Serial No. of Blog (where Latest is 1) large = large size of SVG. Default value is false Eg. sequence=1&username=sandeep&large=false Eg. sequence=2&username=sandeep&large=false Eg. sequence=2&username=sandeep&large=true Eg. sequence=2&username=larsbe&large=true Eg. the latest Blog by Lars Behrenberg @larsbe. It will always be the latest blog. So if he adds a new blog It will change automatically. Go to Hashnode to find more. Set of Latest Hashnode Blogs GET /getLatestHashnodeBlog ⚡ The Above APIs will fetch the Blogs from Hashnode and can be put anywhere in Github .md file, Devpost Description, Postman Documentation 😉, or any markdown editor. It can also be added to any website with HTML syntax. About the API The below syntax when copied to a markdown editor will give an SVG in the image displaying the blog in response like this will be generated. [![Hashnode Blog with Sequence](https://github-cards-external-blogs.souravdey777.vercel.app/getLatestHashnodeBlog?username=larsbe&limit=3&large=true)](https://hashnode.com/@larsbe) This can also be taken as src value in img tag of HTML. ` width attribute can also be defined to resize the SVG image in HTML <a href="https://hashnode.com/@larsbe"> <image src="https://github-cards-external-blogs.souravdey777.vercel.app/getLatestHashnodeBlog?username=larsbe&limit=3&large=true" alt="Sourav Dey's Blog Cards" </a> This API can fetch Blogs from Hashnode when given the username of the blogger as query parameters username and limit as no of the latest blogs. The other parameter is large which is not a required field and the default value is false when given true It shows a larger SVG image in response. Thus, Query Params are: username = username of the blogger limit = No of latest blogs it can be between 1 to 6 . The default value is 3 large = large size of SVG. The default value is false Eg. username=tewarig&limit=1&large=true Eg. username=tewarig&limit=2&large=false Eg. username=larsbe&limit=1&large=true Go to Hashnode to find more. What's next for Hashnode Blog Cards Creation of a web page as API playground <div