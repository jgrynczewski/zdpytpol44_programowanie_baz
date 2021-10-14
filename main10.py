# Grupowanie - metoda grup_by
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

# Grupowanie
stmt = select([invoices])
stmt = stmt.group_by(invoices.columns.BillingCity)
print(stmt)

# Grupowanie z agregatami
# Wyświetlamy całkowitą kwotę na fakturach dla poszczególnych miast
stmt = select([invoices.columns.BillingCity, func.sum(invoices.columns.Total)])
stmt = stmt.group_by(invoices.columns.BillingCity)
print(stmt)


results = connection.execute(stmt).fetchall()
for item in results:
    print(item)
