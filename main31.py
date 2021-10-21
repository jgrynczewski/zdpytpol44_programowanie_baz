# ORM (Maper obiektowo-relacyjny)
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Census(Base):  # Model
    __tablename__ = 'census'
    id = db.Column(db.Integer(), primary_key=True)
    state = db.Column(db.String(255))
    sex = db.Column(db.String(1))
    age = db.Column(db.Integer())
    pop2000 = db.Column(db.Float())
    pop2008 = db.Column(db.Float())

    def __repr__(self):
        return f"<Id: {self.id} - ({self.state}, {self.sex}, {self.age})>"

    def get_population_difference(self):  # FAT MODEL
        return self.pop2008 - self.pop2000


engine = db.create_engine('sqlite:///census.sqlite')

session = sessionmaker(bind=engine)()
query = session.query(Census)  # -> Query

print(query)
print(type(query))
print(dir(query))

# all
results = query.all()
print(results)

# first
result = query.first()
print(result)
print(f"Różnica pomiędzy 2008 a 2000 wynosi: {result.get_population_difference()}")

# iteration
# for item in query:
#     print(item)