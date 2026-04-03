from django.contrib import admin

from .models import BillingProfile, Card, Charge

admin.site.register(BillingProfile)

admin.site.register(Card)
#Change
admin.site.register(Charge)
