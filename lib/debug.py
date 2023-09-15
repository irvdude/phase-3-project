from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == "__main__":
    engine = create_engine("sqlite:///household_chores.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
