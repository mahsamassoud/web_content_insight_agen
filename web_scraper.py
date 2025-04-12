# web_scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_webpage_text(url: str) -> str:
    """
    Fetches the webpage content from a given URL, strips out unneeded elements,
    and returns the clean text. Returns an error message string if there is an issue.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script, style, and common non-content tags
        for tag in soup(["script", "style", "header", "footer", "nav"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        return text.strip()
    except Exception as e:
        return f"Error fetching URL: {str(e)}"
