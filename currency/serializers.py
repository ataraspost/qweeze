
from rest_framework import serializers

from .models import EURCurrency, RUBCurrency, USDCurrency


class EURCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = EURCurrency
        fields = ('quantity', 'value')


class RUBCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = RUBCurrency
        fields = ('quantity', 'value')


class USDCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = USDCurrency
        fields = ('quantity', 'value')

