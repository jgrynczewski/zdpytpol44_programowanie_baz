# Delete (usuwanie wszystkich wpisów)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select, delete

engine = create_engine('sqlite:///census2.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Zbuduj zapytanie, które wyczyści tabele census
# Build a statement to empty the census table: stmt
delete_stmt = delete(census)  # !NIEBEZPIECZNE

# Wykonaj zapytanie, wynik przypisz do zmiennej results
results = connection.execute(delete_stmt)

# Sprawdź ilu wierszy dotknęła zmiana
print(results.rowcount)

# Zbuduj zapytanie o wszystkie wpisy w tabeli census
select_stmt = select([census])

# Wyświetl wynik
print(connection.execute(select_stmt).fetchall())

