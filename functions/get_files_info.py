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
        print(result[0])
        try:
            dir_bounds = os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(dir_bounds, directory))
        except: 
            raise Exception("Error: error in os.path method call")
    else:
        return result[0]

    # get file or directory information
    print(f"Searching directory: {target_dir}")
    dir_contents = os.listdir(target_dir)
    search_dir = directory
    if directory == ".":
        search_dir = "current"
    
    print(f"Result for {search_dir} directory:")
    for element in dir_contents:
        filename = element
        try:
            size = os.path.getsize(os.path.join(target_dir, element))
            is_dir = os.path.isdir(os.path.join(target_dir, element))
            print(f"\t - {filename}: file_size={size} bytes, is_dir={is_dir}")
        except:
            raise Exception(f"Error: os.path method error for {element}")
        
    return f"Success: \"{directory}\" is within the working directory"


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
    
    