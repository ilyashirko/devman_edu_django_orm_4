from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        verbose_name='Название покемона',
        max_length=40,
        blank=True
    )
    title_en = models.CharField(
        verbose_name='Название покемона (англ)',
        max_length=40,
        blank=True
    )
    title_jp = models.CharField(
        verbose_name='Название покемона (яп)',
        max_length=40,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Изображение покемона',
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание покемона',
        blank=True
    )

    evolution = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )

    deevolution = models.ForeignKey(
        to='Pokemon',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        verbose_name='Pokemon',
        to=Pokemon,
        on_delete=models.CASCADE
        )

    latitude = models.FloatField(max_length=15, blank=False)
    longitude = models.FloatField(max_length=15, blank=False)
    
    appeared_at = models.DateTimeField(default=None, blank=False)
    disappeared_at = models.DateTimeField(default=None, blank=False)

    level = models.PositiveSmallIntegerField(
        default=None,
        blank=False
    )
    health = models.PositiveSmallIntegerField(
        default=None,
        blank=False
    )
    strength = models.PositiveSmallIntegerField(
        default=None,
        blank=False
    )
    defence = models.PositiveSmallIntegerField(
        default=None,
        blank=False
    )
    stamina = models.PositiveSmallIntegerField(
        default=None,
        blank=False
    )


    def __str__(self):
        return f'{self.pokemon.title}:   {self.latitude}, {self.longitude}'
