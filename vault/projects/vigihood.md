---
slug: "vigihood"
url: "https://devpost.com/software/vigihood"
title: "VigiHood"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 441
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# VigiHood

> An application that filters the 'noise' from neighborhood groups to transmit only vital emergency alerts (fire, security, medical) between verified neighbors.

[Devpost](https://devpost.com/software/vigihood) · hackathon [[Student HackPad 2025]]

## Facets

**substrate** [[geospatial]]

**stack** firebase-(firestore-&-authentication), google, maps, mgx-(pour-le-developpement-assiste-par-ia), react

## How they structured the write-up

- ## inspiration
- ## ce que nous avons appris
- ## comment nous l'avons construit
- ## les défis rencontrés
- ## la suite pour vigiquartier (ce qui nous attend)

## Body

## Inspiration Nous avons tous des groupes WhatsApp ou Facebook pour notre quartier. Ils commencent avec une bonne intention, mais finissent remplis de "bonjour", de publicités et de discussions inutiles. Notre inspiration est née d'une question simple : que se passe-t-il en cas de véritable urgence ? Dans le "bruit" constant de ces groupes, une alerte vitale (un enfant perdu, un début d'incendie) est noyée. Nous avons décidé de créer une application "anti-sociale" : un outil, pas un jouet. Un outil qui filtre 100% du bruit pour ne transmettre que 100% du signal d'urgence. L'inspiration est le "téléphone rouge" : un seul bouton pour un seul objectif : la sécurité. ## Ce que nous avons appris Durant ce hackathon, nous avons appris que dans une situation de panique, "trop d'informations" est aussi dangereux que "pas assez d'informations". Le plus grand enseignement est que la "confiance" est la fonctionnalité la plus importante . Si n'importe qui peut envoyer une fausse alerte, le système s'effondre. C'est pourquoi la vérification de l'identité des voisins (une priorité pour la sécurité, chère à NordVPN) n'est pas une option, mais le cœur même de VigiQuartier . ## Comment nous l'avons construit Nous avons opté pour une approche moderne et rapide en utilisant MGX, un outil de développement d'applications assisté par IA . Cela nous a permis de prototyper l'interface utilisateur (UX/UI), conçue pour une personne en panique avec un grand bouton d'alerte central, de manière ultra-efficace, directement en code. Pour ce prototype, nous avons également construit : Un Frontend généré en grande partie avec MGX et affiné en React pour simuler l'application web. Un Backend basé sur Firebase (Firestore) . Pourquoi ? Parce qu'il nous fallait une base de données en temps réel pour garantir que la notification d'alerte soit instantanée . Nous avons utilisé l' API Google Maps pour visualiser l'emplacement de l'alerte. ## Les défis rencontrés Le défi n°1 était l'équilibre entre vitesse et confiance . Comment vérifier rapidement qu'un utilisateur est bien un voisin sans compromettre sa vie privée ? Notre solution est un système de vérification unique (par exemple, une preuve d'adresse) qui valide l'utilisateur une seule fois. Le défi n°2 était de garantir une notification instantanée et fiable, que nous avons résolu en choisissant une architecture temps réel (Firebase) plutôt qu'une base de données classique. ## La suite pour VigiQuartier (Ce qui nous attend) L'étape suivante est d'intégrer de l'IA (en lien avec Nexos AI ). Un modèle qui analyse la crédibilité des alertes : par exemple, si 5 utilisateurs signalent de la "fumée" dans la même zone en 2 minutes, l'IA peut automatiquement confirmer et "escalader" l'alerte en "Incendie Vérifié". <div