# Telegram Gemini Auto-Posting Bot

## Description
This is a Telegram bot that automatically posts AI-generated content to a Telegram channel every day. The content is generated using **Google Gemini API** and can include topics like **finance, motivation, and health**.

The bot is fully deployable on **Railway** or other cloud hosting platforms and can run **24/7**.

---

## Files in This Project
- `main.py` → Bot script
- `requirements.txt` → Python dependencies
- `Procfile` → For Railway deployment
- `README.md` → Project description

---

## Usage
- The bot automatically posts at the scheduled time (`09:00` by default)
- Change the time in `main.py` if needed:

```python
schedule.every().day.at("09:00").do(post_to_telegram)