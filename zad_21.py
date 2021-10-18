# Złączenia 2
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

# Zbuduj zapytanie, które wybierze wszystkie kolumny z tabel
# census i state_facts
stmt = select([____, ____])

# Złącz tabele wzdłuż kolumn census.state i state_fact.name
# użyj metody select_from obiektu klasy Select i metody
# join obiektu klasy
stmt_join = stmt.select_from(
    ____(____, census.columns.____ == state_fact.columns.____))

# Wykonaj zapytanie i pobierze pierwszy rekord wyniku
result = connection.execute(stmt_join).first()

# Przeiteruj się po kluczach i wartościach pobranego wpisu
for key in result.keys():
    print(key, getattr(result, key))
