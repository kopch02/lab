from flask import Blueprint, jsonify, request

from data import db_session
from data.users import User 
from num1 import add_user

blueprint = Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_user():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify({
        'users': [
            item.to_dict(only=('surname', 'name', 'age',
                               'position', 'speciality' )) for item in users
        ]
    })


@blueprint.route('/api/users/<int:user_id>')
def get_one_user(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        return jsonify({"error": "Not found"})
    return jsonify({
        "job":
        users.to_dict(only=('surname', 'name', 'age',
                               'position', 'speciality', 'addres','emil' ))
    })


@blueprint.route('/api/users', methods=['POST'])
def create_users():
    if not request.json:
        return jsonify({'Error': 'Empty Request'})
    elif not all(
            key in request.json
            for key in ['surname', 'name', 'age',
                               'position', 'speciality', 'addres','email']):
        return jsonify({'Error': 'Bad Request'})
    add_user(
        request.json['surname'],
        request.json['name'],
        request.json['age'],
        request.json['position'],
        request.json['speciality'],
        request.json['addres'],
        request.json['email'],
    )
    return jsonify({'Success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['DELETE'])
def delete_users(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        return jsonify({'Error': 'Not Found'})
    session.delete(users)
    session.commit()
    return jsonify({'Success': 'OK'})


@blueprint.route('/api/users/<int:users_id>', methods=['PUT'])
def modify_users(users_id):
    if not request.json:
        return jsonify({'Errors': 'Empty Request'})
    elif not all(key in request.json for key in [
            'surname', 'name', 'age',
                               'position', 'speciality', 'addres','email'
    ]):
        return jsonify({'error':'bad request'})
    session = db_session.create_session()
    users = session.query(User).filter(users.id == users_id).first()
    if not users:
        return jsonify({'Error':'Not Found'})
    users.surname = request.json['surname']
    users.name = request.json['name']
    users.age = request.json['age']
    users.position = request.json['position']
    users.speciality = request.json['speciality']
    users.addres = request.json['addres']
    users.email = request.json['email']
    session.commit()
    return jsonify({'Success': 'OK'})
    