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


class Chore(Base):
    __tablename__ = "chores"

    id = Column(Integer(), primary_key=True)
    chore_name = Column(Integer())
    priority = Column(String())
    chore_id = Column(Integer(), ForeignKey("person.id"))

    def __repr__(self):
        return f"Chore: {self.chore_name}" + f"Priority: {self.priority}"
