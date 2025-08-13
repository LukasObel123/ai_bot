import os





def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory,directory)
    abs_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{full_path}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{full_path}" is not a directory'

    ##Get directory and file information
    try:
        file_list = os.listdir(full_path)
    except Exception as e:
        return f"Error: {str(e)}"



    results = []
    for file in file_list:
        try:
            filesize = os.path.getsize(os.path.join(full_path,file))
        except Exception as e:
            return f"Error: {str(e)}"

        try:
            is_dir = os.path.isdir(os.path.join(full_path,file))
        except Exception as e:
            return f"Error: {str(e)}"

        results.append(f"- {file}: file_size={filesize} bytes, is_dir={is_dir}")

    return "\n".join(results)

