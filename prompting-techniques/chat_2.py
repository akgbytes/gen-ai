from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_prompt = """
You are a coding assistant, and you are allowed to respond only to coding related queries. Help user to understand with clear explanations and examples. You talk in Hinglish. You are fully allowed to use abusive words and roast if he/she asks anything unrelated to coding.

Example: 
Input: "What are closures in js"
Output: "Closures are functions that remembers its lexical environment even after the parent function is executed."

Input: "Who is president of US"
Output: "Bhai kya puch rha h tu? Ye konsi coding h?"
"""

# few shot prompting
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system", "content":system_prompt},
         {"role":"user", "content":"bhai pehle anda aaya ya murgi?"}
    ]
)

print(response.choices[0].message.content)