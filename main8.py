# Sortowanie - funkcja order_by
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

stmt = select([invoices])

# Sortujemy wyniki po kolumnie BillingCity
# (domyślnie sortownie w porządku rosnącym)
# dla napisów oznacza to sortownie alfabetyczne
stmt = stmt.order_by(invoices.columns.BillingCity)

# dla porządku malejącego jest funkcja desc
from sqlalchemy import desc
stmt = select([invoices])
stmt = stmt.order_by(desc(invoices.columns.BillingCity))

# ale jest też metoda desc obiektu klasy Column
stmt = select([invoices])
stmt = stmt.order_by(invoices.columns.BillingCity.desc())

# Sortowanie po wielu kolumnach
stmt = select([invoices])
stmt = stmt.order_by(invoices.columns.BillingCity, invoices.columns.Total)

results = connection.execute(stmt).fetchall()
for item in results:
    print(f"Faktura numer {item.InvoiceId} do {item.BillingCity} na kwotę {item.Total}")
