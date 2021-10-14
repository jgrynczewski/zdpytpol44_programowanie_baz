# metoda in_
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Lista instersujących Cię stanów
states = ['New York', 'California', 'Texas']

# Stwórz zapytanie dla tabeli census
stmt = select(____)

# Dodaj warunek: interesują Cię tylko te wpisy, dla których stan znajduje się na liście states.
# Użyj funkcji in_()
stmt = stmt.where(____)

# Przeiteruj się po ResultingProxy i dla każdego otrzymanego wpisu wyświetl
# odpowiadający mu stan i liczebość populacji na rok 2000
for ____ in connection.execute(____):
    print(____, ____)
