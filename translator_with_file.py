from translate import Translator
translator= Translator(to_lang="bg")
with open('input_to_translate.txt',mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    with open('converted_file.txt',mode='w', encoding="utf-8") as write_file:
        write_file.write(translation)
    print(translation)
# Out [3]: 这是一支笔