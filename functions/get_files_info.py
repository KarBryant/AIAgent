import os

def get_files_info(working_directory, directory=None):
    abs_working_path = os.path.abspath(working_directory)
    directory = directory if directory is not None else "."
    full_path = os.path.abspath(os.path.join(abs_working_path, directory)) # type: ignore

    if not full_path.startswith(abs_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    else:
        return format_metadata(full_path)
    

def format_metadata(dir_path):
    lines = []
    try:
        for obj in os.listdir(dir_path):
            obj_path = os.path.join(dir_path, obj)
            lines.append(f"- {obj}: file_size={os.path.getsize(obj_path)} bytes, is_dir={os.path.isdir(obj_path)}")
        
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"