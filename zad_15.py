# Sumowanie - funkcja sum + aliasing - metoda label
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

# Zbuduj wyrażenie, które wyświetli całkowitą populację dla poszczególnych
# stanów USA w roku 2008. Czyli trzeba zsumować kolumnę pop2008, a całość
# pogrupować po kolumnie state. Kolumna z wynikiem powinna mieć etykietę
# population.

# Zbuduj wyrażenie, które zsumuje wartości w kolumnie pop2008, a wynik
# wyświetli w kolumnie z etykietą population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Zbuduj zapytanie, które wyświetli wartości w kolumnie state i zsumowane wartości
# w kolumnie pop2008
stmt = select([census.columns.state, pop2008_sum])

# Wyniki pogrupuj po kolumnie state
stmt = stmt.group_by(census.columns.state)

# Wykonaj zapytanie, wynik przypisz do zmiennej results
results = connection.execute(stmt).fetchall()

# Wyświetl wynik
print(results)

# Wyświetl nazwy kolumn (klucze) wyniku
print(type(results[0].keys()))
