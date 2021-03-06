from django.db import models



class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_clossed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateField(auto_created=False)
    # date = models.DateField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

