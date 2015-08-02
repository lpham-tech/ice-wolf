__author__ = 'bluzky'
from base import db
from lib.utils import get_slug_from_string

class Category(db.Model):
    _table_name = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

    # unique string used to indicate category
    slug = db.Column(db.String(40), unique=True)

    def __init__(self, name):
        self.name = name
        self.slug = get_slug_from_string(name)

    def __repr__(self):
        return "Category: %s ..." % self.name
