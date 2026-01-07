import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale alguma coisa...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language="pt-BR")
    print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não entendi o que você disse.")
except sr.RequestError:
    print("Erro ao conectar com o serviço de reconhecimento.")
