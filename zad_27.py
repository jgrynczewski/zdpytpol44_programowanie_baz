# Tworzenie tabeli - więzy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean

engine = create_engine('sqlite:///my_db.sqlite')
metadata = MetaData()

# Stwórz nową tabelę z kolumnami:
# name - String(255) z wartościami unikalnymi,
# count - Integer() z wartością domyślną 1,
# amount - Float(),
# valid - Boolean z wartością domyślną False

my_table = Table(
    'my_table',
    metadata,
    Column('name', String(255), unique=____),
    Column('count', Integer(), default=____),
    Column('amount', Float()),
    Column('valid', Boolean(), default=____)
)

# Użyj kontenera metadata do stworzenia tabeli
metadata.create_all(engine)

# Wyświetl szczegóły tabeli
print(metadata.tables['my_table'])
