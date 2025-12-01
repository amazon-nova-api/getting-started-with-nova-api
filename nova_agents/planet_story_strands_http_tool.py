"""
Planet Adventure Story Agent using Strands Agents

This agent uses the Strands Agents framework to orchestrate between Nova Act for data extraction
and Nova Lite for story generation.
"""

import os
import json
from dotenv import load_dotenv
from strands import Agent, tool
from nova_act import NovaAct

# Load environment variables
load_dotenv()

# Get Nova API key
NOVA_API_KEY = os.getenv("NOVA_API_KEY")
if not NOVA_API_KEY:
    raise ValueError("NOVA_API_KEY not found in environment variables. Please set it in your .env file.")

# Constants
MODEL_ID = "nova-lite-v1"
API_URL = "https://api.nova.amazon.com/v1/chat/completions"
SEPARATOR = "=" * 80

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

def create_story_with_nova(planet_info: str) -> str:
    """Use Nova Lite API to create an adventure story"""
    from strands_tools import http_request
    
    # Set bypass consent for automated execution
    os.environ["BYPASS_TOOL_CONSENT"] = "true"
    
    agent = Agent(tools=[http_request])
    
    story_prompt = f"""
    Based on the following information about planets, create an engaging adventure story 
    about an astronaut named Nova who visits 2 of these planets.
    
    Planet data:
    {planet_info}
    
    Story requirements:
    - The protagonist is an astronaut named Nova
    - Nova visits exactly 2 different planets from the data
    - On each planet, Nova faces challenges related to the weather conditions, terrain, 
      atmosphere, or environmental hazards specific to that planet
    - Nova must overcome these challenges using creativity and resourcefulness
    - The story should be exciting and adventurous
    - Include specific details about each planet's conditions from the data
    - Make it around 150-200 words
    """
    
    message_json = {
        "model": MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": "You are a creative storyteller who writes engaging adventure stories."
            },
            {
                "role": "user",
                "content": story_prompt
            }
        ],
        "max_tokens": 4096,
        "temperature": 0.7
    }
    
    # Make API call using Strands HTTP tool
    response = agent.tool.http_request(
        method="POST",
        url=API_URL,
        headers={"Content-Type": "application/json"},
        body=json.dumps(message_json),
        auth_type="Bearer",
        auth_token=NOVA_API_KEY
    )
    
    # Extract story from response
    raw_response = response['content'][2]['text']
    raw_response = raw_response.replace('Body: ', '')
    json_response = json.loads(raw_response)
    story = json_response['choices'][0]['message']['content']
    
    return story

def main():
    """Main execution function"""
    try:
        # Gather planet data using Nova Act
        print("🤖 Strands Agent starting...")
        planet_info = gather_planet_data()
        
        # Create adventure story using Nova Lite
        print("\n✍️  Creating adventure story about astronaut Nova...")
        story = create_story_with_nova(planet_info)
        
        print(f"\n{SEPARATOR}")
        print("🪐 ASTRONAUT NOVA'S PLANETARY ADVENTURE")
        print(f"{SEPARATOR}\n")
        print(story)
        print(f"\n{SEPARATOR}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
