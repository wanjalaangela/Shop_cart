from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=28)


class Tag(models.Model):
    name = models.CharField(max_length=28)


class Product(models.Model):
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    image = models.URLField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.name} || price {self.price}'


class Subscription(models.Model):
    name = models.CharField(max_length=50)


class Customer(models.Model):
    subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)


from django.contrib.auth.models import User

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

