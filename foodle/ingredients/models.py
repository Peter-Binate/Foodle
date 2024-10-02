from django.db import models
from ingredients import values as ingredient_values

# Create your models here.
class Ingredient(models.Model):
    name = models.fields.CharField(max_length=30)
    price = models.fields.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    upload = models.ImageField(
        upload_to ='uploads/',
        blank=True, 
        null=True
    )
    shop = models.fields.IntegerField(
        "Nom du magasin",
        choices=ingredient_values.SHOP_NAME,
        default=0
    )

    def __str__(self):
        return f'{self.name}'