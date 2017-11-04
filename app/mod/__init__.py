from app import application
from app.mod.mod_product.controllers import mod_product

application.register_blueprint(mod_product)