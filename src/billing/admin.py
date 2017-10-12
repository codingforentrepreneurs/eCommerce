from django.contrib import admin

from .models import BillingProfile, Card, Charge

admin.site.register(BillingProfile)

admin.site.register(Card)

admin.site.register(Charge)