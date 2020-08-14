from django.shortcuts import render


f = open("/Users/jangbomin/dev/GraduationProject/map/static/data.csv","r", encoding='cp949')
lines = f.readlines()
l = []
for line in lines:
    l.append(line.split(','))
f.close()
data = l[1:]

def main(request):
    time = request.session.get_expiry_age()
    print(time)
    return render(request, "map/main.html", {'data':data})
