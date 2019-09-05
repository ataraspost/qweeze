
def sum_digits(choices, amount):
    dict_digits = dict()
    for item in choices:
        if amount >= item.value:
            quantity = int(amount / item.value)
            dict_digits[item.value] = min(quantity, item.quantity)
            amount = amount - item.value * dict_digits[item.value]
            item.quantity -= quantity
            item.save()
    if amount:
        return None
    return dict_digits

