# Filtrowanie - metoda where ciąg dalszy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table('invoices', metadata, autoload=True, autoload_with=engine)

# Znamy inne operatory porównania
# >, <, >=, <=, !=, ...

# Wszystkie faktury na kwotę większą niż 5
stmt = select([invoices])
stmt = stmt.where(invoices.columns.Total > 5)
print(stmt)

# Wszystkie faktury, które nie zostały wysłane do Warszawy
stmt = select([invoices])
stmt = stmt.where(invoices.columns.BillingCity != 'Warsaw')
print(stmt)

# Operatory logicze: or, and, not
# w SQLAlchemy to odpowiednio funkcje or_, and_, not_

# Alternatywa warunków
# Wszystkie faktury, które zostały wysłane do Warszawy lub Paryża
from sqlalchemy import or_

stmt = select([invoices])
stmt = stmt.where(
    or_(
        invoices.columns.BillingCity == 'Warsaw',
        invoices.columns.BillingCity == 'Paris'
    )
)

# Koniunkcja warunków
# Wszystkie faktury wysłane do Warszawy na kwotę większą niż 3
from sqlalchemy import and_
stmt = select([invoices])
stmt = stmt.where(
    and_(
        invoices.columns.BillingCity == 'Warsaw',
        invoices.columns.Total > 3
    )
)

# Zaprzeczenie
# Wszystkie faktury, które nie zostały wysłane do Warszawy
from sqlalchemy import not_
stmt = select([invoices])
stmt = stmt.where(
    not_(invoices.columns.BillingCity == 'Warsaw')
)

# Operatory IN, LIKE, BETWEEN
# Tutaj to odpowiednio metody in_(), like(), between()

# in_()
# Wszystkie faktury, które zostały wysłane do Warszawy lub Paryża
stmt = select([invoices])
stmt = stmt.where(invoices.columns.BillingCity.in_(['Paris', 'Warsaw']))

# between()
# Wszystkie faktury na kwotę <1, 4>
stmt = select([invoices])
stmt = stmt.where(invoices.columns.Total.between(1, 4))

# like
# Wszyskie faktury, które zostały wysłane do miast zaczynających się na literę B
stmt = select([invoices])
stmt = stmt.where(invoices.columns.BillingCity.like('B%'))
print(stmt)

# I wiele innych metod
# Powyższe możemy zrobić np. w taki sposób:
stmt = select([invoices])
stmt = stmt.where(invoices.columns.BillingCity.startswith('B'))
print(stmt)

# A na przykład zamiast metody between możemy użyć funkcji between
from sqlalchemy import between
stmt = select([invoices])
stmt = stmt.where(between(invoices.columns.Total, 1, 4))
print(stmt)

results = connection.execute(stmt).fetchall()
for item in results:
    print(f"Faktura numer {item.InvoiceId} do {item.BillingCity} na kwotę {item.Total}")
