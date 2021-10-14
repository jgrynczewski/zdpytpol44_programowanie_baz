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
stmt = select([census])

# Dodaj warunek: interesują Cię tylko te wpisy, dla których stan znajduje się na liście states.
# Użyj metody in_()
stmt = stmt.where(census.columns.state.in_(states))

# Przeiteruj się po ResultProxy i dla każdego otrzymanego wpisu wyświetl
# odpowiadający mu stan i liczebość populacji na rok 2000
for item in connection.execute(stmt):
    print(item.state, item.pop2000)
