from django.shortcuts import render


# Create your views here.
def main(request):
    time = request.session.get_expiry_age()
    print(time)
    return render(request, "map/main.html")