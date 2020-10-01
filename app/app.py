from flask import Flask, json, g, request
from flask_cors import CORS

from app.persistence.item_service import ItemService
from app.persistence.schema import ItemSchema

app = Flask(__name__)
CORS(app)


@app.route("/items", methods=["GET"])
def index():
    return json_response(ItemService().find_all_items())


@app.route("/items", methods=["POST"])
def create():
    try:
        item = ItemSchema(exclude=["_id"]).load(json.loads(request.data))

        created_item = ItemService().create_item(item)
        return json_response(created_item)
    except Exception as ex:
        return json_response({'error': str(ex)}, 422)


@app.route("/items/<string:item_id>", methods=["PUT"])
def update(item_id):
    try:
        item = ItemSchema(exclude=["_id"]).load(json.loads(request.data))
        item_service = ItemService()
        if item_service.update_item(item_id, item):
            return json_response(item)
        else:
            return json_response({'error': 'item not found'}, 404)
    except Exception as ex:
        return json_response({'error': str(ex)}, 422)


@app.route("/items/<string:item_id>", methods=["DELETE"])
def delete(item_id):
    item_service = ItemService()
    if item_service.delete_item(item_id):
        return json_response({}, 204)
    else:
        return json_response({'error': 'item not found'}, 404)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})
