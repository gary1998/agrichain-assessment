from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from decimal import Decimal


def index(request):
    return render(request, "index.html")


def checkout(request):
    return render(request, "checkout.html")


def get_products(request):
    products = Product.objects.all()
    data = [
        {
            "id": p.id,
            "image": p.image,
            "name": p.name,
            "unit_price": float(p.unit_price),
            "discount_qty": p.discount_qty,
            "discount_price": float(p.discount_price) if p.discount_price else None,
        }
        for p in products
    ]
    return JsonResponse({"products": data})


def add_to_cart_api(request):
    if request.method == "POST":
        import json

        body = json.loads(request.body)
        product_id = str(body.get("product_id"))
        cart = request.session.get("cart", {})
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session["cart"] = cart
        return JsonResponse({"success": True, "cart": cart})


def reduce_from_cart_api(request):
    if request.method == "POST":
        import json

        body = json.loads(request.body)
        product_id = str(body.get("product_id"))
        cart = request.session.get("cart", {})
        if product_id in cart:
            cart[product_id] -= 1
            if cart[product_id] <= 0:
                del cart[product_id]
            request.session["cart"] = cart
        return JsonResponse({"success": True, "cart": cart})


def remove_from_cart_api(request):
    if request.method == "POST":
        import json

        body = json.loads(request.body)
        product_id = str(body.get("product_id"))
        cart = request.session.get("cart", {})
        if product_id in cart:
            del cart[product_id]
            request.session["cart"] = cart
        return JsonResponse({"success": True, "cart": cart})


def get_cart_details(request):
    from .models import Product

    cart = request.session.get("cart", {})
    details = []
    total = 0

    for product_id, qty in cart.items():
        try:
            p = Product.objects.get(id=product_id)
            subtotal = 0
            if p.discount_qty and p.discount_price:
                q = qty // p.discount_qty
                r = qty % p.discount_qty
                subtotal = q * p.discount_price + r * p.unit_price
            else:
                subtotal = qty * p.unit_price

            details.append(
                {
                    "id": p.id,
                    "name": p.name,
                    "unit_price": float(p.unit_price),
                    "quantity": qty,
                    "discount_qty": p.discount_qty,
                    "discount_price": (
                        float(p.discount_price) if p.discount_price else None
                    ),
                    "subtotal": float(subtotal),
                }
            )

            total += float(subtotal)

        except Product.DoesNotExist:
            continue

    return JsonResponse({"cart": details, "total": total})
