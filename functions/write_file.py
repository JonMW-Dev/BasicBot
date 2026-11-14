import os
from functions.get_files_info import is_valid_path
MAX_CHARS = 10_000

def write_file(working_directory: str, filepath: str, content: str) -> str:
    # Validate path, returns a report string and boolean.
    try:
        dir_bounds = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(dir_bounds, filepath))
        target_dir = os.path.dirname(target_path)
        if not ((result := is_valid_path(dir_bounds, target_dir)) and result[1]):
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


# Schema for the get_file_content function
schema_write_file = {
	"type":"function",
	"function": {
		"name":"write_file",
		"description":"Write or overwrite the contents of a file with the provided string. If the file does not exist, it will be created along with any necessary parent directories.",
		"parameters": {
			"type": "object",
			"properties": {
				"filepath": {
					"type":"string",
					"description": "Directory path to the file to read, relative to the working directory"
				},
                "content": {
                    "type":"string",
                    "description": "Content to write to the file"   
                },
			},
		},
	},
}