# operatory matematyczne
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import desc

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie, które zwróci nazwę stany i różnicę pomiędzy liczebnością populacji
# w latach 2008 i 2000. Kolumnę reprezentującą różnicę nazwij pop_change
stmt = select([
    census.columns.state,
    (census.columns.pop2008 - census.columns.pop2000).label('pop_change')
])

# Wyniki pogrupuj po kolumnie state
stmt_grouped = stmt.group_by(census.columns.state)

# Wyniki uporządkuj po kolumnie pop_change w porządku malejącym (desc)
stmt_ordered = stmt_grouped.order_by(desc('pop_change'))

# Zwróć tylko pięć pierwszych wyników
stmt_top5 = stmt_ordered.limit(5)

# Wykonaj zapytanie na bazie
results = connection.execute(stmt_top5).fetchall()

# Wyświetl wyniki
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
