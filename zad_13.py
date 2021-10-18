# Zliczenia - funkcja count
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

# Zbuduj zapytanie zliczające wszystkie unikalne stany w tabeli census
stmt = select([func.count(census.columns.state.distinct())])

# Wykonaj zapytanie, wynik przechowaj w zmiennej distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Wyświetl liczbę unikalnych stanów
print(distinct_state_count)
