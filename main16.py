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

# Funkcji insert możemy uzyc na dwa sposoby:
# 1. z metodą values
# 2. ze słownikiem

# 1. z metodą values
from sqlalchemy import insert

stmt = insert(
    employees  # Uwaga! W insert tabela, a nie tak jak w select - lista
).values(
    id=3,
    name='Anna',
    salary=300,
    active=True
)  # -> Insert
print(type(stmt))

result_proxy = connection.execute(stmt)  # -> LegacyCursorResult
# dla fetch dostaniemy
# sqlalchemy.exc.ResourceClosedError: This result object does not return rows
print(type(result_proxy))
print(result_proxy.rowcount)  # rowcount - informacja o tym ile zostało
# zmodyfikowanych wierszy

# 2 ze słownikiem (korzyść - łatwo wprowadzić wiele wpisów)

stmt = insert(employees)

values_list = [
    {
        'id': 4,
        'name': 'Rebecca',
        'salary': 0,
        'active': False
    }
]

result_proxy = connection.execute(stmt, values_list)
print(result_proxy.rowcount)

values_list = [
    {
        'id': 5,
        'name': 'Tom',
        'salary': 400,
        'active': True
    },
    {
        'id': 6,
        'name': 'Bob',
        'salary': 200,
        'active': True
    }
]

result_proxy = connection.execute(stmt, values_list)
print(result_proxy.rowcount)
