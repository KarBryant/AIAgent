import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    try:
        content = client.models.generate_content(model ="gemini-2.0-flash-001", contents = sys.argv[1])
        print(content.text)

        print(f"Prompt tokens: {content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {content.usage_metadata.candidates_token_count}")
        print(sys.argv[1])

    except Exception as e:
        print("No Prompt Given.")
        sys.exit(1)
        
    
    

if __name__ == "__main__":
    main()