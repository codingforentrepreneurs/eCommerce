from django.conf.urls import url

from products.views import UserProductHistoryView
from .views import (
        AccountHomeView, 
        AccountEmailActivateView,
        UserDetailUpdateView
        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    url(r'^email/resend-activation/$', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
]

# account/email/confirm/asdfads/ -> activation view