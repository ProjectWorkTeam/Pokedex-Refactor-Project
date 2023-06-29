#models/items.py
from app import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
    createdAt = db.Column(db.Date, nullable=False)
    updatedAt = db.Column(db.Date, nullable=False)


    pokemon = db.relationship(
        "Pokemon",
        back_populates="item"
    )

def __init__(self, happiness, imageUrl, name, price, pokemonId, createdAt, updatedAt):
    self.happiness = happiness
    self.imageUrl = imageUrl
    self.name = name
    self.price = price
    self.pokemonId = pokemonId
    self.createdAt = createdAt
    self.updatedAt = updatedAt


    def __repr__(self):
        return f"<Item {self.name}>"
