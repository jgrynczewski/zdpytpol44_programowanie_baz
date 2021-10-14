# metoda where
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Stwórz zapytanie select
stmt = ____

# Dodaj warunek na stan, interesują Cię tylko wpisy dla stanu - New York
stmt = stmt.____

# Wykonaj zapytanie i pobierz wynik
results = ____

# Przeiteruj się po wyniku i wyświetl wartości w kolumnach: age, sex i pop2000
for ___ in ____:
    print(result.age, ____, ____)
