from flask import Blueprint, jsonify
from flask.templating import render_template
from app.helper.mongo import Mongo as MongoHelper
from app.helper import constant as col

m = MongoHelper()
mod_product = Blueprint('product',__name__)

@mod_product.route("/",methods=["GET"])
def index():
    find_data = m.getCollection(col.PRODUCT).find()
    list_product = []
    for data in find_data:
        print(data)
        data["_id"] = str(data.get("_id"))

        list_product.append(data)

    return render_template("product/index.html", list_product=list_product)

