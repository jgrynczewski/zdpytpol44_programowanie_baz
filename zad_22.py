# Złączenia 3
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

# Zbuduj zapytanie o stan i całkowitą populację w roku 2008
# dla poszczególnych stanów i wartości w kolumnie
# census_division_name tabeli state_fact
stmt = select([
    ____,
    func.sum(____),
    ____
])

# Złącz tabele census i state_fact za pomocą metod select_from - join.
# Złączenie powinno przebiegać wzdłuż kolumn census.state
# i state_fact.name
stmt_joined = stmt.select_from(
    census.join(____, census.columns.____ == state_fact.columns.____)
)

# Wyniki pogrupuj wzdłuż kolumny name tabeli state_fact
stmt_grouped = stmt_joined.group_by(____)

# Wykonaj zapytanie, wynik przypisz do zmiennej results
results = connection.execute(____).fetchall()

# Przeiteruj się po wynikach, wyświetl poszczególne wpisy
for record in results:
    print(record)
