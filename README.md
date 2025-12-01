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

## Examples

1. **getting_started.ipynb**: Basic setup and interaction with Amazon Nova
1. **multi_turn.ipynb**: Shows multi-turn conversation capabilities
1. **nova_tools.ipynb**: Comprehensive guide to Nova's tool calling capabilities
1. **nova_strands_sdk.ipynb**: Building Nova powered agents with Strands SDK
1. **[langchain/](examples/langchain/)**: Examples using LangChain with Amazon Nova models
1. **[nova_agents/](examples/nova_agents/)**: Agentic application examples combining Nova's capabilities such as multimodal, knowledge grounding, and computer use.

## License
This library is licensed under the MIT-0 License. See the [LICENSE](/LICENSE) file.
