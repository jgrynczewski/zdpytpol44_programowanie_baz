from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Odbij tabelę census z bazy census
census = ____(____, ____, autoload=____, autoload_with=____)

# Wyświetl nazwy kolumn
print(____)

# Wyświetl pełne metadane o tabeli census
print(repr(____))
