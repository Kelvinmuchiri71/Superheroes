
from models import db, Hero, Power, HeroPower
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Peter Parker", super_name="Spider-Man")
    
    power1 = Power(name="Super Strength", description="Grants incredible physical strength beyond human limits.")
    power2 = Power(name="Flight", description="Allows the hero to fly at high speeds through the air.")

    db.session.add_all([hero1, hero2, power1, power2])
    db.session.commit()

    hero_power1 = HeroPower(hero_id=hero1.id, power_id=power1.id, strength="Strong")
    hero_power2 = HeroPower(hero_id=hero2.id, power_id=power2.id, strength="Average")

    db.session.add_all([hero_power1, hero_power2])
    db.session.commit()

    print("Database seeded successfully!")