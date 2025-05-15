from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

text = "The cat sat on the mat"

embeddings = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text)

print(embeddings)