import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '6307849521:AAHaczJqO5UZVj6LtADN-LettUCwpOluq_k'

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, json=data)

@app.route('/', methods=['POST'])
def receive_message():
    data = request.json
    message = data['message']
    chat_id = message['chat']['id']
    text = message['text']
    if '/hello' in text:
        send_message(chat_id, 'Hello! How can I assist you?')
    elif '/bye' in text:
        send_message(chat_id, 'Goodbye! Have a nice day!')
    else:
        send_message(chat_id, 'Sorry, I didn\'t understand that command.')
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
