# Insert (wiele wiersz)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import insert
from sqlalchemy import select

engine = create_engine('sqlite:///my_db.sqlite')
connection = engine.connect()

metadata = MetaData()
my_table = Table(
    'my_table',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Zbuduj listę dwóch słowników.
# Pierwszy słownik reprezentuje dane:
# name - 'Eva', count - 1, amount - 2000.00, valid - True
# Drugi słownik reprezentuje dane:
# name - 'Steve', count - 1, amount - 750.00, valid - False
values_list = [
    {'name': 'Eva', 'count': 1, 'amount': 2000, 'valid': True},
    {'name': 'Steve', 'count':1, 'amount': 750, 'valid': False}
]

# Zbuduje zapytanie insert
stmt = insert(
    my_table
)

# Wykonaj zapytanie insert z danymi słownikowymi
results = connection.execute(stmt, values_list)

# Wyświetl liczbę wpisów, które zostały dodane
# do tabeli w ramach zapytania
print(results.rowcount)