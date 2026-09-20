---
slug: "teste-jnk5z4"
url: "https://devpost.com/software/teste-jnk5z4"
title: "Trekkers: Classificador de raio-X de pulmão para COVID-19"
hackathon: "Hackcovid19 "
winner: true
words: 861
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/civic_government"
---

# Trekkers: Classificador de raio-X de pulmão para COVID-19

> Classificador de raio-X de pulmão

[Devpost](https://devpost.com/software/teste-jnk5z4) · hackathon [[Hackcovid19]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[civic_government]]

**stack** matlab, sweep

## How they structured the write-up

- equipe
- motivação
- método
- nosso diferencial
- resultados
- próximos passos

## Body

Pipeline utilizado para o tratamento das imagens de raio-X e treinamento da rede MLP para classificação e auxílio no diagnóstico de COVID-19 Ferramenta SWeeP, originariamente desenvolvida para tratamento de sequências biológicas. Uso da ferramenta SWeeP para tratamento de imagens. EQUIPE Somos a equipe Trekkers formada pelos alunos de mestrado em Bioinformática da UFPR Camila, Monique, Guilherme, André, Leonardo e Selma. Estamos participando do HackCovid 2020 e nosso desafio foi o #d051 IA e Ciência de Dados para Apoio à Decisão Clínica. MOTIVAÇÃO A doença COVID-19 é caracterizada por acometer os pulmões. Dois dos exames realizados para auxiliar no diagnósticos são o raio-X e as tomografias. As tomografias são usadas como exame padrão para o diagnóstico para a COVID-19, uma vez que apresenta uma série de indícios como presença de vidro fosco bilateral, consolidações bilaterais e efusão pleural. Esses indícios são observados com razoável facilidade e são fortes indicativos do COVID-19. Por outro lado, os raios-X não fornecem muitas pistas visíveis, exigindo recorrer a tomografia. Entretanto, os raios-X são exames de rotina, realizados nos pacientes com muito maior frequência e possíveis de se realizar em quase todos os hospitais, inclusive os de maior precariedade. Logo, está nos raios-X o verdadeiro desafio! Se fosse possível utilizando imagens de raios-X ter um indicativo para a COVID, isso permitiria acelerar o seu diagnóstico e assim antecipar o tratamento e evitar maior contágio. Por este motivo, a equipe Trekkers propõe a construção de uma rede classificatória de imagens de radiografias nas classes “NORMAL”, "COVID" e “OUTRAS DOENÇAS”, como um auxiliar no diagnóstico do covid, e na identificação de outras doenças pulmonares. MÉTODO Bancos de Dados Realizamos uma busca por dados nos bancos chestX e de desafios do Kaggle , como nos links indicados: chestX Kaggle01 Kaggle02 Os bancos de dados nos forneceram um número de raios-X mínimo para o treinamento de uma rede classificatória. Totalizamos 458 raios X, dos quais: 148 com covid-19 528 saudáveis 282 raios-X de pulmões acometidos por outras enfermidades Passo 1 - Tratamento das imagens O primeiro passo consistiu no tratamento das imagens para escala de cinza, na sua redimensionalização para uma mesma escala padronizada e então sua conversão da imagem para uma matriz numérica binária. Passo 2 - SWeeP Por segundo, as imagens tiveram uma redução de dimensionalidade com o uso de projeção. Essa redução é feita com o SWeeP, uma ferramenta desenovolvida pelo laboratório de Inteligência artificial aplicada a bioinformática da UFPR. O SWeeP foi publicado este ano de 2020 na Scientific Reports , e está atualmente disponível para download para MATLAB, R e python. Passo 3 - Treinamento da rede de classificação Com as matrizes das imagens com tamanho reduzido pelo SWeeP, foi possível realizar um treinamento com rede MLP ( multilayer perceptron ). Foi utilizado crossvalidation, com kfold de 5. A prorção treino-teste foi 70:30, com reseva de 10% dos dados para validação. Com as redes treinada, tornou-se possível classificar as imagens nas três categorias mencionadas. É preciso enfatizar que essa classificação não é um diagnóstico, mas um indicativo que serve como apoio ao diagnóstico. NOSSO DIFERENCIAL O SWeeP é uma ferramenta originariamente desenvolvida para o processamento de sequências biológicas como de aminoácidos e nucleotídeos em que uma sequência é convertida em matriz binária e então multiplicada por uma matriz de projeção ortonormal randômica, resultando numa redução de dimensionalidade para um vetor de 600 bits cada sequência. Contudo não iremos usar sequências biológicas, mas imagens de raios X também convertidos em binárias. A redução de dimensão por meio de projeção randômica permite que as informações pouco úteis sejam descartadas, e padrões característicos sejam realçados. A redução de dimensão por meio de projeção randômica atua diferentemente de uma PCA (analise dos componentes principais). Na PCA, se mantém apenas os componentes mais correlacionados, podendo haver perda de informações relevantes para a classificação. Uma matriz randômica evita essa perda de informação. Outra vantagem do método é a redução no tempo de processamento e treinamento das redes, permitida pela redução de dimensão mediada pelo SWeeP. RESULTADOS Realizamos uma série de treinamentos com variadas dimensões de rede e parâmetros. Obtivemos nosso melhor resultado com acurácia de 70%, e F1-Score, precisão e recall de 60%. O que é um ótimo resultado, considerando o tamanho reduzido de imagens utilizadas para treinamento. Realizamos crossvalidation com kfold de tamanho 5 e reservamos 10% da amostra para validação. Um estudo similar de classificação de raios x com redes convolucionais obteve 94% de acurácia contudo possuía um banco de imagens 10 vezes maior, o que lhe conferiu vantagem. A nossa ferramenta ainda exigirá maior treinamento para ser disponibilizada, com o uso de um banco de imagens maior, inclusive a presente neste estudo. PRÓXIMOS PASSOS Aprimorar o treinamento com o uso de um banco de dados com maior quantidade de imagens. Realizar um estudo aprofundado da metodologia aqui proposta. Estudar a possível aplicação para outras enfermidades e para outros tipos de imagens que possam auxiliar no diagnóstico do COVID-19 e outras enfermidades. Disponibilizar a ferramenta online, de forma simples e acessível para uso médico livre e gratuito. Estamos buscando mais dados para o desenvolvimento da ferramenta em parcerias com hospitais. Para contato: Camila P Perico: camilapp94@gmail.com Monique Schreiner: nique.mo94@gmail.com <div