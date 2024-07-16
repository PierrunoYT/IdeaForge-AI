# IdeaForge AI

Unleash your creativity with IdeaForge AI! This Python-based tool harnesses the power of OpenRouter's Anthropic Claude-3.5-sonnet model to generate innovative ideas and create mind maps for any topic you can imagine.

## Features

- 🧠 Generate creative ideas using advanced AI
- 🗺️ Visualize concepts with auto-generated network graphs
- 💻 User-friendly command-line interface
- 📄 Export ideas to Word documents

## Getting Started

Follow these steps to quickly set up and start using IdeaForge AI:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenRouter API key in a `.env` file
4. Run the script: `python ideaforge_ai.py`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ideaforge-ai.git
   cd ideaforge-ai
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your API key:
   Create a `.env` file in the project root and add:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

5. Download NLTK data (automatic on first run, or manually):
   ```
   python -c "import nltk; nltk.download('stopwords')"
   ```

## Usage

1. Activate your virtual environment:
   ```
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Run the script:
   ```
   python ideaforge_ai.py
   ```

3. Follow the prompts:
   - Enter your brainstorming topic (e.g., "New viral products for Alibaba" or "Pizza and tech innovations")
   - Choose output format:
     - Option 1: Generate a network graph (saved as "idea_network.png")
     - Option 2: Save ideas to a Word document ("brainstorm_ideas.docx")

## Contributing

We welcome contributions! If you'd like to improve IdeaForge AI:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

This project is open-source and available under the MIT License.

## Requirements

See `requirements.txt` for a list of required Python packages.
