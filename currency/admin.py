from django.contrib import admin

from .models import EURCurrency, RUBCurrency, USDCurrency

admin.site.register(EURCurrency)
admin.site.register(RUBCurrency)
admin.site.register(USDCurrency)

