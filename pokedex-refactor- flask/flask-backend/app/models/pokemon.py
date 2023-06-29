#models/pokemon.py
from app import db
import enum

class Types(enum.Enum):
    fire = "fire"
    electric = "electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water = "water"
    bug = "bug"
    dragon = "dragon"
    grass = "grass"
    fighting = "fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock = "rock"
    steel = "steel"

class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.Enum(Types), nullable=True)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Numeric(3, 2), nullable=False)
    catchRate = db.Column(db.Numeric(3, 2), nullable=False)
    captured = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.Date, nullable=False)
    updatedAt = db.Column(db.Date, nullable=False)

    item = db.relationship("Item", back_populates="pokemon")

def __init__(self, number, attack, defense, imageUrl, name, type, moves, encounterRate, catchRate, captured, createdAt, updatedAt):
    self.number = number
    self.attack = attack
    self.defense = defense
    self.imageUrl = imageUrl
    self.name = name
    self.type = type
    self.moves = moves
    self.encounterRate = encounterRate
    self.catchRate = catchRate
    self.captured = captured
    self.createdAt = createdAt
    self.updatedAt = updatedAt

    def __repr__(self):
        return f"<Pokemon {self.name}>"
