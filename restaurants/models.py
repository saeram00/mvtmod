from django.db import models

# Create your models here.
class Restaurant(models.Model):

    resto_name = models.CharField(max_length=60)
    category = models.CharField(max_length=50)
    stars = models.IntegerField()
    reservation = models.BooleanField()

    def __str__(self):
        return f"""
    {self.resto_name} se especializa en {self.category}.
    Actualmente tiene la clasificación de {self.stars} estrellas.
    """
