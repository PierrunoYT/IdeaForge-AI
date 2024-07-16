import random
from collections import defaultdict

class BrainstormAgent:
    def __init__(self):
        self.ideas = []
        self.mind_map = defaultdict(list)

    def generate_ideas(self, topic, num_ideas=10):
        """Generate a list of ideas related to the given topic."""
        # In a real implementation, this would use more sophisticated NLP techniques
        # For now, we'll use a simple random word generator as a placeholder
        words = ["innovative", "creative", "efficient", "sustainable", "digital",
                 "automated", "intelligent", "flexible", "scalable", "user-friendly"]
        
        self.ideas = [f"{random.choice(words)} {topic}" for _ in range(num_ideas)]
        return self.ideas

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
    agent = BrainstormAgent()
    topic = "product design"
    
    print(f"Generating ideas for: {topic}")
    ideas = agent.generate_ideas(topic)
    print("Generated ideas:")
    for idea in ideas:
        print(f"- {idea}")
    
    print("\nCreating mind map...")
    agent.create_mind_map()
    
    print("Mind Map:")
    agent.print_mind_map()
