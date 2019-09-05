
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps

from .serializers import RUBCurrencySerializer, EURCurrencySerializer, USDCurrencySerializer


class CurrencyView(APIView):

    def post(self, request):
        dict_post = self.get_dict_post(request)
        if dict_post is None:
            return Response(data={"success": False})
        currency = dict_post.pop('currency').upper()
        model_name = currency.upper() + 'Currency'
        model = apps.get_model('currency', model_name)
        class_serializer = self.get_class_serializer(currency)
        instance = self.get_instance(model, dict_post)
        if instance is None:
            serializer = class_serializer(data=dict_post)
            if serializer.is_valid():
                serializer.create(dict_post)
            else:
                return Response(data={"success": False})
        else:
            instance.quantity += int(dict_post['quantity'])
            instance.save()
        return Response(data={"success": True})

    def get_dict_post(self, request):
        dict_post = request.POST.dict()
        if 'currency' in dict_post and 'value' in dict_post and 'quantity' in dict_post:
            return dict_post
        return None

    def get_instance(self, model, dict_post):
        try:
            return model.objects.get(value=dict_post['value'])
        except model.DoesNotExist:
            return None

    def get_class_serializer(self, currency):
        if currency == 'RUB':
            return RUBCurrencySerializer
        elif currency == 'EUR':
            return EURCurrencySerializer
        elif currency == 'USD':
            return USDCurrencySerializer

