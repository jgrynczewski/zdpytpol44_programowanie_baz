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

my_table2 = Table(
    'my_table2',
    metadata,
    Column('name', String(255), unique=True),
    Column('count', Integer(), default=1),
    Column('amount', Float()),
    Column('valid', Boolean(), default=False)
)

# Użyj kontenera metadata do stworzenia tabeli
metadata.create_all(engine)

# Wyświetl szczegóły tabeli
print(metadata.tables['my_table2'])
