---
slug: "eazyform"
url: "https://devpost.com/software/eazyform"
title: "Eazyform for monday.com"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 1132
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "substrate/web_dom"
---

# Eazyform for monday.com

> The easiest and quickest way to create monday forms that look exactly the way you want them.

[Devpost](https://devpost.com/software/eazyform) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[immigration_refugee]] [[retail_commerce]]
**substrate** [[web_dom]]

**stack** react

## How they structured the write-up

- installing it from the monday apps marketplace
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for eazyform
- final words

## Body

Important note - the video has captions/subtitles that explain the features in more detail. Please turn them on. If the video seems too fast, please view it at 0.75 speed. Installing it from the monday apps marketplace Eazyform is listed in the monday apps marketplace. You can install it into your monday account directly from it's listing . Inspiration I've been a CTO (and more recently a volunteering CIO for environmental NGOs) for many years. One huge pain throughout my carrier was having to use different non-configurable workflow apps for different workflows. Those apps didn't really talk to each other without a lot of coding or, more recently, complex zapier zaps. Luckily that problem is being solved by monday these days and the fact that I can implement almost all the workflows my organization needs with a single app using only configuration and almost no coding and zaps is amazing. Another huge pain was to create customer facing website forms that initiate workflows that: Match the website's brand and style and Save the responses into the workflow app For "no-budget" NGOs, I've been implementing this mainly with: To create the forms - the form widget of the elementor page builder for wordpress. To save the responses to my workflow app - cumbersome hard to maintain and modify Zapier zaps. Once I heard that monday is opening an app store / apps marketplace, I realized that it has the potential to truly eliminate coding for ANY type of workflow, in a similar fashion to what shopify did for ecommerce with their app store - these days if shopify doesn't support it, you're almost certain to find an app in their app store that does what you need. I'm hoping that eazyform will help monday customers to: Eliminate coding and zaps for any customer facing form use case. Easily and quickly implement workflows that require advanced and seamlessly embeddable website forms. Eazyform is only the first app in a series of apps that I'm hoping will complement monday and help advance the much needed no-coding revolution for workflows. UX wise, I was inspired by the elementor page builder, which, for me, is the easiest page and form builder for wordpress and also the most popular one. I love it's accurate WYSIWYG responsive editing experience. What it does A completely accurate WYSIWYG form editor Create forms that look great on mobile devices Order fields using drag and drop Hide and show fields using drag and drop Display multiple fields on the same line , with the following field width options: 25%, 50%, 75% and 100%. Choose different colors for almost everything Page background Form title Form description Field - label, description, placeholder, input background, and input border Submit button - text, background and border Compact view - hide labels and descriptions and use input placeholders instead. Completely accurate right to left support with a single switch, to support right to left languages such as Hebrew, Arabic, etc. Preview and fill it directly inside the board view Easily share the form via url Get html code to embed it in your site Eliminate iframe scrollbars when embedding by automatically adjusting the iframe height to the form's content Switch between small, medium and large sized fields in a single click. Supports all of the the following column types: name, text, long text, phone, email, link, numeric, date, checkbox, dropdown, status, country and rating. For dropdown columns, choose between single and multiple select fields . For single select fields (status, country and single select dropdowns), choose between radios, buttons and dropdowns for field input. For multiple select fields (multiple select dropdowns) choose between checkboxes, and dropdowns for field input. Add logo from url or svg code and set the it's height - width will adjust automatically keeping aspect ratio. Modify form title text, size, and alignment Modify form description text, size and alignment Make fields required Modify field label, description and placeholder text Modify submit button text, size, and alignment Modify rounded corners for fields and submit button Thank you page options Choose between internal and external thank you page to redirect to after submission. Modify internal thank you page title and message Add submit another response button to thank you page Create as many forms as you want for the same board by adding the eazyform board view to the board multiple times. How I built it I used react, and some very popular, mature and comprehensive react related and general javascript libraries that improved my development throughput substantially. It also helped make sure my code stays well designed and clean using best industry practices such as object oriented design, separation of concerns, and enforcement of DRY (don't repeat yourself). Security wise, my implementation makes sure that no one can access any information stored about users and the oauth access tokens they granted to eazyform. I will share my implementation with the monday team privately. Challenges I ran into The main challenge was actually not coding related - I didn't find a video producer to help me with the demo video, so I taught myself how to use Camtasia and edited it myself, which was surprisingly easy and a lot of fun :-) Accomplishments that I'm proud of That I was able to create something that not only I and the organizations I support definitely need and will use but that has the potential of being used by almost any monday customer. That I was able to create a pretty mature app in record time. What I learned A lot, mainly in the area of how to stay as agile and quick as possible with complete continuous delivery support. This includes: How to build react and monday apps in record time. The best libraries and bundlers to use for the job. The best hosting providers to use for the job. What's next for Eazyform Eazyform will continue and evolve and bring in all the features that should be part of a modern, state of the art form builder, including: Support all other "supportable" column types Creating forms that update multiple boards, a popular use case that is very cumbersome to implement using zapier and the like. An example of that would be a form for a leads board that creates the contact and the company in the contacts and company boards, if they don't exist yet. Support for conditional logic Support for getting a url after filling the board that the user can use to update his/hers submission. Support for emailing that url to the user after filling the board. More styling options including the option to add custom css Inline after submit messages instead of internal and external thank you pages. Etc. etc. etc. Final words Feel free to contact me at: ronen@eazyform.app Cheers, Ronen <div