from django.shortcuts import render
from django.contrib.auth.models import User


f = open("/Users/jangbomin/dev/GraduationProject/map/static/data.csv","r", encoding='cp949')
lines = f.readlines()
l = []
for line in lines:
    l.append(line.split(','))
f.close()
data = l[1:]

def main(request):
    if not request.user.is_authenticated:
        return render()
    print(time)
    return render(request, "map/main.html", {'data':data})
