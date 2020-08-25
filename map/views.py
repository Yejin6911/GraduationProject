from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import os

from django.urls import reverse

from account.models import CustomUser

path = str(os.getcwd()) + "/map/static/data/"
file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]

# data = []
# for file in file_list_csv:
#     full_path = path + str(file)
#     f = open(full_path, "r", encoding='cp949')
#     lines = f.readlines()
#     l = []
#     for line in lines:
#         l.append(line.split(','))
#     f.close()
#     data += l[1:]

def main(request):
    if not request.user.is_authenticated:
        return redirect(reverse("account:login"))
    else:
        data = []
        location = CustomUser.objects.get(username=request.user.username).location
        full_path = path + str(location)+'.csv'
        f = open(full_path, "r", encoding='cp949')
        lines = f.readlines()
        l = []
        for line in lines:
            l.append(line.split(','))
        f.close()
        data += l[1:]
        return render(request, "map/main.html", {'data': data})


def cctv(request):
    return render(request, "map/cctv.html")
