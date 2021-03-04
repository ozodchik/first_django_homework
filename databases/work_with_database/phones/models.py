from django.db import models


class Phone(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225)
    image = models.URLField(max_length=1000)
    price = models.IntegerField()
    release = models.DateField(auto_now_add=True)
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=225, default=None)
