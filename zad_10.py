# Sortowanie
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie select o wartość w kolumnie 'state'
stmt = ____

# Wynik uporządkuj rosnąco, alfabetycznie po kolumnie stan
stmt = ____

# Wykonaj zapytanie, wynik zapisz do zmiennej results
results = ____

# Wyświetl pierwsze 10 wyników
print(____[:10])
