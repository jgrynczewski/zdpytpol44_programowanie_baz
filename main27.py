# Connection i menadżer kontekstu
import sqlalchemy as db

engine = db.create_engine("sqlite:///census.sqlite")
# connection = engine.connect()

metadata = db.MetaData()
census = db.Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = db.select([census])

with engine.connect() as connection:
    results = connection.execute(stmt).fetchmany(10)

print(results)