---
slug: "uipath-form-designer"
url: "https://devpost.com/software/uipath-form-designer"
title: "SyForms - UiPath Forms Designer"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 724
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
---

# SyForms - UiPath Forms Designer

> RPA is not only about the Robot but also the User

[Devpost](https://devpost.com/software/uipath-form-designer) · hackathon [[Power Up Automation]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]

**stack** .net, uipath, windows-forms

## How they structured the write-up

- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for syforms

## Body

Currently, Intelligent automation is under the RPA spotlights. However, there is another part of the RPA which is taking more and more place in the technology: The attended automation. What inspires me to build this Custom activity is the current state of UiPath and its current features in terms of Attended Automation are good, the recent licensing model made it even better but feature to Build and configure Userform to display, input and works with data during the automation process would make it AMAZING! What it does The UiPath Form Designer will permit the RPA to Developer to build (Windows) Forms using a WYSIWYG approach similar to the way it is done with Visual Studio. In addition, The Form got features to interact directly with UiPath and permit to Input/Get/Visualize/Manipulate Data out of it to satisfy the need for Front Office/Attended automation of interacting with its user. The created forms can be used, reused, shared with other since they are exportable as a File. How I built it The solution is built using native windows form technology as a base, overriding its controls to fit design & automation features The Designer is Form containing an MDI form where the controls are added/remove on runtime for design purpose and have their properties (the ones I decided to expose) editable via a property grid. The designer has its own file system where the form can be exported as JSON (based on a custom se/deserialization approach). Once a form is designed, it exportable and loadable by the Designer. The form Controls all have a property "Expose as argument" which will make them appear as an output (Of System.Windows.Form.Control) to be used within the UiPath Automation workflow. Certain controls even allow to directly invoke a XAML workflow when a specific event triggered (ex: Button_Click,Form_Onload,Combobox_SelectionChanged) by providing it file path as a property. The invoked workflow needs to have specific arguments to be invoked, The Designer has a feature within its menu to create a suitable workflow. Challenges I ran into I encountered many challenges during the development, most of them were related to the rendering/behavior of the control on the MDI form and discrepancies between what appears during design and what will appear during runtime. Another type of issues I faced is related to XAML workflow invocation. The used of certain packages within the XAML invoked from the form requires to use an activity from the same package before executing the form (ex: If the workflow needs to send an email, it is required to use a "Blank" Get Mail activity before using the form activity). Certain activities used inside the workflow are not functioning (Invoke workflow file, Activities communicating with Orchestrator...) - This seems related to a missing Workflow extension (probably ad hoc one created by UiPath) from the Workflow Instance Extension Manager. I am looking forward to communicating and collaborating with UiPath in order to resolve those challenges. Accomplishments that I'm proud of I am proud of the overall outcome in general and to have it an in a functional state, however, I have to say that invoking UiPath logic from the form directly, without having to close it and being able to generate "controls out arguments on demand was something very satisfying to achieve. What I learned This adventure allowed me to sharpen my knowledge around window windows workflows and refreshed the past experiences I had with windows forms. What's next for SyForms First, the present project and its outcome do not have the pretention to be completed software or product but is for now just an Hackaton submission to serve and extend the UiPath capabilities within an area (Attended automation) still quite underrated if we consider the number of potential opportunities that it could cover. We, Symphony and I, believe that the attended automation area will be part of the future of RPA (and by extension the Future of work)and can, at large but also small scale can be game-changing for enterprises. Personally, I truly hope to be able to be able to prioritize this initiative in the future there are many other items and features (More controls, Form scope and activities to take action on it, increase interaction between form and the Studio...) I am looking forward to implementing in order to make the idea more accessible, efficient and spreadable Stay tuned! <div