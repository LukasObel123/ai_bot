import os
from google import genai
from google.genai import types
from system_prompt import *
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content

func_dict = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
    "get_file_content":get_file_content
}

def call_function(function_call_part, verbose=False):
    name = function_call_part.name
    args = function_call_part.args

    if verbose:
        print(f"Calling function: {name}({args})")
    else:
        print(f" - Calling function: {name}")
    
    args["working_directory"] = "./calculator"


    func_result = func_dict[name](**args)

    if name not in func_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name,
                    response={"error": f"Unknown function: {name}"},
                )
            ],
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name,
                response={"result": func_result},
            )
        ],
    )
    



    
            


    
    
