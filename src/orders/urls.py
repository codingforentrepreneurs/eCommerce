from django.conf.urls import url

from .views import (
        OrderListView, 
        OrderDetailView,
        VerifyOwnership
        )

urlpatterns = [
    url(r'^$', OrderListView.as_view(), name='list'),
    url(r'^endpoint/verify/ownership/$', VerifyOwnership.as_view(), name='verify-ownership'),
    url(r'^(?P<order_id>[0-9A-Za-z]+)/$', OrderDetailView.as_view(), name='detail'),
]