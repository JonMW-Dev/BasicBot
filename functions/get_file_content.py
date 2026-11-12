import os
from functions.get_files_info import is_valid_path
MAX_CHARS = 10_000

def get_file_content(working_directory: str, filepath: str) -> str:
    # Validate path, returns a report string and boolean.
    try:
        dir_bounds = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(dir_bounds, filepath))
        target_dir = os.path.dirname(target_path)
        if (result := is_valid_path(dir_bounds, target_dir)) and result[1]:
            print(result[0])
        else:
            # print(f"Failed Dir: {target_dir} | Dir Bounds: {dir_bounds}")
            return f"Error: Cannot read \"{filepath}\" as it is outside the permitted working directory"
    except:
        raise Exception("Error: os.path method call failed")
    
    # if the filepath is a directory, return error
    if not os.path.isfile(target_path):
        return f"Error: File not found or is not a regular file: \"{filepath}\""

    # Read contents of file
    try:
        with open(target_path, 'r') as f:
            contents = f.read(MAX_CHARS)

            if f.read(1):
                contents += f"[...File \"{filepath}]\"  truncated at {MAX_CHARS} characters"
    except:
        raise Exception("Error: error opening or reading from file")

    return contents
        

    