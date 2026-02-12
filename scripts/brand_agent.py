import random

def generate_ad_prompt(theme):
    styles = ["glitchy VHS aesthetic", "distorted noir", "high-contrast neon", "minimalist rebellious"]
    locations = ["downtown Eugene, Oregon", "an abandoned industrial warehouse", "a misty forest", "a glitching digital void"]
    
    style = random.choice(styles)
    loc = random.choice(locations)
    
    prompt = f"Video Prompt: A high-quality 4k cinematic shot of a person wearing a Bland Sheep Apparel graphic tee. " \
             f"The scene is set in {loc} with a {style}. The Bland Sheep logo is visible and slightly distorted. " \
             f"The mood is 'Bland is the new bold'."
    
    return prompt

print("-" * 30)
print("🐑 BLAND SHEEP AD-GEN AGENT 🐑")
print("-" * 30)
theme_input = input("Enter a theme for your next drop (e.g., 'Winter', 'Street'): ")
print("\nGenerated Prompt for your Video AI:")
print(generate_ad_prompt(theme_input))
