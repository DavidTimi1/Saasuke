from django.shortcuts import render
from django.http import HttpResponse

from .settings import *


# Create your views here.
def index(request):
    return HttpResponse(f"""
                        <h1> Welcome to Saasuke </h1>
                        <p>
                            <small> A saas server built by </small>
                            <a href="{DEV_GITHUB}" target="_blank"> TimiDev </a>
                        </p>
                        """)