---
slug: "asesor-pyme-inteligente-mcp-financiero"
url: "https://devpost.com/software/asesor-pyme-inteligente-mcp-financiero"
title: "Asesor PyME Inteligente - MCP Financiero"
hackathon: "HackMty 2025"
organization: "TEC ACM"
winner: true
words: 880
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/supply_logistics"
---

# Asesor PyME Inteligente - MCP Financiero

> "Tu PyME, decisiones financieras inteligentes."

[Devpost](https://devpost.com/software/asesor-pyme-inteligente-mcp-financiero) · hackathon [[HackMty 2025]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[supply_logistics]]

**stack** api, arm, arquitectura, azure, cloud, con, data, elevenlabs, fastapi-(backend), frontend)., gemini, google, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for asesor pyme inteligente - mcp financiero

## Body

Intro Analisis financiera , ingresos Analisis financiera , gastos Chat inteligente Mis datos Analisis financiera , flujo de caja Dashboard Analisis financiera , resumen general simulaciones Dashboard Inspiration La inspiración surgió de la necesidad crítica de las pequeñas y medianas empresas (PyMEs) en México de acceder a asesoría financiera profesional, proactiva y asequible. Observamos que muchas PyMEs carecen de un asesor financiero dedicado, lo que limita su capacidad para tomar decisiones basadas en datos y aprovechar oportunidades de crecimiento. El Reto Banorte de crear una solución financiera innovadora brindó el marco perfecto para fusionar la Inteligencia Artificial (IA) conversacional con el análisis financiero avanzado en la nube para democratizar este acceso. What it does Asesor PyME Inteligente - MCP Financiero es una solución de análisis y asesoría financiera que utiliza el Model Context Protocol (MCP) para ofrecer un asesor financiero virtual con personalidad profesional de Banorte (llamada Maya). Asesoría Conversacional Proactiva: El usuario puede preguntar en lenguaje natural ("¿Cómo puedo mejorar mi flujo de caja?") y recibe respuestas personalizadas, análisis de viabilidad, y recomendaciones de productos Banorte, todo con síntesis de voz natural de ElevenLabs. Análisis Avanzado: Utiliza Snowflake Data Cloud para un análisis masivo y escalable de datos históricos, identificando patrones, tendencias, y métricas financieras complejas. Simulaciones "What-If": Permite proyectar escenarios futuros (ej. inversión en nueva maquinaria) para evaluar el impacto en el flujo de caja y el Retorno de Inversión (ROI). Gestión Empresarial: Ofrece un CRUD completo de transacciones con autenticación empresarial y un panel administrativo seguro (JWT) para la gestión de datos financieros. Eficiencia Energética: La solución está desplegada en Azure VM con arquitectura Arm para una máxima eficiencia energética. How we built it El sistema fue construido con una arquitectura moderna de microservicios: Frontend: Desarrollado con React y Tailwind CSS (utilizando la paleta de colores Banorte) para una Interfaz de Usuario (UI) intuitiva y responsiva. Se usó Chart.js para las visualizaciones financieras. Backend: Construido con FastAPI como framework principal. IA Conversacional: Integración con la API de Google Gemini para el procesamiento del lenguaje natural (NLP) y el razonamiento empresarial, dándole la personalidad profesional al asesor. Voz: Uso de ElevenLabs para generar la síntesis de voz natural de las respuestas del asesor. Análisis de Datos: Conexión con Snowflake Data Cloud como data warehouse y uso de Pandas y Scikit-learn para la ingesta y el análisis de datos. Seguridad: Implementación de JWT para la autenticación empresarial segura. Infraestructura: Despliegue en una Azure VM con arquitectura Arm (para el premio MLH), utilizando Docker para la contenerización y Nginx como proxy inverso. Challenges we ran into Integración con Snowflake: La curva de aprendizaje para optimizar las consultas SQL nativas y asegurar la escalabilidad masiva en Snowflake para las simulaciones complejas fue un reto significativo. Personalidad de la IA: Afinar los prompts de Google Gemini para que el asesor mantuviera un tono profesional, proactivo y alineado con los productos Banorte sin sonar robótico requirió mucha iteración. Despliegue en Arm: Asegurar que todos los paquetes, dependencias (incluyendo las librerías de análisis de datos) y el stack completo fueran compatibles y se ejecutaran eficientemente en la arquitectura Arm de la Azure VM. Latencia del Audio: Optimizar la integración con ElevenLabs para minimizar la latencia y asegurar una experiencia de chat de voz fluida y responsiva para el usuario. Accomplishments that we're proud of Ganar el Reto Banorte: Crear una solución financiera innovadora que responde directamente a las necesidades del patrocinador. Integración de IA y Voz Profesional: Lograr un Asesor Financiero Virtual completamente funcional, inteligente (Gemini), y con voz natural (ElevenLabs), estableciendo un nuevo estándar de interacción. Arquitectura Escalable y Eficiente: Implementar con éxito la integración con Snowflake para análisis Big Data y realizar el despliegue en la arquitectura Arm de Azure (ganando el premio MLH), demostrando eficiencia técnica y energética. Cumplimiento de Múltiples Desafíos MLH: Competir y ser reconocidos en las categorías de Mejor uso de Gemini API, Mejor uso de la API Snowflake, Mejor uso de ElevenLabs y Mejor uso de Arm, validando la complejidad e innovación de la solución. What we learned Aprendimos la importancia de la arquitectura de datos escalable y la versatilidad de Snowflake para manejar cargas de datos empresariales. También profundizamos en el uso avanzado de la API de Gemini para inyectar una personalidad profesional y contextualizada a la IA. La experiencia de optimizar el stack para la arquitectura Arm nos proporcionó valiosos conocimientos sobre la eficiencia y la compatibilidad en entornos de cloud computing. Finalmente, la colaboración interdisciplinaria en el equipo (Migajeros) fue clave para integrar exitosamente tecnologías de front-end, back-end, cloud e inteligencia artificial en un proyecto cohesivo. What's next for Asesor PyME Inteligente - MCP Financiero Monitoreo y Alertas Proactivas: Implementar un sistema de alertas en tiempo real que notifique a las PyMEs sobre riesgos inminentes (ej. déficit de flujo de caja) u oportunidades (ej. optimización de tasas de interés). Integración Directa con Sistemas Contables: Desarrollar conectores para importar datos automáticamente desde plataformas contables populares como QuickBooks o software ERP, reduciendo la entrada manual de datos. Modelos de Machine Learning (ML) Avanzados: Utilizar las funciones de ML de Snowflake para pronósticos más precisos, como predicción de la demanda o churn rate de clientes. Personalización Multi-Idioma: Expandir la capacidad del asesor para atender a PyMEs en diferentes regiones con soporte multi-idioma (ej. Inglés y Portugués). <div