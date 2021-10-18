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
from sqlalchemy import ____, ____, ____

# Utwórz zapytanie zliczające liczbę kobiet w całej populacji USA w 2000 roku
female_pop2000 = func.sum(
    ____([
        (____ == ____, ____)
    ], else_=____))

# Utwórz zapytanie zliczające całkowitą liczebność populacji w 2000 roku.
# Wynik zrzutuj na Float
total_pop2000 = cast(func.sum(____), ____)

# Zbuduj zapytanie obliczające procentowy udział kobiet w społeczeństwie
# wykorzystują utworzone już zapytania
stmt = select([____ / ____* 100])

# Wykonaj zapytanie, wynik przypisz do zmiennej percent_female
percent_female = connection.execute(____).scalar()

# Wyświetl procentowy wynik
print(____)
