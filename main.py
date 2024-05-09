import os
import requests
import json
from gtts import gTTS
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera a chave da API do ambiente
API_KEY = os.getenv('API_KEY')

# Define a URL da API
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

# Define o cabeçalho da solicitação
HEADERS = {
    'Content-Type': 'application/json'
}

# Define os dados da solicitação
DATA = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Tell me a joke"
                }
            ]
        }
    ]
}

def main():
    """Executa o programa."""
    try:
        chatbot_response = get_chatbot_response()
        print(chatbot_response)
        text_to_speech(chatbot_response)
        play_and_remove_audio()
    except Exception as e:
        print(f'Error: {e}')

def get_chatbot_response():
    """Faz uma solicitação para a API e retorna a resposta do chatbot."""
    response = requests.post(f'{API_URL}?key={API_KEY}', headers=HEADERS, data=json.dumps(DATA))
    response.raise_for_status()  # Lança uma exceção se a solicitação falhar
    return response.json()['candidates'][0]['content']['parts'][0]['text']

def text_to_speech(text):
    """Converte o texto em fala e salva o áudio em um arquivo."""
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")

def play_and_remove_audio():
    """Reproduz o arquivo de áudio e o remove."""
    os.system("afplay response.mp3")
    os.remove("response.mp3")

if __name__ == "__main__":
    main()