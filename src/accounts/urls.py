from django.conf.urls import url

from .views import (
        AccountHomeView, 
        )

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
]