from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_alchemy.Models import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


class DbManagement:
    def __init__(self):
        self.session = session

    def add_value(self, projektas):
        self.session.add(projektas)
        self.session.commit()

    def get_value_by_id(self, id):
        value = session.query(Projektas).get(id)
        return value

    def filter_by_name(self, name):
        values = session.query(Projektas).filter_by(name=name).all()
        return values

    def update_value(self, id, new_name, new_price):
        value = session.query(Projektas).get(id)
        value.price = new_price
        value.name = new_name
        session.commit()

    def delete_value(self, id):
        value = session.query(Projektas).get(id)
        session.delete(value)
        session.commit()

    def filter_by_attributes(self, attribute_dict):

        query = session.query(Projektas)
        for attribute, value in attribute_dict.items():
            query = query.filter(getattr(Projektas, attribute) == value)

        matching_objects = query.all()
        return matching_objects

