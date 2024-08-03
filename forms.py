from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Product')
