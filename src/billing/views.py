from django.shortcuts import render



import stripe
stripe.api_key = "sk_test_cu1lQmcg1OLffhLvYrSCp5XE"


STRIPE_PUB_KEY = 'pk_test_PrV61avxnHaWIYZEeiYTTVMZ'


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key": STRIPE_PUB_KEY})