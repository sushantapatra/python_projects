from django import template
import math
register = template.Library()

"""
simple_tag => pass multiple argument
filter => pass one or two argument only.
"""

@register.simple_tag
def calculate_selprice_tag(price, discount):
    if discount is None or discount is 0:
        return price

    selprice = price
    selprice = price - (price * discount / 100)
    return math.floor(selprice)

@register.filter
def rupee(price):
    return f'₹{price}'

