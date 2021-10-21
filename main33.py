# XML
import sqlalchemy as db
import pandas as pd

engine = db.create_engine("sqlite:///census.sqlite")
connection = engine.connect()

metadata = db.MetaData()
census = db.Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = db.select([census])
results = connection.execute(stmt).fetchall()  # ale to mało nam jeszcze mówi

df = pd.DataFrame(results)
df.columns = results[0].keys()

# print(df.to_xml())
df.to_xml('census.xml')
