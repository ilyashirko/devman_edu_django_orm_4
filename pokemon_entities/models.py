from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        verbose_name='Название покемона',
        max_length=40
    )
    title_en = models.CharField(
        verbose_name='Название покемона (англ)',
        max_length=40,
        default='',
        blank=True
    )
    title_jp = models.CharField(
        verbose_name='Название покемона (яп)',
        max_length=40,
        default='',
        blank=True
    )
    image = models.ImageField(
        verbose_name='Изображение покемона'
    )
    description = models.TextField(
        verbose_name='Описание покемона',
        blank=True
    )
    evolution = models.ForeignKey(
        verbose_name='В кого эволюционирует',
        related_name='evo_from',
        to='self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        verbose_name='Покемон',
        to=Pokemon,
        related_name='location',
        on_delete=models.CASCADE
    )
    latitude = models.FloatField(
        verbose_name='Широта',
        max_length=15
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
        max_length=15
    )
    appeared_at = models.DateTimeField(
        verbose_name='Появляется в',
        default=None,
        null=True,
        blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Исчезает в',
        default=None,
        null=True,
        blank=True
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень',
        default=0
    )
    health = models.PositiveSmallIntegerField(
        verbose_name='Здоровье',
        default=0
    )
    strength = models.PositiveSmallIntegerField(
        verbose_name='Сила',
        default=0
    )
    defence = models.PositiveSmallIntegerField(
        verbose_name='Защита',
        default=0
    )
    stamina = models.PositiveSmallIntegerField(
        verbose_name='Выносливость',
        default=0
    )

    def __str__(self):
        return f'{self.pokemon.title}:   {self.latitude}, {self.longitude}'
