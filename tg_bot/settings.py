import os

HOST = os.environ.get("host")

bot_token = os.environ.get("tg_bot_token")
hook_secret = os.environ.get("tg_webhook_secret")
hook_url = HOST + "/tg_bot/webhook"

gemini_api = os.environ.get("gemini_api")

landing_page = "https://davidtimi.pythonanywhere.com/botspage"
mini_app = "t.me/Beetcoin_Bbot/lfgtelegram"