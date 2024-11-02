from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse("Hola! This this a whatsapp bot")


@csrf_exempt
def webhook(request):
    return HttpResponse("Hola! This this a the whatsapp webhook")