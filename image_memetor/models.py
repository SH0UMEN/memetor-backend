from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.image.name


class Mem(models.Model):
    image = models.ImageField(upload_to="static/memes/")

    def __str__(self):
        return self.image.name
