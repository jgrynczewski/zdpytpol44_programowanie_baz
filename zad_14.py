# Grupowanie - funkcja group_by
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zaimportuj moduł func
from sqlalchemy import func

# W tym zadaniu sparwdzimy ile w bazie mamy wpisów w kolumnie age dla poszczególnych
# stanów. Zbuduj zapytanie o wartość w kolumnie state i zliczające wartości kolumny
# ages
stmt = select([census.columns.state, func.count(census.columns.age)])

# Pogrupuj po kolumnie state
stmt = stmt.group_by(census.columns.state)
print(stmt)

# Wykonaj zapytanie, wynik przechowaj w zmiennej results
results = connection.execute(stmt).fetchall()  # -> List (ResultSet)

# Wyświetl wynik
print(results)

# Wyświetl nazwy kolumn (klucze) wyniku
print(results[0].keys())
