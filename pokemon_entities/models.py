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
        null=True,
        blank=True
    )
    title_jp = models.CharField(
        verbose_name='Название покемона (яп)',
        max_length=40,
        null=True,
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
        verbose_name='В кого эволюционирует',
        to='self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )
    deevolution = models.ForeignKey(
        verbose_name='Из кого эволюционировал',
        to='self',
        related_name='+',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        verbose_name='Покемон',
        to=Pokemon,
        on_delete=models.CASCADE
    )
    latitude = models.FloatField(
        verbose_name='Широта',
        max_length=15,
        blank=False
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
        max_length=15,
        blank=False
    )
    appeared_at = models.DateTimeField(
        verbose_name='Появляется в',
        default=None,
        null=True,
        blank=False
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Исчезает в',
        default=None,
        null=True,
        blank=False
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень',
        default=None,
        null=True,
        blank=False
    )
    health = models.PositiveSmallIntegerField(
        verbose_name='Здоровье',
        default=None,
        null=True,
        blank=False
    )
    strength = models.PositiveSmallIntegerField(
        verbose_name='Сила',
        default=None,
        null=True,
        blank=False
    )
    defence = models.PositiveSmallIntegerField(
        verbose_name='Защита',
        default=None,
        null=True,
        blank=False
    )
    stamina = models.PositiveSmallIntegerField(
        verbose_name='Выносливость',
        default=None,
        null=True,
        blank=False
    )

    def __str__(self):
        return f'{self.pokemon.title}:   {self.latitude}, {self.longitude}'
