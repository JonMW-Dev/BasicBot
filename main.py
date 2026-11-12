# Project: BasicBot
# Author: Jonathan Windle
# File: main.py
# 
# Tutorial project learning how to build an AI agent, use OpenAI REST API, and OpenRouter

import os 
import argparse
from dotenv import load_dotenv
from openai import OpenAI #OpenAI Client object

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
    messages: list[dict[str,str]] = [{
        "role":"user",
        "content":f"{args.user_prompt}",
    }]

    # send prompt to model and receive response
    response = generate_content(client, messages)

    # Print the token usage of the message-response and the model response
    if response.usage == None:
        raise RuntimeError("Failed API request - No response recieved")

    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    
    print(response.choices[0].message.content)


def generate_content(client: OpenAI, messages: list[dict[str,str]]):
    # Send a chat (single message here) to a selected OpenRouter model (free)
    return client.chat.completions.create(
        model = "openrouter/free",
        messages=messages
    )

if __name__ == "__main__":
    main()
