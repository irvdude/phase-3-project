from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Household, Chore

fake = Faker()

if __name__ == "__main__":
    engine = create_engine("sqlite:///household_chores.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Household).delete()
    session.query(Chore).delete()
    session.commit()
