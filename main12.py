# Złączenia (JOIN)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import desc

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

stmt = select([
    census.columns.pop2008,
    state_fact.columns.abbreviation
])  # Iloczyn kartezjański

stmt = select([
    census.columns.pop2008,
    state_fact.columns.abbreviation
]).where(
    census.columns.state == state_fact.columns.name
)  # Iloczyn kartezjański z warunkiem = złączeniem (JOIN)
print(stmt)

results = connection.execute(stmt).fetchall()
print(len(results))

# JOIN
# 1. metoda obiektu klasy Select (płynny interfejs, ang. fluent interface)
# 2. metoda obiektu klasy Table

# 1. metoda klasy Select
stmt = select([
    census.columns.pop2008, state_fact.columns.abbreviation
]).join(
    state_fact,  # prawa strona złączenia
    census.columns.state == state_fact.columns.name  # warunek złączenia
)
print(stmt)

# A bez warunku się nie da?
# stmt = select([
#     census.columns.pop2008, state_fact.columns.abbreviation
# ]).join(state_fact)  # sqlalchemy.exc.InvalidRequestError: Don't know how to join to Table
# Zadziała jeżeli mamy zdefiniowany na tabeli klucz obcy. Skąd weźmie informacje ?
# Z kontenera z metadanymi.
# print(metadata.tables)

# 2. metoda klasy Table (to wtedy trzeba użyć metody obiektu klasy Select - select_from)
# metodę join (Table) i select_from (Select)

stmt = select([
    census.columns.pop2008, state_fact.columns.abbreviation
]).select_from(
    census.join(
        state_fact,  # prawa strona złączenia
        census.columns.state == state_fact.columns.name  # warunek złączenia
    )
)  # I znów można pozbyć się warunku, ale musi być zdefiniowany klucz obcy na tabeli.

print(stmt)

results = connection.execute(stmt).fetchall()
print(len(results))

# Znajdź liczebność populacji w 2008 roku w obszarze wschodnio-południowo-centralnym
# (east-south-central)

# Metodą join klasy Table
stmt = select([
    func.sum(census.columns.pop2008)
]).select_from(
    census.join(
        state_fact,
        state_fact.columns.name == census.columns.state
    )
).where(
    state_fact.columns.census_division_name == 'East South Central'
)

result = connection.execute(stmt).scalar()
print(result)

# Alterantywnie metodą join klasy Select
stmt = select([
    func.sum(census.columns.pop2008)
]).join(
        state_fact,
        state_fact.columns.name == census.columns.state
).where(
    state_fact.columns.census_division_name == 'East South Central'
)

result = connection.execute(stmt).scalar()
print(result)
