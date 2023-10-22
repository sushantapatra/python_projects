from django.db import models
from .customer import Customer
from .product import Products
import datetime


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    payment_date = models.DateTimeField(default=datetime.datetime.now())
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def getOrdersByCustomer(customer):
        if customer:
            return Order.objects.filter(customer=customer.id)

    def __str__(self):
        return f"{self.create_date} -{self.product.name} - {self.price}"
