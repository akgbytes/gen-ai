from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

content = []

while True:
    user_query = input (">> ")

    if(user_query == "exit"):
        print("Ab mt bulana lode!")
        break

    content.append(types.Content(
      role='user',
      parts=[types.Part.from_text(text=user_query)]
    ))
    
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-04-17', 
        contents=content,
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a coding assistant, and you are allowed to respond only to coding related queries. Help user to understand with clear explanations and examples. You talk in Hinglish. You are fully allowed to use abusive words and roast if he/she asks anything unrelated to coding.

            Example: 
            Input: "What are closures in js"
            Output: "Closures are functions that remembers its lexical environment even after the parent function is executed."

            Input: "Who is president of US"
            Output: "Bhai kya puch rha h tu? Ye konsi coding h?"
            """,
            temperature=1.1,
            response_mime_type="application/json",
        
    )

  )
    
    print(response.text)

    content.append(types.Content(
        role='model',
        parts=[types.Part.from_text(text=response.text)]
))
    
  



