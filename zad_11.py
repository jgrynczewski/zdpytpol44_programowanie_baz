# Sortowanie w odwróconym porządku
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zaimportuj funkcję desc
from ____ import ____

# Zbuduj zapytanie o wartości w kolumnie state tabeli census
stmt = ____

# Posortuj wyni w kolejności odwrotnej
rev_stmt = stmt.order_by(____)

# Wykonaj zapytanie i zapisz wynik w zmiennej rev_results
rev_results = ____

# Wyświetl piersze 10 wpisów
print(____)
