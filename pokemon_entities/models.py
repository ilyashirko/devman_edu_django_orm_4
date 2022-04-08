from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=40, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
