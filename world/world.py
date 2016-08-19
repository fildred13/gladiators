from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from world.models import *

engine = create_engine('sqlite:///world/world.sqlite')
WorldBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
world = Session()

def generate_name():
    first_name = world.query(Name).filter('is_first').order_by(func.random()).limit(1).one().name
    last_name = world.query(Name).filter('is_last').order_by(func.random()).limit(1).one().name
    return '{} {}'.format(first_name, last_name)
