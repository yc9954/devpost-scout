---
slug: "crystal-costs-crystal-clear-costs-in-snowflake"
url: "https://devpost.com/software/crystal-costs-crystal-clear-costs-in-snowflake"
title: "Crystal Costs: crystal-clear costs in Snowflake!"
hackathon: "THE FUTURE OF AI IS OPEN"
organization: "Snowflake"
winner: true
words: 648
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/general_public"
---

# Crystal Costs: crystal-clear costs in Snowflake!

> A conversational AI agent that monitors, forecasts and helps optimize your Snowflake credit spends, constantly observing and learning from your account’s credit consumption patterns.

[Devpost](https://devpost.com/software/crystal-costs-crystal-clear-costs-in-snowflake) · hackathon [[THE FUTURE OF AI IS OPEN]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**user** [[general_public]]

**stack** arctic, cortex, langchain, openai, python, snowflake, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crystal cost

## Body

Landing interface Breakdown of credit consumption by all the warehouses Forecasting credit consumption for a particular warehouse Predicting and Comparing total credits used this week and in the coming weel Comparison of credit consumed last week and the week before Total elapsed time for the longest running query in last week Inspiration In managing data warehouses like Snowflake, one of the persistent challenges is monitoring and forecasting credit and cost consumption effectively. The motivation for Crystal Costs stemmed from our own experiences at Houseware, where we recognized the need for a tool that simplifies these tasks through an intuitive, conversational interface. Our goal was to empower Snowflake administrators by enabling them to interact with their data warehouse in natural language, making the process more accessible and less technically intimidating. What it does Crystal Costs is a conversational AI agent that helps Snowflake administrators monitor credit consumption, answer queries about credits, and forecast future costs. By simply asking questions in natural language, users can retrieve detailed analyses, comparisons of credit usage across different warehouses, and visual forecasts of future expenditures. The agent is capable of generating visual data representations, such as bar and line charts, to enhance understanding and decision-making. How we built it We developed Crystal Costs by integrating multiple models and technologies. At its core, it utilizes Snowflake's Arctic to process and understand natural language queries and OpenAI's GPT-4 Turbo for data reference. The coordination between these technologies is managed through LangChain, which orchestrates the workflow and ensures that each component effectively contributes to the query resolution process. This multi-model setup allows Crystal Costs to provide accurate data insights and predictions while maintaining a seamless conversational user experience. Challenges we ran into Integrating different technologies such as Arctic, GPT-4 Turbo, and LangChain posed significant challenges, particularly in handling JSON outputs correctly and ensuring seamless integration with Snowflake Cortex, which is not a first-class citizen in the Langchain ecosystem. We also couldn’t use Arctic entirely for this project since it doesn’t support function-calling yet, hence we had to resort to using it for the conversational agent. Additionally, managing hallucinations in the agent's execution plans required careful attention to detail and constant adjustments to maintain accuracy and reliability in the outputs. Accomplishments that we're proud of Our team successfully integrated Arctic LLMs for conversational use cases and utilized Cortex ML functions for robust forecasting scenarios. Orchestrating multiple LLMs, including OpenAI GPT and Snowflake Arctic, to handle the entire execution plan has been a major accomplishment, demonstrating the flexibility and power of our solution. We achieved a significant reduction in latency and enhanced performance compared to traditional methods, which greatly improved the user experience and operational efficiency. Lastly, we created ephemeral user interfaces that dynamically generate visualizations based on the nature of the query, enhancing user interaction and understanding. What we learned Through this project, we learned how to package Cortex functions as tools within the Langchain agent's framework and leveraged conversation history (short-term memory) to efficiently handle repetitive or redundant questions. This approach helped us improve the system's efficiency and user experience by avoiding unnecessary repetition in visualizations and responses. We also experimented with LangGraph for the agent’s execution plan and attempted integration with Streamlit; however, due to lack of native support for the same, these were not included in the final implementation. Additionally, this was our first experience utilizing Snowflake's Cortex and Arctic models, providing us with valuable insights into their capabilities and integration challenges, which were crucial for developing a robust conversational agent. What's next for Crystal Cost Looking ahead, we plan to expand Crystal Costs' capabilities to include alerting mechanisms for significant spikes or dips in credit usage, enhancing the agent’s ability to not only forecast costs but also provide insights into query observability and patterns. This will further equip Snowflake administrators with a comprehensive tool for managing their data warehouse more effectively and efficiently. <div