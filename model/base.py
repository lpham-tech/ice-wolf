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
    def get(cls, filter_dict=None, limit=20, start=0, order_by=None):
        if filter_dict:
            if order_by:
                return cls.query.filter_by(**filter_dict).order_by(order_by).offset(start).limit(limit).all()
            else:
                return cls.query.filter_by(**filter_dict).offset(start).limit(limit).all()

        else:
            if order_by:
                return cls.query.order_by(order_by).offset(start).limit(limit).all()
            else:
                return cls.query.offset(start).limit(limit).all()

    @classmethod
    def search(cls, search_dict, limit=20, start=0, order_by=None):
        search_str = ""
        for k,v in search_dict.items():
            search_str += " {0} LIKE '%{1}%' or".format(k,v)
        if search_str:
            search_str = search_str[:len(search_str)-2]
        if order_by:
            return cls.query.filter(search_str).order_by(order_by).offset(start).limit(limit).all()
        else:
            return cls.query.filter(search_str).offset(start).limit(limit).all()
