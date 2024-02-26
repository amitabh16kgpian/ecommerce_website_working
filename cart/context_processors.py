from .cart import Cart

def cart(request):
    # return the default data from the cart
    return {'cart': Cart(request)}