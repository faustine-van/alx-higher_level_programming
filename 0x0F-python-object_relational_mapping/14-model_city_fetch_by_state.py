#!/usr/bin/python3
"""
- prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    pwd = args[2]
    db = args[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db),
        pool_pre_ping=True
    )

    # create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # lists all State objects from the database hbtn_0e_6_usa
    cities = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
