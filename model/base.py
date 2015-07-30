__author__ = 'bluzky'
from config import db

class ModelMethods(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_one(cls, filter_dict):
        return cls.query.filter_by(**filter_dict).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get(cls, filter_dict, limit=20, start=0, order_by=None):
        if order_by:
            return cls.query.filter_by(**filter_dict).offset(start).limit(limit).all()
        else:
            return cls.query.filter_by(**filter_dict).offset(start).limit(limit).order_by(order_by)

