from .config import CHARACTER_LIMIT
import os

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    full_path: str  = os.path.join(abs_working_directory, file_path)


    print(f"working_directory: {working_directory}")
    print(f"file_path: {file_path}")
    print(f"abs_working_directory: {abs_working_directory}")
    print(f"full_path: {full_path}")
    print(f"File exists at full_path: {os.path.exists(full_path)}")

    if not full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return(f'Error: File not found or is not a regular file: "{file_path}"')
    else:
        with open(full_path,"r") as file:
            content = file.read()
            if len(content) > CHARACTER_LIMIT:
                lines = []
                lines.append(content[:CHARACTER_LIMIT])
                lines.append(f'[...File "{file_path}" truncated at 10000 characters]')
                result = "\n".join(lines)

                return result

            return content