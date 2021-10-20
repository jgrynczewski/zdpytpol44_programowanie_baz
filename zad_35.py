# Wizualizacja
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func

engine = create_engine('sqlite:///chinook.sqlite')
connection = engine.connect()

metadata = MetaData()
invoices = Table(
    'invoices',
    metadata,
    autoload=True,
    autoload_with=engine
)

stmt = select([
    invoices.columns.BillingCountry.label('country'),
    func.sum(invoices.columns.Total).label('total')
]).group_by(
    invoices.columns.BillingCountry
)

results = connection.execute(stmt).fetchall()

# import pandas
import pandas as pd

# import matplotlib
import matplotlib.pyplot as plt

# Stwórz obiekty klasy DataFrame (podstawowy obiekt biblioteki pandas)
# w inicjalizatorze przekaż wynik zapytania (results)
df = pd.DataFrame(results)

# Kolumnom dataframe przypisz klucze pojedynczego wpisu w results
df.columns = results[0].keys()

# Wyświetl dataframe
print(df)

#  Rzutowanie wartości w kolumnie total dataframe do wartośći numerycznych
df[["total"]] = df[["total"]].apply(pd.to_numeric)

# Wyświetl wykres, na którym bedzie przedstawiona wartość
# całkowita faktur wystwionych dla poszczególnych krajów
df.plot.barh(x='country', y='total')
plt.show()
