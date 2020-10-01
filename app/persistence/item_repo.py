import os
from pymongo import MongoClient

COLLECTION_NAME = 'items'


class MongoRepository(object):
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).items

    def find_all(self, selector):
        return self.db.items.find(selector)

    def find(self, selector):
        return self.db.items.find_one(selector)

    def create(self, item):
        return self.db.items.insert_one(item)

    def update(self, selector, item):
        return self.db.items.replace_one(selector, item).modified_count

    def delete(self, selector):
        return self.db.items.delete_one(selector).deleted_count
