from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class News(models.Model):
    heading = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.heading
