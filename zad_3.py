from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Odbij tabelę census z bazy census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Wyświetl nazwy kolumn
print(census.columns.keys())

# Wyświetl pełne metadane o tabeli census
print(repr(census))
