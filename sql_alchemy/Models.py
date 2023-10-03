from datetime import datetime
from sqlalchemy import Column, Text, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///projektai.db')

Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Pavadinimas", String, default=None)
    price = Column("Kaina", Float)
    is_in_stock = Column("Yra", Boolean)
    location = Column("Lokacija", Text, default=None)
    create_date = Column("Sukūrimo data", DateTime, default=datetime.utcnow)

    def __init__(self, name, price, is_in_stock, location):
        self.name = name
        self.price = price
        self.is_in_stock = is_in_stock
        self.location = location

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.create_date}"


# Base.metadata.create_all(engine)
