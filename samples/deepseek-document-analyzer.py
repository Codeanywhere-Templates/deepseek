"""
OpenAI Document Analyzer - Summarize text files using OpenAI with streaming output
"""
import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

def summarize_text_streaming(text):
    """Get a summary of text using Deepseek with streaming output."""
    
    messages = [
        {"role": "system", "content": "You are an expert summarizer. Be concise but comprehensive."},
        {"role": "user", "content": f"Please summarize the following text:\n\n{text}"}
    ]
    
    try:
        print("\n--- SUMMARY ---")
        
        # Collect the complete response while streaming
        full_response = []
        
        # Stream the response
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.3,
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
        print("Usage: python samples/openai-document-analyzer.py <filename> [output_filename]")
        return
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
        
        print(f"Analyzing: {sys.argv[1]}")
        summary = summarize_text_streaming(text)
        
        # Save summary if requested
        if len(sys.argv) > 2 and summary:
            with open(sys.argv[2], 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"\nSummary saved to: {sys.argv[2]}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()