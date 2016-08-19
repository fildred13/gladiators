from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from world.world import generate_name 

Base = declarative_base()

class Gladiator(Base):
    __tablename__ = 'gladiator'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)

    def create(self):
        self.name = generate_name()

