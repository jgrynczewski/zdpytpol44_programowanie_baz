from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

# Zaimportuj funkcję select
from ____ import ____

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()

# Odbij tabelę census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie select na tabeli census
stmt = ____

# Wyświetl instrukcję, w celu sprawdzenia wygenerowanej sqlki
print(stmt)

# Wykonaj instrukcję select na połączeniu i pobierz tylko 10 wpisów
results = ____.____(____).____(size=___)

# Wykonaj instrukcję i wyświetl wynik.
print(results)
