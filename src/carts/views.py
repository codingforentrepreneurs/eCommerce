from django.shortcuts import render



def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None: # and isinstance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print('Cart ID exists')
    return render(request, "carts/home.html", {})
