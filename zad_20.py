# Złączenia 1
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie złączające tabele census i state_fact,
# interesują Cię kolumna pop2008 tabeli census
# oraz tabela abbrevation tabeli state_fact
stmt = select([____, ____])

# Wykonaj zapytanie i pobierz pierwszy rekord wyniku
result = connection.execute(____).first()

# Przeiteruj się po nazwach kolumn pobranego wyniku
# Wyświetl klucz i odpowiadającą mu wartość we wpisie
# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(f"{key}: \t {result[key]}")
