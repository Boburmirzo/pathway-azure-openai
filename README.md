# Data streaming for real-time enterprise AI apps

This repository demonstrates how to build real-time generative AI applications using  [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-kafka-overview) + [Pathway](https://pathway.com/)+ [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service)+[Azure CosmosDB](https://azure.microsoft.com/en-us/products/cosmos-db).

## How it works?

Real-time AI app needs real-time data to respond with the most up-to-date information to user queries or perform quick actions autonomously. To achieve this, you must build a real-time data pipeline with Azure Event Hubs, Pathway, and Azure Data Services. This combination empowers businesses to build and deploy enterprise AI applications that provide the freshest contextual data.

## Example scenario

User sets an alert for flight status changes. Pathway LLM App combines both structured and semi-structured data. The system continuously checks flight or policy updates from Kafka topics and if there is a flight change, it sends an alert to the end user using any messaging service. Asks the user to confirm new flight changes and also updates the booking entries in CosmosDB automatically or after confirmation to another flight so that the external booking app is aware of this change.
