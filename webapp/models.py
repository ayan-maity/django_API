from django.db import models


# Create your models here.

class itemcatalog(models.Model):
    id = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.itemname


class orderhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=100)
    item_id = models.IntegerField(null=False)
    username = models.CharField(max_length=100)
    datetime = models.DateTimeField(null=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.order_id, self.item_id
