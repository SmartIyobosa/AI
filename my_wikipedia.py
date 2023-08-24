import wikipedia
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

searchQuestion = input('What do you want to know? ')

# you can edit the number of sentences below

result = wikipedia.summary(searchQuestion, sentences=3)

# Split the summary into smaller chunks
chunk_size = 200  # Adjust the chunk size as needed
chunks = [result[i:i + chunk_size] for i in range(0, len(result), chunk_size)]

for chunk in chunks:
    print(chunk)  # Print each chunk for visibility
    engine.say(chunk)
    engine.runAndWait()

engine.say("Do you want to translate the result? ")
engine.runAndWait()
while True:
    decision = input('Do you want to translate the result? ')
    if decision.lower() == 'yes':
        engine.say('select your language')
        engine.runAndWait()
        print("here is the list of languages: 'fr','es','ru', 'ja', 'de', 'ko', 'nl' ")
        target_language = input('select your language: ')
        engine.say('OK, here is the translated text')
        engine.runAndWait()
        translator = Translator()

        text_to_translate = result
        translated_text = translator.translate(
            text_to_translate, dest=target_language)

        print(translated_text.text)
        engine.say(translated_text.text)
        engine.runAndWait()
    else:
        engine.say('Have a nice day')
        engine.runAndWait()
    break
