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
____

# Zbuduj wyrażenie, które wyświetli całkowitą populację dla poszczególnych
# stanów USA w roku 2008. Czyli trzeba zsumować kolumnę pop2008, a całość
# pogrupować po kolumnie state. Kolumna z wynikiem powinna mieć etykietę
# population.

# Zbuduj wyrażenie, które zsumuje wartości w kolumnie pop2008, a wynik
# wyświetli w kolumnie z etykietą population
pop2008_sum = func.sum(____).label(____)

# Zbuduj zapytanie, które wyświetli wartości w kolumnie state i zsumowane wartości
# w kolumnie pop2008
stmt = select([____, ____])

# Wyniki pogrupuj po kolumnie state
stmt = stmt.group_by(____)

# Wykonaj zapytanie, wynik przypisz do zmiennej results
results = connection.execute(____).fetchall()

# Wyświetl wynik
print(results)

# Wyświetl nazwy kolumn (klucze) wyniku
print(____)