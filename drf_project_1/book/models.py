from django.db import models

class AuthorModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.f_name} {self.l_name} {self.id}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

class BookModel(models.Model):
    name = models.CharField(max_length=255)
    page_n = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

