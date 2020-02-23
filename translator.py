from googletrans import Translator
translator = Translator()


with open('raw.txt', encoding='UTF-8', mode='r') as raw:
    textToBetranslated = raw.read()


translatedText = translator.translate(textToBetranslated, dest='en')
# print(textToBetranslated)
print(translatedText)



with open('translated.txt', encoding='UTF-8', mode='w') as translated:
    translated.write(translatedText.text)


