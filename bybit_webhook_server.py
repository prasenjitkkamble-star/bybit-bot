from flask import Flask, request, jsonify
from pybit.unified_trading import HTTP
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SYMBOL = "SOLUSDT"

session = HTTP(
    testnet=False,
    api_key=API_KEY,
    api_secret=API_SECRET,
)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True).lower()
    print(f"Webhook received: {data}")

    try:
        if "buy" in data:
            qty = float(data.split()[1])
            return place_order("Buy", qty)
        elif "sell" in data:
            qty = float(data.split()[1])
            return place_order("Sell", qty)
        elif "tp hit" in data or "sl hit" in data:
            return close_position()
        else:
            return "Unrecognized alert", 400
    except Exception as e:
        return f"Error: {str(e)}", 500

def place_order(side, qty):
    result = session.place_order(
        category="linear",
        symbol=SYMBOL,
        side=side,
        order_type="Market",
        qty=qty,
        time_in_force="GoodTillCancel"
    )
    return jsonify(result)

def close_position():
    pos_data = session.get_positions(category="linear", symbol=SYMBOL)
    pos = pos_data['result']['list'][0]
    size = float(pos['size'])
    side = "Sell" if pos['side'] == "Buy" else "Buy"

    if size > 0:
        result = session.place_order(
            category="linear",
            symbol=SYMBOL,
            side=side,
            order_type="Market",
            qty=size,
            time_in_force="GoodTillCancel",
            reduce_only=True
        )
        return jsonify(result)
    else:
        return "No position to close", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
