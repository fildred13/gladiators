from sqlalchemy import Table, Column, Boolean, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

WorldBase = declarative_base()

class Name(WorldBase):
    __tablename__ = 'name'

    __table_args__ = (CheckConstraint("'is_first' OR 'is_last'"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String(24), nullable=False, unique=True)
    is_first = Column(Boolean(), nullable=False)
    is_last = Column(Boolean(), nullable=False)

