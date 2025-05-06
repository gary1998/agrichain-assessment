from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout/", views.checkout, name="checkout"),
    path("api/products/", views.get_products),
    path("api/add-to-cart/", views.add_to_cart_api),
    path("api/checkout/", views.get_cart_details),
    path("api/reduce-from-cart/", views.reduce_from_cart_api),
    path("api/remove-from-cart/", views.remove_from_cart_api),
]
