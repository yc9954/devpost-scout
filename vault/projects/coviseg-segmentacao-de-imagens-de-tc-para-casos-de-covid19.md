---
slug: "coviseg-segmentacao-de-imagens-de-tc-para-casos-de-covid19"
url: "https://devpost.com/software/coviseg-segmentacao-de-imagens-de-tc-para-casos-de-covid19"
title: "COVISEG - Segmentação de imagens de TC para casos de COVID19"
hackathon: "Hackcovid19 "
winner: true
words: 468
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
---

# COVISEG - Segmentação de imagens de TC para casos de COVID19

> Utilizar a tecnologia de Inteligência Artificial para ajudar no diagnóstico de pacientes com COVID19 através da segmentação de Tomografias computadorizadas.

[Devpost](https://devpost.com/software/coviseg-segmentacao-de-imagens-de-tc-para-casos-de-covid19) · hackathon [[Hackcovid19]]

## Facets

**mechanism** [[vision_ocr]]

**stack** keras, matplotlib, numpy, python, tensorflow

## How they structured the write-up

- inspiração
- o que faz?
- como construímos?
- desafios que encontramos
- conquistas que estamos orgulhosos
- o que aprendemos?
- o que vem a seguir coviseg - segmentação de imagens de tc para casos de covid19

## Body

Logo do projeto Resultado da rede para uma das imagens COVISEG Inspiração Com o crescimento dos casos de contaminação por COVID19 pelo mundo, formas diferentes de detectar o vírus estão surgindo. Um dessas formas é a Tomografia Computadorizada (TC) na região do pneumotórax. A técnica já é bastante conhecida pelo mundo, porém alguns desses exames feitos em pacientes com COVID19 apresentaram alguns achados importantes, tais como: (i) opacidades em vidro fosco; (ii) consolidação pulmonar; (iii) efusão pleural. Mesmo sendo os principais achados, muitas das vezes se tornam difíceis de detectar devido a sensibilidade do equipamento utilizado. Nos últimos anos, temos visto uma revolução do uso de Inteligência artificial na medicina, com aplicações em diagnóstico, descobrimento de remédios, dentre outros. Portanto,nos pareceu natural aplicar métodos de inteligência artificial para podermos segmentar as áreas de interesse para os profissionais de saúde possam avaliar com maior detalhe. O que faz? Nosso software segmenta imagens de TC para ajudar a perceber situações clínicas como derrame pleural, opacificação e consolidação em vidro fosco. Como construímos? Construímos uma rede neural na arquitetura UNET que faz a segmentação de TCs a partir das imagens fornecidas pelo MedSeg . Desafios que encontramos Foi nossa primeira vez trabalhando com imagens do tipo fornecido pelo MedSeg . Isso dificultou a parte inicial de visualização de dados. Além disso, foi a primeira vez tratando com o problema de segmentação de imagens, portanto foi necessário buscar na literatura tipos de arquitetura para essa tarefa. No entanto, conseguimos apenas aplicar a arquitetura UNET. Conquistas que estamos orgulhosos Aprendemos a utilizar a UNET para segmentação de imagens médicas. Aprendemos a sintetizar a nossa ideia em um pitch. Conseguimos desenvolver um projeto robusto (TRL 4) em apenas três dias, pois toda a iniciativa começou a partir do Hackcovid19. O que aprendemos? Aprendemos a trabalhar em equipe e delegar tarefas razoáveis para cada participante. Além disso, aprendemos a segmentar imagens de Tomografia Computadorizada utilizando Deep Learning. E também como o processo de TC influencia no diagnóstico e tratamento da COVID19. Com isso, tivemos contato com uma área da medicina nunca explorada por nós antes. Aprendemos também sobre como empreender e fazer parcerias para que podemos aplicar o nosso conhecimento no mundo. O que vem a seguir COVISEG - Segmentação de imagens de TC para casos de COVID19 Podemos aprimorar a rede já construída utilizando novos dados segmentados que podem ser obtidos através do sistema único de saúde (SUS). Também buscamos testar arquiteturas que necessitam de menos dados para obter a segmentação, podendo melhorar a precisão do nosso software. Além disso, a rede possui potencial de ser aplicada para outros exames de imagem, como mamografia e ultrassom. Podendo impactar mais áreas do que apenas o COVID19. Para isso seria necessário colaboração com instituições de P&D, como a FIOCRUZ, e investimento em maior poder computacional. <div