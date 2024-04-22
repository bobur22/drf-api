# from django.db import models
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name
#
# class Women(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=False)
#     cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return self.title
