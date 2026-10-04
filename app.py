import os
import telebot
from flask import Flask
import threading
import time

app = Flask(name)

TOKENS = {
    "goleador": os.getenv("TOKEN_GOLEADOR"),
    "handicap": os.getenv("TOKEN_HANDICAP"),
    "btts": os.getenv("TOKEN_BTTS"),
    "escanteios": os.getenv("TOKEN_ESCANTEIOS"),
    "exato": os.getenv("TOKEN_EXATO")
}

print("=== FIRE ESPORTIVA PRO ===")

for nome, token in TOKENS.items():
    if token and len(token) > 20:
        print(f"✅ {nome} - Token OK")
        bot = telebot.TeleBot(token)

        @bot.message_handler(commands=['start'])
        def start_cmd(message):
            bot.reply_to(message, f"🔥 FIRE ESPORTIVA PRO - {nome.upper()}!\n\n✅ Bot Online em Luanda!\n\nManda /jogos")

        @bot.message_handler(commands=['jogos'])
        def jogos_cmd(message):
            bot.reply_to(message, "⚽ Jogos de hoje em análise...")

        def run_bot(b, n):
            while True:
                try:
                    print(f">>> {n} POLLING LIGADO - Aguardando /start")
                    b.infinity_polling(skip_pending=True)
                except Exception as e:
                    print(f"Erro {n}: {e}")
                    time.sleep(5)

        threading.Thread(target=run_bot, args=(bot, nome), daemon=True).start()
    else:
        print(f"❌ {nome} - SEM TOKEN no Render")

@app.route('/')
def home():
    return "🔥 FIRE ESPORTIVA PRO - 5 Robos Online!"

if name == 'main':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
