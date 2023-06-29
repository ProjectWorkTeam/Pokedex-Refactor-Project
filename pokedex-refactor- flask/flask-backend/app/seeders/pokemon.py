#seeders/pokemon.py
from app.models import Pokemon

def seed_data(db):
    pokemons = [
    {
        'number': 60,
        'imageUrl': '/images/pokemon_snaps/60.svg',
        'name': 'Poliwag',
        'attack': 50,
        'defense': 40,
        'type': 'water',
        'moves': ['bubble', 'water gun'],
        'captured': True
    },
    {
        'number': 52,
        'imageUrl': '/images/pokemon_snaps/52.svg',
        'name': 'Meowth',
        'attack': 45,
        'defense': 35,
        'type': 'normal',
        'moves': ['scratch', 'bite'],
        'captured': True
    },
    {
        'number': 80,
        'imageUrl': '/images/pokemon_snaps/80.svg',
        'name': 'Slowbro',
        'attack': 75,
        'defense': 110,
        'type': 'water',
        'moves': ['psychic', 'water gun', 'confusion', 'headbutt'],
        'captured': True
    },
    {
        'number': 94,
        'imageUrl': '/images/pokemon_snaps/94.svg',
        'name': 'Gengar',
        'attack': 65,
        'defense': 60,
        'type': 'ghost',
        'moves': ['tackle', 'lick', 'shadow punch', 'shadow ball'],
        'captured': True
    },
    {
        'number': 110,
        'imageUrl': '/images/pokemon_snaps/110.svg',
        'name': 'Weezing',
        'attack': 90,
        'defense': 120,
        'type': 'poison',
        'moves': ['tackle', 'smog', 'sludge'],
        'captured': True
    },
    {
        'number': 113,
        'imageUrl': '/images/pokemon_snaps/113.svg',
        'name': 'Chansey',
        'attack': 5,
        'defense': 5,
        'type': 'normal',
        'moves': ['pound', 'egg bomb'],
        'captured': True
    },
    {
        'number': 121,
        'imageUrl': '/images/pokemon_snaps/121.svg',
        'name': 'Starmie',
        'attack': 75,
        'defense': 85,
        'type': 'water',
        'moves': ['water gun', 'swift'],
        'captured': True
    },
    {
        'number': 131,
        'imageUrl': '/images/pokemon_snaps/131.svg',
        'name': 'Lapras',
        'attack': 85,
        'defense': 80,
        'type': 'water',
        'moves': ['water gun', 'body slam', 'ice beam', 'hydro pump'],
        'captured': True
    },
    {
        'number': 143,
        'imageUrl': '/images/pokemon_snaps/143.svg',
        'name': 'Snorlax',
        'attack': 110,
        'defense': 65,
        'type': 'normal',
        'moves': ['tackle', 'headbutt', 'snore', 'body slam'],
        'captured': True
    },
    {
        'number': 7,
        'imageUrl': '/images/pokemon_snaps/7.svg',
        'name': 'Squirtle',
        'attack': 48,
        'defense': 65,
        'type': 'water',
        'moves': ['tackle', 'bubble', 'water gun'],
        'captured': True
    },
    {
        'number': 65,
        'imageUrl': '/images/pokemon_snaps/65.svg',
        'name': 'Alakazam',
        'attack': 50,
        'defense': 45,
        'type': 'psychic',
        'moves': ['confusion', 'psybeam', 'psychic'],
        'captured': True
    },
    ]

    for pokemon_data in pokemons:
        pokemon = Pokemon(**pokemon_data)
        db.session.add(pokemon)

    db.session.commit()
