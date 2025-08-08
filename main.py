from flask import Flask
import threading
import time
import bybit_martingale_bot  # Import your bot logic

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Bybit Martingale Bot is Running on Fly.io"

def run_bot():
    """This function runs your bot in a loop forever."""
    while True:
        try:
            bybit_martingale_bot.start_bot()  # Replace with your bot's main function
        except Exception as e:
            print(f"Bot error: {e}")
        time.sleep(1)  # Avoid CPU overuse

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
