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

def translate_text(input_text, src_lang, dest_lang):

    # Perform translation
    result = GoogleTranslator(src_lang ='en', dest_lang='hu').translate(input_text)

    # Output the translated text
    print(f"Original text: {input_text}")
    print(f"Translated text: {result}")
    return result

if __name__ == "__main__":
 
    # input_file = input("Enter input text file name (e.g. input.txt): ").strip()
    # src_lang = input("Enter source language code (e.g. hu, en, de): ").strip()
    # dest_lang = input("Enter destination language code (e.g. en, hu, fr): ").strip()
    # output_file = input("Enter output file name (default: translated.txt): ").strip() or "translated.txt"
    #
    # translate_text_file(input_file, src_lang, dest_lang, output_file)
    input_text = "Hello, how are you?"
    translated2 = GoogleTranslator(source='en', target='hu').translate(input_text)
    print(f"Translated: {translated2}");

    translated3 = translate_text (input_text, 'en', 'hu');
    print(f"translate_text: {translated3}");