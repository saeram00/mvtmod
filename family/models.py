from django.db import models

class Relative(models.Model):

    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth = models.DateField()
    job = models.CharField(max_length=50)

    def __str__(self):
        return f"""
                Nombre: {self.name}.
                Edad: {self.age}.
                Fecha de Nacimiento: {self.birth}.
                Ocupación: {self.job}.
                """

