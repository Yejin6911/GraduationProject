from django.shortcuts import render
from django.contrib.auth.models import User

import os

path = str(os.getcwd()) + "/map/static/data/"
file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]

data = []
for file in file_list_csv:
    full_path = path + str(file)
    f = open(full_path, "r", encoding='utf-8')
    lines = f.readlines()
    l = []
    for line in lines:
        l.append(line.split(','))
    f.close()
    data += l[1:]


def main(request):
    return render(request, "map/main.html", {'data': data})


def cctv(request):
    return render(request, "map/cctv.html")
