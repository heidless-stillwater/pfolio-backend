from django.db import models

class App(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
