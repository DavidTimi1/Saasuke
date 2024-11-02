import json


from google.auth.transport import requests
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from google.oauth2 import id_token
from django.views.decorators.csrf import csrf_exempt

from .settings import GOOGLE_OAUTH2_ID

@login_required
def home(request):
    return render(request, 'home.html')


def index(request):
    return HttpResponse("""Hola, this is the main page for auth requests.
                        Where to from here?""")


def login(request):
    client_id = GOOGLE_OAUTH2_ID
    return render(request, 'login.html', {"client_id": client_id})


def logout(request):
    auth_logout(request)
    return redirect('/')


@csrf_exempt
def google_signin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("token")
        
        try:
            # Verify the token with Google's OAuth2 service
            id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_OAUTH2_ID)

            # Retrieve user info from the token
            google_user_id = id_info["sub"]
            email = id_info.get("email")
            first_name = id_info.get("given_name", "")
            last_name = id_info.get("family_name", "")

            # Check if the user already exists
            defaults={
                'username': email,
                'first_name': first_name,
                'last_name': last_name,
            }
            user, created = User.objects.get_or_create(email=email, defaults=defaults)

            # Log the user in
            login(request, user)
            
            return JsonResponse({"success": True, "message": "User signed in successfully", "data": defaults})
        
        except ValueError:
            # Invalid token
            return JsonResponse({"success": False, "message": "Invalid token"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)

