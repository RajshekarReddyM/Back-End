import pyttsx3

text_speech = pyttsx3.init()

text = 'Go with the flow'
text_speech.say(text)
text_speech.runAndWait()
