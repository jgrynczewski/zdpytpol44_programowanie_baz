# Sortowanie po wielu kolumnach
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import desc

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie o wartości w kolumnie state i age tabeli census
stmt = select([census.columns.state, census.columns.age])

# Posortuje wyniki w następującej kolejności:
# po wartości w kolumnie state w porządku rosnącym
# po wartości w kolumnie age w porządku malejącym
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Wykonaj zapytanie, wynik przypisz do zmiennej results
results = connection.execute(stmt).fetchall()

# Wyświetl piersze 20 wpisów
print(results[:20])
