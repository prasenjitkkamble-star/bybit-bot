# Bybit Martingale Trading Bot

A crypto bot that uses a Martingale strategy on Bybit with 90x leverage.

## Deployment on Render

1. Push this folder to GitHub.
2. Create a new **Web Service** on Render.
3. Set start command to:
   ```
   python main.py
   ```
4. Add your API keys in Render Environment Variables.
5. Deploy and connect TradingView Webhook to:
   ```
   https://your-app-name.onrender.com/webhook
   ```
