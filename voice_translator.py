import googletrans
import gtts
import playsound
import speech_recognition
recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language="fr")
    print(text)
#print (googletrans.LANGUAGES)
translator=googletrans.Translator()
translation=translator.translate(text,dest="hi")
print(translation.text)
converted_audio=gtts.gTTS(translation.text,lang="fr")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
