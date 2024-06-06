from flask import Flask, request, Response
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv
from main import user_input
from io import BytesIO

load_dotenv()

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("API_KEY"))

app = Flask(__name__)
# Get Telegram Bot Token from environment variables
token = os.getenv("TELEGRAM_BOT_TOKEN")
print(token)

def generate_answer(question):
    answer = user_input(question)['output_text']
    return answer

def message_parser(message):
    try:
        chat_id = message['message']['chat']['id']
        if 'text' in message['message']:
            text = message['message']['text']
            print("Chat ID: ", chat_id)
            print("Text Message: ", text)
            return chat_id, text, 'text'
        elif 'voice' in message['message']:
            file_id = message['message']['voice']['file_id']
            print("Chat ID: ", chat_id)
            print("Voice Message file_id: ", file_id)
            return chat_id, file_id, 'voice'
        else:
            print(f"Unhandled message type received: {message}")
            return chat_id, None, None
    except KeyError as e:
        print(f"KeyError: {e} in message: {message}")
        return None, None, None

def send_message_telegram(chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, content, msg_type = message_parser(msg)
        
        if chat_id is None or content is None:
            return Response('Bad Request: Invalid message format', status=400)
        
        if msg_type == 'text':
            answer = generate_answer(content)
        elif msg_type == 'voice':
            answer = "Sorry, I couldn't understand the audio message."
        else:
            answer = "Unsupported message type received."
        
        send_message_telegram(chat_id, answer)
        print("BOT Answer: ", answer)
        return Response('ok', status=200)
    else:
        return "<h1>Something went wrong</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=5000)
