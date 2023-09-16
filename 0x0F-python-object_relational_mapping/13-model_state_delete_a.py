#!/usr/bin/python3
"""
 -  deletes all State objects with a name containing the letter a
    from the database

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

    # retrieve all state contain a and delete all states
    all_states = session.query(State).filter(State.name.like('%a%')).delete()

    session.commit()

    session.close()
