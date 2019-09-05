
from django.urls import path

from .views import CurrencyView, WithdrawView

urlpatterns = [
    path('deposit/', CurrencyView.as_view()),
    path('withdraw/', WithdrawView.as_view()),
]
