import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
  
    try:
        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]
        content = client.models.generate_content(model ="gemini-2.0-flash-001", contents = messages)

        if sys.argv[2] == "--verbose":
            print(f"User prompt: {content.text}")
            print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {content.usage_metadata.candidates_token_count}")
        

    except Exception as e:
        print("No Prompt Given.")
        sys.exit(1)
        
    
    

if __name__ == "__main__":
    main()
