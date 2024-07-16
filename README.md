# BrainstormAgent

BrainstormAgent is a Python-based tool that uses OpenRouter's Anthropic Claude-3.5-sonnet model to generate innovative ideas and create mind maps for various topics.

## Features

- Generate ideas using advanced AI model
- Create mind maps from generated ideas
- Simple command-line interface

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenRouter API key as an environment variable:
   ```
   export OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the script with:

```
python brainstorm_agent.py
```

When prompted, enter your brainstorming topic or question. For example:
- "Create a mindmap about new viral products to sell on Alibaba"
- "Please brainstorm ideas about pizza and tech"

The script will generate ideas based on your input and create a mind map from those ideas.

## Requirements

See `requirements.txt` for a list of required Python packages.

## License

This project is open-source and available under the MIT License.
