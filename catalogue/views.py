from django.shortcuts import render
from .models import Product

# Create your views here.
def list_products(request):
    products = Product.objects.all()
    return render(request,"catalogue/products.html", {"products":products})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,"catalogue/products_details.html",{"product":product})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect("cart_detail")

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "catalogue/cart_detail.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect("cart_detail")

