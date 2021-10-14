# metoda where
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Stwórz zapytanie select
stmt = select([census])

# Dodaj warunek na stan, interesują Cię tylko wpisy dla stanu - New York
stmt = stmt.where(census.columns.state == 'New York')

# Wykonaj zapytanie i pobierz wynik
results = engine.execute(stmt)

# Przeiteruj się po wyniku i wyświetl wartości w kolumnach: age, sex i pop2000
for result in results:
    print(result.state, result.age, result.sex, result.pop2000)
