from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Gladiator

d = datetime.now().strftime('%m%d%H%M%S')
engine = create_engine('sqlite:///save/save{}.sqlite'.format(d))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

gladiator1 = Gladiator()
gladiator2 = Gladiator()

gladiator1.create()
gladiator2.create()

session.add(gladiator1)
session.add(gladiator2)
session.commit()

print('Once, there was a Gladiator, and his name was {}'.format(gladiator1.name))
print('Then there was another, and his name was {}'.format(gladiator2.name))

def fight(combatant1, combatant2):
    import random
    combatants = [combatant1, combatant2]  
    winner = random.choice(combatants)
    loser = [combatant for combatant in combatants if combatant not in [winner]][0]
    return {'winner': winner, 'loser': loser} 

print('One day, they met in glorious blood-sport for all to see.')
results = fight(gladiator1, gladiator2)

loser = results['loser']
winner = results['winner']
print('The fight left {} dead, and {} victorious.'.format(loser.name, winner.name))
