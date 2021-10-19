# Obsługa zapytań (Cursor)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

stmt = select([census]).limit(10)

result_proxy = connection.execute(stmt)

# fetchone
result = result_proxy.fetchone()  # -> LegacyRow
print(result)
print(type(result))

# fetchmany
results = result_proxy.fetchmany(2)  # -> List[LegacyRow]
print(results)
print(len(results))
print(type(results))
print(type(results[0]))

# fetchall
results = result_proxy.fetchall()
print(len(results))

# Załóżmy że mamy bardzo dużo danych w tabeli
# (miliardy wpisów)
stmt = select([census])

# Zmienne pomocnicze
batch_size = 1000
batch_number = 0

result_proxy = connection.execute(stmt)

batch = result_proxy.fetchmany(batch_size)

while batch:
    print(f"Pierwszy element batcha {batch_number} - {batch[0]}")
    batch = result_proxy.fetchmany(batch_size)
    batch_number += 1