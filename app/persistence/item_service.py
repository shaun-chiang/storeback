from bson import ObjectId

from app.persistence import Repository
from app.persistence.item_repo import MongoRepository
from app.persistence.schema import ItemSchema


class ItemService(object):
    def __init__(self, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client

    def find_all_items(self):
        items = self.repo_client.find_all({})
        return [self.dump(item) for item in items]

    def create_item(self, item):
        self.repo_client.create(item)
        return self.dump(item)

    def update_item(self, item_id, item):
        records_affected = self.repo_client.update({'_id': ObjectId(item_id)}, item)
        return records_affected > 0

    def delete_item(self, item_id):
        records_affected = self.repo_client.delete({'_id': ObjectId(item_id)})
        return records_affected > 0

    def dump(self, data):
        return ItemSchema().dump(data)
