from django.db import models


class Product(models.Model):
    name = models.CharField(unique=True)
    image = models.URLField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False
    )
    discount_qty = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    discount_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def calculate_price(self, quantity):
        if self.discount_qty and self.discount_price:
            num_discounts = quantity // self.discount_qty
            remainder = quantity % self.discount_qty
            return num_discounts * self.discount_price + remainder * self.unit_price
        return quantity * self.unit_price
