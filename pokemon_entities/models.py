from django.db import models  # noqa F401
from datetime import datetime


class Pokemon(models.Model):
    title = models.CharField(max_length=40, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=15)
    longitude = models.FloatField(max_length=15)
    appeared_at = models.DateTimeField(default=None, blank=False)
    disappeared_at = models.DateTimeField(default=None, blank=False)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
