---
slug: "dra-june-1el0uh"
url: "https://devpost.com/software/dra-june-1el0uh"
title: "Dra June"
hackathon: "Hackcovid19 "
winner: true
words: 809
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/health_clinical"
---

# Dra June

> Chatbot + simples + inclusivo de atendimento primário em COVID-19. Use voz ou digite. Acesse via link para o WhatsApp. Sinaliza novos focos às lideranças comunitárias e à vigilância em saúde.

[Devpost](https://devpost.com/software/dra-june-1el0uh) · hackathon [[Hackcovid19]]

## Facets

**domain** [[civic_government]] [[health_clinical]]

**stack** app, dialogflow, firebase, firestore, react-native

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for dra june

## Body

Dra June Almeida diagrama de construção ícone desafios relacionados Inspiration Nossa inspiração inicial foi criar uma ferramenta que seja um meio de comunicação de linguagem fácil, acessível, inclusivo e popular, que pudesse atingir o maior número de pessoas, independente de nível de formação, classe social, idade, limitação de digitação, etc. Pensamos em uma solução de simples interface que ajude os grupos mais vulneráveis e possa também auxiliar a vigilância em saúde na tomada de decisão acerca dos eventos da pandemia de COVID-19. Quem é a Dra June? A inspiração do nome do chatbot: June Almeida (1930-2007) foi a cientista que identificou o primeiro coronavírus humano (B814) em 1964. Apesar do sobrenome aportuguesado, a Dra June era escocesa e trabalhava como virologista na Escola de Medicina do Hospital St. Thomas. Como em várias outras histórias de mulheres cientistas, sua descoberta não foi valorizada imediatamente. Dra June enviou o artigo de sua descoberta para uma revista científica que recusou a publicação, argumentando que as provas enviadas eram apenas imagens de baixa qualidade de partículas do vírus da gripe. Somente em 1965, o British Medical Journal divulgou a façanha e, dois anos depois, o Journal of General Virology publicou as fotografias. Hoje esse artigo pode ser lido gratuitamente na internet. A descoberta da Dra June foi e é fundamental no combate à pandemia da COVID-19, pois os cientistas ainda utilizam suas técnicas descritas no artigo. Para reconhecer e divulgar sua grande contribuição, resolvemos homenageá-la dando seu nome ao nosso projeto. What it does O Dra June permite ao usuário interagir com um bot programado para atendimento primário em pessoas que estejam com sintomas da COVID-19 e que precisam de orientação primária, evitando assim a superlotação na rede pública de atendimento em saúde e hospitais de referência para atendimento em COVID-19. Ele dá orientações de cuidados básicos domiciliares para casos que considere leves e indica o posto de saúde ou rede hospitalar de referência mais próxima aos casos que considere necessidade de atendimento médico imediato. Diferenciais do Dra June em relação aos demais chatbots para atendimento primário em COVID-19: Proporciona a inclusão social! O Dra June é acessado via link que leva ao WhatsApp e então inicia o diálogo por digitação ou por voz, o que desobriga o usuário a ter que instalar um app em seu celular e consumir mais dados do seu plano de internet, já que muitas operadoras já disponibilizam tráfego livre para esse aplicativo. A dificuldade no acesso à internet e a um celular que possua hardware suficiente para baixar novos apps é uma realidade para muitos brasileiros que vivem situações vulneráveis. O WhatsApp é a rede social mais popular dentre todas as classes sociais. Também pensamos nos deficientes visuais, idosos e pessoas com problemas motores. Eles podem ter acesso ao atendimento, sem problemas, falando com a Dra June. Sinaliza as lideranças comunitárias e órgãos de saúde pública sobre novos focos da COVID-19 As informações sobre sinais clínicos da COVID-19 das pessoas que utilizam o Dra June são armazenadas, avaliadas por IA e direcionadas às lideranças comunitárias da região e aos órgãos de vigilância responsáveis a partir de 10 casos identificados como possíveis casos de COVID-19. Esta funcionalidade permite melhor alocação de recursos, tomada de decisões e ações preventivas em tempo hábil, antes que ocorra um número maior de pessoas suspeitas na região. How I built it Dra June utiliza Dialogflow para geração do chatbot integrado com o Firestore para persistência dos dados e Firebase Storage. Desenvolvimento do app com React Native integrado ao Dialogflow (ver diagrama da construção em anexo) Futuramente: Desenvolvimento de aplicação web em Python para disponibilização de previsões a partir dos dados coletados pelo chatbot tratados por algoritmos de Machine Learning. Challenges I ran into As dificuldades encontradas para apresentar o protótipo foi linkar o chatbot ao WhatsApp, pois solicitamos permissão ao app para integração via conta, porém a solicitação não foi respondida a tempo de finalizar o protótipo. Também não houve tempo hábil para implantar o algoritmo e aprendizagem de máquina com os dados coletados pelo bot. Accomplishments that I'm proud of Nos orgulhamos em participar de uma equipe com skills distintos e tão afinada, focada em desenvolver uma solução para amenizar os problemas de controle da contaminação e atendimento de saúde da COVID-19, onde cada um pode auxiliar para o desenvolvimento de um produto que trará uma contribuição social neste momento de pandemia. What I learned Aprendemos que uma equipe multidisciplinar possibilita o desenvolvimento de produtos melhores e mais adequados à demanda da sociedade. E aprendemos que um produto só é verdadeiramente útil se não excluir ninguém. What's next for Dra June Incluir a geolocalização por meio da integração com o software do usuário; Desenvolver a funcionalidade de alerta às lideranças comunitárias da Região e aos órgãos de vigilância em saúde; Fazer a versão para IOS; Realizar campanha publicitária para divulgação ampla. <div