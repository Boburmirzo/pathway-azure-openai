# Data streaming for real-time enterprise AI apps

This repository demonstrates how to build real-time generative AI applications using [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-kafka-overview) + [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) + [Pathway](https://pathway.com/)’s [LLM App](https://github.com/pathwaycom/llm-app)+[Streamlit](https://streamlit.io/).

## Example scenario: Customer support and sentiment analysis dashboard

Real-time AI app needs real-time data to respond with the most up-to-date information to user queries or perform quick actions autonomously. To achieve this, you must build a real-time data pipeline with Azure Event Hubs, Pathway, and Azure OpenAI. This integrated system leverages the strengths of Kafka for robust data processing, LLMs like GPT for advanced text analytics, and Streamlit for user-friendly data visualization. This combination empowers businesses to build and deploy enterprise AI applications that provide the freshest contextual visual data. 

### Background

For example, a multinational corporation wants to improve its customer support by analyzing customer feedback and inquiries in real-time. They aim to understand common issues, track customer sentiment, and identify areas for improvement in their products and services. To achieve this, they need a system that can process large streams of data, analyze text for insights, and present these insights in an accessible way.