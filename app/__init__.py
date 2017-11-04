from flask import Flask

application = Flask(__name__)

application.config.from_object('config')

from app.helper.mongo import Mongo as MongoHelper
m = MongoHelper()

from app import mod