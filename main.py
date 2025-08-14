import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

from system_prompt import *
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content
from functions.call_function import call_function


def handle_response(prompt,response):

    metadata = response.usage_metadata
    function_calls = response.function_calls
    response_text = response.text
    if "--verbose" in sys.argv:
        verb = True
    else:
        verb = False
    


    if function_calls is not None:
        for call in function_calls:
            func_resp = call_function(call,verb)
            try:
                func_resp.parts[0].function_response.response
                if verb:
                    print(f"-> {func_resp.parts[0].function_response.response}")
                    print(response_text)
                    print(f"User prompt: {prompt}")
                    print(f"Prompt tokens: {metadata.prompt_token_count}")
                    print(f"Response tokens: {metadata.candidates_token_count}")
            except:
                    raise ValueError("This is a fatal error message.")
    else:
        print(response_text)
        
        

    



def main():
    #Setup the ai model
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = 'gemini-2.0-flash-001'

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
    
    #Get a list of the functions available for it
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,schema_write_file,schema_run_python_file,schema_get_file_content
        ]
    )

    #Get the response and print it
    response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=SYS_PROMPT),
    )

    handle_response(prompt,response)
    

if __name__ == "__main__":
    main()
