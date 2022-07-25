from sqlite3 import Date
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 4000)
    date = models.DateField(default=Date.today)
    image = models.ImageField(upload_to = "blog/images/")
    image2 = models.ImageField(upload_to = "blog/images/")
    image3 = models.ImageField(upload_to = "blog/images/")

    def __str__(self):
        return self.title
