!pip install google-generativeai schedule requests

import google.generativeai as genai
import requests
import schedule
import time

# ---- CONFIG ----
# Using your existing tokens (unsafe if shared publicly)
TELEGRAM_TOKEN = "8411334329:AAGEH8ir7HhDTZ1YQF0FFGZgPPxDEgbTTUA"
CHANNEL_ID = "@Satish064_bot"   # Remove double @@
GEMINI_API_KEY = "AIzaSyAUUix41ECUpCnWddK4tv-t6e-gUeLeT5k"

# ---- SETUP GEMINI ----
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# ---- GENERATE AI POST ----
def generate_post():
    prompt = "Write a short, engaging Telegram post about personal finance, motivation, or health. Add 2 hashtags."
    response = model.generate_content(prompt)
    return response.text

# ---- SEND TO TELEGRAM ----
def post_to_telegram():
    message = generate_post()
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHANNEL_ID, "text": message}
    requests.post(url, data=data)
    print("✅ Posted:", message)

# ---- SCHEDULE DAILY ----
schedule.every().day.at("09:00").do(post_to_telegram)  # Change time if needed

print("🤖 Bot started... Waiting for schedule...")

while True:
    schedule.run_pending()
    time.sleep(60)