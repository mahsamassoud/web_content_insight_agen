# Web Content Insight Agent

This project is a web-based agent that fetches webpage or blog post content, then uses a large language model via the Hugging Face Inference API (powered by Cerebras) to generate:
- **A Summary** of the content.
- **Accessibility & Content Quality Recommendations**, such as improving alt text, structuring headings, and clarifying language.

The tool is designed for quick insights, making it easier for content managers, bloggers, and web developers to quickly assess and optimize content.

## Features

- **Web Scraping:**  
  Extracts clean text from a user-provided URL by removing unnecessary elements (scripts, styles, navigation, etc.).

- **Dual Output Analysis:**  
  Uses the Hugging Face Inference API to generate:
  - A concise summary of the content.
  - Actionable recommendations to improve accessibility and overall content quality.

- **Interactive UI:**  
  Built with Streamlit, the web interface allows users to input a URL and immediately view results.

## Folder Structure

