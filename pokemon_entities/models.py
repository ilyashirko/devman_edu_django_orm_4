from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=40, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(max_length=15)
    longitude = models.FloatField(max_length=15)
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
