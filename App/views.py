from django.shortcuts import render
from . import models
import random


def home(request):
    return render(request, 'Home.html')


def data(request):
    context = {}
    if request.method == 'GET':
        pkr = random.randint(10, 100)
        usd = random.randint(180, 250)
        kwd = random.randint(800, 900)
        eru = random.randint(200, 300)
        pond = random.randint(200, 400)
        context = {'pkr': pkr, 'usd': usd, 'kwd': kwd, 'eru': eru, 'pond': pond}

    return render(request, 'Data.html', context)
