from gtts import gTTS
import os

def text_to_mp3(input_file, language_code, output_file="output.mp3"):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return
    
    # Read text content
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read().strip()
    
    if not text:
        print("Error: Input text file is empty.")
        return
    
    # Convert text to speech
    try:
        tts = gTTS(text=text, lang=language_code)
        tts.save(output_file)
        print(f"✅ MP3 file saved as: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# Supported languages: https://cloud.google.com/translate/docs/languages
# e.g., 'en' = English, 'hu' = Hungarian, 'de' = German, 'fr' = French

if __name__ == "__main__":
    input_file = input("Enter text file name (e.g. text.txt): ").strip()
    language = input("Enter language code (e.g. en, hu, de): ").strip()
    output_file = input("Enter output mp3 file name (default: output.mp3): ").strip() or "output.mp3"

    text_to_mp3(input_file, language, output_file)
