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
import ____ as pd

# import matplotlib
import ____.____ as plt

# Stwórz obiekty klasy DataFrame (podstawowy obiekt biblioteki pandas)
# w inicjalizatorze przekaż wynik zapytania (results)
df = ____.____(____)

# Kolumnom dataframe przypisz klucze pojedynczego wpisu w results
df.columns = ____[0].____()

# Wyświetl dataframe
print(____)

#  Rzutowanie wartości w kolumnie total dataframe do wartośći numerycznych
df[["total"]] = df[["total"]].apply(pd.to_numeric)

# Wyświetl wykres, na którym bedzie przedstawiona wartość
# całkowita faktur wystwionych dla poszczególnych krajów
df.____.____(x=____, y=____)
____.____()
