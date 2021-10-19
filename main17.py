# Popatrzmy na DML (Data Modification Language - CUD (CREATE, UPDATE, DELETE))
# C - czyli Insert
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table


engine = create_engine('sqlite:///my_employees.sqlite')
connection = engine.connect()
metadata = MetaData()
employees = Table(
    'employees',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Update
from sqlalchemy import update

stmt = update(
    employees  # Uwaga! Tak jak w insert - tabela, a nie tak jak w select - lista
).where(
    employees.columns.id == 3
).values(
    active=False  # Uwaga! Nie tak jak w where (obiekt_tabeli.columns.nazwa_kolumny)
    # tylko sama nazwa kolumny
)  # -> Update
print(type(stmt))

result_proxy = connection.execute(stmt)
print(result_proxy.rowcount)

# UWAGA! Bez metody where zostaną zmodyfikowane wszystkie wpisy!
stmt = update(
    employees
).values(
    active=False
)  # to zapytanie zmodyfikuje WSZYSTKIE wpisy w tabeli

result_proxy = connection.execute(stmt)
print(result_proxy.rowcount)
