# Project: BasicBot
# Author: Jonathan Windle
# File: main.py
# 
# Tutorial project learning how to build an AI agent, use OpenAI REST API, and OpenRouter

import os
import sys
import argparse
from dotenv import load_dotenv
from openai import OpenAI #OpenAI Client object
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    # Load API Key from .env
    load_dotenv() #Collect .env variables from local dir
    api_key = os.environ.get("OPENROUTER_API_KEY") # Get API key value from env variable arg
    if api_key == None:
        raise RuntimeError("OpenRouter API key was not assigned") # Catch invalid key assignment

    # Create OpenAI API client object and connect it to OpenRouter instead of OpenAI, using our key.
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Parse cli arguments to get user provided prompt and other arguments
    parser = argparse.ArgumentParser(description="Chat Bot")
    parser.add_argument("user_prompt", type=str, help="User provided prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages: list[dict] = [
        {"role":"system", "content": system_prompt},
        {"role":"user", "content": args.user_prompt},
    ]

    # Stop when the model answers with text, or after 20 model calls.
    # The else clause runs only when the loop never breaks.
    for _ in range(20):
        response = generate_content(client, messages)

        if response.usage is None:
            raise RuntimeError("Failed API request - No response received")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        # A turn with no tool calls is the final answer. An empty one is not.
        if not message.tool_calls:
            content = (message.content or "").strip()
            if content:
                print(f"Final response: {content}")
                break
            messages.append({
                "role": "user",
                "content": (
                    "Please answer the original question in plain text. "
                    "Do not call any more tools."
                ),
            })
            continue

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if result_message.get("content") is None:
                raise Exception("Error: Function call returned no content")
            if args.verbose:
                print(f"-> {result_message['content']}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result_message["content"],
            })
    else:
        print("Maximum iterations reached. Exiting.")
        sys.exit(1)

    
def generate_content(client: OpenAI, messages: list[dict[str,str]]):
    # Send a chat (single message here) to a selected OpenRouter model (free)
    return client.chat.completions.create(
        model = "openrouter/free",
        messages=messages,
        temperature= 0,
        tools=available_functions,
    )






if __name__ == "__main__":
    main()
