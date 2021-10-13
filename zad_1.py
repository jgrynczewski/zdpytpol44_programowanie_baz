# Zaimportuj funkcję create_engine
from sqlalchemy import create_engine

# Stwórz silnik do bazy sqlite (pliku) census.sqlite
engine = create_engine('sqlite:///census.sqlite')

# Wyświetl nazwy tabel znajdujących się w bazie census.sqlite
print(engine.table_names())
