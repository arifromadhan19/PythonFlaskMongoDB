from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name_product = StringField('name_product', validators=[validators.optional()])
    qty = IntegerField('qty', validators=[validators.optional()])