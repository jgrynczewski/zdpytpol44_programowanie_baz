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
from sqlalchemy import desc

# Zbuduj zapytanie o wartości w kolumnie state tabeli census
stmt = select([census.columns.state])

# Posortuj wyni w kolejności odwrotnej
rev_stmt = stmt.order_by(desc(census.columns.state))

# Wykonaj zapytanie i zapisz wynik w zmiennej rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Wyświetl piersze 10 wpisów
print(rev_results)
