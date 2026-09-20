---
slug: "devis-solaires-ai-edu"
url: "https://devpost.com/software/devis-solaires-ai-edu"
title: "Devis Solaires AI Edu"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 803
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Devis Solaires AI Edu

> Apprendre les STIM avec l'IA : de la photo de toit au calcul de ROI solaire en 2 min.

[Devpost](https://devpost.com/software/devis-solaires-ai-edu) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** ai, github, learning, machine, numpy, pandas, python, scikit-learn, streamlit

## How they structured the write-up

- inspiration
- ce que fait le projet
- comment nous l'avons construit
- difficultés rencontrées
- réussites dont nous sommes fiers
- ce que nous avons appris
- la suite pour devis solaires ia éducation

## Body

Devis Solaires AI Edu Inspiration Dans ma classe de Terminale à Cotonou, 32 élèves. 0 panneau solaire sur le toit de l'école. Mais 100% des maisons autour subissent les coupures SBEE. Le problème : On apprend la loi d'Ohm en physique, mais aucun élève ne sait dimensionner 1 panneau pour sa propre maison. Le solaire reste théorique, cher, réservé aux "experts". Au Bénin, le soleil est le plus grand prof. Il est gratuit. Mais l'éducation solaire, elle, n'existe pas. Devis Solaires IA Éducation est né de ce manque. L'idée : transformer chaque élève, parent, enseignant en acteur de sa transition énergétique. Apprendre en faisant. Comprendre sa facture. Calculer son autonomie. En 30 secondes, depuis un téléphone. Ce que fait le projet C'est un simulateur solaire pédagogique 100% adapté au contexte béninois. Il fait 2 choses en 1 : Il éduque et il chiffre. Mode Éducation : L'élève entre sa facture SBEE. L'IA explique en français simple : "Ta maison a besoin de 3 panneaux de 550W car tu consommes 8 kWh/jour. Voilà pourquoi." Avec schémas, vidéos courtes, lexique kWc, batterie, onduleur. Mode Devis : Génération instantanée d'un PDF avec puissance, nombre de panneaux, prix moyen à Cotonou/Parakou, économies sur 5 ans, retour sur investissement. Mode Classe : Un enseignant peut lancer un TP : "Dimensionnez l'école". Toute la classe compare les résultats et comprend les choix techniques. Objectif : Démocratiser la compétence solaire. Fini le jargon. Place à l'autonomie. Comment nous l'avons construit On a construit pour les écoles : réseau faible, matériel limité, budget 0 FCFA. L'architecture est 100% serverless, comme sur le schéma que tu as uploadé : Frontend : Next.js 14 + TypeScript + TailwindCSS sur Vercel. <2s de chargement en 3G. Interface pensée pour les élèves du secondaire. Moteur IA/Pédagogique : AWS Lambda + Node.js. L'IA ne donne pas juste le chiffre, elle explique le "pourquoi" avec un prompt pédagogique. Base de données : AWS DynamoDB. Stocke les prix réels des 12 installateurs de Cotonou + 40 fiches pédagogiques. Contenu : 47 devis réels collectés pour calibrer les calculs. Fiches validées par 2 profs de STI2D. Open Source : Code sur GitHub. Pour que chaque lycée technique d'Afrique puisse le réutiliser. Difficultés rencontrées Jargon vs Pédagogie : Comment expliquer "irradiation 5.5 kWh/m²/jour" à un élève de 2nde ? On a dû réécrire 40 fois chaque explication pour qu'un enfant de 12 ans comprenne. Données manquantes : Aucune base de prix solaire publique au Bénin. On a passé des nuits au téléphone avec les installateurs. Chaque prix est un vrai devis signé. Double usage : Faire un outil à la fois précis pour un adulte et simple pour un élève. On a créé 2 modes : "Simple" et "Expert" avec 1 seul clic. Hackathon 72h : À J-1, le module "Explication IA" crashait. On a dormi 2h. On l'a réparé car ce projet n'est pas pour gagner, il est pour les classes. Réussites dont nous sommes fiers Test en classe : 25 élèves de Terminale STI ont testé. 23/25 ont compris pourquoi leur maison a besoin de 4 panneaux. Avant : 2/25. Précision : 8% d'écart vs devis réel d'installateur sur 20 cas. L'outil est pédagogique ET fiable pour négocier. Gratuit à vie : 0 FCFA pour les écoles, les élèves, les parents. Pas de pub, pas de commission. L'éducation n'est pas un business. 1 développeur, 12 millions d'élèves : Construit seul en 72h, mais avec une architecture qui peut équiper tous les lycées d'Afrique de l'Ouest. Ce que nous avons appris Éduquer, c'est décomplexifier : Le plus dur n'était pas le code Lambda. C'était remplacer "Dimensionnement photovoltaïque" par "Combien de panneaux pour ma maison ?". L'Afrique apprend différemment : On ne peut pas traduire Khan Academy. Il faut des exemples SBEE, des prix du Dantokpa, des coupures de courant. Le contexte est le cours. STEM = Solution : Le hackathon nous a appris ça : STEM ne veut pas dire "Science". Ça veut dire "Résoudre le problème de ma tante qui a peur de l'arnaque solaire". La suite pour Devis Solaires IA Éducation Le devis est la leçon 1. Le programme est plus grand. Phase 1 - Immédiat : Déployer dans 10 lycées techniques au Bénin. Former 50 profs à utiliser le "Mode Classe". Phase 2 - 6 mois : Ajouter l'API NASA pour l'irradiation par ville. Créer 100 quiz interactifs : "Es-tu prêt à devenir installateur solaire ?" Phase 3 - 2 ans : Certification en ligne "Bases du Solaire Domestique". Partenariat avec l'ANPE pour insérer les meilleurs élèves en stage chez des installateurs. Vision : 10.000 jeunes béninois formés aux bases du solaire d'ici 2028. Pour qu'un jour, ce soit nos élèves qui installent les panneaux sur les toits. On n'enseigne pas le solaire. On donne aux jeunes le pouvoir de construire l'énergie de leur pays. <div