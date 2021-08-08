from flask import Blueprint, json, jsonify, request
from flask_migrate import current
from werkzeug.wrappers import response
from marvel_app.helpers import token_required
from marvel_app.models import db, User, Character, character_schema, characters_schema


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'someValue':52, 'anotherValue':800}

#route to create a character
@api.route('/characters', methods = ['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    movies = request.json['movies']
    events = request.json['events']
    series = request.json['series']
    powers = request.json['powers']
    snapped = request.json['snapped']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    character = Character(name, description, movies, events, series, powers, snapped, user_token = user_token)

    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)

# route to retrieve multiple characters
@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)

# route to retrieve one item
@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    character = Character.query.get(id)
    response = character_schema.dump(character)
    return jsonify(response)

# Route to update a character
@api.route('/characters/<id>', methods = ['POST'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)
    if character:
        character.name = request.json['name']
        character.description = request.json['description']
        character.movies = request.json['movies']
        character.events = request.json['events']
        character.series = request.json['series']
        character.powers = request.json['powers']
        character.snapped = request.json['snapped']
        character.user_token = current_user_token.token

        db.session.commit()

        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That character does not exist'})

# Delete a character
@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    if character:
        db.session.delete(character)
        db.session.commit()
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That character does not exist'})