from django.db import models
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

# Create your models here.

class registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    


class category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="upload/")
    status = models.BooleanField(help_text="0-show,1-hide")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class product(models.Model):
    cat = models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to="upload/")
    details = models.CharField(max_length=60)
    status = models.BooleanField(help_text="0-show,1-hide")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    prod = models.ManyToManyField(product,through="Cartitem")
    # product = models.CharField(max_length=100)
    user = models.ForeignKey(registration,on_delete=models.CASCADE)


class Cartitem(models.Model):
    prods = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # def subtotal(self):
    #     return self.product.price * self.quantity


class Order(models.Model):
    name = models.CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )


