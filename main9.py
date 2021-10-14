# Agregaty
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

# Zliczenia - funkcja count
stmt = select([func.count(invoices.columns.Total)])
print(stmt)

# Zliczenia unikalnych wartości
stmt = select([func.count(invoices.columns.Total.distinct())])
print(stmt)

# Sumowanie
stmt = select([func.sum(invoices.columns.Total)])
print(stmt)

# Aliasy - metoda label
stmt = select([func.sum(invoices.columns.Total).label('amount')])
print(stmt)

# Dla pojedynczej wartości w pojednczej kolumnie możemy
# użyć funkcji scalar
results = connection.execute(stmt).scalar()
print(results)