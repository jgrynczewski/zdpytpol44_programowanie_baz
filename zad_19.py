# Operatory matematyczne
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# zaimportuj z sqlalchemy case, cast i Float
from sqlalchemy import case, cast, Float

# Utwórz zapytanie zliczające liczbę kobiet w całej populacji USA w 2000 roku
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Utwórz zapytanie zliczające całkowitą liczebność populacji w 2000 roku.
# Wynik zrzutuj na Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Zbuduj zapytanie obliczające procentowy udział kobiet w społeczeństwie
# wykorzystują utworzone już zapytania
stmt = select([female_pop2000 / total_pop2000 * 100])
print(stmt)
# Wykonaj zapytanie, wynik przypisz do zmiennej percent_female
percent_female = connection.execute(stmt).scalar()

# Wyświetl procentowy wynik
print(percent_female)
