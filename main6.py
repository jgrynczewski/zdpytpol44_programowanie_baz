# Filtrowanie - metoda where
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

stmt = select([invoices])
stmt = stmt.where(invoices.columns.BillingCity == "Warsaw")

# Ale możemy też łańcuchować
# stmt = select([invoices]).where(invoices.columns.BillingCity == "Warsaw")

print(stmt)

result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

for item in results:
    print(f"Faktura numer {item.InvoiceId} do {item.BillingCity} na kwotę {item.Total}")

# Jako ciekawostka.
# Obiket klasy LegacyCursorResult jest iterowalny. Możemy go
# skonsumować bez wywołania metody fetchall,...
# for item in result_proxy:
#     print(f"Faktura numer {item.InvoiceId} do {item.BillingCity} na kwotę {item.Total}")
