import os
from functions.get_files_info import is_valid_path
MAX_CHARS = 10_000

def write_file(working_directory: str, filepath: str, content: str) -> str:
    # Validate path, returns a report string and boolean.
    try:
        dir_bounds = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(dir_bounds, filepath))
        target_dir = os.path.dirname(target_path)
        if (result := is_valid_path(dir_bounds, target_dir)) and result[1]:
            print(result[0])
        else:
            # print(f"Failed Dir: {target_dir} | Dir Bounds: {dir_bounds}")
            return f"Error: Cannot write to \"{filepath}\" as it is outside the permitted working directory"
    except:
        raise Exception("Error: os.path method call failed")

    # Write contents to file
    if os.path.isdir(target_path):
        return f"Error: Cannot write to \"{filepath}\" as it is a directory"

    # Permit the creation of new parent directories if required. 
    try: 
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
    except:
        raise Exception(f"Error: Failed to create parent directories for \"{filepath}\"")

    try:
        with open(target_path, 'w') as f:
            f.write(content)
    except:
        raise Exception(f"Error: Could not write to file \"{filepath}\"")

    return f"Successfully wrote to file \"{filepath}\" ({len(content)} characters written)"


