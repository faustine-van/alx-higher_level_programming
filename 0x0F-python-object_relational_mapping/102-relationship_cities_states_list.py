#!/usr/bin/python3
"""
 - script that lists all City objects from the database hbtn_0e_101_usa
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

    # script that lists all City objects
    cities = session.query(City).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # close session
    session.close()
