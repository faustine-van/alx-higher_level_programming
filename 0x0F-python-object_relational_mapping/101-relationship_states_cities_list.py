#!/usr/bin/python3
"""
   - lists all State objects, and corresponding City objects, contained in
     the database hbtn_0e_101_usa
"""

from relationship_state import Base, State
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

    # script that lists all State objects
    states = session.query(State).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # close session
    session.close()
