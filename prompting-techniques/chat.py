from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# zero-shot prompting
response = client.chat.completions.create(
    temperature=1.1,
    max_tokens=50,
    model="gpt-4",
    messages=[
        {"role":"user", "content":"hello there"}
    ]
)

print(response.choices[0].message.content)

