"""
Visual Planet Explorer using Nova Act and Nova Multimodal

This agent uses Nova's reasoning and image analysis capabilities and Nova Act's UI automation to navigate and analyze a planet's vibe
based on its visual presentation.
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
GYM_URL = "https://nova.amazon.com/act/gym"

def get_planet_info(nova: NovaAct) -> tuple[str, str]:
    """Navigate to a planet and extract its name and visual description"""
    # Navigate to destinations
    print("📍 Navigating to explore destinations...")
    nova.act("Click on NextDot, then click on 'Explore possible destinations'")
    
    # Explore planet
    print("\n🪐 Exploring a planet...")
    nova.act("Click on 'Details' for the first planet")
    
    # Get the planet name
    print("📸 Getting planet information...")
    planet_name = nova.act("Tell me the planet name shown on this page")
    
    # Get visual description
    print("👁️  Analyzing the planet's visual presentation...")
    visual_desc = nova.act(
        "Describe in detail the visual elements on this page: colors, layout, "
        "images, text styling, and overall design aesthetic"
    )
    
    return planet_name, visual_desc

def analyze_vibe(planet_name: str, visual_desc: str) -> str:
    """Use Nova to analyze the planet's vibe based on visual description"""
    print("\n🎨 Analyzing the planet's vibe...")
    
    vibe_prompt = f"""
    Based on this visual description of a planet profile page, describe the overall "vibe" 
    or atmosphere that the planet conveys. Consider the emotional tone, the feeling it evokes, 
    and what kind of experience a visitor might expect.
    
    Planet: {planet_name}
    
    Visual Description:
    {visual_desc}
    
    Describe the vibe in 2-3 sentences, focusing on the mood and atmosphere.
    """
    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": vibe_prompt}],
        max_tokens=512
    )
    
    return response.choices[0].message.content

def display_results(planet_name: str, visual_desc: str, vibe: str):
    """Display the analysis results in a formatted way"""
    print(f"\n{SEPARATOR}")
    print("🪐 PLANET VIBE ANALYSIS")
    print(f"{SEPARATOR}\n")
    print(f"Planet: {planet_name}\n")
    print("Visual Description:")
    print(SUB_SEPARATOR)
    print(visual_desc)
    print(f"\n{SEPARATOR}\n")
    print("🎨 The Vibe:")
    print(SUB_SEPARATOR)
    print(vibe)
    print(f"\n{SEPARATOR}")

def explore_planet_vibe():
    """
    Use Nova Act to navigate and analyze a planet's vibe
    """
    print("🚀 Visual Planet Vibe Explorer")
    print(SEPARATOR)
    print("\nThis agent will:")
    print(f"  1. Navigate to {GYM_URL}")
    print("  2. Explore a planet destination")
    print("  3. Analyze the visual presentation")
    print("  4. Determine the planet's vibe and atmosphere")
    print(f"\n{SEPARATOR}\n")
    
    with NovaAct(starting_page=GYM_URL) as nova:
        planet_name, visual_desc = get_planet_info(nova)
    
    # Analyze the vibe using Nova
    vibe = analyze_vibe(planet_name, visual_desc)
    
    # Display results
    display_results(planet_name, visual_desc, vibe)

def main():
    """Main execution function"""
    try:
        explore_planet_vibe()
        print("\n✅ Visual exploration completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
