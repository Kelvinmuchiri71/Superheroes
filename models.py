from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade="all, delete-orphan")

    @validates('name', 'super_name')
    def validate_names(self, key, value):
        if len(value) < 3:
            raise ValueError(f"{key} must be at least 3 characters long.")
        return value

    def serialize(self):
        return {"id": self.id, "name": self.name, "super_name": self.super_name}

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade="all, delete-orphan")

    @validates('name', 'description')
    def validate_attributes(self, key, value):
        if key == 'description' and len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        if key == 'name' and len(value) < 3:
            raise ValueError("Power name must be at least 3 characters long.")
        return value

    def serialize(self):
        return {"id": self.id, "name": self.name, "description": self.description}

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'.")
        return value

    def serialize(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero": self.hero.serialize(),
            "power": self.power.serialize()
        }