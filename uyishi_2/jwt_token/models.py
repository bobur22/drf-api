from django.db import models

class AuthorsModel(models.Model):
    name = models.CharField(max_length=100)
    #
    # class Meta:
    #     verbose_name = 'author'
    #     verbose_name_plural = 'authors'
    #
    # def __str__(self):
    #     return f'{self.name}'

class BooksModel(models.Model):
    name = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(AuthorsModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f'{self.name}'





