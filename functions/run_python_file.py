# Function to run a Python file

import os
import subprocess
#from os import subprocess, STDOUT
from functions.get_files_info import is_valid_path

def run_python_file(working_directory: str, filepath: str, args: list[str] | None = None) -> str:
    # Validate path, returns a report string and boolean.
    try:
        dir_bounds = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(dir_bounds, filepath))
        target_dir = os.path.dirname(target_path)
        if not ((result := is_valid_path(dir_bounds, target_dir)) and result[1]):
            return f"Error: Cannot execute \"{filepath}\" as it is outside the permitted working directory"
    except:
        raise Exception("Error: os.path method call failed")



    # Confirm that the file exists and is a Python file
    if not os.path.isfile(target_path):
        return f"Error: \"{filepath}\" does not exist or is not a regular file"
    if not filepath.endswith(".py"):
        return f"Error: \"{filepath}\" is not a Python file"



    # Prepare command to run the Python file
    command = ["python", target_path] # command to run the Python file
    if args != None and len(args) > 0: # add any additional arguments to the command
        command.extend(args)

    try: 
        # Execute the CP with command and capture the output and errors
        completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)

        # Check return code of CP and handle errors
        result: list[str] = []
        if completed_process.returncode != 0:
            result.append(f"Process exited with code {completed_process.returncode}")
        
        if len(completed_process.stdout) and len(completed_process.stdout) == 0:
            # add a message to the output string if the stdout is empty
            result.append("Error: No output produced")

        result.append(f"\nSTDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}") 
        return "\n".join(result)
    except:
        raise Exception(f"Error: executing Python file: {filepath}")
    
# Schema for the run_python_file function
schema_run_python_file = {
	"type":"function",
	"function": {
		"name":"run_python_file",
		"description":"Execute a Python file with optional arguments and return the output. The file must be within the working directory.",
		"parameters": {
			"type": "object",
			"properties": {
				"filepath": {
					"type":"string",
					"description": "Directory path to the file to read, relative to the working directory"
				},
                "args": {
                    "type":"array",
                    "description": "Optional list of arguments to pass to the Python file when executing it",
                    "items": {
                        "type": "string"
                    }
                }
			},
		},
	},
}