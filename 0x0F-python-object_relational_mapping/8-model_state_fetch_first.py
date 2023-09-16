#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

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

    # lists all State objects from the database hbtn_0e_6_usa
    states = session.query(State).first()

    if states is None:
        print("Nothing")

    print(f"{states.id}: {states.name}")
