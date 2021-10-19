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
from sqlalchemy import insert
from sqlalchemy import select

# Zbuduj zapytanie insert.
# Nowy wpis w tabeli my_table ma postać:
# name - 'Anna'
# count - 1
# amount - 1000.00
# valid - True
insert_stmt = insert(
    my_table
).values(
    name='Anna',
    count=1,
    amount=1000.00,
    valid=True
)

# Wykonaj zapytanie na bazie
results = connection.execute(insert_stmt)

# Wyświetl liczbę wpisów dodanych do bazy
print(results.rowcount)

# Zbuduj zapytanie select, które zweryfikuje zawartość tabeli.
# Zapytaj o właśnie dodany wpis
select_stmt = select([
    my_table
]).where(
    my_table.columns.name == 'Anna'
)

# Wyświetl pobrany wpis
print(connection.execute(select_stmt).fetchall())
