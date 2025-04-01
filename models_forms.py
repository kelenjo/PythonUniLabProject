# models_forms.py
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange

db = SQLAlchemy()  


# ✅ Item Model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Item(name={self.name}, quantity={self.quantity})"


# ✅ Item Form (Validation)
class ItemForm(FlaskForm):
    class Meta:
        csrf = False  # Disable CSRF globally for APIs

    name = StringField("name", validators=[InputRequired(), Length(min=1, max=100)])
    quantity = IntegerField("quantity", validators=[InputRequired(), NumberRange(min=1)])
