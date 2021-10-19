# Do tej pory patrzyliśmy na DQL (Data Query Language) - sprowadza się
# do zapytania select.
# Popatrzmy na DDL (Data Definition Language)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean

# Tworzenie bazy - wystarczy podać nieistniącą bazę w napisie połączeniowym
engine = create_engine('sqlite:///my_employees.sqlite')
metadata = MetaData()
metadata.create_all(engine)

# Tworzenie tabeli
# # Bazę tworzym bardzo podobnie do tego jak robimy odbicie bazy
employees = Table(
    'employees',
    metadata, # i przy odbiciu jeszcze dwa parametry autoload i autoload_with
    # przy tworzeniu poniżej umiszczamy informacje o kolumnach powstającej tabeli.
    Column('id', Integer),
    Column('name', String(255)),
    Column('salary', Float()),
    Column('active', Boolean())
)

metadata.create_all(engine)

# Więzy
employees2 = Table(
    'employees2',
    metadata, # i przy odbiciu jeszcze dwa parametry autoload i autoload_with
    # przy tworzeniu poniżej umiszczamy informacje o kolumnach powstającej tabeli.
    Column('id', Integer),
    Column('name', String(255), unique=True, nullable=False),
    Column('salary', Float(), default=100.00),
    Column('active', Boolean(), default=True)
)

metadata.create_all(engine)
