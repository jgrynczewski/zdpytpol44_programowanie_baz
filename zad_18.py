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
stmt = select([____, (____-____).label(____)])

# Wyniki pogrupuj po kolumnie state
stmt_grouped = stmt.group_by(____)

# Wyniki uporządkuj po kolumnie pop_change w porządku malejącym (desc)
stmt_ordered = stmt_grouped.order_by(____)

# Zwróć tylko pięć pierwszych wyników
stmt_top5 = ____

# Wykonaj zapytanie na bazie
results = connection.execute(____).fetchall()

# Wyświetl wyniki
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
