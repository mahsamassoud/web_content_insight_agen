# app.py

import streamlit as st
from web_scraper import fetch_webpage_text
from inference import generate_insights

def parse_response(response: str):
    """
    Parses the LLM response into summary and recommendations.
    Expects the LLM response to contain the sections "Summary:" and "Recommendations:".
    """
    if "Summary:" in response and "Recommendations:" in response:
        summary_section = response.split("Recommendations:")[0].replace("Summary:", "").strip()
        recommendations = response.split("Recommendations:")[1].strip()
    else:
        summary_section = response
        recommendations = "No clear recommendations extracted."
    return summary_section, recommendations

def main():
    st.title("Web Content Insight Agent")
    st.write("Enter a webpage or blog post URL below to generate a summary and get accessibility & content quality insights.")
    
    url = st.text_input("Webpage URL:")
    
    if st.button("Analyze"):
        if not url.strip():
            st.error("Please enter a valid URL.")
            return
        
        st.info("Fetching webpage content...")
        content = fetch_webpage_text(url)
        if content.startswith("Error"):
            st.error(content)
            return
        
        # Optionally display a preview of the fetched content
        st.text_area("Extracted Content (preview):", value=(content[:1000] + "..." if len(content) > 1000 else content), height=150)
        
        st.info("Generating insights—please wait...")
        response = generate_insights(content)
        summary, recommendations = parse_response(response)
        
        st.subheader("Summary")
        st.write(summary)
        
        st.subheader("Accessibility & Content Quality Recommendations")
        st.write(recommendations)

if __name__ == "__main__":
    main()
