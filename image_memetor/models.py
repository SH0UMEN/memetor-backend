from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Image(models.Model):
    image = models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.image.name


class Mem(models.Model):
    image = models.ImageField(upload_to="static/memes/")

    def __str__(self):
        return self.image.name


@receiver(post_delete, sender=Mem)
def afterMemDelete(sender, instance, **kwargs):
    instance.image.delete(False)
