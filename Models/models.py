from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd


Base = declarative_base()

class Employee(Base):
    __tablename__ = 'Azure_Employee_Table'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, Id, Name, Age):
        self.id = Id
        self.name = Name
        self.age = Age

    def __repr__(self):
        return f"{self.id} {self.name} {self.age}"