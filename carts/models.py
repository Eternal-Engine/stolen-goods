from django.db import models
from product.models import Product


class Cart(models.Model):

    cart_id = models.CharField(max_length=500, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):

        return self.cart_id


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    is_active = models.BooleanField(default=True)

    class Meta:
        
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def sub_total(self):

        return self.product.price * self.quantity

    def __unicode__(self):

        return self.product