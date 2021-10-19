# D - w DDL (Data Definition Language) czyli drop
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table


engine = create_engine('sqlite:///my_employees.sqlite')
connection = engine.connect()
metadata = MetaData()
employees = Table(
    'employees',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Usunięcie tabeli
employees.drop(engine)

# Usunięcie wszystkich tabeli
metadata.drop_all(engine)