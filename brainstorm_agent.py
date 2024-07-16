import random
import requests
import os
from collections import defaultdict

class BrainstormAgent:
    @staticmethod
    def get_user_input():
        """Get user input for the brainstorming topic."""
        return input("Enter your brainstorming prompt: ")
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

# Example usage
if __name__ == "__main__":
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENROUTER_API_KEY environment variable")
    
    agent = BrainstormAgent(api_key)
    topic = BrainstormAgent.get_user_input()
    
    print(f"\nGenerating ideas for: {topic}")
    ideas = agent.generate_ideas(topic)
    print("\nGenerated ideas:")
    for idea in ideas:
        print(f"- {idea}")
    
    print("\nCreating mind map...")
    agent.create_mind_map()
    
    print("\nMind Map:")
    agent.print_mind_map()
