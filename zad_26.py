# Tworzenie tabeli
from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('sqlite:///my_db.sqlite')
metadata = MetaData()

# Zaimportuj Table, Column, String, Integer, Float, Boolean z sqlalchemy
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean

# Stwórz nową tabelę z kolumnami:
# name - String(255),
# count - Integer(),
# amount - Float(),
# valid - Boolean

my_table = Table(
    'my_table',
    metadata,
    Column('name', String(255)),
    Column('count', Integer()),
    Column('amount', Float()),
    Column('valid', Boolean())
)

# Użyj kontenera metadata do stworzenia tabeli
metadata.create_all(engine)

# Wyświetl szczegóły tabeli
print(repr(my_table))
