cd .\result
Python ..\Python\translate_text_file.py ..\TextInput\text1_eng.txt .\text1_hun.txt
Python ..\Python\Text_to_mp3.py ..\TextInput\text1_eng.txt .\text1_hun.txt ..\Pause\2sec.mp3 ..\Pause\1sec.mp3
del .\output_en_*.mp3
del .\output_hu_*.mp3