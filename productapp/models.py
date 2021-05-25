from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    picture = models.ImageField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
        return self.quantity

