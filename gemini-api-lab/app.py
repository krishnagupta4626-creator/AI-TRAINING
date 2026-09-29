from google import genai

# Put your actual Gemini key here
API_KEY ="AQ.Ab8RN6I2LoUXAHQInB8N3TrBQH13WFxpZ3sV6uGCkVK6iDt4Bg"

client = genai.Client(api_key=API_KEY)

# Use Gemini 3.5 Flash-Lite (fastest response, rarely overloaded)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain artificial intelligence in simple terms."
)

print(response.text)