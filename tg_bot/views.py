from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from telebot import types as bot_types

from .bot import bot

# Create your views here.

def index(request):
    return HttpResponse("Hola! This this a telegram bot")


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        json_str = request.body.decode("UTF-8")
        update = bot_types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return JsonResponse({"status": "ok"})

    return HttpResponseBadRequest({
        "error": "Bad Method"
    })

