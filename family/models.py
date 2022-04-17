from django.db import models

class Relative(models.Model):

    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth = models.DateField()

    def __str__(self):
        return f"Name: {self.name}. Age: {self.age}. Date of Birth: {self.birth}"

