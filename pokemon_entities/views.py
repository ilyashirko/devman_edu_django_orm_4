import folium
from pogomap.settings import MEDIA_URL
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)
MEDIA_DIR = ''.join(MEDIA_URL.split('/'))


class TooManyPokemonsFound(Exception):
    def __init__(self, error_message, pokemon_id, pokemons):
        self.error_message = error_message
        self.pokemon_id = pokemon_id
        self.pokemons = pokemons
    
    def __str__(self):
        return f'{self.error_message}\nPokemon ID: {self.pokemon_id}\n{self.pokemons}'


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in PokemonEntity.objects.all():
        add_pokemon(
            folium_map,
            entity.latitude,
            entity.longitude,
            f'{MEDIA_DIR}/{entity.pokemon.image}'
        )
    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(
                location=f"{MEDIA_DIR}/{pokemon.image}"
            ),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except AttributeError:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    except Pokemon.MultipleObjectsReturned as error:
        return 

    seiralized_pokemon = {
        "pokemon_id": requested_pokemon.id,
        "title_ru": requested_pokemon.title,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "img_url": request.build_absolute_uri(
            location=f"{MEDIA_DIR}/{requested_pokemon.image}"
        ),
        "description": requested_pokemon.description,
    }
    if requested_pokemon.evolves_into is not None:
        seiralized_pokemon.update({
            "next_evolution": {
                "title_ru": requested_pokemon.evolves_into.title,
                "pokemon_id": requested_pokemon.evolves_into.id,
                "img_url": request.build_absolute_uri(
                    location=f"{MEDIA_DIR}/{requested_pokemon.evolves_into.image}"
                )
            }
        })
    evolution_from = requested_pokemon.evolved_from.all()
    if evolution_from:
        seiralized_pokemon.update({
            "previous_evolution": {
                "title_ru": evolution_from[0].title,
                "pokemon_id": evolution_from[0].id,
                "img_url": request.build_absolute_uri(
                    location=f"{MEDIA_DIR}/{evolution_from[0].image}"
                )
            }
        })

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities = requested_pokemon.entities.all()

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(
                location=f"{MEDIA_DIR}/{requested_pokemon.image}"
            )
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': seiralized_pokemon
    })
