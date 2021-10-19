# Update (wiele wierszy)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import update

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
state_fact = Table(
    'state_fact',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Zaktualizuj wszystkie wpisy w tabeli fact_state, które
# w kolumnie census_region_name mają wartość 'West'.
# Takim wpisom ustaw wartość w kolumnie notes na
# "The Wild West".

# Zbuduj zapytanie aktualizujące (wartość w kolumnie notes
# powinna być ustawiana na 'The Wild West')
stmt = update(____).values(____=____)

# Ustaw filtr na wpisy których wartość w kolumnie census_region_name na "West"
stmt_west = stmt.____(____ == ____)

# Wykonaj zapytanie
results = connection.execute(____)

# Wyświetl licznę zaktualizowanych wpisów
print(results.rowcount)
