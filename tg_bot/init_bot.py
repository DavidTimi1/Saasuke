from .bot import bot
from .settings import hook_url, hook_secret


bot.remove_webhook()
bot.set_webhook(hook_url, secret_token=hook_secret)
# bot.infinity_polling()