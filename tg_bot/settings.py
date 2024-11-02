import os

HOST = os.environ.get("host")

bot_token = os.environ.get("tg-bot-token")
hook_secret = os.environ.get("tg-webhook-secret")
hook_url = HOST + "/tg-bot/webhook"

gemini_api = os.environ.get("gemini-api")

landing_page = "https://davidtimi.pythonanywhere.com/botspage"
mini_app = "t.me/Beetcoin_Bbot/lfgtelegram"