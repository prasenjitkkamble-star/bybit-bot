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


## 🚀 Free 24/7 Deployment on Replit

You can run this bot for free 24/7 using **Replit** + **UptimeRobot**:

1. **Import Repo into Replit**
   - Go to [Replit](https://replit.com)
   - Click **Create Repl → Import from GitHub**
   - Select this repository

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Bybit API Keys**
   - Go to **Tools → Secrets (Environment Variables)** in Replit
   - Add:
     ```
     BYBIT_API_KEY = your_api_key
     BYBIT_API_SECRET = your_api_secret
     ```

4. **Run the Bot**
   - Click **Run** in Replit
   - Copy the generated web URL (e.g., `https://your-repl-name.username.repl.co`)

5. **Keep Alive with UptimeRobot**
   - Go to [UptimeRobot](https://uptimerobot.com)
   - Add a new **HTTP(s) monitor**
   - Paste your Replit URL and set check interval to **5 minutes**
   - Save → bot now stays online 24/7

The bot will:
- Keep running your Martingale strategy in the background
- Accept webhook trades from TradingView
- Stay awake with free uptime pings



## 🔑 Setting API Keys in Replit

To keep your Bybit API keys safe, **never hardcode them** into your bot.  
Instead, store them in Replit's built-in **Secrets** system:

1. Open your Replit project.
2. On the left sidebar, click **Tools → Secrets (Environment Variables)**.
3. Add the following keys:
   ```
   BYBIT_API_KEY = your_api_key_here
   BYBIT_API_SECRET = your_api_secret_here
   ```
4. Your bot will now automatically load these keys securely at runtime.

**Note:** The updated `bybit_martingale_bot.py` already uses these environment variables, so you don't need to modify your code.
