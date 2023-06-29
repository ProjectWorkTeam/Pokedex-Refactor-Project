from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length, Optional, URL
from enum import Enum
from datetime import datetime

class Types(Enum):
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

class PokemonForm(FlaskForm):
    number = IntegerField('number', validators=[DataRequired(), NumberRange(min=1, message="Number must be greater than or equal to 1")])
    attack = IntegerField('attack', validators=[DataRequired(), NumberRange(min=0, max=100, message="Attack must be between 0 and 100")])
    defense = IntegerField('defense', validators=[DataRequired(), NumberRange(min=0, max=100, message="Defense must be between 0 and 100")])
    imageUrl = StringField('imageUrl', validators=[DataRequired(), URL(message="Invalid URL"), Length(max=255, message="Image Url must be less than 255 characters")])
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=255, message="Name must be between 3 and 255 characters")])
    type = SelectField('Type', choices=[(t, t.value) for t in Types])
    moves = StringField('moves', validators=[DataRequired(), Length(max=255, message="Moves must be less than 255 characters")])
    encounterRate = DecimalField('encounterRate', validators=[DataRequired(), NumberRange(min=0, max=100, message="Encounter rate must be between 0 and 100")])
    catchRate = DecimalField('catchRate', validators=[DataRequired(), NumberRange(min=0, max=100, message="Catch rate must be between 0 and 100")])
    captured = BooleanField('captured', validators=[DataRequired()])




##second option


from wtforms import Form, IntegerField, StringField, SelectField, DecimalField, BooleanField, validators
from enum import Enum
from wtforms.fields.html5 import DateField
from wtforms.validators import Optional, URL, NumberRange, Length, DataRequired

class Types(Enum):
    fire = "fire"
    electric = "electric"
    normal = "normal"
    ghost = "ghost"
    psychic = "psychic"
    water ="water"
    bug ="bug"
    dragon ="dragon"
    grass ="grass"
    fighting ="fighting"
    ice = "ice"
    flying = "flying"
    poison = "poison"
    ground = "ground"
    rock = "rock"
    steel = "steel"

class PokemonForm(Form):
    number = IntegerField('Number', [DataRequired(), NumberRange(min=1)])
    attack = IntegerField('Attack', [DataRequired(), NumberRange(min=0, max=100)])
    defense = IntegerField('Defense', [DataRequired(), NumberRange(min=0, max=100)])
    imageUrl = StringField('Image URL', [DataRequired(), URL()])
    name = StringField('Name', [DataRequired(), Length(min=3, max=255)])
    type = SelectField('Type', [Optional()], choices=[(t, t.value) for t in Types], coerce=Types)
    moves = StringField('Moves', [DataRequired(), Length(max=255)])
    encounterRate = DecimalField('Encounter Rate', [DataRequired(), NumberRange(min=0, max=100)])
    catchRate = DecimalField('Catch Rate', [DataRequired(), NumberRange(min=0, max=100)])
    captured = BooleanField('Captured', [DataRequired()])
    createdAt = DateField('Created At', [DataRequired()])
    updatedAt = DateField('Updated At', [DataRequired()])
