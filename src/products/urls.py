from django.conf.urls import url

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]

