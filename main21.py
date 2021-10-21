# Zasilanie bazy z pliku zewnętrznego JSON (fixtures)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import insert

engine = create_engine('sqlite:///new_census.sqlite')
connection = engine.connect()

metadata =  MetaData()
census = Table(
    'census4',
    metadata,
    Column('state', String(64)),
    Column('sex', String(1)),
    Column('age', Integer()),
    Column('pop2000', Integer()),
    Column('pop2008', Integer())
)
metadata.create_all(engine)

# Obsługa json
import json

json_file = open('census.json')
fixtures = json.load(json_file)

stmt = insert(census)
result_proxy = connection.execute(stmt, fixtures)
print(result_proxy.rowcount)
