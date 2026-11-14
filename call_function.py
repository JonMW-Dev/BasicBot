# allows the AI to call funcitons
import json
from collections.abc import Callable
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file

available_functions = [
    schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file
]

def _tool_message(tool_call_id: str, content: str) -> dict:
    return {
        "role": "tool",
        "tool_call_id": tool_call_id,
        "content": content,
    }

# calls one of the four defined functions
def call_function(tool_call, verbose: bool = False) -> dict:
    func_name = tool_call.function.name
    raw_args = tool_call.function.arguments or "{}"

    try:
        func_args = json.loads(raw_args)
        if not isinstance(func_args, dict):
            raise ValueError("arguments must be a JSON object")
    except (json.JSONDecodeError, ValueError) as error:
        if verbose:
            print(f" - Calling function: {func_name}({raw_args})")
        else:
            print(f" - Calling function: {func_name}")
        return _tool_message(
            tool_call.id,
            f"Error: Invalid arguments for {func_name}: {error}",
        )

    # Inject the working directory. The model must not be able to choose it.
    func_args["working_directory"] = "./calculator"

    if verbose:
        print(f" - Calling function: {func_name}({func_args})")
    else:
        print(f" - Calling function: {func_name}")

    function_map: dict[str, Callable[..., str]] = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    if func_name not in function_map:
        return _tool_message(tool_call.id, f"Error: Unknown function: {func_name}")

    try:
        result = function_map[func_name](**func_args)
    except Exception as error:
        result = f"Error: {error}"

    if not isinstance(result, str):
        result = "Error: Function call returned no content"

    return _tool_message(tool_call.id, result)