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

    house_members = [
        Household(name=fake.name(), age=random.randint(10, 40)) for i in range(4)
    ]

    session.add_all(house_members)
    session.commit()

    chores = []
    for member in house_members:
        for i in range(3):
            chore = Chore(
                chore_name=random.choice(
                    ["dishes", "laundry", "sweeping", "mopping", "trash"]
                ),
                priority=random.choice(["high", "medium", "low"]),
            )

            chores.append(chore)

    session.bulk_save_objects(chores)
    session.commit()
    session.close()
