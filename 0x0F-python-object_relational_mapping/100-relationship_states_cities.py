#!/usr/bin/python3
"""
 - creates the State “California” with the City “San Francisco” from the
   database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from relationship_state  import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    pwd = args[2]
    db = args[3]

    # Create a SQLite database in memory
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db),
        pool_pre_ping=True
      )

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create the State “California” with the City “San Francisco”
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()

    # close session
    session.close()
