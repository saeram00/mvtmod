from django.db import models

# Create your models here.
class Book(models.Model):

    book_title = models.CharField(max_length=60)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    publised = models.IntegerField()
    book_length = models.IntegerField()


    def __str__(self):
        return f"""
    {self.book_title} por {self.author}.
    Publicado en: {self.publised}.
    Género: {self.genre}.
    Duración: {self.book_length}.
    """
