"""
Planet Adventure Story Agent using Strands Agents with Nova Model Provider

This agent uses the Strands Agents framework with Nova as the core reasoning engine
to orchestrate between Nova Act for data extraction and Nova for story generation.
"""

import os
from dotenv import load_dotenv
from nova_act import NovaAct
from strands import Agent, tool
from strands_amazon_nova import NovaAPIModel

# Load environment variables
load_dotenv()

# Get Nova API key
NOVA_API_KEY = os.getenv("NOVA_API_KEY")
if not NOVA_API_KEY:
    raise ValueError(
        "NOVA_API_KEY not found in environment variables. Please set it in your .env file."
    )

# Constants
SEPARATOR = "=" * 80

# Initialize Nova Model Provider for Strands
nova_model = NovaAPIModel(
    api_key=NOVA_API_KEY, 
    model_id="nova-lite-v2",
    stream=False
)


@tool
def gather_planet_data() -> str:
    """
    Use Nova Act to navigate to nova.amazon.com/act/gym and gather information about 2 planets.
    Returns detailed information about planet environments and conditions.
    """
    print("🚀 Starting planet data gathering...")
    print("📍 Navigating to nova.amazon.com/act/gym...")

    planet_data = ""

    with NovaAct(starting_page="https://nova.amazon.com/act/gym") as nova:
        # Navigate to explore destinations
        print("🪐 Navigating to explore destinations...")
        nova.act("Click on NextDot, then click on 'Explore possible destinations'")

        # Gather information for both planets
        planets = []
        for i in range(1, 3):
            print(f"🪐 Gathering information for planet {i}...")
            planet_selector = "first" if i == 1 else "second"
            nova.act(f"Click on 'Details' for the {planet_selector} planet")

            extraction_prompt = "Extract all information from the planetary profile including planet name, weather conditions, terrain, atmosphere, and environmental characteristics"
            if i == 1:
                extraction_prompt += ". Then go back to the destinations list."

            result = nova.act(extraction_prompt)
            planets.append(f"Planet {i}:\n{result}")

        planet_data = "\n\n".join(planets)

    print(f"✅ Gathered data about 2 planets")
    return planet_data


# Create the Strands agent with Nova Model Provider and Nova Act Tool
agent = Agent(
    model=nova_model,
    tools=[gather_planet_data],
    system_prompt=(
        "You are a creative storyteller who writes engaging adventure stories.\n\n"
        "Your expertise includes:\n"
        "- Creating exciting space adventure stories\n"
        "- Writing about astronauts facing planetary challenges\n"
        "- Incorporating specific environmental details into narratives\n"
        "- Making stories adventurous and engaging\n\n"
        "When creating stories:\n"
        "- The protagonist should be an astronaut named Nova\n"
        "- Nova should visit exactly 2 different planets from the provided data\n"
        "- On each planet, Nova should face challenges related to the specific weather conditions, terrain, atmosphere, or environmental hazards\n"
        "- Nova must overcome these challenges using creativity and resourcefulness\n"
        "- Include specific details about each planet's conditions from the data\n"
        "- Make the story exciting, adventurous, and around 150-200 words\n"
    ),
)


def main():
    """Main execution function"""
    try:
        print("🤖 Strands Agent with Nova Model Provider starting...")

        # Agent uses Nova as core reasoning engine to orchestrate the workflow
        response = agent(
            "Use the gather_planet_data tool to collect information about planets, "
            "then create an engaging adventure story about astronaut Nova visiting 2 of these planets. "
            "Make sure Nova faces specific challenges related to each planet's environmental conditions."
        )

        print(f"\n{SEPARATOR}")
        print("🪐 ASTRONAUT NOVA'S PLANETARY ADVENTURE")
        print(f"{SEPARATOR}\n")
        print(response)
        print(f"\n{SEPARATOR}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise


if __name__ == "__main__":
    main()