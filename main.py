from flask import Flask
import threading
import time
import os
import bybit_martingale_bot  # Import your bot logic

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Bybit Martingale Bot is Running on Fly.io (Live Mode)"

def run_bot():
    """Runs your bot continuously in the background."""
    while True:
        try:
            bybit_martingale_bot.start_bot()
        except Exception as e:
            print(f"Bot error: {e}")
        time.sleep(1)  # Avoid 100% CPU usage

if __name__ == "__main__":
    # Start the bot in a separate thread
    threading.Thread(target=run_bot, daemon=True).start()
    # Bind Flask to Fly.io PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
