import os

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory,file_path)
    abs_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    #print(f"abs_path = {abs_path}\nabs_working_dir= {abs_working_dir}")
    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000

    
    with open(full_path, "r") as f:
        content = f.read()
        if len(content)>MAX_CHARS:
            file_content_string = content(MAX_CHARS)
            file_content_string += f'...File "{file_path}" truncated at 10000 characters'
        else:
            file_content_string = content
            
   
    return file_content_string