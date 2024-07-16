# IdeaForge AI

IdeaForge AI is a Python-based tool that uses OpenRouter's Anthropic Claude-3.5-sonnet model to generate innovative ideas and create mind maps for various topics.

## Features

- Generate ideas using advanced AI model
- Create mind maps from generated ideas
- Simple command-line interface

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Create a `.env` file in the project root directory and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```
7. The script will automatically download the required NLTK data on first run. If you want to download it manually, you can run:
   ```
   python -c "import nltk; nltk.download('stopwords')"
   ```

## Usage

Make sure your virtual environment is activated before running the script.

Run the script with:

```
python ideaforge_ai.py
```

When prompted:
1. Enter your brainstorming topic or question. For example:
   - "Create a mindmap about new viral products to sell on Alibaba"
   - "Please brainstorm ideas about pizza and tech"
2. Choose your output option:
   - Enter "1" to generate a mind map using the AI model and Graphviz.
   - Enter "2" to generate ideas and save them to a Word document.

The script will either create a Graphviz mind map (saved as "mind_map.png") or save the ideas to a Word file named "brainstorm_ideas.docx" in the current directory.

## Requirements

See `requirements.txt` for a list of required Python packages.

## License

This project is open-source and available under the MIT License.
