# Zaimportuj create_engine, MetaData, and Table
from sqlalchemy import create_engine
from sqlalchemy import ____
from sqlalchemy import ____

# Stwórz silnik
engine = create_engine('sqlite:///census.sqlite')

# Stwórz obiekt z metadanymi
metadata = ____

# Odbij tabelę census z bazy census
census = Table(____, ____, autoload=____, autoload_with=____)

# Wyświetl metadatane o tabeli census
print(____)
