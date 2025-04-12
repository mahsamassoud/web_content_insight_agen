# inference.py

from huggingface_hub import InferenceClient

# Replace with your actual Hugging Face API key

MODEL_NAME = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    provider="cerebras",
    api_key=API_KEY,
)
def generate_insights(text: str, max_tokens: int = 512) -> str:
    """
    Generates insights (summary and recommendations) for the given text.
    Uses the HF Inference API with the specified model.
    """
    prompt = (
        "You are an expert digital content and accessibility advisor. "
        "Given the following content from a webpage or blog post, provide two outputs:\n\n"
        "1. A concise summary of the content (a few sentences highlighting the key points).\n"
        "2. Actionable recommendations for improving accessibility (e.g., alt text for images, clear headings, language clarity) "
        "and overall content quality.\n\n"
        "Format:\n"
        "Summary:\n<Your summary here>\n\n"
        "Recommendations:\n<Your recommendations here>\n\n"
        f"Content:\n{text}\n\n"
        "Your analysis:"
    )

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=max_tokens,
    )
    # Assuming the API returns a field 'message' in the first choice.
    result = completion.choices[0].message
    return result
