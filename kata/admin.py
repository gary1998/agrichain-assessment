from django.contrib import admin

from kata.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit_price",
        "discount_qty",
        "discount_price",
        "has_discount",
    )
    list_filter = ("discount_qty",)
    search_fields = ("name",)
    list_editable = ("unit_price", "discount_qty", "discount_price")

    def has_discount(self, obj):
        if obj.discount_qty * obj.unit_price > obj.discount_price:
            return True
        return False

    has_discount.short_description = "Discount Active"
