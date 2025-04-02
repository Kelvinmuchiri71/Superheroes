
from flask import request, jsonify
from models import db, Hero, Power, HeroPower


from app import app


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify(hero.serialize())

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.serialize())

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
    return jsonify(power.serialize())

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength")

    if not hero_id or not power_id:
        return jsonify({"errors": ["Hero ID and Power ID are required"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero:
        return jsonify({"errors": ["Hero not found"]}), 404
    if not power:
        return jsonify({"errors": ["Power not found"]}), 404
    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}), 400

    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)

    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.serialize()), 201

@app.route('/hero_powers', methods=['GET'])
def get_hero_powers():
    hero_powers = HeroPower.query.all()
    return jsonify([hp.serialize() for hp in hero_powers])
