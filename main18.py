# Popatrzmy na DML (Data Modification Language - CUD (CREATE, UPDATE, DELETE))
# D - czyli delete
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

# Delete
# Usunąć wpis
from sqlalchemy import delete

stmt = delete(
    employees  # Uwaga! Tak jak w insert - tabela, a nie tak jak w select - lista
).where(
    employees.columns.id == 1
)  # -> Delete
print(type(stmt))

result_proxy = connection.execute(stmt)
print(result_proxy.rowcount)
