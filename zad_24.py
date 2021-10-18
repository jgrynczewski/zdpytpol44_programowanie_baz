# Grupowanie i samozłączenia
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
managers = ____

# Zbuduj zapytanie o wartość w kolumnie name tabeli managers
# i zliczające ich podwładnych
stmt = select([____, func.count(____)])

# Dodaj filtr na wartość w kolumnie id tabeli manager (powinna być
# równa wartości mgr w tabeli employee)
stmt_matched = stmt.____

# Wynik pogrupuj po wartości w kolumnie name tabeli managers
stmt_grouped = stmt_matched.group_by(____)

# Wykonaj zapytanie
results = connection.execute(stmt_grouped).fetchall()

# Wyświetl wyniki
for record in results:
    print(record)

