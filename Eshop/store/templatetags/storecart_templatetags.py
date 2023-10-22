from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, arg):
    """Removes all values of arg from the given string"""
    # Uses => {{ somevariable|cut:"0" }}
    return value.replace(arg, "")


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):  # Only one argument.
    """Converts a string into all lowercase"""
    keys = cart.keys()
    for id in keys:
        if id != 'null' and int(id) == product.id:
            return True

    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):  # Only one argument.
    """Converts a string into all lowercase"""
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)

    return 0


@register.filter(name='price_total')
def price_total(product, cart):  # Only one argument.
    """Converts a string into all lowercase"""
    price = 0
    price = product.price * cart_quantity(product, cart)
    return price


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):  # Only one argument.
    """Converts a string into all lowercase"""
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum


@register.filter(name='currency')
def currency(amount):  # Only one argument.
    """Converts a string into all lowercase"""
    return f"₹ {amount:.2f}"


@register.filter(name='total_price')
def total_price(price, qun):  # Only one argument.
    """Converts a string into all lowercase"""
    sum = price * qun
    return sum
