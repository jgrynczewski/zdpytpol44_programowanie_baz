# Samozłączenie
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///employees.sqlite')
connection = engine.connect()

metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)

# Utwórz alias do tabeli employees - managers
managers = employees.alias()

# Zbuduj zapytanie o imiona managerów i ich podwładnych
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Dopasuj wartości w kolumnie id tabeli manager
# z klumną mgr tabeli employees
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Uporządkuj wynik po kolumnie name tabeli managers
stmt_ordered = stmt_matched.order_by(managers.columns.name)

# Wykonaj zaptanie
results = connection.execute(stmt_ordered).fetchall()

# Wyświetl wyniki
for record in results:
    print(record)

