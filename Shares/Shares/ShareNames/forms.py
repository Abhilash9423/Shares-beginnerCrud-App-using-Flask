from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField

class AddForm(FlaskForm):
    name = StringField("enter the name of that share")
    price = IntegerField("enter the price of that share")
    quantity = IntegerField("enter the quantity")
    submit = SubmitField("submit")


class DeleteForm(FlaskForm):
    id = IntegerField("enter the Id")
    submit = SubmitField("Delete")
