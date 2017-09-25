from django.shortcuts import render



def cart_home(request):
    return render(request, "carts/home.html", {})
