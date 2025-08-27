# from django.urls import path
# from .views import list_products,product_detail


# urlpatterns = [
#     path('products/', list_products, name='list_products'),
#     path('product/<int:id>/', product_detail,name="product_details")

# ]

from django.urls import path
from .views import list_products, product_detail, add_to_cart, cart_detail, remove_from_cart,Create_product,product_upload
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('product/<int:id>/', product_detail, name="product_details"),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('products/create/',Create_product, name="create_product"),
    path("product/upload/", product_upload, name="product_upload"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]



