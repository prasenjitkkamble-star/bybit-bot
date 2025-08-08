import os

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

def start_bot():
    if not API_KEY or not API_SECRET:
        print("❌ API keys not set. Please set BYBIT_API_KEY and BYBIT_API_SECRET in Fly.io secrets.")
        return
    print("✅ Bot loop running... (Here your live Martingale logic will execute)")
