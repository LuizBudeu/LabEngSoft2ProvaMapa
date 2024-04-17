from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import HttpRequest
from datetime import datetime
from datetime import date
import requests

from django.shortcuts import render, redirect


def mapa(request: HttpRequest):
    ingressos = get_todos_ingressos()
    return render(request, 'mapa.html', {'ingressos': ingressos})


def get_todos_ingressos():
    ingressos = requests.get('http://localhost:8000/get_ingressos/')
    return ingressos.json()
