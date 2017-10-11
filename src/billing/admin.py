from django.contrib import admin

from .models import BillingProfile, Card

admin.site.register(BillingProfile)

admin.site.register(Card)