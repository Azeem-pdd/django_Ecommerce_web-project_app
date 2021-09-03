from django import template

register = template.Library()

@register.filter(name='product_quantity')
def product_quantity(product,wishlist):
    keys = wishlist.keys()
    for key in keys:
        if int(key)==product.id:
            return wishlist.get(key)
        else: 
            return 0

