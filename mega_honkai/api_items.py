from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.items import Item


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('rank', required=True)
parser.add_argument('type', required=True)


def abort_if_item_not_found(item_id):
    session = db_session.create_session()
    item = session.query(Item).get(item_id)
    if not item:
        abort(404, message=f"item {item_id} not found")


class ItemsResource(Resource):
    def get(self, item_id):
        abort_if_item_not_found(item_id)
        session = db_session.create_session()
        items = session.query(Item).get(item_id)
        return jsonify({'item': items.to_dict(
            only=('id', 'name', 'rank','type'))})
    
    def delete(self, item_id):
        abort_if_item_not_found(item_id)
        session = db_session.create_session()
        item = session.query(Item).get(item_id)
        session.delete(item)
        session.commit()
        return jsonify({'success': 'OK'})
        
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        item = Item(
            id = args['id'],
            name = args['name'],
            rank = args['rank'],
            type = args['type']
        )
        session.add(item)
        session.commit()
        return jsonify({'success': 'OK'})

class ItemsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        items = session.query(Item).all()
        return jsonify({'items':[item.to_dict(only=('id','name','rank','type')) for item in items]})