from django.shortcuts import render
from django.contrib.auth.models import User

import os

path = str(os.getcwd()) + "\map\static\data.csv"
f = open(path, "r", encoding='cp949')
lines = f.readlines()
l = []
for line in lines:
    l.append(line.split(','))
f.close()
data = l[1:]


def main(request):
    return render(request, "map/main.html", {'data': data})


def cctv(request):
    return render(request, "map/cctv.html")
