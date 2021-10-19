# Tworzenie tabeli
from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('sqlite:///my_db.sqlite')
metadata = MetaData()

# Zaimportuj Table, Column, String, Integer, Float, Boolean z sqlalchemy
from sqlalchemy import ____
from sqlalchemy import ____
from sqlalchemy import ____
from sqlalchemy import ____
from sqlalchemy import ____
from sqlalchemy import ____

# Stwórz nową tabelę z kolumnami:
# name - String(255),
# count - Integer(),
# amount - Float(),
# valid - Boolean

my_table = Table(
    'my_table',
    ____,
    Column(____, ____),
    Column('count', Integer()),
    Column(____, ____),
    Column(____, ____)
)

# Użyj kontenera metadata do stworzenia tabeli
metadata.create_all(____)

# Wyświetl szczegóły tabeli
print(repr(my_table))
