"""
OpenAI Code Reviewer - Get AI feedback on your code using OpenAI with streaming output
"""
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

def get_language(file_path):
    """Get language from file extension."""
    ext = Path(file_path).suffix.lower()
    return {'.py': 'python', '.js': 'javascript', '.java': 'java', 
            '.html': 'html', '.css': 'css', '.cpp': 'cpp', 
            '.go': 'go', '.ts': 'typescript'}.get(ext, 'code')

def review_code_streaming(code, language):
    """Review code using Deepseekwith streaming output."""
    
    messages = [
        {"role": "system", "content": f"You are an expert {language} code reviewer. Be concise but thorough."},
        {"role": "user", "content": f"Review this {language} code for bugs, improvements, and best practices:\n\n```{language}\n{code}\n```"}
    ]
    
    try:
        print("\n--- CODE REVIEW ---")
        
        # Collect the complete response while streaming
        full_response = []
        
        # Stream the response
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.2,
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                time.sleep(0.01)  # Small delay for typing effect
                full_response.append(content)
        
        print("\n")  # Final newline
        return ''.join(full_response)
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python samples/openai-code-reviewer.py <code_file>")
        return
    
    try:
        file_path = sys.argv[1]
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        language = get_language(file_path)
        print(f"Reviewing {language} code in: {file_path}")
        
        review_code_streaming(code, language)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()