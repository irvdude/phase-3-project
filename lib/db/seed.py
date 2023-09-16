from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


fake = Faker()

engine = create_engine("sqlite:///household_chores.db")
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    from models import Person, Chore

    session.query(Person).delete()
    session.query(Chore).delete()
    session.commit()

    house_members = [
        Person(name=fake.name(), age=random.randint(10, 40)) for i in range(4)
    ]

    session.add_all(house_members)
    session.commit()

    chores = []
    for member in house_members:
        chore = Chore(
            chore_name=random.choice(
                ["dishes", "laundry", "sweeping", "mopping", "trash"]
            ),
            priority=random.choice(["high", "medium", "low"]),
            chore_id=member.id,
        )

        chores.append(chore)

    session.bulk_save_objects(chores)
    session.commit()
    session.close()
