import logging
import traceback
import time
from pymongo.mongo_client import MongoClient
from app import application


class Mongo():
    def __init__(self):
        self.mdb = None
        self.mcdb = None

    def get_mongo_client(self):
        return MongoClient(application.config.get('MONGO_URL_CONNECTION'))

    def select_db(self, db):
        if not self.mcdb:
            self.mcdb = self.get_mongo_client()

        oke = False
        while not oke:
            try:
                self.mcdb.server_info()
                oke = True
            except:
                logging.error(traceback.format_exc())
                time.sleep(1)
                self.mcdb = self.get_mongo_client()

        return self.mcdb[db]

    def mongo_db(self):
        if not self.mdb:
            self.mdb = self.select_db(application.config.get("MONGO_DB"))

        return self.mdb

    def getCollection(self, collection_name, db=None):
        if not db:
            db = application.config.get("MONGO_DB")

        collection = self.select_db(db)[collection_name]
        return collection

    def fineOneFromCollectio(self, query, collection_name, db=None):
        collection = self.getCollection(collection_name, db)
        return collection.find_one(query)

    def insert(self, query, collection_name, db=None):
        collection = self.getCollection(collection_name, db)
        collection.insert_one(query)