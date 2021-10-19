# Delete (usuwanie wybranych wpisów)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import and_

engine = create_engine('sqlite:///census3.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

# Import delete
from sqlalchemy import ____

# Zapytanie zliczające liczbę wpisów posiadających wartość 'M'
# w kolumnie sex i wartość 36 w kolumnie age
count_stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Wykonanie zapytania. Zapytanie przechowuje informacje o liczbie
# wierszy do usunięcia. Porównamy tą liczbę z liczbą wierszy usuniętych
# na końcy skryptu.
to_delete = connection.execute(count_stmt).scalar()

# Zbuduj zapytanie na usunięci wpisów z tabeli census
delete_stmt = ____

# Usuń tylko te wpisy, które w kolumnie sex mają wartość 'M',
# a w kolumnie age 36
delete_stmt = delete_stmt.____(
    ____(census.columns.sex == ____,
         ____ == ____)
)

# Wykonaje zapytanie
results = connection.execute(____)

# Porównanie liczby wierszy, które zostały usunięte z liczbą wierszy
# które były do usunięcia
print(results.rowcount, to_delete)
