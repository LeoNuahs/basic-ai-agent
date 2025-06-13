import os
import sys

from google import genai
from dotenv import load_dotenv
from google.genai import types

def main():
    _ = load_dotenv()

    verbose = "--verbose" in sys.argv
    args = sys.argv[1:]
    if not args:
        print("Basic AI Agent")
        print("Usage: python main.py \"your-prompt-here\" [--verbose]")
        print("Example: python main.py \"Testing API connection...\"")
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = messages
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
