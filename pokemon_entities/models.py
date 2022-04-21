from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        verbose_name='Название покемона',
        max_length=40
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
        verbose_name='Изображение покемона'
    )
    description = models.TextField(
        verbose_name='Описание покемона',
        blank=True
    )
    evolves_into = models.ForeignKey(
        verbose_name='В кого эволюционирует',
        related_name='evolved_from',
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
        related_name='entities',
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
        null=True,
        blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Исчезает в',
        null=True,
        blank=True
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень'
    )
    health = models.PositiveSmallIntegerField(
        verbose_name='Здоровье'
    )
    strength = models.PositiveSmallIntegerField(
        verbose_name='Сила'
    )
    defence = models.PositiveSmallIntegerField(
        verbose_name='Защита'
    )
    stamina = models.PositiveSmallIntegerField(
        verbose_name='Выносливость'
    )

    def __str__(self):
        return f'{self.pokemon.title}:   {self.latitude}, {self.longitude}'
