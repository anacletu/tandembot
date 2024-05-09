import os
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
import threading
import sounddevice as sd
import scipy.io.wavfile as wav
import google.generativeai as genai

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera as configurações do ambiente
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
fs = int(os.getenv("FS"))
duration = int(os.getenv("DURATION"))

# Cria uma instância do Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def main():
    # Lógica de interação com o usuário
    print("\n*** Bem-vindo ao Chatbot! ***\n")
    print("Escolha um idioma para conversar: ")
    print("1 - Português")
    print("2 - Inglês")
    print("3 - Espanhol\n")

    language = {'1': 'pt-BR', '2': 'en-US', '3': 'es-ES', '4': 'pl-PL'}
    chosen_lang = "0"

    while chosen_lang not in ["1", "2", "3", "4"]:
        chosen_lang = input("Digite o número correspondente ao idioma: \n")
        chat_lang = language[chosen_lang]
    
    # Inicia a gravação de áudio em uma thread separada
    thread = threading.Thread(target=record_audio)
    thread.start()

    # Espera a entrada do usuário para terminar a gravação
    input()

    # Para a gravação de áudio
    sd.stop()

    # Salva o arquivo de áudio
    filename = "audio.wav"
    wav.write(filename, fs, audio)
    
    try:
        user_text = speech_to_text(filename, chat_lang)
        chatbot_response = get_chatbot_response(user_text)
        print(chatbot_response)
        text_to_speech(chatbot_response, chat_lang)
        play_and_remove_audio()
    except Exception as e:
        print(f"Error: {e}")


def record_audio():
    """Grava áudio do microfone e salva em um arquivo."""
    print("\nNão seja tímido(a)! Fala algo e pressione Enter.")
    global audio
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype="int16")


def speech_to_text(audio_file_path, language='en-US'):
    """Converte fala em texto usando a biblioteca SpeechRecognition."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=language)
        return text


def get_chatbot_response(user_interaction="Hello"):
    # Faz uma solicitação para a API e retorna a resposta do chatbot.
    response = chat.send_message(user_interaction)
    return response.text
    #to_markdown(response.text)


def text_to_speech(text, lang='en'):
    """Converte o texto em fala e salva o áudio em um arquivo."""
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")


def play_and_remove_audio():
    """Reproduz o arquivo de áudio e o remove."""
    os.system("afplay response.mp3")
    os.remove("response.mp3")
    os.remove("audio.wav")


if __name__ == "__main__":
    main()
