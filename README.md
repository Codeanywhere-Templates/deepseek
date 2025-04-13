[![Open in Codeanywhere](https://codeanywhere.com/img/open-in-codeanywhere-btn.svg)](https://app.codeanywhere.com/#https://github.com/Codeanywhere-Templates/deepseek)

This is a template project for OpenAI applications in [Codeanywhere](https://codeanywhere.com/). [Try it out](https://app.codeanywhere.com/#https://github.com/codeanywhere-templates/deepseek)

## Getting Started

Set your Deepseek API key:
```bash 
export DEEPSEEK_API_KEY=your_api_key_here
```

Open the terminal and run one of the example scripts:

```bash
python samples/openai-document-analyzer.py util/report.txt
python samples/openai-code-reviewer.py util/script.js
python samples/openai-content-creator.py "AI Applications" --type blog --tone professional
```

All dependencies are pre-installed in the devcontainer. You only need to create a `.env` file with your API key:

```
DEEPSEEK_API_KEY=your_api_key_here
```

## Features

- Development container for Deepseek applications
- Pre-installed dependencies
- Document analysis and summarization tools
- Code review and improvement utilities
- Content generation capabilities

## Usage Examples

### Document Analysis

```bash
# Summarize a document
python samples/deepseek-document-analyzer.py util/report.txt

# Summarize and save to a file
python samples/deepseek-document-analyzer.py util/report.txt summary.txt
```

### Code Review

```bash
# Review JavaScript code
python samples/deepseek-code-reviewer.py util/script.js
```

### Content Creation

```bash
# Create a blog post
python samples/deepseek-content-creator.py "Machine Learning Trends" --type blog

# Create social media content with a friendly tone
python samples/deepseek-content-creator.py "Product Launch" --type social --tone friendly

# Create a marketing email with a persuasive tone
python samples/deepseek-content-creator.py "Summer Sale" --type email --tone persuasive
```

## Learn More

To learn more about OpenAI, take a look at the following resources:

- [Deepseek Documentation](https://platform.deepseek.com) - learn about OpenAI features and API
- [API Reference](https://api-docs.deepseek.com/) - detailed API documentation


You can check out [the official Deepseek GitHub repository](https://github.com/deepseek-ai) - your feedback and contributions are welcome!

## Want to contribute?

Feel free to [open a PR](https://github.com/codeanywhere-templates/deepseek) with any suggestions for this template project 😃
