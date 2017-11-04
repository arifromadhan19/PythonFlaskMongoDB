from app.helper.mongo import Mongo as MongoHelper
from app.helper import constant as col
m = MongoHelper()

class QueryInsert():

    def insertData(self, name_product, qty):
        json_insert_data = {
            "name_product": name_product,
            "qty": qty
        }
        m.insert(json_insert_data, col.PRODUCT)
        return json_insert_data