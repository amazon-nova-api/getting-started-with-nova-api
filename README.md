# Amazon Nova API Cookbook

## Introduction
Amazon Nova foundation models deliver frontier intelligence and industry-leading price-performance, enabling you to build generative AI applications that are safe, reliable and cost-effective.

This repository contains code samples demonstrating how to use the Amazon Nova API, an OpenAI-compatible interface for Amazon Nova's latest models.

> ⚠️ Please note: The Amazon Nova API is not currently intended for production usage. See our [API Documentation](https://nova.amazon.com/dev/documentation) for rate limits and quotas. For higher rate limits and quotas, explore Amazon Nova models on [AWS](https://aws.amazon.com/nova/). 

## Get Started

To get started, ensure you have an Amazon Nova API Key. You can get one at [nova.amazon.com/dev](https://nova.amazon.com/dev/api).

If you are building on AWS, please see [AWS Samples for Amazon Nova](https://github.com/aws-samples/amazon-nova-samples/).


## Prerequisites

- Python 3.x
- Jupyter Notebook (for running .ipynb files)
- Nova API Key from [nova.amazon.com/dev](https://nova.amazon.com/dev/api)

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key:
```bash
cp .evn.example .env
```
4. Edit `.env` and replace `your_api_key_here` with your actual Amazon Nova API Key

> ⚠️  Important: Never commit your `.env` file to version control

## Suggested Workflow
### Getting Started with Amazon Nova
1. **[Getting Started](/00_getting_started.ipynb)**: Complete basic set up, make your first calls, and learn Amazon Novas new features
1. **[Multi Turn](/01_multi_turn_interactions.ipynb)**: Go from single calls, to chaining promp turns to complete a conversation with Amazon Nova
1. **[Multi Modal Understanding](/02_multimodal_understanding.ipynb)**: Get started with Amazon Nova's multi modal understanding capabilities, like image, and video understanding
1. **[Tool Use with Nova](/03_tool_use_with_nova.ipynb)**: Learn the basics of tool use with Amazon Nova
1. **[Nova Strands Agent](/04_nova_api_strands_sdk.ipynb)**: Get your first taste of building a simple agent with Strands SDK
### Build Agents with Amazon Nova
1. **[langchain/](/langchain/)**: Advanced examples of building Nova Agents with LangChain
1. **[strands/](/strands/)**: Advanced examples of building Nova Agents with LangChain
1. **[nova_agents/](/nova_agents/)**: Agentic application examples combining Nova Acts computer use capabilities


## License
This library is licensed under the MIT-0 License. See the [LICENSE](/LICENSE) file.
