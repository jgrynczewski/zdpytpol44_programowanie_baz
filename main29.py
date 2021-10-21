# ORM (Maper obiektowo-relacyjny)
import sqlalchemy as db

# Dwa rodzaje ORM w sqlalchemy:
# 1. klasyczne mapowanie
# 2. deklaratywne API

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = db.MetaData()
census = db.Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = db.select([
    census
]).where(
    census.columns.state == "New York"
)

print(stmt)

results = engine.execute(stmt).first()
print(results)

# 1. Mapowanie klasyczne

# Do mapowanie klasycznego potrzebujemy trzy rzeczy:
# 1. klasę, która będzie miała informacje o tabeli - to już
# mamy - to jest odicie tabeli
# 2. klasa, która będzie W PEŁNI reprezentowała tabelę z bazy danych
# 3. mapper, który powiąże ze sobą 1 i 2

# To robimy
# 1 mamy - census

# 2. (klasa z atrybutami reprezentującymi poszczególne kolumny)
# to jest zwykła klasa pythonowa. Dopóki ją nie połączymy z
# odbiciem to niczego więcej poza zwykłą klasą pythonową
# nie potrafi.
class Census:  # Tą klasę nazywamy modelem (aka modelem domeny)
    def __init__(self, id, state, sex, age, pop2000, pop2008):
        self.id = id
        self.state = state
        self.sex = sex
        self.age = age
        self.pop2000 = pop2000
        self.pop2008 = pop2008

# 3. mapper
from sqlalchemy.orm import mapper

census_mapper = mapper(Census, census)

# Od teraz klasa Census W PEŁNI reprezentnuje
# tabelę z bazy

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
with Session() as session:
    # results = session.execute(stmt).fetchall()
    results = session.query(Census).all()

print(results)
print(results[0].state)  # Dostajemy obiekty modelu
