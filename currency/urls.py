
from django.urls import path

from .views import CurrencyView

urlpatterns = [
    path('deposit/', CurrencyView.as_view()),
]
