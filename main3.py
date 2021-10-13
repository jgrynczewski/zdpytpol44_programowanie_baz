# SELECT function
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Silnik i napis połączeniowy
conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

# inicjalizacja połączenia
connection = engine.connect()

# odbicie tabeli
metadata = MetaData()
artists = Table('artists', metadata, autoload=True, autoload_with=engine)

# zapytanie
stmt = select([artists])
print(stmt)

results = connection.execute(stmt).fetchall()
print(results)
