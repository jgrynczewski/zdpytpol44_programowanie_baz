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
from sqlalchemy import and_

# Zbuduj zapytanie
stmt = select([census])

# Dodaj warunek. Interesują Cię tylko wpisy, które nie dotyczą mężczyzn dla stanu California.
# Użyj funkcji and_()
stmt = stmt.where(
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Przeiteruj się po ResultProxu i wyświetl wiek oraz płeć dla każdego otrzymanego wpisu
for result in connection.execute(stmt):
    print(result.sex, result.age)
