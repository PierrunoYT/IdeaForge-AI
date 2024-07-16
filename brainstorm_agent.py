import requests
import os
from collections import defaultdict
from dotenv import load_dotenv
from docx import Document

# Load environment variables from .env file
load_dotenv()

class BrainstormAgent:
    @staticmethod
    def get_user_input():
        """Get user input for the brainstorming topic and output option."""
        topic = input("Enter your brainstorming prompt: ")
        output_option = input("Choose output option (1: Generate mind map, 2: Print ideas to Word file): ")
        return topic, output_option
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
            "model": "anthropic/claude-3.5-sonnet",
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


    def write_ideas_to_word(self, filename="brainstorm_ideas.docx"):
        """Write generated ideas to a Word document."""
        doc = Document()
        doc.add_heading('Brainstorming Ideas', 0)
        for idea in self.ideas:
            doc.add_paragraph(idea, style='List Bullet')
        doc.save(filename)
        print(f"Ideas have been written to {filename}")

    def generate_mind_map(self, topic):
        """Generate a mind map structure using OpenRouter API."""
        prompt = f"Create a mind map for the topic: {topic}. Provide the output as a JSON object where the key is the main topic and the value is a dictionary of subtopics and their related ideas."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "anthropic/claude-3.5-sonnet",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
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
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return None

# Example usage
if __name__ == "__main__":
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENROUTER_API_KEY in the .env file")
    
    agent = BrainstormAgent(api_key)
    topic, output_option = BrainstormAgent.get_user_input()
    
    if output_option == "1":
        print(f"\nGenerating mind map for: {topic}")
        mind_map = agent.generate_mind_map(topic)
        if mind_map:
            print("\nMind Map structure:")
            agent.print_mind_map()
        else:
            print("Failed to generate mind map. Please check your API key and try again.")
    elif output_option == "2":
        print(f"\nGenerating ideas for: {topic}")
        ideas = agent.generate_ideas(topic)
        print("\nGenerated ideas:")
        for idea in ideas:
            print(f"- {idea}")
        agent.write_ideas_to_word()
    else:
        print("Invalid option selected. Please run the script again and choose either 1 or 2.")
