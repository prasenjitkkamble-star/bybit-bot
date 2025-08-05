import os
import time
import hmac
import hashlib
import requests
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

BASE_URL = "https://api.bybit.com"
SYMBOL = "SOLUSDT"
LEVERAGE = 90
INITIAL_QTY = 0.2
TP_PROFIT = 2
TP_RESET = 1
position = None
entry_price = None
current_qty = INITIAL_QTY

def send_telegram_alert(message):
    try:
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                     params={"chat_id": CHAT_ID, "text": message})
    except Exception as e:
        print(f"Telegram error: {e}")

def get_server_time():
    res = requests.get(BASE_URL + "/v5/market/time")
    return res.json()["time"]

def sign(params, secret):
    ordered = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
    return hmac.new(secret.encode(), ordered.encode(), hashlib.sha256).hexdigest()

def place_order(side, qty):
    global entry_price, position
    timestamp = str(get_server_time())
    endpoint = "/v5/order/create"
    url = BASE_URL + endpoint

    params = {
        "apiKey": API_KEY,
        "symbol": SYMBOL,
        "side": side,
        "orderType": "Market",
        "qty": str(qty),
        "timeInForce": "IOC",
        "timestamp": timestamp,
    }

    params["sign"] = sign(params, API_SECRET)
    res = requests.post(url, json=params)
    data = res.json()
    if data["retCode"] == 0:
        position = side
        entry_price = float(data["result"]["orderPrice"]) if "orderPrice" in data["result"] else None
        send_telegram_alert(f"📈 {side} {qty} {SYMBOL}")
    else:
        print("Order failed:", data)

def close_position():
    global position, current_qty
    opposite = "Sell" if position == "Buy" else "Buy"
    place_order(opposite, current_qty)
    send_telegram_alert("✅ Profit booked. Resetting...")
    position = None
    current_qty = INITIAL_QTY

def double_and_reverse():
    global current_qty
    current_qty *= 2
    close_position()
    new_side = "Sell" if position == "Buy" else "Buy"
    place_order(new_side, current_qty)

async def listen_pnl():
    ws_url = "wss://stream.bybit.com/v5/public/linear"
    async with websockets.connect(ws_url) as ws:
        await ws.send('{"op": "subscribe", "args": ["tickers.SOLUSDT"]}')
        while True:
            msg = await ws.recv()
            print(msg)

def main():
    place_order("Buy", INITIAL_QTY)
    send_telegram_alert("🚀 Bot started!")

if __name__ == "__main__":
    main()
