from django import template
register = template.Library()

@register.filter(name='product')
def product(value, arg):
    return value.filter(product=arg)