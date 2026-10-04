from flask import Flask
import threading, os
import requests
import time
from datetime import datetime

app = Flask(name)

@app.route('/')
def home():
    return "Esportiva Pro - 5 Robos Online"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask, daemon=True).start()

TOKENS = {
    "goleador": "8290316435:AAFLp_M1PatmJDnXuivcaHCF7lzWw90cIvo",
    "handicap": "8320545096:AAGNzohuBxe0BXBNFw7XBcLxBS_2emuN628",
    "btts": "8885934358:AAGjGVmtvDDm05-eSysJa2Nrj1nDAtcOvIY",
    "escanteios": "8699971350:AAGIL5sQE3AyHO1-sF9anwn2Mv5rXsolGjI",
    "exato": "8935155320:AAHsdQJkOMQ2KlEo0rQY3NAFUKSFTvLAGew"
}

print("FIRE ESPORTIVA PRO - 5 ROBOS LIGADOS")

while True:
    agora = datetime.now().strftime('%H:%M:%S')
    print(f"[{agora}] Sistema online - Luanda")
    time.sleep(60)
