import os
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
import threading
import sounddevice as sd
import scipy.io.wavfile as wav
import google.generativeai as genai
import platform

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera as configurações do ambiente
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
fs = int(os.getenv("FS"))
duration = int(os.getenv("DURATION"))

# Mensagem de instrução para o sistema
system_instruction = "You are a tandem partner. Reply with simple sentences and avoid using slang or idioms. If you don't understand something, ask for clarification. In your reply, do NOT include any markdown formatting nor emojis, as your responses will be converted to speech. Begin the conversation by asking about which topic the user would like to practice or talk about. Use the same language as the user."

# Cria uma instância do Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    "gemini-1.5-pro-latest", system_instruction=system_instruction
)
chat = model.start_chat(history=[])


def main():
    chat_lang = app_start()
    if chat_lang.lower() in ("exit", "quit", "sair", "salir"):
        close_app()

    while True:  # Loop para a interação do chat
        user_interaction = process_voice()
        clear_terminal()

        try:
            user_text = speech_to_text(user_interaction, chat_lang)
            chatbot_response = get_chatbot_response(user_text)
            text_to_speech(chatbot_response, chat_lang)
            play_and_remove_audio()
        except Exception as e:
            print(f"Error: {e}")

        print_chat_history()


def app_start():
    '''Exibe a mensagem de boas-vindas e solicita ao usuário que escolha um idioma para conversar.'''

    print("\n*** Bem-vindo ao tandembot! ***\n")
    print("Escolha um idioma para conversar e pratique suas habilidades: ")
    print("1 - Português")
    print("2 - Inglês")
    print("3 - Espanhol\n")

    language = {"1": "pt-BR", "2": "en-US", "3": "es-ES"}
    chosen_lang = "0"
    
    while chosen_lang not in ["1", "2", "3", "sair", "quit", "exit"]:
        chosen_lang = input("Digite o número correspondente ao idioma que quer praticar ou 'sair': \n")
        chat_lang = language.get(chosen_lang)

    return chat_lang


def close_app():
    '''Encerra a aplicação.'''
    print("\nVolte logo para praticar mais!")
    exit()


def print_chat_history():
    # Exibe o histórico da conversa a cada iteração
    print("------------------------")
    for message in chat.history:
        print(f"{message.role}: {message.parts[0].text}")
    print("------------------------")


def process_voice():
    '''Gerencia a thread de gravação de voz retorna o caminho para o arquivo wav.'''
    # Inicia a gravação de áudio em uma thread separada
    thread = threading.Thread(target=record_audio)
    thread.start()

    # Espera a entrada do usuário para terminar a gravação
    action = input()
    if action.lower() in ("exit", "quit", "sair"):
        close_app()

    # Para a gravação de áudio
    sd.stop()

    # Salva o arquivo de áudio
    prompt = "prompt.wav"
    wav.write(prompt, fs, audio)
    return prompt


def record_audio():
    """Grava áudio do microfone e salva em um arquivo."""
    print("\nNão seja tímido(a)! Diga algo e pressione Enter.")
    print("Quando não quiser mais praticar, digite 'exit' ou 'sair'.")
    global audio
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype="int16")


def speech_to_text(audio_file_path, language="en-US"):
    """Converte fala em texto usando a biblioteca SpeechRecognition."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=language)
        return text


def get_chatbot_response(user_interaction="Hello"):
    '''Obtém a resposta do chatbot para a interação do usuário.'''
    # Faz uma solicitação para a API e retorna a resposta do chatbot.
    response = chat.send_message(user_interaction, stream=True)
    response.resolve()
    return response.text


def text_to_speech(text, lang="en"):
    """Converte o texto em fala e salva o áudio em um arquivo."""
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")


def play_and_remove_audio():
    """Reproduz o arquivo de áudio e o remove."""
    if platform.system() == "Windows":
        os.system("start response.mp3")
    elif platform.system == "Linux":
        os.system("mpg123 response.mp3")
    else: # MacOS
        os.system("afplay response.mp3")
    
    os.remove("response.mp3")
    os.remove("prompt.wav")


def clear_terminal():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
