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
query = session.query(Census)

# Filtry
# metoda filter_by
results = query.filter_by(
    state='New York'  # UWAGA! Sama nazwa kolumny i nie ma == jak w where tylko =
).all()

# metoda filter
results = query.filter(
    Census.state == 'New York'  # UWAGA! A tu z kolei z powrotem ==
    # To jest ClauseElement
).all()

# like
results = query.filter(
    Census.state.like("New%")
).all()

# startswith
results = query.filter(
    Census.state.startswith("New")
).all()

# contains
results = query.filter(
    Census.state.contains("an")  # like("%an%')
).all()

# Agregaty
results = session.query(
    db.func.sum(Census.pop2008)
).filter(
    Census.state == "New York"
).scalar()  # all()

# Operacje matematyczne
results = session.query(
    Census,
    Census.pop2008 - Census.pop2000
).filter(
    Census.state == "New York"
).all()

# Rzutowanie
results = session.query(
    Census,
    db.cast((Census.pop2008 - Census.pop2000), db.Numeric(12, 2))
).filter(
    Census.state == "New York"
).all()

# Etykietowanie
results = session.query(
    Census,
    db.cast((Census.pop2008 - Census.pop2000), db.Numeric(12, 2)).label('population_difference')
).filter(
    Census.state == "New York"
).all()

# LIMIT
results = session.query(
    Census,
    db.cast((Census.pop2008 - Census.pop2000), db.Numeric(12, 2)).label('population_difference')
).filter(
    Census.state == "New York"
).limit(5).all()

# order_by
results = session.query(
    Census,
    db.cast((Census.pop2008 - Census.pop2000), db.Numeric(12, 2)).label('population_difference')
).filter(
    Census.state == "New York"
).order_by(
    'population_difference'
).limit(5).all()

# desc
results = session.query(
    Census,
    db.cast((Census.pop2008 - Census.pop2000), db.Numeric(12, 2)).label('population_difference')
).filter(
    Census.state == "New York"
).order_by(
    db.desc('population_difference')
).limit(5).all()

print(results)


# INSERT

new_entry = Census(
    state='Polska',
    sex='M',
    age=20,
    pop2000=12456,
    pop2008=13451
)

session.add(new_entry)
session.commit()

# Update
result = session.query(
    Census
).filter(
    Census.id == 1
).first()

print(result)

result.age = 100
session.commit()

# delete
session.delete(result)
session.commit()