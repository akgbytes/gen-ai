from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI assistant, who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for the next input.
3. Carefully analyze the user query.

Output Schema:
{{step: "string", content: "string"}}

Example:
Input: What is 2 + 2.
Output: {{step:"analyse", content:"Alright! The user is interested in maths and he/she is asking a basic arithmatic question."}}
Output: {{step:"think", content:"To perform addition I must go from left to right and add all operands one by one"}}
Output: {{step:"output", content:"4"}}
Output: {{step:"validate", content:"Seems like 4 is the correct answer for 2 + 2"}}
Output: {{step:"result", content:"2 + 2 = 4 and that is calculated by adding them"}}

"""

messages = [
    {"role":"system", "content":system_prompt},
]

query = input("> ")
messages.append({"role":"user", "content":query})

while True:
    response = client.chat.completions.create(
        response_format={"type": "json_object"},
        model="gpt-4o",
        messages=messages,
    )

    parsed_response = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_response)})

    if parsed_response.get("step") != "result":
        print(f"🧠: {parsed_response.get("content")}")
        continue

    print(f"🤖: {parsed_response.get("content")}")
    break;


