from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    chore = relationship("Chore", backref=backref("person"))

    def __repr__(self):
        return f"Person: {self.name}" + f"Age: {self.age}" + f"Chore: {self.chore}"

    # class method to list all people
    @classmethod
    def list_people(cls, session):
        member = session.query(cls).all()
        return member

    # class method to get all of the chores by person name
    @classmethod
    def chores_by_person(cls, session, name):
        chore = session.query(cls).filter_by(name=name).first()
        if chore:
            return chore.chore
        else:
            return []

    # class method to assign chores to a person


class Chore(Base):
    __tablename__ = "chores"

    id = Column(Integer(), primary_key=True)
    chore_name = Column(String())
    priority = Column(String())
    chore_id = Column(Integer(), ForeignKey("person.id"))

    def __repr__(self):
        return f"Chore: {self.chore_name}" + f"Priority: {self.priority}"

    # class method to list all chores
    @classmethod
    def list_chores(cls, session):
        chore = session.query(cls).all()
        return chore

    # class method to list all people by chore
