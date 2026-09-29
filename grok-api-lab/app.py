from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Create client pointing to Groq's OpenAI-compatible endpoint
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Send request to a Groq-supported model
response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "user", "content": "Explain artificial intelligence in simple terms."}
    ]
)

# Display the response
print(response.choices[0].message.content)