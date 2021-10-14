# Filtrowanie - select po wybranych kolumnach
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

# Chcemy tylko kolumnę InvoiceId
# Funkcja select przyjmuje obiekty klasy Table lub klasy Column
stmt = select([invoices.columns.InvoiceId])
print(stmt)

# A kilka kolumn ?
stmt = select(
    [
        invoices.columns.InvoiceId,
        invoices.columns.BillingCity,
        invoices.columns.Total
    ]
)
print(stmt)

result_proxy = connection.execute(stmt)
result = result_proxy.fetchall()

print(invoices.columns.Total.type)

for item in result:
    print(item)