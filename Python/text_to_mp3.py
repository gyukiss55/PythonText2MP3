from deep_translator import GoogleTranslator
from wsgiref.types import InputStream
from gtts import gTTS
import os
import sys

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

def text_to_mp3(input_str, lang, output_file):
    try:
        tts = gTTS(text=input_str, lang=lang)
        tts.save(output_file)
        print(f"✅ MP3 file saved as: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

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

def append_binfile(target_file, source_file):
    """
    Appends the contents of source_file to target_file in binary mode.

    :param target_file: The destination binary file (will be appended to)
    :param source_file: The source binary file to append
    """
    try:
        with open(source_file, "rb") as src, open(target_file, "ab") as dst:
            while chunk := src.read(4096):
                dst.write(chunk)
        print(f"✅ Appended '{source_file}' to '{target_file}' successfully.")
    except FileNotFoundError as e:
        print(f"❌ File not found: {e.filename}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

def translate_text_en_to_hun(input_text):

    # Perform translation
    result = GoogleTranslator(src_lang ='en', dest_lang='hu').translate(input_text)

    # Output the translated text
    print(f"Original text: {input_text}")
    print(f"Translated text: {result}")
    return result

def convert_to_mp3 (filename_en, filename_hu, long_pause, short_pause):
    result_en = read_textfile_byline(filename_en)
    result_hu = read_textfile_byline(filename_hu)
    list_en=[]
    for i, line_en in enumerate(result_en, start=1):
        list_en.append(line_en)
    list_hu=[]
    for i, line_hu in enumerate(result_hu, start=1):
        list_hu.append(line_hu)

    print("✅ Lines read from file:")
    for i in range(len(list_en)):
        print(f"{i:03d}: {list_en[i]} - {list_hu[i]}")
        fn_en = f"output_en_{i:03d}.mp3"
        fn_hu = f"output_hu_{i:03d}.mp3"
        text_to_mp3(list_en[i], 'en', fn_en)
        text_to_mp3(list_hu[i], 'hu', fn_hu)
        append_binfile(f"output.mp3", long_pause)
        append_binfile(f"output.mp3", fn_hu)
        append_binfile(f"output.mp3", short_pause)
        append_binfile(f"output.mp3", fn_en)
    append_binfile(f"output.mp3", long_pause)


def translate (filename_in, filename_out):
 
    print ("Input file:", filename_in)
    print ("Output file:", filename_out)
    result = read_textfile_byline(filename_in)
    print("✅ Lines read from file:")
    fo = open(filename_out, "a", encoding="utf-8")
    for i, line in enumerate(result, start=1):
        print(f"{i:03d}: {line}")
        result = translate_text_en_to_hun(line)
        print(f"Translated text2: {result}")
        fo.write(result + "\n")


# Example usage
# python E:\Work\GitHub\_MyGit\PythonText2MP3\Python\text_to_mp3.py
# E:\Work\GitHub\_MyGit\PythonText2MP3\TextInput\text1_eng.txt
# E:\Work\GitHub\_MyGit\PythonText2MP3\Result\text1_hu.txt

if __name__ == "__main__":
    if len(sys.argv) < 5: 
      print("Usage: python script.py <input engish file name> <input hungarien file name> <long pause> <short pause>") 
      sys.exit(1) 
    first_argument = sys.argv[1]  
    second_argument = sys.argv[2]  
    third_argument = sys.argv[1]  
    forth_argument = sys.argv[2]  
    convert_to_mp3(first_argument, second_argument, third_argument, forth_argument)

