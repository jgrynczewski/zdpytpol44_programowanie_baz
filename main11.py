# Operatory matematyczne
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

stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008 - census.columns.pop2000).label('population_change')
]).group_by(
    census.columns.state
).order_by(
    desc('population_change')
).limit(10)

results = connection.execute(stmt).fetchall()
print(results)

# Funkcja case
from sqlalchemy import case

# Standardowo
stmt = select([
    func.sum(census.columns.pop2008)
]).group_by(
    census.columns.state
).where(
    census.columns.state == "New York"
)

# Funckja case - switch
stmt = select([
    func.sum(case([
        (census.columns.state == 'New York', census.columns.pop2008),
    ], else_=0))
])

results = connection.execute(stmt).fetchall()
print(results)

# funkcja cast - rzutowanie
from sqlalchemy import cast
from sqlalchemy import Float
from sqlalchemy import Numeric
stmt = select([
    cast(census.columns.pop2008, Float)
]).limit(1)

results = connection.execute(stmt).fetchall()
print(results)

# Procentowy udział populacji Nowego Jorku w całej populacji US w 2008

ny_population = func.sum(
    case([
        (census.columns.state == "New York", census.columns.pop2008)
    ], else_=0)
)

us_population = func.sum(census.columns.pop2008)


stmt = select([ny_population / cast(us_population, Float)*100])
print(stmt)

results = connection.execute(stmt).scalar()
print(results)