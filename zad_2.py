# Zaimportuj create_engine, MetaData, and Table
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

# Stwórz silnik
engine = create_engine('sqlite:///census.sqlite')

# Stwórz obiekt z metadanymi
metadata = MetaData()

# Odbij tabelę census z bazy census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Wyświetl metadatane o tabeli census
print(metadata.tables)
