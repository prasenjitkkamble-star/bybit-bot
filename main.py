from flask import Flask, request, jsonify
import os
from bybit_martingale_bot import run_martingale_bot

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    print(f"📩 Webhook data received: {data}")
    try:
        run_martingale_bot(signal=data.get("signal", "").lower())
        return jsonify({"status": "trade executed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "🚀 Bybit Martingale Bot is running"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
