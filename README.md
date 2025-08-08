# Bybit Martingale Bot - Fly.io Ready

## Deployment Steps
1. Push these files to a GitHub repo.
2. In Fly.io dashboard, create a new app and link the repo.
3. Set your API keys:
   flyctl secrets set BYBIT_API_KEY=your_key BYBIT_API_SECRET=your_secret
4. Deploy:
   flyctl deploy

Bot will run 24/7 and also serve a web page.
