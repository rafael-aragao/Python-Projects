import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import requests
import webbrowser
import random
from urllib.parse import quote

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.setProperty('rate', 170)
maquina.setProperty('volume', 1.0)

voices = maquina.getProperty('voices')

for voice in voices:
    if "brazil" in voice.name.lower():
        maquina.setProperty('voice', voice.id)

print("Ajustando microfone para o ruído da sala... aguarde.")

with sr.Microphone() as source:
    audio.adjust_for_ambient_noise(source, duration=1)


def falar(texto):
    texto = str(texto) 
    print(f"Alexandria: {texto}")

    try:
        maquina.say(texto)
        maquina.runAndWait()
    except Exception as e:
        print(f"Erro na fala: {e}")

def ouvirComando():
    comando = ""

    try:
        with sr.Microphone() as source:

            voz = audio.listen(source, phrase_time_limit=5)

            comando = audio.recognize_google(voz,language='pt-BR')

            comando = comando.lower()

            if "alexandria" in comando:

                comando = comando.replace("alexandria", "").strip()

                respostas_ativacao = ["Sim?","Pois não?","Estou ouvindo.","Oi!"]

                falar(random.choice(respostas_ativacao))

                return comando

    except sr.UnknownValueError:
        pass

    except Exception as e:
        print(f"Erro: {e}")

    return ""

def buscar_clima(cidade):

    cidade_codificada = quote(cidade)

    api_key = "0cc5b6faa55d0681bc9827b57a39ebeb"

    link = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={cidade_codificada}"
        f"&appid={api_key}"
        f"&lang=pt_br"
        f"&units=metric"
    )

    try:

        requisicao = requests.get(link)

        dados = requisicao.json()

        if dados['cod'] == 200:

            temp = dados['main']['temp']
            desc = dados['weather'][0]['description']

            return (
                f"Em {cidade}, faz "
                f"{temp:.1f} graus "
                f"com {desc}."
            )

    except:
        return "Não consegui checar o clima agora."

    return "Cidade não encontrada."


def executar_alexandria():

    comando = ouvirComando()

    if comando == "":
        return

    print(f"Comando recebido: {comando}")

    # -------------------------
    # HORAS
    # -------------------------
    if "horas" in comando or "horario" in comando: 

        hora = datetime.datetime.now().strftime("%H:%M")

        falar(f"Agora são {hora}")

    # -------------------------
    # WIKIPEDIA
    # -------------------------
    elif "pesquisar" in comando:

        procurar = comando.replace("pesquisar", "").strip()

        if procurar == "":
            falar("O que você quer pesquisar?")
            return

        falar(f"Buscando {procurar}")

        wikipedia.set_lang("pt")

        try:
            resultado = wikipedia.summary(procurar, sentences=1)
            falar(resultado)
        except Exception:
            falar("Não consegui encontrar esse assunto na Wikipédia.")

    # -------------------------
    # CLIMA
    # -------------------------
    elif 'tempo em' in comando or "clima em" in comando:

        cidade = comando.replace('tempo em', '').replace('clima em', '').strip()

        if cidade == "":
            falar("De qual cidade você quer saber o clima?")
            return

        resultado = buscar_clima(cidade)
        falar(resultado)

    # -------------------------
    # ABRIR GITHUB
    # -------------------------
    elif 'github' in comando:
        falar("Abrindo seu GitHub, bons códigos!")
        webbrowser.open("https://github.com/")
    # -------------------------
    # ABRIR YOUTUBE
    # -------------------------
    elif 'abrir youtube' in comando:
        falar("Abrindo YouTube, aproveite os vídeos!")
        webbrowser.open("https://www.youtube.com/")
    # -------------------------
    # ABRIR NOTÍCIAS
    # -------------------------
    elif 'notícias' in comando or 'noticias' in comando:
        falar("Abrindo as últimas notícias para você.")
        webbrowser.open("https://g1.globo.com/")

    # -------------------------
    # ANOTAÇÕES
    # -------------------------
    elif 'anote' in comando or 'anotar' in comando:

        nota = (comando.replace('anote', '').replace('anotar', '').strip())
        with open("notas.txt", "a", encoding="utf-8") as f:
            f.write(f"- {nota}\n")
        falar("Anotei no seu bloco de notas.")

    elif 'unity' in comando:
        falar("Abrindo o Unity")

        try:
            os.startfile("Unity.exe")
        except Exception:
            falar("Não consegui achar o Unity!")

    elif "toque" in comando or "tocar musica" in comando:
        musica = comando.replace("toque", "").replace("tocar musica", "").strip()
        falar(f"Tocando sua musica favorita {musica} no Youtube")
        pywhatkit.playonyt(musica)

    elif "google" in comando:
        pesquise = comando.replace("google", "").strip()
        falar(f"Pesquisando {pesquise}")
        pywhatkit.search(pesquise)              
    # -------------------------
    # SAIR
    # -------------------------
    elif "desligar" in comando or "sair" in comando:

        falar("Encerrando sistemas. Até logo!")
        exit()

falar("Alexandria online e pronta.")

while True:
    executar_alexandria()