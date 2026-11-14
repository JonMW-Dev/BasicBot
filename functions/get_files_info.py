# get_files_info.py | Date: 12-11-2026 | Author: Jonathan Windle
# Validates that the path the AI wants to work in is a permitted path

import os #for pathing functions

# get_file_info - Confirm that the directory an AI is acting on is contained
# within a pre-approved location.
	# Inputs: The absolute path of the approved dir called working_directory,        
	# and the ai determined directory
	# Outputs: a string that reports the status of the function to the LLM. 
def get_files_info(working_directory: str, directory: str = ".") -> str:
    # Validate path, returns a report string and boolean.
    if (result := is_valid_path(working_directory, directory)) and result[1]:
        try:
            dir_bounds = os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(dir_bounds, directory))
        except Exception:
            return "Error: error in os.path method call"
    else:
        return result[0]

    # The model only sees the return value, so the listing has to be in it.
    try:
        dir_contents = os.listdir(target_dir)
    except Exception:
        return "Error: error in os.path method call"

    lines: list[str] = []
    for element in dir_contents:
        try:
            element_path = os.path.join(target_dir, element)
            size = os.path.getsize(element_path)
            is_dir = os.path.isdir(element_path)
            lines.append(f"- {element}: file_size={size} bytes, is_dir={is_dir}")
        except Exception:
            return f"Error: os.path method error for {element}"

    return "\n".join(lines)

# Schema for the get_files_info function
schema_get_files_info = {
	"type":"function",
	"function": {
		"name":"get_files_info",
		"description":"Lists files in a specified directory relative to the working directory",
		"parameters": {
			"type": "object",
			"properties": {
				"directory": {
					"type":"string",
					"description": "Directory path to list files from , relative to the working directory (default is the working directory itself)"
				},
			},
		},
	},
}

def is_valid_path(working_directory: str, directory: str = ".") -> tuple[str, bool]:
    # Confirm that directory is a valid path
    try:
        dir_bounds = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(dir_bounds, directory))
        common_pth = os.path.commonpath([dir_bounds, target_dir])
        # Confirm that directory is a valid path
        if not os.path.isdir(target_dir):
            return f"Error: \"{directory}\" is not a directory", False
        # Validate that directory is within working_directory
        if common_pth != dir_bounds:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory", False


    except:
        raise Exception("Error: error in os.path method call")

    return f"Path validated", True
    
