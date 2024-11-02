from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index():
    return HttpResponse("This is a saikyou feedback route")


@csrf_exempt
def feedback(request, app_name):
    return HttpResponse(f"You wanna submit a feedback for {app_name}? Choto matte!!")
