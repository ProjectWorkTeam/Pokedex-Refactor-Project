import random
from app.models.items import Item


def random_100():
    return random.randint(1, 100)

def random_image():
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    return random.choice(images)

def random_adjective(adjectives):
    return random.choice(adjectives)

def item_name_from_image(image_url):
    item_mapping = {
        "/images/pokemon_berry.svg": "Berry",
        "/images/pokemon_egg.svg": "Egg",
        "/images/pokemon_potion.svg": "Potion",
        "/images/pokemon_super_potion.svg": "Super Potion",
    }
    return item_mapping.get(image_url, "Item")

def generate_items():
    adjectives1 = ['Gigantic', 'Tiny', 'Ancient', 'Mysterious', 'Incredible']
    adjectives2 = ['Special', 'Shiny', 'Sparkling', 'Radiant', 'Exquisite']
    items = []
    for pokemon_id in range(1, 11):
        for _ in range(3):
            image = random_image()
            name = f'{random_adjective(adjectives1)} {random_adjective(adjectives2)} {item_name_from_image(image)}'
            item = Item(
                pokemon_id=pokemon_id,
                name=name,
                price=random_100(),
                happiness=random_100(),
                image_url=image,
            )
            items.append(item)
    return items

def seed_items(db):
    items = generate_items()
    for item in items:
        db.session.add(item)
    db.session.commit()

def delete_items(db):
    Item.query.delete()
    db.session.commit()
