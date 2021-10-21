# Zasilanie bazy z pliku zewnętrznego CSV (fixtures)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import insert

engine = create_engine('sqlite:///new_census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table(
    'census2',
    metadata,
    Column('state', String(64)),
    Column('sex', String(1)),
    Column('age', Integer()),
    Column('pop2000', Integer()),
    Column('pop2008', Integer())
)
metadata.create_all(engine)

# obsługa CSV
import csv

fixtures = []
with open('census.csv') as csv_file:
    # reader = csv.reader(csv_file)
    # for item in reader:
    #     fixtures.append(
    #         {
    #             'state': item[0],
    #             'sex': item[1],
    #             'age': item[2],
    #             'pop2000': item[3],
    #             'pop2008': item[4]
    #         }
    #     )

    dict_reader = csv.DictReader(csv_file)

    for item in dict_reader:
        fixtures.append(item)

stmt = insert(census)

results = connection.execute(stmt, fixtures)
print(results.rowcount)
