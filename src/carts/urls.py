from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update, 
        checkout_home
        )

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
]

