# Insert (pojedynczy wiersz)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///my_db.sqlite')
connection = engine.connect()

metadata = MetaData()
my_table = Table(
    'my_table',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Zaimportuj funckje insert i select z sqlalchemy
from sqlalchemy import ____
from sqlalchemy import ____

# Zbuduj zapytanie insert.
# Nowy wpis w tabeli my_table ma postać:
# name - 'Anna'
# count - 1
# amount - 1000.00
# valid - True
insert_stmt = insert(
    ____
).values(
    name=____,
    ____,
    ____,
    ____
)

# Wykonaj zapytanie na bazie
results = connection.execute(____)

# Wyświetl liczbę wpisów dodanych do bazy
print(____)

# Zbuduj zapytanie select, które zweryfikuje zawartość tabeli.
# Zapytaj o właśnie dodany wpis
select_stmt = select([
    my_table
]).where(
    ____ == ____
)

# Wyświetl pobrany wpis
print(connection.execute(select_stmt).fetchall())
