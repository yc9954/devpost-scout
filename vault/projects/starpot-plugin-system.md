---
slug: "starpot-plugin-system"
url: "https://devpost.com/software/starpot-plugin-system"
title: "Starport plugin system"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 282
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Starport plugin system

> Extend starport commands using hashicorp/go-plugin

[Devpost](https://devpost.com/software/starpot-plugin-system) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** https://github.com/hashicorp/go-plugin

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for starport plugin system

## Body

What it does Extend list of starport available commands thanks to a plugin system. The plugins should be declared in the config.yml file. A plugin is defined with a name and a path to a repository. Such repository can contain multiple plugins, but a plugin path in config should point to a single plugin. How we built it Using https://github.com/hashicorp/go-plugin , which basically handles communication between 2 binaries using RPC. When the starport binary is executed, it checks if there's a config.yaml and reads the plugins from it. The plugins are fetched, compiled and ran. Starport then asks the plugin's commands and add them to the list of existing commands. If one the command is invoked by the command line, Starport calls the execute method of the plugin, with the related command. Challenges we ran into I started with the legacy go plugin system but it has serious drawbacks as we discussed in the discord channel. Accomplishments that we're proud of The code is very well tested and I'm confident it has very few bugs and is reliable for future developments. The plugin scaffold command can help developers to kick off a plugin very quickly, and since a local path is authorized as a plugin path, it allows fast development iteration because you can test your plugin in a chain immediately after it has been scaffolded. The other nice feature is starport will recompile a local plugin if it detects the plugin sources has changed. What's next for Starport plugin system Since I'm very new to starport, I have no idea of what can do a real plugin, so I can't wait to see what kind of plugins can be built. <div