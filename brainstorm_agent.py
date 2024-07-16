import random
import requests
import os
from collections import defaultdict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BrainstormAgent:
    @staticmethod
    def get_user_input():
        """Get user input for the brainstorming topic and mind map option."""
        topic = input("Enter your brainstorming prompt: ")
        generate_mindmap = input("Do you want to generate a mind map directly? (yes/no): ").lower() == 'yes'
        return topic, generate_mindmap
    def __init__(self, api_key):
        self.ideas = []
        self.mind_map = defaultdict(list)
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate_ideas(self, topic, num_ideas=10):
        """Generate a list of ideas related to the given topic using OpenRouter API."""
        prompt = f"Generate {num_ideas} innovative ideas related to {topic}. Provide each idea as a short phrase or sentence."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "openrouter/anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        ideas_text = result['choices'][0]['message']['content']
        
        self.ideas = [idea.strip() for idea in ideas_text.split('\n') if idea.strip()]
        return self.ideas[:num_ideas]  # Ensure we return exactly num_ideas

    def create_mind_map(self):
        """Create a mind map from the generated ideas."""
        for idea in self.ideas:
            words = idea.split()
            for word in words:
                self.mind_map[word].append(idea)
        return dict(self.mind_map)

    def print_mind_map(self):
        """Print the mind map in a simple text format."""
        for key, values in self.mind_map.items():
            print(f"{key}:")
            for value in values:
                print(f"  - {value}")
            print()

    def generate_mind_map(self, topic):
        """Generate a mind map directly using OpenRouter API."""
        prompt = f"Create a mind map for the topic: {topic}. Provide the output as a JSON object where keys are main concepts and values are lists of related ideas."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "openrouter/anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        mind_map_text = result['choices'][0]['message']['content']
        
        # Extract the JSON part from the response
        import json
        start = mind_map_text.find('{')
        end = mind_map_text.rfind('}') + 1
        mind_map_json = mind_map_text[start:end]
        
        self.mind_map = json.loads(mind_map_json)
        return self.mind_map

# Example usage
if __name__ == "__main__":
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENROUTER_API_KEY in the .env file")
    
    agent = BrainstormAgent(api_key)
    topic, generate_mindmap = BrainstormAgent.get_user_input()
    
    if generate_mindmap:
        print(f"\nGenerating mind map for: {topic}")
        agent.generate_mind_map(topic)
    else:
        print(f"\nGenerating ideas for: {topic}")
        ideas = agent.generate_ideas(topic)
        print("\nGenerated ideas:")
        for idea in ideas:
            print(f"- {idea}")
        
        print("\nCreating mind map...")
        agent.create_mind_map()
    
    print("\nMind Map:")
    agent.print_mind_map()
