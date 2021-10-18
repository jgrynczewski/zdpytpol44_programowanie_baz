# Praca z danym hierarchicznym - samozłączenia (self-join)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import desc

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)

# Tworzymy alias tabeli
managers = employees.alias()

stmt = select([
    employees.columns.FirstName.label('employee'),
    managers.columns.FirstName.label('manager')
]).select_from(
    employees.join(
        managers,  # prawa strona złączenia
        employees.columns.ReportsTo == managers.columns.EmployeeId  # warunek złączenia
    )
).order_by(
    managers.columns.FirstName
)

results = connection.execute(stmt).fetchall()
print(results)