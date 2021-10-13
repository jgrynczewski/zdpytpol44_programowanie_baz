# Engine, connection string

from sqlalchemy import create_engine

conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

# print(engine)
# print(type(engine))
# print(dir(engine))

# print(engine.table_names())

# Reflection
from sqlalchemy import MetaData
from sqlalchemy import Table

metadata = MetaData()
# print(metadata)
# print(dir(metadata))
# print(metadata.tables)  # pusty przed odbiciem

artists = Table('artists', metadata, autoload=True, autoload_with=engine)  # odbicie

print(artists)  # __str__
print(repr(artists))  # __repr__

print(metadata.tables)  # po odbiciu