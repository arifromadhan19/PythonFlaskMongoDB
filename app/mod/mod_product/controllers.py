from flask import Blueprint, jsonify, redirect
from flask.templating import render_template
from app.helper.mongo import Mongo as MongoHelper
from app.helper import constant as col
from app.mod.mod_product.form import ProductForm
from app.utils.query_insert import QueryInsert as QueryHelper

m = MongoHelper()
insert_data = QueryHelper()
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

@mod_product.route("/create",methods=["GET"])
def create_product():
    return render_template("product/create.html")

@mod_product.route("/create", methods=["POST"])
def save_product():
    form = ProductForm()
    if not form.validate():
        return jsonify({"error": form.errors})

    name_product = form.name_product.data
    qty = form.qty.data
    insert_data.insertData(name_product,qty)

    return redirect("/")
