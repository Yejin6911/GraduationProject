from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def main(request):
    if not request.user.is_authenticated:
        return render()
    print(time)
    return render(request, "map/main.html")
