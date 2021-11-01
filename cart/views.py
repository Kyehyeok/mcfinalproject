from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

# Create your views here.
from articleapp.models import Ingredient, Mealkit
from cart.models import Cart, CartItem


def _cart_id(request):
    cart = request.seesion.session_key
    if not cart:
        cart = request.seesion.create()

    return cart

def add_ingre_cart(request, product_id):
    product_ingre = Ingredient.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except:
        cart = Cart.objects.create(
            cart_id= _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product_ingre, cart= cart)
        cart_item.quantity +=1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(
            product= product_ingre,
            quantity = 1,
            cart= cart
        )
        cart_item.save()

    return redirect('cart:cart_detail')

def add_mealkit_cart(request, product_id):
    product_mealkit = Mealkit.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except:
        cart = Cart.objects.create(
            cart_id= _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product_mealkit, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(
            product=product_mealkit,
            quantity=1,
            cart=cart
        )
        cart_item.save()

    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html',dict(cart_items= cart_items, total=total, counter= counter))
