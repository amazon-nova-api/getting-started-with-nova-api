# Nova Agent Examples

This folder demonstrates how to use the Nova API to use Amazon Nova models to build agentic applications. These are simple examples meant to spark ideas and serve as a starting point for development.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Strands Agents and Nova](#strands-agents-and-nova)
- [Image Analysis and Computer Use](#image-analysis-and-computer-use)
- [Knowledge Grounding and Computer Use](#knowledge-grounding-and-computer-use)

## Prerequisites

Before running any examples, you'll need:

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys:**

   ```bash
   # Nova API key
   echo "NOVA_API_KEY=your_nova_api_key_here" >> .env

   # Nova Act API key
   echo "NOVA_ACT_API_KEY=your_nova_act_api_key_here" >> .env
   ```

   **Where to get API keys:**

   - **Nova API Key**: Visit [nova.amazon.com/dev/api](https://nova.amazon.com/dev/api) to get your Nova API key
   - **Nova Act API Key**: Visit [nova.amazon.com/act/api](https://nova.amazon.com/act/api) to get your Nova Act API key

## Strands Agents and Nova

This section showcases Nova API integrated with Strands in 2 ways: Nova Strands Model Provider and Strands HTTP request tool. Both implementations coordinate UI automation with Nova Act and Nova Lite for story generation.

### Strands Model Provider

[`planet_story_strands_model_provider.py`](planet_story_strands_model_provider.py)

A Strands Agents implementation that configures Nova as the core Strands reasoning engine via the Nova API and the [Nova Strands Model Provider](https://github.com/amazon-nova-api/strands-nova).

**Features:**

- Uses Nova as the core reasoning engine for the Strands agent
- Nova orchestrates tool usage and story generation decisions
- Custom tool for planet data extraction with Nova Act
- Demonstrates native Nova integration within agent architecture

**Usage:**

```bash
python planet_story_strands_model_provider.py
```

### Strands HTTP Request Tool

[`planet_story_strands_http_tool.py`](planet_story_strands_http_tool.py)

A Strands Agents implementation that utilizes the Nova API via a [Strands HTTP Request tool](https://strandsagents.com/latest/documentation/docs/examples/python/agents_workflows/?h=http_request#http_request) for direct API integration, coordinating UI automation with Nova Act and Nova Lite for story generation.

**Features:**

- Uses Strands Agents framework with HTTP tool
- Direct Nova API calls via Strands SDK HTTP Request tool
- Custom tool for planet data extraction with Nova Act
- Demonstrates HTTP tool usage within agent architecture

**Usage:**

```bash
python planet_story_strands_http_tool.py
```

## Image Analysis and Computer Use

[`visual_planet_explorer.py`](visual_planet_explorer.py)

Uses Nova Act to navigate the web browser to find the planet profile and analyzes its "vibe" using Nova's Image Analysis capabilities based on visual presentation elements like colors, design, and layout.

**Features:**

- Uses Nova Act to navigate and analyze planet visual presentation
- Extracts detailed visual descriptions (colors, layout, design aesthetic)
- Uses Nova 2 Lite to interpret the overall vibe and atmosphere
- Demonstrates combining navigation with visual analysis

**Usage:**

```bash
python visual_planet_explorer.py
```

## Knowledge Grounding and Computer Use

[`grounded_planet_research.py`](grounded_planet_research.py)

Combines Nova Grounding to research real exoplanets, creating a comparison between science fiction and reality with Nova Act's UI automation for exploring fictional planets.

**Features:**

- Uses Nova Grounding to research real exoplanets with similar characteristics
- Uses Nova Act to extract information about fictional planets from the gym
- Use Nova Lite to compare fictional planets to actual astronomical discoveries
- Generates insights about sci-fi vs reality
- Demonstrates combining web navigation with grounded real-world research

**Usage:**

```bash
python grounded_planet_research.py
```
