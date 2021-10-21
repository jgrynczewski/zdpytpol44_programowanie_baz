# ORM (Maper obiektowo-relacyjny)
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

# 2. Deklaratywne API
# Używamy tzw. deklaratywnej klasy bazowej
# udostępnia ją nam SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # deklaratywna klasa bazowa


class Census(Base):  # Model
    __tablename__ = 'census'
    id = db.Column(db.Integer(), primary_key=True)
    state = db.Column(db.String(255))
    sex = db.Column(db.String(1))
    age = db.Column(db.Integer())
    pop2000 = db.Column(db.Float())
    pop2008 = db.Column(db.Float())


engine = db.create_engine('sqlite:///census.sqlite')

session = sessionmaker(bind=engine)()
results = session.query(Census).all()
print(results)
print(type(results[0]))

