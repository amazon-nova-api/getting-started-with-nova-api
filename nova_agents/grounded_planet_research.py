"""
Grounded Planet Research using Nova Act and Nova Grounding

This agent uses Nova Act's UI automation to explore planets on the gym website, then uses
Nova's grounding capability to research real-world information about similar
exoplanets and compare them.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from nova_act import NovaAct

# Load environment variables
load_dotenv()

# Initialize Nova API client
api_key = os.getenv("NOVA_API_KEY")
if not api_key:
    raise ValueError("NOVA_API_KEY not found in environment variables. Please set it in your .env file.")

base_url = "https://api.nova.amazon.com/v1"
client = OpenAI(api_key=api_key, base_url=base_url)

# Constants
MODEL_ID = "nova-lite-v1"
SEPARATOR = "=" * 80
SUB_SEPARATOR = "-" * 80

def call_nova_api(query: str, use_grounding: bool = False, max_tokens: int = 2048) -> str:
    """Call Nova API with optional grounding"""
    request_params = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": query}],
        "max_tokens": max_tokens
    }
    
    if use_grounding:
        request_params["extra_body"] = {"system_tools": ["nova_grounding"]}
    
    response = client.chat.completions.create(**request_params)
    return response.choices[0].message.content

def grounded_planet_research():
    """
    Use Nova Act to explore fictional planets, then use Nova Grounding
    to research real exoplanets and create a comparison
    """
    print("🚀 Grounded Planet Research Agent")
    print(SEPARATOR)
    print("\nThis agent will:")
    print("  1. Use Nova Act to explore planets on nova.amazon.com/act/gym")
    print("  2. Extract planet characteristics from the gym")
    print("  3. Use Nova Grounding to research real exoplanets")
    print("  4. Create a comparison between fictional and real planets")
    print(f"\n{SEPARATOR}\n")
    
    planets_info = []
    
    with NovaAct(starting_page="https://nova.amazon.com/act/gym") as nova:
        # Navigate to destinations
        print("📍 Navigating to explore destinations...")
        nova.act("Click on NextDot, then click on 'Explore possible destinations'")
        
        # Gather information for both planets
        for i in range(1, 3):
            print(f"\n🪐 Exploring Planet {i}...")
            planet_selector = "first" if i == 1 else "second"
            
            if i == 2:
                nova.act("Go back to the destinations list")
            
            nova.act(f"Click on 'Details' for the {planet_selector} planet")
            
            # Get planet information
            print("📊 Extracting planet characteristics...")
            planet_info = nova.act(
                "Extract the following information about this planet: "
                "planet name, distance from Earth, environmental conditions, "
                "and any unique characteristics mentioned"
            )
            
            planets_info.append(planet_info)
    
    # Research real exoplanets using Nova Grounding
    print(f"\n{SEPARATOR}")
    print("🌍 RESEARCHING REAL EXOPLANETS")
    print(f"{SEPARATOR}\n")
    
    print("🔍 Using Nova Grounding to research real exoplanets...")
    research_query = f"""
    I found information about these fictional planets from a space travel website:
    
    Planet 1: {planets_info[0]}
    Planet 2: {planets_info[1]}
    
    Please research real exoplanets that have similar characteristics to these fictional ones.
    For each fictional planet, find a real exoplanet with similar:
    - Distance from Earth
    - Environmental conditions
    - Habitability factors
    
    Provide a brief comparison showing how the fictional planets compare to real discoveries.
    """
    
    grounded_research = call_nova_api(research_query, use_grounding=True)
    
    # Display results
    print(f"\n{SEPARATOR}")
    print("📋 FICTIONAL VS REAL EXOPLANETS")
    print(f"{SEPARATOR}\n")
    
    print("Fictional Planets from Nova Act Gym:")
    print(SUB_SEPARATOR)
    for i, info in enumerate(planets_info, 1):
        print(f"\nPlanet {i}:")
        print(info)
    
    print(f"\n{SEPARATOR}\n")
    print("Real Exoplanet Research (with Nova Grounding):")
    print(SUB_SEPARATOR)
    print(grounded_research)
    print(f"\n{SEPARATOR}")
    
    # Generate final insights
    print("\n🔬 Generating insights...")
    insights_query = f"""
    Based on this comparison between fictional planets and real exoplanets:
    
    Fictional: {planets_info[0]} and {planets_info[1]}
    Real Research: {grounded_research}
    
    Provide 2-3 interesting insights about how science fiction representations 
    compare to actual exoplanet discoveries. Keep it brief and engaging.
    """
    
    insights = call_nova_api(insights_query, max_tokens=512)
    
    print("\n💡 KEY INSIGHTS")
    print(SUB_SEPARATOR)
    print(insights)
    print(f"\n{SEPARATOR}")

def main():
    """Main execution function"""
    try:
        grounded_planet_research()
        print("\n✅ Grounded research completed successfully!")
        print("\n📚 This demo showed how Nova Act (web navigation) and Nova Grounding")
        print("   (real-world research) can work together to compare fictional and real data.")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
