# Konsumowanie danych (wizualizacja) (matplotlib)
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
    db.func.sum(census.columns.pop2008)
]).group_by(
    census.columns.state
)

results = connection.execute(stmt).fetchall()
print(results)

# Wizualizacja
import matplotlib.pyplot as plt

X = [item[0] for item in results]
Y = [item[1] for item in results]

plt.barh(X, Y)
plt.show()
