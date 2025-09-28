from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)


@register.filter(name='multiply')
def multiplyh(number , number1):
    return number * number1


