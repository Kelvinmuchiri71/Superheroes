
from flask import request, jsonify
from models import db, Hero, Power, HeroPower


from app import app


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify(hero.to_dict())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict())

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    if "description" in data:
        if len(data["description"]) < 20:
            return jsonify({"errors": ["Description must be at least 20 characters long"]}), 400
        power.description = data["description"]

    db.session.commit()
    return jsonify(power.to_dict())

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    hero = Hero.query.get(data.get("hero_id"))
    power = Power.query.get(data.get("power_id"))

    if not hero or not power:
        return jsonify({"errors": ["Hero or Power not found"]}), 400

    if data.get("strength") not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}), 400

    hero_power = HeroPower(
        hero_id=data["hero_id"],
        power_id=data["power_id"],
        strength=data["strength"]
    )

    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.to_dict()), 201