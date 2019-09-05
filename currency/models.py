from django.db import models


RUB_CHOICES = (
    (5,'5 RUB'),
    (10, '10 RUB'),
    (50, '50 RUB'),
    (100, '100 RUB'),
    (200, '200 RUB'),
    (500, '500 RUB'),
    (1000, '1000 RUB'),
    (2000, '2000 RUB'),
    (5000, '5000 RUB'),
)
EUR_CHOICES = (
    (5, '5 EUR'),
    (10, '10 EUR'),
    (20, '20 EUR'),
    (50, '50 EUR'),
    (100, '100 EUR'),
    (200, '200 EUR'),
    (500, '500 EUR'),
)
USD_CHOICES = (
    (1, '1 USD'),
    (2, '2 USD'),
    (5, '5 USD'),
    (10, '10 USD'),
    (20, '20 USD'),
    (50, '50 USD'),
    (100, '100 USD'),
)


class MixinDate(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        abstract = True


class CurrencyModel(models.Model):
    quantity = models.SmallIntegerField()
    value = None

    class Meta:
        abstract = True


class RUBCurrency(MixinDate, CurrencyModel):
    value = models.SmallIntegerField(choices=RUB_CHOICES, unique=True)


class EURCurrency(MixinDate, CurrencyModel):
    value = models.SmallIntegerField(choices=EUR_CHOICES, unique=True)


class USDCurrency(MixinDate, CurrencyModel):
    value = models.SmallIntegerField(choices=USD_CHOICES, unique=True)

