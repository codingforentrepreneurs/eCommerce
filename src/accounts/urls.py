from django.conf.urls import url

from .views import (
        AccountHomeView, 
        AccountEmailActivateView
        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    url(r'^email/resend-activation/$', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
]

# account/email/confirm/asdfads/ -> activation view