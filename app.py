import os
import threading
from flask import Flask
import telebot

app = Flask(name)

# Pega os tokens do Render
TOKENS = {
    "goleador": os.getenv("TOKEN_GOLEADOR"),
    "handicap": os.getenv("TOKEN_HANDICAP"),
    "btts": os.getenv("TOKEN_BTTS"),
    "escanteios": os.getenv("TOKEN_ESCANTEIOS"),
    "exato": os.getenv("TOKEN_EXATO"),
}

def criar_bot(nome, token):
    if not token:
        print(f"❌ {nome} - SEM TOKEN")
        return
    try:
        bot = telebot.TeleBot(token)
        print(f"✅ {nome} - Token OK")

        @bot.message_handler(commands=['start'])
        def start(message):
            bot.reply_to(message, f"🤖 Bot {nome} online!\n\nComandos:\n/start - Iniciar\n/jogos - Ver jogos")

        @bot.message_handler(commands=['jogos'])
        def jogos(message):
            bot.reply_to(message, f"⚽ Jogos do {nome} em breve...")

        bot.infinity_polling()
    except Exception as e:
        print(f"❌ Erro no {nome}: {e}")

@app.route('/')
def home():
    return "🤖 Esportiva Pro - 5 Robos Online!"

# Inicia os bots em threads separadas
for nome, token in TOKENS.items():
    t = threading.Thread(target=criar_bot, args=(nome, token))
    t.daemon = True
    t.start()

if name == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
