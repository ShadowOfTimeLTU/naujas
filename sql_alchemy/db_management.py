from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from sql_alchemy.Models import Projektas

Session = sessionmaker()


class DbManagement:
    def __init__(self, engine):
        self.session = Session(bind=engine)

    def commit_changes(self):
        self.session.commit()

    def add_value(self, projektas):
        self.session.add(projektas)
        self.commit_changes()

    def get_value_by_id(self, id):
        value = self.session.query(Projektas).get(id)
        return value

    def filter_by_name(self, name):
        values = self.session.query(Projektas).filter_by(name=name).all()
        return values

    def update_value(self, id, new_name, new_price):
        value = self.session.query(Projektas).get(id)
        value.price = new_price
        value.name = new_name
        self.commit_changes()

    def delete_value(self, id):
        value = self.session.query(Projektas).get(id)
        self.session.delete(value)
        self.commit_changes()

    def filter_by_attributes(self, attribute_dict):
        query = self.session.query(Projektas)
        conditions = []

        for attribute, value in attribute_dict.items():
            if isinstance(value, bool):
                conditions.append(getattr(Projektas, attribute) == value)
            else:
                conditions.append(getattr(Projektas, attribute) == value)

        if conditions:
            query = query.filter(and_(*conditions))

        matching_objects = query.all()
        return matching_objects
