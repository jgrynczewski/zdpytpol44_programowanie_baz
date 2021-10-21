# Konsumowanie danych (wizualizacja) (pandas + matplotlib)
import sqlalchemy as db

engine = db.create_engine("sqlite:///census.sqlite")
connection = engine.connect()

metadata = db.MetaData()
census = db.Table(
    'census',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = db.select([
    census.columns.state,
    db.func.sum(census.columns.pop2008).label('population')
]).group_by(
    census.columns.state
)

results = connection.execute(stmt).fetchall()  # -> List[LegacyRow]

# Wizualizacja
# pandas
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame - podsatwowy obiekt w pandas
df = pd.DataFrame(results)
df.columns = results[0].keys()
# print(dir(df))
print(df)

df.plot.barh(x='state', y='population')

plt.savefig('census.jpg')
plt.show()
