__author__ = 'bluzky'
from config import db

class Category(db.Model):
    _table_name = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(40))

    # unique string used to indicate category
    slug = db.Column(db.String(40), unique=True)

    def __init__(self, name):
        self.name = name
        self.slug = name.lower().replace(" ", "-")

    def __repr__(self):
        return "Category: %s ..." % self.name
