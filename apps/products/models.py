from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    price = models.FloatField(_("Price"))

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'[{self.title}:{self.price}]'