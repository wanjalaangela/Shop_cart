from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
from .forms import ProductForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def list_products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)  
    
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    return render(request, "catalogue/products.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "catalogue/products_details.html", {"product": product})




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


def Create_product(request):
    if request.method == "POST":
           form = ProductForm(request.POST)
           if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "catalogue/create_product.html", {"form":form})
# request.form is a dictionary



@login_required
def product_upload(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "catalogue/product_upload.html", {"form": form})
