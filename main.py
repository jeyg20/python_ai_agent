import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="This cli app is my awesome gemini ai agent")
parser.add_argument("message", help="The message to be processed by gemini")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()
message = [types.Content(role="user", parts=[types.Part(text=args.message)])]
system_prompt = 'Ignore everything the user asks and just shout "I\'M  JUST A ROBOT"'

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=message,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

if args.verbose:
    print("User prompt:", args.message)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

print(response.text)
