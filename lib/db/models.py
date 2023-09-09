from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Household(Base):
    __tablename__ = "people"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    chore = relationship("Chore", backref=backref("member"))

    def __repr__(self):
        return f"Person: {self.name}" + f"Age: {self.age}" + f"Chore: {self.chore}"


class Chore(Base):
    __tablename__ = "chores"

    id = Column(Integer(), primary_key=True)
    chore_name = Column(Integer())
    priority = Column(String())

    def __repr__(self):
        return f"Chore: {self.chore_name}" + f"Priority: {self.priority}"
