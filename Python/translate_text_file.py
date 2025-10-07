from deep_translator import GoogleTranslator
import os

def translate_text_file(input_file, src_lang, dest_lang, output_file="translated.txt"):
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found.")
        return

    # Read the text from the file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("⚠️ Error: Input text file is empty.")
        return


    print(f"🔄 Translating from '{src_lang}' to '{dest_lang}' ...")

    # Translate the text
    try:
        result = GoogleTranslator(src_lang='en', dest_lang='hu').translate(text)
        translated_text = result.text

        # Save the translated text
        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write(translated_text)

        print(f"✅ Translation complete! Saved to: {output_file}")

    except Exception as e:
        print(f"❌ Translation failed: {e}")

def translate_text_en_to_hun(input_text):

    # Perform translation
    result = GoogleTranslator('en', 'hu').translate(input_text)

    # Output the translated text
    print(f"Original text: {input_text}")
    print(f"Translated text: {result}")
    return result

# Example usage:
# Supported languages: https://cloud.google.com/translate/docs/languages
# e.g., 'en' = English, 'hu' = Hungarian, 'de' = German, 'fr' = French

def read_textfile_byline(filename):
    """
    Reads a text file line by line and returns a list of strings.

    :param filename: Path to the text file
    :return: List of strings (each line without newline characters)
    """
    lines = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = [line.rstrip("\n") for line in file]
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")

    return lines

# python E:\Work\GitHub\_MyGit\PythonText2MP3\Python\translate_text_file.py
# E:\Work\GitHub\_MyGit\PythonText2MP3\TextInput\text1_eng.txt

if __name__ == "__main__":
 
    filename_in = input("Enter input text file name (e.g. input.txt): ").strip()
    filename_out = input("Enter output text file name (e.g. output.txt): ").strip()
    result = read_textfile_byline(filename_in)
    print("✅ Lines read from file:")
    fo = open(filename_out, "a", encoding="utf-8")
    for i, line in enumerate(result, start=1):
        print(f"{i:03d}: {line}")
        result = translate_text_en_to_hun(line)
        print(f"Translated text2: {result}")
        fo.write(result + "\n")
