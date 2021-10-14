# Funckja and_
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zaimportuj funkcję and_
from ____ import ____

# Zbuduj zapytanie
stmt = select(____)

# Dodaj warunek. Interesują Cię tylko wpisy, które nie dotyczą mężczyzn dla stanu California.
# Użyj funkcji and_()
stmt = stmt.where(
    ____(census.columns.state == ____,
         census.columns.sex != ____
         )
)

# Przeiteruj się po ResultProxu i wyświetl wiek oraz płeć dla każdego otrzymanego wpisu
for result in ____:
    print(____, ____)
