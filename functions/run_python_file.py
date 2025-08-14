import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory,file_path)
    abs_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    #Checking if files and path exists and are correct format for safety
    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    instruc = ['python3',full_path] + args

    try:
        result = subprocess.run(instruc,capture_output=True,timeout = 30,cwd = abs_working_dir)
    except Exception as e:
        return f"Error: executing python file: {e}"

    out = result.stdout.decode()
    err = result.stderr.decode()
    base_str = f"STDOUT:{out}\nSTDERR:{err}"
    
    if result.returncode == 0:
        return base_str
    elif out + err == "":
        return "No output produced"
    else:
        return base_str + "\n"+ f"Process exited with code {result.returncode}"