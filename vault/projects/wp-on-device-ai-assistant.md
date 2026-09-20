---
slug: "wp-on-device-ai-assistant"
url: "https://devpost.com/software/wp-on-device-ai-assistant"
title: "WP On-Device AI Assistant"
hackathon: "Google Chrome Built-in AI Challenge"
organization: "Google"
winner: true
words: 426
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# WP On-Device AI Assistant

> This WordPress plugin provides an on-device AI assistant for your website. It exposes three main features: the AI Assistant Block, the Paragraph Rewriter and the Title Generator.

[Devpost](https://devpost.com/software/wp-on-device-ai-assistant) · hackathon [[Google Chrome Built-in AI Challenge]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** promptapi, wordpress

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for wp on-device ai assistant

## Body

GIF GIF GIF Inspiration LLMs are a great tool to help you write content. And where is the best place for that? Of course in you CMS. And which CMS is by far the most popular? WordPress. Furthermore, with the block editor, WordPress also offers a great way to create and manage content easily and intuitively. So my goal was to see if and how I can improve the writing experience in the WordPress BlockEditor with on-device AI. What it does Once installed an activated, it exposes three main features: the AI Assistant Block the Paragraph Rewriter the Title Generator All of them can be used in the WordPress block editor. How I built it First of all I had to create a WordPress plugin that hooks into the block editor JavaScript API. I was then able to identify three pain points: gettings started with your post adjusting existing content finding a catchy title I then created three features that address those pain points. They are either using the PromptAPI, the WriterAPI or the RewriterAPI. Challenges I ran into It has been a while since I hooked into the WordPress block editor. A lot has changed, but mainly to the better. I then wanted to focus on a quite specific topic: Should I use the "low-level" PromptAPI, with specific system prompts for each task, or should I use the "higher-level" (Re-)WriterAPI. I tried both and right now, both can be used using different branches in my repository. I have not yet found a perfect answer. But it is definitely great to play around with both approaches. Accomplishments that I am proud of The WordPress block editor is a pretty amazing piece of software. It does provide a great UX to the enduser, but it is also super flexible for developers to add their own plugins. So I am first of all quite proud I was able to merge the UX of the block editor with the efficiency of an LLM. "WP On-Device AI Assistant" brings the power of on-device AI to ~40% of the Web What I learned I learned a lot about the UX of using LLMs as a writing assistant, the technology behind the PromptAPI, WriterAPI and RewriterAPI and WordPress itself What's next for WP On-Device AI Assistant I am sure there are more use-cases for AI than just those three. So I will definitely look into those and add new features as I approach the problem. Also I might add fallback solutions (WebLLM, CloudLLMs) and a propper settings-/landingpage to the WordPress plugin. <div