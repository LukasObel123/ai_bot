import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



def handle_response(prompt,response):

    metadata = response.usage_metadata
    
    if "--verbose" in sys.argv:
        print(response.text)
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")
    else:
        print(response.text)
    



def main():
    #Setup the ai model
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    #Setup the prompt
    if len(sys.argv) < 2:
        print("Error! must provide prompt")
        sys.exit
    else:
        prompt = sys.argv[1]
    
    #Store a list of messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    #Get the response and print it
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    handle_response(prompt,response)
    

if __name__ == "__main__":
    main()
