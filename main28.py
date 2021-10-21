# Engine, connection, session i metoda execute
import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
# Dla danego silnika można utworzy wiele połączeń.
# connection pool - zbiornik na połączenia

metadata = db.MetaData()
census = db.Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = db.select([
    census
]).where(
    census.columns.state == "New York"
)

results = engine.execute(stmt).fetchall()
# Na engine metoda execute działa
# Pod maską silnik tworzy połączenie i commituje (autocommit)
print(results)

connection = engine.connect()
results = connection.execute(stmt).fetchall()
# Na connection metoda execute też działa

print(results)

# To po co na connection metoda execute?
# Przydaje się jeżeli chcemy mieć większą
# kontrolę, zwłaszcza nad połączeniem (connection)
# Na przyklad chcemy ręcznie obsłużyć całą transakcję.

transaction = connection.begin()
try:
    connection.execute("INSERT INTO census VALUES ('New York', 'F', 101, 212, 234, 8774);")
    connection.execute("INSERT INTO census VALUES ('New York', 'F';")
    transaction.commit()
except:
    transaction.rollback()
    print("Coś poszło nie tak")


# Sesja (session)
# Sesja przechowuje informacje potrzebne
# ormowi do działania (connection tego nie robi).
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

# Można tak
session = Session()
session.execute("INSERT INTO census VALUES ('New York', 'F', 110, 1, 2, 8775);")
session.commit()

# A można tak
with Session() as session:
    session.execute("INSERT INTO census VALUES ('New York', 'F', 110, 1, 2, 8775);")
    session.commit()
