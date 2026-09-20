---
slug: "vegplace"
url: "https://devpost.com/software/vegplace"
title: "VegPlace"
hackathon: "monday.com climate change app challenge"
organization: "Monday.com"
winner: true
words: 1260
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "user/social_worker"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# VegPlace

> Vegetarian ordering widget on Monday.com that helps companies manage healthy food intake for team members while effectively fight against climate change.

[Devpost](https://devpost.com/software/vegplace) · hackathon [[monday.com climate change app challenge]]

## Facets

**domain** [[climate_energy]] [[finance_payments]]
**user** [[social_worker]]
**substrate** [[financial_record]] [[structured_db]]

**stack** aliyun, css, javascript, laravel, linux, monday.com, mysql, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenge i faced
- what's next

## Body

VegPlace VegPlace widget Overview of big idea Place an order and show how much you're contributing to climate change by eating this meal Admins customize the food data displayed to team members How much team have contribute to climate change Inspiration What is the benefit for the company if they fight against with climate change? This is the first thing that comes to my mind when I see this hackathon topic. The reason why I have this mindset is because I'm as a project manager on a small team, I always think in terms of how to bring benefits to the company, improve the company's productivity, and help the company generate revenue. Even when I surveyed my startup friends and my boss, their responses were the same. Instead of talking in the way like "people should fight against with climate change because it's our duty to save the world", but the reality is that usually only big companies will talk about climate change, most of the SMEs don't even have the time and resources to care about climate change, and how can they help climate change if their businesses can't even survive? Monday.com is powerful and flexible enough to build any application, but building a climate change application for Monday.com platform is a different story. It's easy to get off topic like building a standalone app that has nothing to do with Monday.com use cases and doesn't add any value to the user. Let's say I build an emissions calculation tool, a climate change game, or even systems for that spread the message of climate change, but let me ask you from the user's point of view, will you use it? Will the user really use it? If we think from the perspective of a project manager or project owner, a single decision will affect the performance, productivity and company revenue of the entire team. Based on the two points I mentioned above, so I'm wondering if it's possible to have a solution that can cover the majority of the user base, benefit companies in the first place, and at the same time it contributes a lot to climate change, doesn't affect companies' productivity, but increases their productivity. Therefore I created VegPlace. What it does VegPlace is a vegetarian ordering widget on Monday.com that helps companies manage healthy food intake for team members while effectively fight against climate change. So how exactly VegPlace works ? Here is the overview of the big idea : VegPlace works like a middleman platform, integrating with different food delivery services and food subscription services, and filtering out food items based on admin settings. Admins need to top up credits into the system, and team members can place orders directly on Monday.com. Wait, hold on. Food ordering system again ? Well here is the few points why I came out with this idea : I can't believe there's no ordering system on Monday.com, I mean it's weird right? Because I personally feel that managing team food intake is important and it's part of team management. Research shows that the healthier people eat throughout the day, the happier, more creative, and more productive they are . As a project manager, I do manage the team's food intake because I want to make sure (at least) that their food intake is healthy during office hours and maximize team productivity. Research shows that “A vegan diet is probably the single biggest way to reduce your impact on planet Earth, not just greenhouse gases, but global acidification, eutrophication, land use and water use. It is far bigger than cutting down on your flights or buying an electric car” Research shows that “ Eating vegetarian everyday can save nearly 664kgs of CO2 per year !” Research shows that "Vegetarian generating a 41.7 percent smaller volume of greenhouse gases than meat-eaters do" Research shows that "global switch to a plant-based diet, would effectively halt the increase of atmospheric greenhouse gases for 30 years" I did some research and based on the points I mentioned above, I believe that the most effective and best way companies can contribute to climate change is to eat vegetarian food. That's why I came up with the idea for a vegetarian ordering system on Monday.com. Functionality The following is a list of VegPlace features: Unified payment : Instead of each team member make payment individually, the company controls the payment and team member can place order directly without payment. Why ? One is to promote a healthy work environment, the second is to increase team motivation and productivity, and the third is to fight against climate change. By the way, the initial idea was to bind with credit card/using the Monday.com Apps monetization, but due to time constraints I have no choice but choose to use the top-up method. Food List Setting : Companies can customize the list of foods displayed in the system by controlling price ranges and food options. Place Order : Just imagine that you can straight away place food order on your project management tool without making payment. Food ordering has never been easier. Report Overview : An overview of the team's contribution to climate change. Business Impact From a team member's point of view, they would be more willing to eat vegetarian because they don't have to pay and the ordering process is simple. From the company's perspective, they can create a healthy work environment that ultimately increases the motivation and productivity of the team From VegPlace's point of view, the business model can generate revenue from transactions so that the system can be sustained and maintained in the long term, while bringing benefits to climate change and companies. It's actually a win-win-win situation. How I built it Project Background The backend system is built using the Laravel framework and the frontend system is built using React. Both system are hosted on the Alibaba Cloud ECS server. Since some functions seem to require the use of HTTPs, so I point subdomain and register SSL certificate with Let's Encrypt. Overall project planning is using Miro to illustrate the input, process flow and output. UI & UX Ensuring a good user experience is always my top priority. The system is design with modern and Minimalist style. I also did some UX analysis and applied UX design to the system, such as UI theme consistency, overall eye-catching design, etc. But there is still a lot to improve. Challenge I faced Found this hackathon a week ago. Lack of time Quite new to React , need to learn from zero. Quite new to Monday.com, need to learn from scratch also. Building a complete food ordering widget with new technology is super challenging. What's next The current system is far from a complete production system. There is still a lot to improve: Since the idea is like a mid-sized startup idea, the business model needs to be refined and complete to start the business Currently system is using fake data as I didn't managed to get their API until now because I'm asking for their API in the name of a hackathon instead of a solid company . Next step is form a company, request for API and integrate with third part food ordering service API, . Improve security, code quality, UI & UX Bug fixing Feature enhancement Expand team and find partnership Discuss with monday.com about apps monetization : pay inside Monday.com Integrate with foodDB database to further analyze how heathy they eat Define clear revenue modal, recruit team, marketing plan and operation model <div