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
3. Create a `.env` file in the project root directory and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Usage

Run the script with:

```
python brainstorm_agent.py
```

When prompted:
1. Enter your brainstorming topic or question. For example:
   - "Create a mindmap about new viral products to sell on Alibaba"
   - "Please brainstorm ideas about pizza and tech"
2. Choose whether you want to generate a mind map directly or generate ideas first:
   - If you choose "yes" for generating a mind map directly, the script will create a mind map using the AI model.
   - If you choose "no", the script will generate ideas based on your input and then create a mind map from those ideas.

The script will display the resulting mind map in both cases.

## Requirements

See `requirements.txt` for a list of required Python packages.

## License

This project is open-source and available under the MIT License.
